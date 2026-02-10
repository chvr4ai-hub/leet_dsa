# WEB_SECURITY_THREATS

## Common Web Threats
Prevent known attack vectors in web applications.

**Real-time example (SQL injection):**
A search endpoint that concatenates user input into SQL can leak or delete data.

**Notes:**
- SQLi: use parameterized queries.
- XSS: escape output and use CSP.
- CSRF: use anti-CSRF tokens or same-site cookies.
- SSRF: restrict outbound access with allowlists.
- Input validation and rate limiting reduce abuse.
