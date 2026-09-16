# Handoff record spec (one file per record)

> Version v1.2.0

> File name: `YYYY-MM-DD_topic_AI-tag.md` (AI tag: `{PLATFORM}-{AI_NAME}-{SHORT_CODE}`, short code 2-4 random characters — multiple instances on the same platform never collide; list the reports\ directory first to confirm there is no duplicate name).
> A new record MUST be created whenever code changes are completed, a deliverable is produced, the user makes a new decision, or an unsolved problem is hit.
> **Minimality principle**: write only what this task needs — no full diff, no copied code, no unrelated history, no repeating what MAP already holds.
> **Meta-management routing**: the skill's own affairs (REVIEWS retrospectives, version drift, recovery-action registration) are **never written here** — append them to the workspace REVIEWS.md; this directory holds project work records only.
> All unfinished work goes through the full end-of-work four-piece set (handoff reports → card → INDEX → STATE); completion-type goes through the simplified set (simplified handoff reports → move card to archives\done\ → INDEX → STATE). There is no "skip writing to disk" exception.

## Handoff template (6 mandatory blocks + block 7 "Task card update", mandatory when a matching task card exists)

### Handoff  YYYY-MM-DD HH:MM

> **Evidence**: `EVENT-ID: EVT-[UTC_DATE]-[SEQUENCE]` · `TASK-ID: TASK-[STABLE_SLUG]` · `DESIGN-ID: DES-[SLUG]` or `—` · `revision: [N]` · `content-sha256: [SHA256_OF_EXACT_UTF8_BYTES]` · `encoding: UTF-8 (BOM present/absent)` · `source pointer: [PATH_OR_EVENT-ID]`

- **This request**: one line (what the user wants)
- **Code context for this task**: list only the file paths relevant to this task (do not give the whole directory tree)
- **Changes**: file + location + what changed (3-5 items, one line each; when the project uses git, attach a commit hash to each — a precise traceability anchor; `git show` yields the full diff when needed)
- **Verification**: whether it was verified, which functions were checked
- **Data impact**: data directory changes / whether migration is needed
- **Next step**: where the next AI continues from + decision points awaiting user confirmation
- **Task card update (block 7)**: the key points/anchors distilled this round → overwrite-update the matching task card (mandatory when a matching task card exists) → **and sync STATE** (end-of-work four-piece set: handoff → card update/move → INDEX → STATE; STATE is written entry-level — in a parallel end-of-work update only your own task entry and the human-read zone)

> **End-of-work check (4/4)**: Handoff ✓ / Card updated or moved ✓ / INDEX ✓ / STATE ✓
> **Card quality self-check**: key points are actionable (what + where) / "Files involved" holds concrete paths / "Last handoff" points at reports (use "—" only when there is no handoff)

---
