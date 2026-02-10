# LOAD_BALANCING

## Load Balancing
Distribute incoming traffic across multiple servers.

**Real-time example (web app):**
Requests are routed to the least busy server so no single node is overloaded.

**Notes:**
- L4: routes based on IP/port.
- L7: routes based on HTTP paths/headers.
- Health checks remove unhealthy nodes.
- Sticky sessions keep a client on the same server when needed.
