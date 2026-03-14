## 2024-03-02 - Async Table Content Accessibility
**Learning:** Tables that are dynamically updated via JS polling (like the Home Assistant sensor dashboard) need `aria-live` regions on the container (`<tbody>`) so screen readers can announce new data when it arrives. Static placeholder content (like "Sensor 42") in async tables is confusing for users on slow connections; a clear "Loading..." state is essential.
**Action:** When working with async data tables that poll for updates, always add `aria-live="polite"` to the container and replace hardcoded placeholder rows with a semantic loading state (`colspan` matching the table width).

## 2024-11-20 - Retaining ARIA Attributes on DOM Replacement
**Learning:** When dynamically replacing elements entirely (e.g., using `replaceChild` to swap a `tbody`), accessibility attributes like `aria-live` present on the replaced element are lost, causing screen reader announcements to fail.
**Action:** Always place `aria-live` attributes on a static parent element that is not replaced during data updates, rather than on the dynamically replaced child element itself.