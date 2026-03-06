## 2024-05-18 - Python Requests Connection Pooling
**Learning:** In a Python Flask application that makes sequential API calls to a local service (like the Home Assistant Supervisor API) inside a loop, using `requests.get()` repeatedly opens and closes a new TCP connection for each request.
**Action:** When making multiple sequential HTTP requests to the same host, always initialize a `requests.Session()` object outside the loop and use `session.get()` inside. This enables TCP connection pooling, drastically reducing latency and network overhead.
## 2026-03-06 - Poly VVX Embedded Browser Compatibility
**Learning:** The target Polycom VVX IP phones have extremely constrained, potentially outdated embedded WebKit browsers. Using modern ES6 JavaScript syntax (like `let` or `const`) can cause `SyntaxError` crashes, breaking the page entirely.
**Action:** Always write strictly ES5 compatible JavaScript (e.g., using `var` instead of `let`) when adding logic to the frontend templates to ensure maximum compatibility with the legacy embedded browsers.
