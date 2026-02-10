# INDEXING

## Indexing
Use data structures to speed up lookups at the cost of extra storage and write time.

**Real-time example (email lookup):**
An index on `email` lets login queries find users quickly without scanning the table.

**Notes:**
- B-tree indexes are common for range and equality queries.
- Composite indexes speed up multi-column filters.
- Covering indexes avoid extra table lookups.
