# Validation report — regenerable Impact Radar

Validated behavior:

- `static-demo.html` can be regenerated in BASE mode with `impactData = null`.
- Running the renderer for `pricing-service / contract` overwrites the same HTML and produces ROOT=`pricing-service`, risk=81 and decision=`NO-GO`.
- Running it again for `order-db / schema` overwrites the prior scenario and produces ROOT=`order-db`.
- Resetting without `--component` returns the same HTML to BASE mode.
- HTML validator confirms graph container, payload, SVG renderer, node/edge renderer, offline operation and mode markers.
- Impact engine tests: 4 passed.
- JavaScript syntax check: passed when Node.js is available.

The ZIP is delivered with `demo_arch_radar/static-demo.html` in BASE mode so the first Copilot prompt visibly evolves the radar.
