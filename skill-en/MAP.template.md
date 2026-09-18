# [PROJECT_NAME] · Project Map (MAP)

> Version v1.2.1

> This file is the project's project map: **environment / rules / protocol / path registry** — it records "what is where and by what rules things run", and never records progress (progress belongs to STATE, records belong to reports\ + INDEX).
> **Reading**: read it at a first takeover / across modules / for an overall review; for a day-to-day named task, do not read this file.
> **About the protocol section**: section 3 "Protocol" is a **derived snapshot** of SKILL.md (the workspace protocol entry); its version number must match SKILL.md; where the two disagree, SKILL.md wins.

---

## 1. Environment

- Platform: `{PLATFORM}` (win / mac / linux) · shell: `{SHELL}` (powershell / bash)
- Workspace root: `{WORKSPACE_ROOT}` (the collaborative workspace, outside the project, physically separated; **confirmed once with the user at initialization** — default or custom; every project goes under that root)
- Code path (the code workspace): `[CODE_PATH]` (provided by the user, physically separated from the management directory)
- **Skill source package path**: `[SKILL_SOURCE_PATH]` (absolute path of the skill package — used by gap filling and outdated-version detection; filled in at initialization, "—" if not registered)
- **Manager (decision maker)**: `[DECISION_MAKER]` (the final decider on REVIEWS dispositions, cross-branch conflict resolution and escalation of meta events — REVIEWS records this field)
- **Workspace backup method**: `[BACKUP_METHOD]` (git / periodic copy / none — deleting a whole directory exceeds what the protocol can recover, and this is the last resort; the protocol registers it, it does not package an implementation)
- Tech stack: `[TECH_STACK]`
- Run/build (if applicable): `[RUN_COMMAND]` / `[BUILD_COMMAND]`
- **Explicitly out of scope**: `[OUT_OF_SCOPE_MODULES/BOUNDARIES]`
- **Placeholder convention**: `{}` = runtime variable (evaluated by the AI or confirmed once with the user, e.g. platform / workspace root / AI tag); `[]` = project information (filled in directly by a human, e.g. code path / tech stack / commands / source package path)

## 2. Rules (working rules)

