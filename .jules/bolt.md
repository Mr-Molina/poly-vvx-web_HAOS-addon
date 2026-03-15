## 2024-05-18 - Python Requests Connection Pooling
**Learning:** In a Python Flask application that makes sequential API calls to a local service (like the Home Assistant Supervisor API) inside a loop, using `requests.get()` repeatedly opens and closes a new TCP connection for each request.
**Action:** When making multiple sequential HTTP requests to the same host, always initialize a `requests.Session()` object outside the loop and use `session.get()` inside. This enables TCP connection pooling, drastically reducing latency and network overhead.

## 2024-05-24 - Avoiding Redundant JSON parsing and DOM rebuilds
**Learning:** Polling an API on low-power embedded devices (like the Poly VVX browser) is expensive if the device has to parse identical JSON and completely reconstruct the DOM (`replaceChild`) every 30 seconds even when no sensor data has actually changed.
**Action:** Cache the raw HTTP response text (`xhr.responseText`) on the client. If the next polled response is an exact string match, return early to skip `JSON.parse` and the DOM rebuilding logic entirely. Ensure strictly ES5 compatible code (e.g., use `var`).
