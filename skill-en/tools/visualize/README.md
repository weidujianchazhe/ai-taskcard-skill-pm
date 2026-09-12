# Visualization spec (visualize\)

> **Platform-agnostic spec**: an AI on any platform can express structural relations with deterministic charts/diagrams (not dependent on any platform-specific visualization solution).
> **Execution principles**: analyze to the best of your ability · stop when the point is made · resource restraint · complete information is the floor.
> **No capability tiers**: no tiering by capability is required; analyze to the maximum of the AI's own ability while controlling token/compute usage.

---

## 1. Applicability and routing

| Content | Presentation |
|---|---|
| Trend/share/ranking/distribution/comparison (precise data) | data chart (ECharts-type) |
| Flow/mechanism/architecture/relations/timeline/state machine | structural diagram (HTML/SVG-type) |
| Original-image evidence (location/area/path must be pointed out) | keep the original image + annotate |
| Cannot be drawn clearly and reliably | fall back to text (do not fall back on an unverifiable image) |

## 2. Principles

1. **Use charts for precise data**; use diagrams for structural relations; fall back to text when it cannot be drawn clearly and reliably
2. **Static first**: do not add interaction where a static image suffices; enable interaction only when the operation can reveal a new state/causality/process
3. **Data verifiable**: real numbers must come from the input or a verification result, never fabricated; example data is marked explicitly
4. **Stop when the point is made**: do not chase excessive polish/complex animation; control resource usage
5. **Complete information is the floor**: axes/units/legends/scope notes are not omitted

## 3. Boundaries

- Does not take on posters/avatars/realistic illustration/artistic creation
- Maps/geographic tracks/administrative-division graphics are disallowed (use text or non-map expression instead)
- Deliver attachments (PDF/PPT/Word/Excel/image) with the corresponding file capability; do not fake them with a renderer
- When an original image serves as evidence keep it intact; do not crop out key context, do not substitute a schematic

## 4. Execution restraint (token/compute usage)

- A single visualization ≤ 300 lines; split complex content
- Prefer simple implementation (plain HTML/SVG/Canvas); have a static fallback when an external library fails
- Gauge output length: stop once the information is clear; no decorative embellishment
