(inputTable as table) as table =>
    Table.TransformColumns(
        inputTable,
        List.Transform(
            Table.ColumnNames(inputTable),
            (col) => {
                col,
                each try
                    if Value.Is(_, type record) then
                        // take "string" field if exists
                        if Record.HasFields(_, "string") then Record.Field(_, "string") else null
                    else if Value.Is(_, type list) then
                        // list of records → extract "name" and join
                        let
                            Names =
                                List.Transform(
                                    List.Select(_, each Value.Is(_, type record)),
                                    (r) => try Record.Field(r, "name") otherwise null
                                ),
                            CleanNames = List.RemoveNulls(Names)
                        in
                            Text.Combine(CleanNames, ", ")
                    else
                        Text.From(_)
                otherwise null
            }
        )
    )