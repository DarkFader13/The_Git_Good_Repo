(Table as text, optional Fields as text, optional Filters as text) =>
let
    // Step 1: Get total record count
    StatsSource = Json.Document(Web.Contents(ServiceNowApi,
        [RelativePath="api/now/stats/" & Table,
        Query=[sysparm_count="true"]
    ])),
    StatsResult = StatsSource[result],
    StatsCount = Number.FromText(StatsResult[stats][count]),
    Iterations = Number.RoundUp(StatsCount / 1000),

    // Step 2: Apply RowLimit cap if provided
    LimitIterations = if RowLimit <> -1 then Number.RoundUp(RowLimit / 1000) else Iterations,
    FinalIterations = if LimitIterations < Iterations then LimitIterations else Iterations,

    // Step 3: Generate list of iteration numbers
    IterationList = List.Numbers(1, FinalIterations, 1),

    // Step 4: Fetch data for each iteration
    FetchPage = (Iteration as number) =>
        let
            PageSource = Json.Document(Web.Contents(ServiceNowApi,
                [RelativePath="api/now/table/" & Table,
                Query=[
                    sysparm_offset = Number.ToText((Iteration - 1) * 1000),
                    sysparm_limit = "1000",
                    sysparm_display_value = "true"
                ] 
                & (if Fields <> null and Text.Length(Fields) > 0 then [ sysparm_fields = Fields ] else [])
                & (if Filters <> null and Text.Length(Filters) > 0 then [ sysparm_query = Filters ] else [])
            ])),
            PageResult = try PageSource[result] otherwise {},
            PageTable = if Value.Is(PageResult, List.Type) then Table.FromRecords(PageResult) else #table({}, {})
        in
            PageTable,

    // Step 5: Combine all pages
    AllPages = List.Transform(IterationList, each FetchPage(_)),
    CombinedTable = Table.Combine(AllPages),

    // Step 6: Apply row limit if provided
    Result = if RowLimit <> -1 then Table.FirstN(CombinedTable, RowLimit) else CombinedTable
in
    Result