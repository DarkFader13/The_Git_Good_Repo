(Endpoint as text, optional Fields as text, optional QueryText as text) =>
let
    Limit = if RowLimit = null then -1 else RowLimit,

    // --- Parse QueryText JSON into a record ---
    QueryRecord =
        if QueryText <> null and Text.Length(QueryText) > 0
        then try Json.Document(QueryText) otherwise null
        else null,

    // --- Fetch first page to get pagination ---
    FirstPageQuery =
        if QueryRecord <> null then Record.AddField(QueryRecord, "page", "1")
        else [page="1"],

    FirstPage =
        Json.Document(
            Web.Contents(
                API_Web,
                [RelativePath = "v4/" & Endpoint, Query = FirstPageQuery]
            )
        ),

    PageMeta = try FirstPage[pagination] otherwise [last_visible_page=1],
    LastPage = PageMeta[last_visible_page],

    Iterations =
        if Limit <> -1 and Number.RoundUp(Limit / 25) < LastPage
        then Number.RoundUp(Limit / 25)
        else LastPage,

    IterationList = List.Numbers(1, Iterations),

    // --- Fetch each page ---
    FetchPage = (PageNum as number) =>
        let
            PageQuery =
                if QueryRecord <> null
                then Record.AddField(QueryRecord, "page", Number.ToText(PageNum))
                else [page = Number.ToText(PageNum)],

            PageSource =
                Json.Document(
                    Web.Contents(
                        API_Web,
                        [RelativePath = "v4/" & Endpoint, Query = PageQuery]
                    )
                ),

            PageResult = try PageSource[data] otherwise {},
            PageTable =
                if Value.Is(PageResult, List.Type)
                then Table.FromRecords(PageResult)
                else #table({}, {})
        in
            PageTable,

    AllPages = List.Transform(IterationList, each FetchPage(_)),
    Combined = Table.Combine(AllPages),

    Limited = if Limit <> -1 then Table.FirstN(Combined, Limit) else Combined,

    Result =
        if Fields <> null and Text.Length(Fields) > 0
        then Table.SelectColumns(Limited, Text.Split(Fields, ","))
        else Limited
in
    Result