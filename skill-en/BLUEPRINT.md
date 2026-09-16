# Design Blueprint (BLUEPRINT)

> Version v1.2.0

> This file IS the authoritative quick-reference of the design blueprint (the 6 points below cover the core mechanisms and are valid inside the package). The HTML version `project-management-lite-blueprint.html` is a supplementary design document outside the package — this skill package is pure Markdown and does not carry the HTML; a publisher only needs to place it somewhere visible outside the package (e.g. the repository root), and its absence does not affect operation.

## Design points (quick reference)

1. **Across obstacles**: multiple AIs / platforms / time / projects — the taking-over AI understands the work at a lower reading cost
2. **Read on demand**: a project may be complex and heavy, yet takeover reads only the task-relevant part (one task card ± 1 reports)
3. **Creation is the universal first step**: every project creates the management directory first; after that the skill is never re-read
4. **Legacy onboarding**: lightweight registration + progressive tidying, no deep historical reorganization (LEGACY_ONBOARDING.md)
5. **Human-read zone + AI zone**: human-read zone (3-line summary) + AI zone (work coordinates); the human-read zone is auto-generated from the AI zone and rewritten in sync on overwrite updates
6. **Skill size principle**: only add what existing mechanisms cannot cover; the protocol registers, it does not package implementations
