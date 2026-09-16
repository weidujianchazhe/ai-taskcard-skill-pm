# Check protocol (checks\)

> This directory is the check-protocol documentation (not executable scripts) — a pure-document check checklist (human/AI tick against it).
>
> **Trigger**: mainly human-triggered — the project manager turns checks on as needed; the AI **does not execute them on its own initiative**.
> **Optional occasions (not mandatory)**: before start of work / during execution / after long inactivity — these are only occasions on which the manager may check, not mandatory checks.
> **Switch**: an AI periodic sweep can be configured (on/off); **the switch state is stored in the MAP rules section "AI periodic sweep"** (change that row to toggle), default off; only after it is enabled does the AI run it periodically.
> **An AI taking over work does not run checks**: the taking-over AI reads only the work files it needs and takes on no extra burden from checks.

---

## 1. Check checklist

> **Type selection**: the user says "check the work records / check the records" → use checklist_record; the user says "check the whole project / check the project status" → use checklist_project; the user says neither → ask the user which one first.

### checklist_record (work-record check)

- [ ] INDEX type markers correct (`[handoff]`/`[done]`/`[dropped]`), and the [handoff] chain is continuous
- [ ] Task cards updated overwrite-style (no snowballing, no history piling up inside the card)
- [ ] STATE overwrite-style (human-read zone + AI zone in sync, timestamp latest)
- [ ] reports naming conformant (`YYYY-MM-DD_topic_AI-tag.md`)
- [ ] Dropped requests leave a trace (one INDEX line + reason)
- [ ] Skill files complete (against the MAP Path registry list; missing items are either restored from the skill source package or marked "to be added")

### checklist_project (project sweep)

- [ ] All task cards are active tasks (move the card to archives\done\ as soon as it is complete)
- [ ] Active cards carry the "end-of-work protocol quick note" at the card tail (the protocol hook is in place — cards missing the quick note are mostly old cards or rebuilds that skipped the copy; prompt to add it)
- [ ] Interrupted-card handling: cards whose Claimed by is not "—" but whose Progress anchor is stuck mid-way and untouched for a long time → prompt the user to resume / reassign / drop (dropping is the manager's decision; the AI only prompts)
- [ ] Takeover cost is still "one task card ± 1 reports read" (no bloat points)
- [ ] Archiving executed (the reports count reaches the MAP "reports archive threshold" (default 20) → archives\; the AI triggers this check automatically at end of work)
- [ ] Completed cards moved to archives\done\ (completion-type end of work does not delete the card; keep the record)
- [ ] Decision points registered (STATE decision points / task card Key points)
- [ ] Legacy projects: whether the historical gaps marked "to be tidied on demand" are reasonable
- [ ] MAP Path registry matches the actual directories (no dead paths; corresponds to audit Checkpoint 7) — v1.2.0
- [ ] No files deleted/moved in reports\ and archives\ (archive red line; when deleted, the INDEX pointer dangles → discoverable by Checkpoint 4 / Recovery point 3) — v1.2.0

## 2. Three-state disposition loop

| Status | Disposition |
|---|---|
| Normal | Record "no problem" |
| Needs attention | Record the problem + a suggestion (do not touch files) |
| Needs action | Create a task card + update the STATE decision points + write to INDEX ([handoff]) |

## 3. Check output

- Write the check result as one reports record (`[done]` or `[handoff]` type) and register it in INDEX
- Turn discovered problems into task cards (handle on demand); do not make sweeping file changes directly
