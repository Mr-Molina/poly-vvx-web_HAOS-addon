## 2024-05-24 - Retaining ARIA Attributes on DOM Replacement
**Learning:** When dynamically replacing elements entirely (e.g., using `replaceChild` to swap a `tbody`), accessibility attributes like `aria-live` present on the original element are lost unless explicitly set on the newly created element before replacement.
**Action:** Always verify that newly created replacement elements re-apply necessary ARIA roles, states, and properties to maintain accessibility continuity.

## 2024-11-20 - Visual Feedback for Background Updates on Embedded Devices
**Learning:** On simple embedded screens where user interactions are sparse, periodic background data refreshes can feel abrupt and disorienting. Applying a short, CSS-only fade-in animation on DOM element replacement provides smooth, lightweight visual feedback that data has updated without needing complex JS logic.
**Action:** Always consider using lightweight CSS animations (e.g., `@keyframes fadeIn`) when replacing data containers dynamically on low-power displays to improve the perceived fluidity of updates.
