## RDB's

### Fact table:
Has Primary & Foreign Keys,
Opt for lowest level of aggregation/highest grain for performance

### Dimension Table:
Only Individual, non-overlapping data elements,
No Foreign keys or Aggregations
Use for filtering, labelling & grouping

### Factless Table:
Fact Table with only foreign keys.
Used for bridging many to many relationships (Many to Many -> One to Many to One)
Transactional Fact Table

### Grain: 
Dimension of foreign keys

### Cardinality (of column): 
No. of Unique entries

### Fact Table types (Exactly 3):
- Transactional: Record of every entity (Low Grain)
- Snapshot: Record for different points in time (Mid Grain)
- Accumulated: Record for every process step (High Grain)

### Table Sub-Types:
Consolidated: Merge of 2 tables
Conformed Tables: 2 tables at a different grain
Aggregated: Table with some level of aggregation
Factless: Fact table with no measures

### Partitioned-Hybrid Table:
- Composite Fact/Dimension table for Hybrid star-snowflake schema
- Can partition table directly into separate fact & dimension table
- Requires a bridge for each filter for aggregated dimension measure Fact Partition (Foreign IDs, Dates), (Dimensions, Descriptors}

## DAX 
Filters work through function but NOT through variables

Limit pages to 30points assuming:
- Cards: 1
- Gauges: 2
- Charts: 3
- Maps: 3
- Grids: 5