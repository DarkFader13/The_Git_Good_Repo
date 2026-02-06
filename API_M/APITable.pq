(SourceTableName as text, optional SourceFields as text, optional SourceFilters as text) =>
let
    // Step 1: Source Table
    Source = Table.FromRows({{SourceTableName}}, type table [Table = text]),

    // Step 2: Fetch Data (pass SourceFields through)
    GetData = Table.AddColumn(Source, "Data", each TableFromJson([Table], SourceFields, SourceFilters)),

    // Step 3: Navigation to Table
    Navigation = GetData{0}[Data],

    // Step 4: Limit to 100 Rows (optional RowLimit logic can be added later)
    Extract = Navigation,

    // Step 5: Extract Ids from Records
    SafeExtract = SafeExtractIds(Extract)
in
    SafeExtract