# CACHING

## Caching (General)
Store computed or fetched data to serve future requests faster.

**Real-time example (product page):**
A product detail response is cached so repeated views do not hit the database each time.

**Notes:**
- Cache-aside: app reads cache, falls back to DB, then fills cache.
- Write-through: writes go to cache and DB together.
- Write-back: writes go to cache first, then DB later.
- TTLs and invalidation avoid stale data.
