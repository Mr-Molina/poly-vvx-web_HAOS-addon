## 2024-05-24 - Retaining ARIA Attributes on DOM Replacement
**Learning:** When dynamically replacing elements entirely (e.g., using `replaceChild` to swap a `tbody`), accessibility attributes like `aria-live` present on the original element are lost unless explicitly set on the newly created element before replacement.
**Action:** Always verify that newly created replacement elements re-apply necessary ARIA roles, states, and properties to maintain accessibility continuity.
