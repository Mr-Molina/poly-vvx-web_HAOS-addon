## 2024-05-24 - Retaining ARIA Attributes on DOM Replacement
**Learning:** When dynamically replacing elements entirely (e.g., using `replaceChild` to swap a `tbody`), accessibility attributes like `aria-live` present on the original element are lost unless explicitly set on the newly created element before replacement.
**Action:** Always verify that newly created replacement elements re-apply necessary ARIA roles, states, and properties to maintain accessibility continuity.

## 2024-11-20 - Visual Feedback on Low-Power Devices
**Learning:** On low-power embedded devices (like the Poly VVX), initial network requests can take time. Providing an animated loading state (like a CSS `@keyframes pulse`) is critical to assure the user the app isn't frozen.
**Action:** Always include immediate, animated visual feedback for initial loading states in embedded applications, using constrained styles like subdued colors (#aaa) where appropriate.