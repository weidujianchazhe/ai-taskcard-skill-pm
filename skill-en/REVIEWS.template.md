# Skill retrospective log (meta-management loop)

> **Serves**: the project-management skill itself (not a retrospective of project work — project summaries go to reports\).
> **Triggers**: ① automatic event capture — whenever any "recovery action" occurs (task card rebuilt / STATE restored / broken handoff link / out-of-scope file change, ...), log a blocker line in passing (no human needs to start it); ② manual retrospective — project wrap-up / periodic retrospective / hitting an obstacle in use.
> **How to record**: append-style, four sections per round, one sentence each (prevents bloat).
> **Storage location (meta-management routing)**: every retrospective event is appended to **`REVIEWS.md` at the project workspace root** (instantiated from this template at initialization) — **never written to reports\, never logged in INDEX**. Entries marked "recommend escalation" in the workspace REVIEWS.md are manually excerpted by the manager back into the **skill source package** for unified handling; the source package accepts only refined, general improvements (kept clean and shareable); when an improvement lands, sync the source package templates and increment the version.
> **Decision maker**: the manager (the actual owner of the project or the skill, registered in the MAP environment section at initialization); deferred items are automatically reopened for review on the "3rd recurrence".
> **Closed loop**: blocker → root cause → suggestion → disposition → landed (per the SKILL maintenance rules: change the authoritative source SKILL.md first → sync the README/MAP derived snapshots → all three versions consistent) → then use.

---

## Retrospective #N  YYYY-MM-DD

### Blocker (encountered while using the skill)

- [blocker description + impact: reading cost / error rate / level of confusion]

### Root cause (why it happened, one line)

- [attribute it to a concrete mechanism/file/field; write "to be investigated" if it is not found — never skip the root cause and jump straight to a suggestion]

### Improvement suggestion

- [suggestion + where to change: template / protocol / tools area / naming] (a suggestion must pass the skill size principle: only add what existing mechanisms cannot cover)

### Disposition

- [adopt / defer / reject — decided by the manager] (one-line reason; a deferral must state "review on recurrence #N", a rejection must state "under what conditions to re-evaluate")
