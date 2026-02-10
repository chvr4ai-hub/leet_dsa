# PAGINATION

## Pagination
Split large result sets into smaller pages.

**Real-time example (order history):**
A user loads 20 orders at a time instead of all orders at once.

**Notes:**
- Offset pagination is simple but slow for deep pages.
- Cursor pagination is stable and efficient for large datasets.
- Use a consistent sort order to avoid missing or duplicate items.
