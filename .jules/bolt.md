## 2024-05-18 - Python Requests Connection Pooling
**Learning:** In a Python Flask application that makes sequential API calls to a local service (like the Home Assistant Supervisor API) inside a loop, using `requests.get()` repeatedly opens and closes a new TCP connection for each request.
**Action:** When making multiple sequential HTTP requests to the same host, always initialize a `requests.Session()` object outside the loop and use `session.get()` inside. This enables TCP connection pooling, drastically reducing latency and network overhead.

## 2024-05-19 - Python Requests Concurrent Fetching
**Learning:** Sequential network requests inside a loop bind the endpoint's response time linearly to the number of requests (O(N) latency).
**Action:** Use `concurrent.futures.ThreadPoolExecutor` with `executor.map()` to fetch network responses concurrently. This transforms the time complexity of the wait to O(max(latency)), greatly speeding up the API response.
