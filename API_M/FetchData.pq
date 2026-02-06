(Endpoint as text, Page as number) =>
let
    Source =
        Json.Document(
            Web.Contents(
                API_Web,
                [
                    RelativePath = "v4/" & Endpoint,
                    Query = [page = Number.ToText(Page)]
                ]
            )
        ),

    result = try Source[data] otherwise {},

    Output =
        if Value.Is(result, List.Type)
        then Table.FromRecords(result)
        else #table({}, {})
in
    Output