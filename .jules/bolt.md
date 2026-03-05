## 2024-05-18 - Python Requests Connection Pooling
**Learning:** In a Python Flask application that makes sequential API calls to a local service (like the Home Assistant Supervisor API) inside a loop, using `requests.get()` repeatedly opens and closes a new TCP connection for each request.
**Action:** When making multiple sequential HTTP requests to the same host, always initialize a `requests.Session()` object outside the loop and use `session.get()` inside. This enables TCP connection pooling, drastically reducing latency and network overhead.
## 2024-05-18 - Flask API Connection Pooling and Concurrency
**Learning:** Sequential network calls inside a Flask route using `requests.get()` scale latency linearly with O(N).
**Action:** Use `concurrent.futures.ThreadPoolExecutor` mapped to a helper function, passing the target variables from the main request thread. This works seamlessly with a pre-configured `requests.Session()` which handles threaded network pools natively, significantly reducing total response latency from O(N) to roughly O(1).
