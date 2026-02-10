# DATA_MODELING

## Data Modeling
Structure data to match how it is read and written.

**Real-time example (orders):**
Store order headers separately from order items so item lists are queried efficiently.

**Notes:**
- Normalization reduces duplication but adds joins.
- Denormalization speeds reads but complicates writes.
- Model around your most frequent queries.
