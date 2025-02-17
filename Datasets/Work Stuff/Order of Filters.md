### 1. Report-level Filters
Applied to the entire report and affect all the pages within the report
### 2. Page-Level Filters
Applied to a specific page within the report 
### 3. Visual-Level Filters (including DAX)
Applied to individual visuals within a report page and affect only that specific visual. This is typically where DAX filters are used:
- Measures: These calculations are context-sensitive and will respond to the current filter context
- Calculated columns: These are evaluated at row-level during data refresh, so they don't change based on the filter context. They can only be filtered based on row context
### 4. Slicers
Although not technically a filter, slicers applied after all other filters