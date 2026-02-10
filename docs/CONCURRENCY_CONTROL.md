# CONCURRENCY_CONTROL

## Concurrency Control
Prevent conflicting updates when multiple clients write simultaneously.

**Real-time example (inventory update):**
Two buyers try to purchase the last item. Concurrency control ensures only one purchase succeeds.

**Notes:**
- Optimistic locking uses version checks and retries.
- Pessimistic locking blocks others until the lock is released.
- Choose based on conflict rate and latency tolerance.
