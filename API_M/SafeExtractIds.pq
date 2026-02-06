(inputTable as table) as table =>
    Table.TransformColumns(
        inputTable,
        List.Transform(
            Table.ColumnNames(inputTable),
            (col) => {
                col,
                each try
                    if Value.Is(_, type record) then
                        if Record.HasFields(_, "value") then
                            Record.Field(_, "value")
                        else if Record.HasFields(_, "link") then
                            List.Last(Text.Split(
                                Record.Field(_, "link")
                            , "/"))
                        else null
                else Text.From(_)
                otherwise ""
            }
        )
    )