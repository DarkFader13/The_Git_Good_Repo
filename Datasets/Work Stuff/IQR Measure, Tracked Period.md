Variables Used:
[[Calendar Global]], [[Time-Series]], [[Measure, Tracked Period]], [[FixedDate]]

```dax
VAR StartRange = EOMONTH([FixedDate], -#)
VAR DateRange = CALCULATE(MAX('Calendar Global'[Date]), FILTER('Calendar Global', 'Calendar Global'[Date] <= [FixedDate]))

VAR Q1 =
	CALCULATE(PERCENTILE.INC('Time-Series', [Measure, Tracked Period], 0.25)
	, CROSSFILTER('Calendar Global'[Date], 'Fact Table'[Date (Tracked)], None)
)

VAR Q3 =
	CALCULATE(PERCENTILE.INC('Time-Series', [Measure, Tracked Period], 0.75)
	, CROSSFILTER('Calendar Global'[Date], 'Fact Table'[Date (Tracked)], None)
)

Return IF(StartRange < DateRange && DateRange <= [FixedDate], Q3 - Q1, BLANK())
```