# Design Blueprint (BLUEPRINT)

> Version v1.2.1

> This file IS the authoritative quick-reference of the design blueprint (the points below cover the core mechanisms and are valid inside the package). The HTML version `project-management-lite-blueprint.html` is a supplementary design document outside the package — this skill package is pure Markdown and does not carry the HTML; a publisher only needs to place it somewhere visible outside the package (e.g. the repository root), and its absence does not affect operation.

## Design points (quick reference)

1. **Across obstacles**: multiple AIs / platforms / time / projects — the taking-over AI understands the work at a lower reading cost
2. **Read on demand**: a project may be complex and heavy, yet takeover reads only the task-relevant part (one task card ± 1 reports)
3. **Creation is the universal first step**: every project creates the management directory first; after that the skill is never re-read
4. **Legacy onboarding**: lightweight registration + progressive tidying, no deep historical reorganization (LEGACY_ONBOARDING.md)
5. **Human-read zone + AI zone**: human-read zone (3-line summary) + AI zone (work coordinates); the human-read zone is auto-generated from the AI zone and rewritten in sync on overwrite updates
6. **Skill size principle**: only add what existing mechanisms cannot cover; the protocol registers, it does not package implementations
7. **Stable identifiers (v1.2.0)**: `TASK-ID` / `EVENT-ID` / `DESIGN-ID` are immutable after creation; file names may change, but references use only IDs
8. **Design lifecycle (v1.2.0)**: design cards (DESIGN-ID + state machine + lifecycle gate) — **unapproved design cards must not generate execution cards**, and approval/rejection/retirement each write an EVENT-ID
9. **Three modes (v1.2.0)**: `light` / `standard` / `coordination` — each with its own file set, roles and checks, and upgrade path; upgrading expands the set, history is never back-filled
10. **Single-writer and consistency (v1.2.0)**: permission matrix + single-writer responsibility; CAS / atomic writes / conflict files `CONFLICT_*.md`; read revision/hash before writing, verify after writing; cross-branch conflicts are not arbitrated by timestamp
11. **Two ceiling devices (v1.2.1)**: "INDEX main-file row count" and "STATE character limit" — both are **ceiling devices for the reading cost of a taking-over AI, not expandable capacity**; when the limit is exceeded, move history sections into reports\ and archive files per the overwrite-style discipline, and the layered reading structure must never be merged
12. **Boundary statement (v1.2.0)**: this package defines only the generation specification for protocols, templates, and scripts; it does not implement or enable by default any runtime daemon, auto-archiver, permission system, or continuous supervision
