# AI-Relay Project Management Lite (user guide)

> Version v1.2.1

> This is a **general-purpose project management skill template**: any project can copy this template to build its own collaborative workspace; it supports multi-AI / cross-platform / cross-time / cross-project relay work.
>
> Core philosophy: **a project may be complex and heavy, the taking-over AI reads only what it needs** — the burden does not grow with project size.
>
> This file is the **user guide** (for humans and for an AI coming in for the first time); the single source of truth for the protocol text is `SKILL.md`, and this file does not restate its rules in detail.

## 1. What this template solves

| Problem | Solution |
|---|---|
| No continuity after switching AI | Every work session ends with a handoff/summary + overwrite-style state + a registered task card |
| A new AI has to read every document (wasted compute) | **Task-card-driven takeover**: locate via the task card → understand the structure via MAP → continue via reports; read on demand |
| Vague instructions, the AI works on the wrong task | The task card holds **file paths involved + a last-handoff pointer**, so it arrives precisely instead of guessing |
| Handoff files are too wordy | A minimal handoff template (only what this task needs) + a simplified summary for completion-type work |
| Change history is untraceable | One line per entry in INDEX + a pointer to the full handoff record |
| Several AIs step on each other | Task cards are claimed on takeover + division by module/branch + separate handoff files |
| Documents keep growing | Overwrite-style state + read only what is needed + rolling archive; MAP records structure, never progress |
| The skill's own affairs pollute the project archive | **Meta-management routing**: retrospectives/version/recovery registration all go to REVIEWS.md, while reports/INDEX hold work records only |

## 2. Directory structure (physical separation)

The skill source package (outside, general-purpose) and the project workspace layer (inside, being managed) are physically separated — **the management directory is created outside the project path** (not mixed into the source tree, not swept into builds); the project workspace is an instantiated copy of the skill (including the protocol files), and project source code is never written into the management directory.

```
# Project workspace (one per project · file composition per section 3 "Workspace file list")
{WORKSPACE_ROOT}\<project-name>\        # Workspace root {WORKSPACE_ROOT}, confirmed once with the user at initialization (default or custom)
├── SKILL.md             # Protocol entry (the workspace is self-contained; MAP's "collaborative protocol in SKILL.md" points here)
├── MAP.md               # Project map: environment/rules/protocol/path registry (low frequency, written only on new structure)
├── STATE.md             # Current state: human-read zone (3-line summary) + AI zone (entry-level overwrite; read on first/cross-module/review)
├── REVIEWS.md           # Meta-management record: skill retrospectives/recovery registration (append-style; not into reports/INDEX)
├── tasks\               # Task cards: one file per card named after the work (human-read locator + AI field block; the first takeover entry)
├── INDEX.md             # Record index: type markers [handoff]/[done]/[dropped] (traceback index + human-readable table)
├── reports\             # Work archive: handoff records/simplified summaries (one per session, read along the anchor; project work records only)
├── archives\            # Archive (in only, never out)
│   ├── done\            # Completed-card archive (created at initialization; the move target for completion-type work)
│   └── INDEX_archived.md  # Full INDEX archive (created at the first INDEX archiving; may not exist before that)
└── tools\               # Optional tools area (pulled on demand, off the takeover path)
    └── README.md        # Tools-area entry (overview + three iron rules + built-in tool table; sub-specs pulled from the skill source package on demand)
```

## 3. Initialization flow (new project onboarding)

