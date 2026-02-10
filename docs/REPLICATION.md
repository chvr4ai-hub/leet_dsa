# REPLICATION

## Replication
Keep multiple copies of data for availability and read scaling.

**Real-time example (read replicas):**
Product pages read from replicas while writes go to the primary database.

**Notes:**
- Synchronous replication reduces data loss but adds latency.
- Asynchronous replication improves latency but may have lag.
- Failover promotes a replica if the primary fails.
