# DISTRIBUTED_SYSTEMS_FUNDAMENTALS

## Leader Election
Pick a single coordinator to avoid conflicts.

**Real-time example:**
Only one node generates order numbers so there are no duplicates.

## Consensus (Raft)
Nodes agree on a shared log of changes.

**Real-time example:**
A feature-flag service uses consensus so all nodes apply the same config updates in the same order.

## Quorum
Read/write operations require a majority of nodes.

**Real-time example:**
In a 3-node store, a write must succeed on 2 nodes before it is accepted.

## Split-Brain
Two leaders exist due to a partition, causing conflicting writes.

**Real-time example:**
Two primaries accept orders, creating duplicate order IDs.

**Notes:**
- Use leases, fencing tokens, and quorum to prevent split-brain.
