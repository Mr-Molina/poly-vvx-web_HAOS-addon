## 2024-05-18 - Python Requests Connection Pooling
**Learning:** In a Python Flask application that makes sequential API calls to a local service (like the Home Assistant Supervisor API) inside a loop, using `requests.get()` repeatedly opens and closes a new TCP connection for each request.
**Action:** When making multiple sequential HTTP requests to the same host, always initialize a `requests.Session()` object outside the loop and use `session.get()` inside. This enables TCP connection pooling, drastically reducing latency and network overhead.

## 2024-05-18 - Home Assistant API Response Caching
**Learning:** When multiple local clients (e.g. multiple VVX phones) poll an endpoint, the backend translates this into multiple identical backend requests to the HA Supervisor API.
**Action:** Add a simple in-memory cache with a short TTL (e.g., 15s) for the `/api` endpoint to drastically reduce load on the Home Assistant core.
