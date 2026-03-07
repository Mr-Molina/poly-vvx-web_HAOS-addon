## 2024-05-18 - Python Requests Connection Pooling
**Learning:** In a Python Flask application that makes sequential API calls to a local service (like the Home Assistant Supervisor API) inside a loop, using `requests.get()` repeatedly opens and closes a new TCP connection for each request.
**Action:** When making multiple sequential HTTP requests to the same host, always initialize a `requests.Session()` object outside the loop and use `session.get()` inside. This enables TCP connection pooling, drastically reducing latency and network overhead.

## 2024-05-24 - DOM Rebuilds on Low-Power Embedded Browsers
**Learning:** Constantly replacing large DOM fragments (like `tbody`) using `replaceChild` causes expensive reflows and garbage collection, which is a significant performance bottleneck on devices with low-power embedded browsers like the Poly VVX.
**Action:** When polling for data updates, always check if the number of elements has changed. If the structure is the same, iterate over existing DOM elements and only update their `textContent` if the data differs. This prevents unnecessary reflows and reduces CPU/memory usage.
