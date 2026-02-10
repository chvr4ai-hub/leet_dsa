# PARTITIONING_AND_SHARDING

## Partitioning and Sharding
Split data across multiple nodes to scale horizontally.

**Real-time example (user profiles):**
Users are stored by `user_id` hash so each shard stores a subset of users.

**Notes:**
- Hash sharding spreads load evenly.
- Range sharding supports range queries but can create hotspots.
- Consistent hashing reduces data movement during scaling.
- Rebalancing is required when adding/removing shards.
