# [PROJECT_NAME] · Current State (STATE)

> Version v1.2.1

> Overwrite-style: keep only the latest forever, overwrite old content when modifying, never accumulate history. Ownership: updated by the AI currently responsible for the task card at end-of-work.
> Last updated: `YYYY-MM-DD HH:MM`

━━━ Human-read locator ━━━
Project: [ONE_LINE_POSITIONING]
Tasks: in progress [N] (card count in tasks\) · recently completed [one-line]
Directory guide: current → STATE · tasks · archive → reports · index → INDEX · meta → REVIEWS
━━━━━━━━━━━━━

## Current progress

- [one-line latest status (what was last completed / where it stands now; when parallel, the last one to finish overwrites this line)]

## Concurrency metadata

- owner: [TASK-ID / AI identity]
- revision: [integer]
- NORMALIZED-SHA256: [hash]
- write proof: [atomic rename / CAS; conflict path or `—`]

## Tasks in progress

- [TASK_NAME]: status / progress / open questions
- [TASK_NAME]: status / progress / open questions

## Decision points awaiting confirmation

| # | Decision point | Options |
|---|---|---|
| 1 | [DECISION_POINT] | [OPTION] |
| 2 | [DECISION_POINT] | [OPTION] |

## Known limitations

- [LIMITATION_1]
- [LIMITATION_2]

---

> Update rules: update this file at end-of-work, **entry-level write** — read the latest first, update only the entries of your own task and the human-read zone, leave every other entry untouched; a failed CAS creates a conflict file and blocks completion. The human-read zone is auto-generated from the AI zone; history goes to reports\ + INDEX, this file never accumulates. **Size cap**: the word-count limit for this file is defined in the MAP rules section under "STATE character limit" (default 15k) — when the limit is exceeded, apply the overwrite-style discipline: move completed/archived history sections into `reports\` (write a handoff record and register it in INDEX), and keep only the current snapshot and active entries in this file; the limit must not be raised on the grounds of "more completeness" — the cap is a **ceiling device**, not an expandable capacity.
