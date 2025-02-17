Variables Used:
[[Snapshot Period, Measure]], [[Date (Tracked)]]

Use:
Calculates 

```dax
Measure, Period =
VAR P = DATESINPERIOD('Calendar Global'[Date], [FixedDate], -#, PERIOD)
CALCULATE (
	[Snapshot Period, Measure]
	, 'Fact Table'[Date (Tracked)] in P
	--, Filters
	,USERELATIONSHIP('Calendar Global', 'Fact Table'[Date(Tracked)])
)
RETURN Results
```