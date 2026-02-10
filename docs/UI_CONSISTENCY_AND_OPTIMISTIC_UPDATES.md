# UI_CONSISTENCY_AND_OPTIMISTIC_UPDATES

## UI Consistency and Optimistic Updates
Update the UI immediately, then confirm with the server later.

**Real-time example (like button):**
The UI shows +1 instantly; if the server rejects the action, the UI rolls back.

**Notes:**
- Use retries with idempotent requests.
- Handle conflicts with server truth.
- Eventual consistency is acceptable for non-critical UI state.
