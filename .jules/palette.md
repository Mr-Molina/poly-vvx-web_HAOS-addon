## 2024-05-24 - Retaining ARIA Attributes on DOM Replacement
**Learning:** When dynamically replacing elements entirely (e.g., using `replaceChild` to swap a `tbody`), accessibility attributes like `aria-live` present on the original element are lost unless explicitly set on the newly created element before replacement.
**Action:** Always verify that newly created replacement elements re-apply necessary ARIA roles, states, and properties to maintain accessibility continuity.

## 2024-11-20 - Actionable Empty States on Embedded Screens
**Learning:** Designing empty/error states for embedded desk phone screens requires explicit, actionable text (like "Check config.yaml") since users cannot access debugging tools on the device itself.
**Action:** Always include actionable resolution steps in embedded UI error/empty states, and use subdued colors (#aaa) to distinguish them from active sensor data.