0. Read `SKILL.md` first (the skill entry: positioning/triggers/workflow/initialization checklist)
1. **Confirm the workspace root {WORKSPACE_ROOT}** (default or custom — confirmed once, every project goes under that root; the management-directory subfolders are created automatically by the skill, so the user need not create folders beforehand)
> **Dedup check first**: after confirming the workspace root and before creating directories, probe whether a management instance for this project already exists under that root; if it does → merge / confirm the single copy first, and never start a second directory.
2. **Build the workspace per the "workspace file list"** (do not copy the whole package; both initialization paths share this list, legacy onboarding is in LEGACY_ONBOARDING.md):
   - **Instantiate** (rename the template and refill): `MAP.template.md` → `MAP.md`, `STATE.template.md` → `STATE.md`, `INDEX.template.md` → `INDEX.md`, `REVIEWS.template.md` → `REVIEWS.md`
   - **Copy verbatim**: `SKILL.md` (the protocol entry, which travels with the workspace), `tasks\TASK_CARD.template.md` (format reference), `designs\DESIGN_CARD.template.md` (design-card format), `reports\HANDOVER.template.md` (format reference), `archives\README.md`, `tools\README.md`
   - **Create empty directories and archive index**: `tasks\`, `reports\`, `archives\done\`; create `archives\INDEX_archived.md` as the append-only canonical index (with its header, even when empty)
   - **Not into the workspace** (stay in the skill source package, pulled on demand): `README.md`, `BLUEPRINT.md`, `LEGACY_ONBOARDING.md`, the tools\ sub-specs (checks / visualize / schedule / report / custom)
3. Open `MAP.md` and replace the two kinds of placeholder — the `[]` human-filled items (below) and the `{}` runtime variables (`{WORKSPACE_ROOT}` is confirmed once with the user; `{PLATFORM}`/`{SHELL}` are filled per environment):
   - `[PROJECT_NAME]`, `[CODE_PATH]`, `[TECH_STACK]`, `[OUT_OF_SCOPE_MODULES/BOUNDARIES]`, `[RUN_COMMAND]`, `[BUILD_COMMAND]`, `[PROJECT_RULE]`, `[SKILL_SOURCE_PATH]` (used by gap filling and outdated-version detection)
   - Confirm the rules-section configuration: INDEX main-file row count / STATE character limit / reports archive threshold / periodic AI audit switch / collaboration mode (light/standard/coordination)
4. Register the first task card under `tasks\` (one file per card, named after the work, with a human-read locator block)
5. Tell the participating AIs: **"the collaborative workspace is at {WORKSPACE_ROOT}\<project-name>\; read the matching task card under tasks\ first"**

> **Legacy project (already under way, no management structure)**: do not run steps 2-4 above; instead read `LEGACY_ONBOARDING.md` and onboard — create the management directory per the same "workspace file list" + lightweight registration of the current state, with history handled by progressive tidying rather than deep reorganization.

## 4. Takeover flow (task-card-driven · precise arrival)

1. Read the matching task card → it hits (description / key points / files involved / last handoff); when instructions are vague, fall back on the task card, and if it is still unclear ask the user
2. Key points suffice → start directly; they do not → read the previous entry in `reports\` along "Last handoff" (the [handoff] chain)
3. After reading reports, **distill the increments back onto the task card** (distill back to card — the next takeover need not read that file again)
4. Follow the card's "Files involved" paths → read the concrete working files and start
5. When a global judgement is needed (first takeover / across modules / review): read `STATE.md` (with its human-read zone) and `MAP.md`; for deep traceback read `INDEX.md` (locating by the [handoff] marker)

> As long as "end-of-work routing" is followed (has a next step → full handoff + overwrite-update the task card; no next step → simplified summary + move the card to archives\done\), the takeover cost stays constant ≈ one task card + occasionally 1 reports — even if the project sits untouched for half a year.

## 5. Protocol overview (for details, `SKILL.md` is the single source of truth)

1. **Task-card-driven**: at takeover read the matching task card first to locate the work, claim it in the card's "Claimed by" before starting, and do not wander through the whole project
2. **End-of-work four-piece set**: handoff reports → card update/move → INDEX entry → STATE update (entry-level write when parallel); unfinished work must have a card, completed work is moved to archives\done\ and the card is never deleted
3. **Minimal handoff**: 6 blocks + block 7 "Task card update" (mandatory when a matching task card exists); when the project uses git, every "Changes" item carries a commit hash
4. **Naming and numbering**: reports `YYYY-MM-DD_topic_AI-tag.md` (the AI tag contains a short code; list the directory before writing to avoid duplicate names); ID XXNNNN — register a branch in MAP first, increase digits by numeric value, and on a collision add +1 with a trace
5. **Concurrent-write rules**: read-before-write / verify-after-write / STATE entry-level write; across branches do not compare IDs and do not decide by timestamp — leave a trace and hand it to the manager
6. **Overwrite-style update**: the task card/STATE always hold only the latest, and history goes to reports + INDEX; when reports reach the MAP "reports archive threshold" (default 20) they are rolled into the archive; when STATE's word count reaches the MAP "STATE character limit" (default 15k), move history sections into reports\ and keep only the current snapshot
7. **Archive red line**: reports\ and archives\ must not be deleted or moved (the only exception is the end-of-work archiving flow, repointing the INDEX row after the move); register new files/paths/branches in MAP
8. **Meta-management routing**: the skill's own affairs go to REVIEWS.md, never into reports/INDEX
9. **Progress anchor**: while working, overwrite at each landing point into the card's "Progress anchor" line — after an interruption resume along the anchor + `git status`, and clear it to "—" once distilled at end-of-work
10. **The human-read zone is auto-generated from the AI zone** (task ← first sentence of the description, status ← the status field, next step ← key point ①), rewritten in sync on overwrite

10. **Stable identifiers**: TASK-ID / EVENT-ID / DESIGN-ID are immutable after creation; file names may change, references use IDs only; a collision must be regenerated and traced
11. **Design-card lifecycle**: state machine (draft → in review → approved / rejected / discarded) with an approval gate — **no execution card before approval**; each approval / rejection / discard writes an EVENT-ID
12. **Three collaboration modes**: light / standard / coordination — each with its own file set, roles, checks and upgrade path; upgrading widens the set and never rewrites history
13. **Permission matrix and single writer**: clear permissions for execution AI / audit AI / manager / recovery AI; single-writer responsibility plus conflict files CONFLICT_*.md; read revision/hash before writing, atomic rename preferred, CAS as fallback, verify after writing
14. **Two ceilings**: the INDEX main-file row count and the STATE character limit — ceiling devices for the taking-over AI's reading cost, not expandable capacity; overflow history moves into reports\\ and the archive
15. **Boundary statement**: this package defines protocol, templates and script-**generation specs** only; it does not implement or enable a runtime daemon, auto-archiver, permission system or continuous supervision

> **Before updating/slimming/simplifying/merging this skill, pass every item of section 8 "Change-protection zone" in `SKILL.md`** (zero feature loss / cross-impact check / takeover cost must not rise / **three cost-attribution principles**: constant write path · snapshot vs ledger division · main-file capacity as a ceiling / load-bearing structures preserved / the interlocking six-question self-check / **reconciliation mindset**: the four anchors of time, ID, identity and evidence are the audit interface, and ID rules are not a formatting preference); **when a change conflicts with a gate, the AI must raise a flag to the user and must not execute without confirmation**.

## 6. Template file descriptions

| File | Description |
|---|---|
| `SKILL.md` | Skill entry and single source of truth for the protocol (positioning/triggers/workflow/core protocol/checklists/viewing view/maintenance rules/change-protection zone) |
| `MAP.template.md` | Project map skeleton; copy to `MAP.md` and fill the placeholders (fixed four sections: environment/rules/protocol/paths; the protocol section is a derived snapshot of SKILL.md) |
| `STATE.template.md` | Current-state snapshot skeleton (human-read zone 3 lines + progress/blockers/decision points/timestamp, entry-level overwrite; the character limit is in the MAP "STATE character limit", default 15k — when exceeded, move history sections into `reports\`) |
| `tasks\TASK_CARD.template.md` | Task card skeleton with stable TASK-ID, DESIGN-ID, EVENT-ID, concurrency metadata, and completion gate |
| `designs\DESIGN_CARD.template.md` | Design lifecycle template; only an approved design card may generate an execution card |
| `reports\HANDOVER.template.md` | Minimal handoff template (6 blocks + block 7 task card update), one file per record |
| `INDEX.template.md` | Record index (type markers [handoff]/[done]/[dropped], created at initialization; rows are never lost — rows past N move into the archive file) |
| `LEGACY_ONBOARDING.md` | Legacy project onboarding guide (companion file: lightweight registration + progressive tidying, not part of the mandatory protocol reading path) |
| `REVIEWS.template.md` | Skill retrospective template (meta-management: blocker → root cause → suggestion → disposition, four one-line sections; **instantiated as the workspace REVIEWS.md at initialization**) |
| `BLUEPRINT.md` | Design blueprint (the 12 points are the authoritative quick-reference; design points only, it carries no protocol and takes no part in version syncing; the HTML edition is a supplementary document outside the package) |
| `archives\README.md` | Archive notes (in only, never out; prevents accidental deletion) |
| `tools\` | Optional tools area (the checks/visualize/schedule/report/custom specs stay in the skill source package and are pulled on demand); adding tools on demand follows the three iron rules |

## 7. Dual-platform command examples (PowerShell / bash)

> All commands are parameterized: `{WORKSPACE_ROOT}` (workspace root, confirmed at initialization), `{PROJECT_NAME}` (project name), `{SHELL}` (powershell / bash).
> The management directory is created automatically by the skill; the commands below are for reference during initialization and daily maintenance.

| Scenario | PowerShell ({SHELL}=powershell) | bash ({SHELL}=bash) |
|---|---|---|
| Check whether the workspace root exists | `Test-Path "{WORKSPACE_ROOT}"` | `test -d "$WORKSPACE_ROOT" && echo ok` |
| Create the management directory and archive index | `New-Item -ItemType Directory -Force -Path "{WORKSPACE_ROOT}\{PROJECT_NAME}\tasks","{WORKSPACE_ROOT}\{PROJECT_NAME}\reports","{WORKSPACE_ROOT}\{PROJECT_NAME}\archives\done"; New-Item -ItemType File -Force -Path "{WORKSPACE_ROOT}\{PROJECT_NAME}\archives\INDEX_archived.md"` | `mkdir -p "$WORKSPACE_ROOT/$PROJECT_NAME"/{tasks,reports,archives/done}; touch "$WORKSPACE_ROOT/$PROJECT_NAME/archives/INDEX_archived.md"` |
| View the directory structure | `Get-ChildItem -Recurse "{WORKSPACE_ROOT}\{PROJECT_NAME}"` | `ls -R "$WORKSPACE_ROOT/$PROJECT_NAME"` |
| Run the project (if applicable) | `{RUN_COMMAND}` (per the MAP environment section) | `{RUN_COMMAND}` (per the MAP environment section) |
| Build the project (if applicable) | `{BUILD_COMMAND}` (per the MAP environment section) | `{BUILD_COMMAND}` (per the MAP environment section) |

| Initialize the archive index | `New-Item -ItemType File -Force -Path "{WORKSPACE_ROOT}\{PROJECT_NAME}\archives\INDEX_archived.md"` | `touch "$WORKSPACE_ROOT/$PROJECT_NAME/archives/INDEX_archived.md"` |

> Environment convention: pick one of the commands per `{PLATFORM}` (win / mac / linux) and `{SHELL}`; never mix platforms. The path separator follows the platform (Windows `\` / POSIX `/`).

> **v1.2.1 protocol boundary**: `SKILL.md` specifies protocol, templates, and optional script generation only; it does not define or enable a default runtime. `TASK-ID`, `EVENT-ID`, and `DESIGN-ID` are stable identifiers. Completion is an explicit trigger and a blocking gate: missing handoff/card/INDEX/STATE evidence, pointer, revision, or hash keeps work active. `archives\INDEX_archived.md` is immutable and append-only; corrections are new pointer/supersession events. Two ceiling devices (INDEX row count and STATE character limit) bound the default takeover reading cost.

## 8. Requirements and platform compatibility

**Requirements**: this skill is a local project-management engineering setup and needs **a local filesystem plus command/file execution ability** — able to create the management directory on disk and read/write task cards and handoff files.

**Platforms are judged by capability dimension, not enumerated by name**: any platform with the above abilities (harness-style / IDE agent / desktop workspace agent, etc.) is automatically compatible; it depends on no platform's private API, skill system or SDK (install it if the platform has a skill system, otherwise read it as documentation).

**Not applicable**: scenarios without local file ability (web chat / mobile app / pure conversation / raw API calls) do not meet the requirements, so this skill does not apply.
