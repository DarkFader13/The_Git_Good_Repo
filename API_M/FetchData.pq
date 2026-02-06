(Table, Iteration) =>
let


    // Load data from API
    Source = Json.Document(Web.Contents(Api,
        [RelativePath="" & Table,
        Query=[
            sysparm_offset=Number.ToText((Iteration-1)*1000),
            sysparm_limit="1000",
            sysparm_display_value="true"
        ]])),
    
    // Safely extract and convert result to table
    result = try Source[result] otherwise {},
    #"Converted to Table" = if Value.Is(result, List.Type) then Table.FromRecords(result) else #table({}, {})
in
    #"Converted to Table"