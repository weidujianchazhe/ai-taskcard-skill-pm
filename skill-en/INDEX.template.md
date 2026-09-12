# [PROJECT_NAME] · Record Index (INDEX)

> Version v1.0.1

> **Type markers**: `[handoff]` chain node (has a next step) — takeover reads along it, current relevant work context / `[done]` completed — takeover does not read it, only review/archiving does / `[dropped]` dropped requirement — do not read, leave a trace so it is not accidentally redone later (**dropping is decided by the manager; an AI never drops on its own — it only leaves the trace, never executes**).
> **Confidence label**: history that came from a session summary (legacy project onboarding) is marked "session summary"; formal work records are marked "formal".
> **Project work records only**: the skill's own affairs (retrospective / version / recovery registration) are not logged in this file — they go to REVIEWS.md (meta-management routing).
> **Double-write mechanism**: the main file keeps only the most recent N rows (N configured in MAP, default 20); every end-of-work **writes the main file and the archive file at the same time** (archives\INDEX_archived.md, the single full index); when the main file exceeds N rows, the old rows are **moved into** the archive file (the archive file is never deleted) — **rows are never lost, never physically deleted**. Row-count annotation and adjustment wording are in SKILL.md section 6.
> **Daily reading**: a taking-over AI reads only the N rows of the main file by default; if that is not enough, or for the full history → the archive file (the single full index).

| ID | Date | Type | Topic | AI | Handoff file |
|---|---|---|---|---|---|
| XXNNNN | YYYY-MM-DD | [handoff] | [ONE_LINE_SUMMARY] | {PLATFORM}-{AI_NAME}-{SHORT_CODE} | reports\xxx.md |
| XXNNNN | YYYY-MM-DD | [done] | [ONE_LINE_SUMMARY] | {PLATFORM}-{AI_NAME}-{SHORT_CODE} | reports\xxx.md |
| XXNNNN | YYYY-MM-DD | [dropped] | [ONE_LINE_SUMMARY + reason] | {PLATFORM}-{AI_NAME}-{SHORT_CODE} | reports\xxx.md |

> ID rules: `XXNNNN` (two letters = category + four digits = sequence number) — a branch letter must be registered in the MAP "branch numbering registry" before first use, to avoid collisions; within a branch the digits increase strictly **by numeric value** (EX10000 > EX9999); **the ID is the record/version sequence number (incremented at every end-of-work) — a task card's stable identity is its file name, and the ID field on a card refers only to the current version**. Conflict resolution: within a branch the larger numeric value overwrites the smaller; across branches IDs are not compared and timestamps do not decide — both sides leave a record in their own reports and hand it to the manager for a decision, timestamps are supporting evidence only (cross-platform clocks are untrustworthy); **collision retry**: if verify-after-write finds that the same ID already exists in the same branch → the later writer adds +1 to its ID, rewrites the row and leaves a trace in its own reports.
> **reports file archiving**: once the number of reports reaches the MAP "reports archive threshold" (default 20), the oldest is archived into archives\ — archived reports files do not take part in the active chain numbering, and the "Handoff file" column of the matching INDEX row is updated to point into archives\.
> Extreme case: if a single branch passes 9999, the number simply continues to five digits by numeric value (EX9999 → EX10000); comparison is always numeric, never string-based; if a new cycle is needed, archive first, restart the same branch from 0001 and register the new cycle in MAP.
> Handoff column: inside the same workspace write a relative path `reports\xxx.md`; for historical / cross-workspace records write the full path (e.g. `F:\...\old-workspace\reports\xxx.md`).
