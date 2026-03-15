## 2024-05-24 - Retaining ARIA Attributes on DOM Replacement
**Learning:** When dynamically replacing elements entirely (e.g., using `replaceChild` to swap a `tbody`), accessibility attributes like `aria-live` present on the original element are lost unless explicitly set on the newly created element before replacement.
**Action:** Always verify that newly created replacement elements re-apply necessary ARIA roles, states, and properties to maintain accessibility continuity.

## 2024-11-20 - Maximizing Screen Real Estate on Embedded Browsers
**Learning:** Default browser body margins (typically 8px) consume a disproportionate amount of screen real estate on small embedded screens (like the 320x240 Poly VVX). This can cause unnecessary text truncation or line breaks.
**Action:** Always explicitly reset `body` margin to `0` and apply a minimal, controlled padding (e.g., `2px`) for embedded web interfaces to maximize usable space while preventing text from touching the physical screen bezel.
