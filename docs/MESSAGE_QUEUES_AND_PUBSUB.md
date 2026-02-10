# MESSAGE_QUEUES_AND_PUBSUB

## Message Queues and Pub/Sub
Decouple services by sending messages asynchronously.

**Real-time example (order workflow):**
Order service publishes "order_created"; inventory and email services consume it independently.

**Notes:**
- At-least-once delivery may create duplicates; consumers must dedupe.
- Exactly-once is hard; aim for idempotent consumers.
- Backpressure protects downstream services from overload.
