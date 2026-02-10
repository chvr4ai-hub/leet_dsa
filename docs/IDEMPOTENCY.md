# IDEMPOTENCY

## Idempotency (General)
An operation is idempotent if performing it multiple times has the same effect as performing it once.

**Real-time example (payments):**
If a customer clicks "Pay" multiple times due to a slow/internet issue, a non-idempotent system might create multiple charges or duplicate orders. With idempotency, repeated clicks result in a single charge/order, and the system returns the same result each time.

## Idempotency in APIs
An API request is idempotent when repeated identical requests do not change the final state beyond the first request.

**Notes:**
- Typically idempotent: `GET`, `PUT`, `DELETE` (same request repeated yields the same state).
- Typically non-idempotent: `POST` (may create multiple resources).
- Idempotency keys: clients send a unique key (e.g., `Idempotency-Key`) so the server can safely deduplicate repeated requests like payments or order creation.
