Variables Used:
[[FixedDate]], [[Date (Tracked)]], [[Date (Snapshot)]], [[Measure]]

Use:
Staging measure for further measures within the reporting period (extraction period / system image period) ,
Use [Measure] directly if there's no reporting requirements on other date fields or is snapshot agnostic / live

Purpose:
Extracts a measure for fixed snapshot period, when Date(Snapshot) = FixedDate

```dax
VAR Results =
CALCULATE ([Measure]
, 'Fact Table'[Date(Snapshot)] = [FixedDate]
,CROSSFILTER('Calendar Global', 'Fact Table'[Date (Snapshot)], None)
)

Return Results
```
