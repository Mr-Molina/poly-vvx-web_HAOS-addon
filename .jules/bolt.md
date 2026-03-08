## 2024-05-18 - Python Requests Connection Pooling
**Learning:** In a Python Flask application that makes sequential API calls to a local service (like the Home Assistant Supervisor API) inside a loop, using `requests.get()` repeatedly opens and closes a new TCP connection for each request.
**Action:** When making multiple sequential HTTP requests to the same host, always initialize a `requests.Session()` object outside the loop and use `session.get()` inside. This enables TCP connection pooling, drastically reducing latency and network overhead.

## 2026-03-08 - Server-Side Rendering (SSR) for Time-to-Interactive
**Learning:** When serving simple UI directly to an embedded browser (like on the Poly VVX phone), fetching data on load with an immediate client-side AJAX call creates a substantial delay in Time-to-Interactive (TTI) since the page loads empty, parses JavaScript, executes an AJAX request, waits for a response, and then forces the browser to rebuild the DOM.
**Action:** Whenever a simple, data-driven web app loads its first state via AJAX immediately on page load, refactor the backend logic to retrieve that initial data *before* rendering the template, and pre-populate the HTML server-side (Server-Side Rendering). Only use client-side AJAX for subsequent polling.
