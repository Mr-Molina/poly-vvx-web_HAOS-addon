## 2024-05-18 - Python Requests Connection Pooling
**Learning:** In a Python Flask application that makes sequential API calls to a local service (like the Home Assistant Supervisor API) inside a loop, using `requests.get()` repeatedly opens and closes a new TCP connection for each request.
**Action:** When making multiple sequential HTTP requests to the same host, always initialize a `requests.Session()` object outside the loop and use `session.get()` inside. This enables TCP connection pooling, drastically reducing latency and network overhead.

## 2024-05-24 - Python ThreadPoolExecutor for Sequential I/O Bottlenecks
**Learning:** In the Flask application, looping through sequential API requests is a significant bottleneck. The network latency `x` for `n` API requests turns into `O(n * x)` total execution time, unnecessarily blocking the main thread.
**Action:** Use Python's `concurrent.futures.ThreadPoolExecutor.map()` to run sequential independent I/O-bound API requests concurrently. This scales the execution time down to `O(max(x))` while maintaining the original order.
