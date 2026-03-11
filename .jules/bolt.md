## 2024-05-18 - Python Requests Connection Pooling
**Learning:** In a Python Flask application that makes sequential API calls to a local service (like the Home Assistant Supervisor API) inside a loop, using `requests.get()` repeatedly opens and closes a new TCP connection for each request.
**Action:** When making multiple sequential HTTP requests to the same host, always initialize a `requests.Session()` object outside the loop and use `session.get()` inside. This enables TCP connection pooling, drastically reducing latency and network overhead.

## 2024-05-24 - HTTP ETag for API Polling Bandwidth Optimization
**Learning:** Embedded devices (like the Poly VVX) polling an API every 30 seconds often receive identical JSON payloads if the underlying sensor states haven't changed. Sending the full payload repeatedly wastes network bandwidth and forces the client to re-parse the JSON unnecessarily.
**Action:** Implement HTTP ETag hashing on the backend. By generating an MD5 hash of the payload (`response.set_etag`) and using Flask's `response.make_conditional(request)`, the backend automatically responds with `304 Not Modified` when the client sends a matching `If-None-Match` header, drastically reducing bandwidth and client processing overhead.
