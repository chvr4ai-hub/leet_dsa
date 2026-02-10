# AUTHN_AUTHZ

## Authentication and Authorization
Authentication verifies identity; authorization determines permissions.

**Real-time example (admin portal):**
Users log in with a JWT (authn), then only admins can access user management (authz).

**Notes:**
- OAuth2 handles delegated access.
- JWTs carry signed claims.
- RBAC uses roles; ABAC uses attributes.
