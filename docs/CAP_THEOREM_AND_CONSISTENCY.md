# CAP_THEOREM_AND_CONSISTENCY

## CAP Theorem
In the presence of a network partition, a distributed system must choose between Consistency and Availability.

**Real-time example (payments vs catalog):**
During a network split, a payment service may choose Consistency (reject writes to avoid double charges), while a product catalog may choose Availability (serve slightly stale data so users can browse).

## Consistency Models
Consistency defines how quickly all clients see the same data.

**Real-time example (bank balance):**
With strong consistency, every balance check shows the latest transfer. With eventual consistency, a recent transfer might not appear for a short time.

**Notes:**
- Strong consistency: latest write visible immediately.
- Eventual consistency: replicas converge over time.
- Linearizability vs serializability: real-time order vs transaction order.