- `[PROJECT_RULE_1]`
- `[PROJECT_RULE_2]`
- The collaborative protocol is detailed in the workspace SKILL.md (the skill entry; section 3 of this file is its derived snapshot)
- **Branch numbering registry**: `XX` = module category, registered here on first use (e.g. EX = export, UI = interface, DB = database); register a new branch before using it — two AIs must never each start their own numbers
- **INDEX main-file row count**: `20` (the user may customize it — small projects stay at 20, large projects raise it as needed; when the count reaches 80% of the configured value at end-of-work, the AI reminds the user to adjust)
- **STATE character limit**: `15k` (the word-count ceiling for STATE.md — when exceeded, move history sections into reports\ per the overwrite-style discipline, keeping only the current snapshot; the AI reminds the user when the count reaches 80% of the configured value at end-of-work)
- **reports archive threshold**: `20` (once the number of files in reports\ reaches it, the oldest is archived into archives\ by month; the user may customize)
- **Periodic AI audit**: `off` (the scheduled-execution switch for the checks checklist, **its state recorded on this line**, off by default; once set to "on", the AI runs it per the platform's scheduling ability)
- **Collaboration mode**: `standard` (`light` / `standard` / `coordination`; file set, roles, checks and upgrade rules per SKILL.md)
- **Protocol identifiers**: `TASK-ID` / `EVENT-ID` / `DESIGN-ID` are stable and never reused; lifecycle and role/permission/mode rules are defined in `SKILL.md` v1.2.1
- **Concurrency policy**: single logical writer per file; revision + SHA-256 CAS and atomic same-directory writes; stale writes create `*.conflict.<EVENT-ID>.md`
- **Archive policy**: `archives\INDEX_archived.md` is immutable, append-only, canonical, and must be created during initialization; active rows point to canonical reports
- **Project viewing view**: the human-eyes convention is in section 6 of SKILL.md (entry / granularity / item-by-item viewing / presentation conventions)

## 3. Protocol (collaborative protocol · derived snapshot; the authoritative source is the workspace SKILL.md)

> The 8 lines below are a high-frequency memo covering every action of one ordinary end-of-work; for details (gap filling / concurrency resolution / the full archive red line) see section 3 of the workspace SKILL.md.

1. **Task-card-driven**: at takeover, read the matching task card first (tasks\), claim it in the card's "Claimed by" before starting, and do not wander through the whole project
2. **End-of-work routing**: unfinished → a card is mandatory; has a next step → full handoff + overwrite-update the task card; no next step → simplified summary + move the card to archives\done\ (never delete the card)
3. **End-of-work four-piece set**: handoff reports → card update/move → INDEX adds one row (type [handoff]/[done]/[dropped]; rows are never lost — rows past N in the main file move into the archive file) → STATE entry-level write (blind whole-file overwrite is forbidden; when STATE's word count exceeds the "STATE character limit" (default 15k), move history sections into reports\ and keep only the current snapshot)
4. **Minimal handoff**: 6 blocks + block 7 "Task card update" (mandatory when a matching task card exists); no diff, no copied code
5. **Naming rules**: reports `YYYY-MM-DD_topic_AI-tag.md` (AI tag: `{PLATFORM}-{AI_NAME}-{SHORT_CODE}`, 2-4 random characters; list the directory first to confirm there is no duplicate name); task cards are named after the work
6. **Stable IDs and concurrency**: TASK-ID / EVENT-ID / DESIGN-ID are immutable; read revision/hash before writing, use atomic rename or CAS, verify after writing; a single-writer conflict creates `CONFLICT_*.md` and goes to the manager, never to timestamp arbitration
7. **Distill back to card + progress anchor**: after reading reports, distill the increments back onto the card (each file is read at most once); while working, overwrite at each landing point into the card's "Progress anchor" line, resume along the anchor + git status after an interruption, and clear it to "—" once distilled at end-of-work
8. **Archive and meta-management**: reports\ and archives\ must not be deleted or moved (the only exception is end-of-work archiving, repointing via a new pointer event); `archives\INDEX_archived.md` is immutable/append-only; the skill's own affairs go to REVIEWS.md, never into reports\, never logged in INDEX
9. **Blocking completion gate**: completion is explicit, and cannot pass until handoff → card/archive → INDEX pointer → STATE plus revision/hash verification all land successfully

## 4. Path registry (written only when something is added)

| File/directory | Purpose | Read/update |
|---|---|---|
| `SKILL.md` | Workspace protocol entry (authoritative source) | Read when the protocol is in doubt |
| `STATE.md` | Current state (human-read zone + AI zone, entry-level overwrite) | Read on review / update at end-of-work |
| `REVIEWS.md` | Meta-management record (skill retrospective / recovery registration, append-style) | Append when a meta event occurs / read on retrospective |
| `tasks\` | Task cards (one file per card, named after the work) | The first takeover entry |
| `reports\` | Handoff/summary archive (named by date, **project work records only**) | Read along the task card's "Last handoff" |
| `INDEX.md` | Record index (type markers) | Traceback / end-of-work entry |
| `archives\` | Archive (in only, never out) | Written when archiving |
| `archives\done\` | Completed-card archive (moved in on completion, keeping the completion record) | Moved in at a completion-type end-of-work |
| `archives\INDEX_archived.md` | Full INDEX archive (the single full index, created at the first archiving) | Read when looking up the full history |
| `tools\` | Optional tools area (pulled on demand) | Read only when needed |
| `skill source package` | Authoritative source of protocol templates (general-purpose; **path in the environment section "Skill source package path"**) | File missing/outdated → copy from there, instantiate and refill |
| `[NEW_PATH]` | `[PURPOSE]` | `[WHEN_TO_READ]` |
