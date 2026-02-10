# RATE_LIMITING

## Rate Limiting
Restrict how often a client can perform an action to protect the system.

**Real-time example (login attempts):**
Limit a user to 5 login attempts per minute to reduce brute-force attacks.

**Notes:**
- Token bucket: allows bursts up to a limit.
- Leaky bucket: smooths traffic at a fixed rate.
- Sliding window: more accurate windowed limits.
- Respond with `429 Too Many Requests` and retry info.
