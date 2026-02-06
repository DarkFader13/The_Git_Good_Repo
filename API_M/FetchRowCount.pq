
let
  Query = (Table as text, optional Fields as text, optional Filters as text) =>
let
    Source = Json.Document(Web.Contents(Api,
    [RelativePath="api/now/stats/"&Table,
    Query=[sysparm_limit="10",
    sysparm_count="true"]
    & (if Fields <> null and Text.Length(Fields) > 0 then [ sysparm_fields = Fields ] else [])
    & (if Filters <> null and Text.Length(Filters) > 0 then [ sysparm_query = Filters ] else [])
   ])),
    result = Source[result],
    stats = result[stats],
    count = stats[count],
    iterations_list = List.Numbers(1,(Number.FromText(count)/1000),1),
    iterations_table = Table.FromList(iterations_list, Splitter.SplitByNothing(), {"Iteration"}, null, ExtraValues.Error),
    change_types = Table.TransformColumnTypes(iterations_table,{{"Iteration", Int64.Type}})
in
    change_types
in
  Query