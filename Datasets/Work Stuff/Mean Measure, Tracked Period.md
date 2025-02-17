Variables Used:
[[Calendar Global]], [[Time-Series]], [[Measure, Tracked Period]], [[FixedDate]]

```dax
VAR StartRange = EOMONTH([FixedDate], -#)

VAR DateRange = CALCULATE(MAX('Calendar Global'[Date]), FILTER('Calendar Global', 'Calendar Global'[Date] <= [FixedDate]))

VAR Results =
	CALCULATE([Measure, Snapshot Period]
	, CROSSFILTER('Calendar Global'[Date], 'Fact Table'[Date (Tracked)], None)
)/#

Return IF(StartRange < DateRange && DateRange <= FixedDate, Results, BLANK())
```