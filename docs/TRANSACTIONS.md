# TRANSACTIONS

## Transactions
Group operations so they either all succeed or all fail.

**Real-time example (money transfer):**
Debit account A and credit account B in a single transaction to avoid partial transfers.

**Notes:**
- Isolation levels trade off consistency vs performance.
- Deadlocks can occur; use timeouts and retry.
- 2PC coordinates across databases; sagas coordinate across services.
