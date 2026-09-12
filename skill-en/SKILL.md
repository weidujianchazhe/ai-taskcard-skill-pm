---
name: AI-Relay-project-management-lite
description: General-purpose project management skill: task-card-driven lightweight takeover, overwrite-style state, end-of-work routing handoff, INDEX type markers, supporting multi-AI / cross-platform / cross-time / cross-project relay. A project may be complex and heavy while the taking-over AI reads only what it needs. Use when starting a new project, taking over a long-idle project, or onboarding a legacy project.
author: 如天之星
license: MIT
version: 1.0.1
---

# Project Management Lite (skill entry)

> **Positioning**: a general-purpose project management skill that serves no particular project. Core philosophy — a project may be complex and heavy, the taking-over AI reads only what it needs: the burden does not grow with project size.
> **Essential goal (across obstacles)**: cross the obstacles of platform, AI, time and project, so the taking-over AI understands the work at a lower reading cost and with fewer errors.
> **Legacy project (already under way, no management structure)**: read `LEGACY_ONBOARDING.md` first (lightweight registration + progressive tidying, no deep historical reorganization).
> **Language edition**: this is the English edition, mirroring the Chinese package v1.0.1. The two editions are structurally identical; the Chinese↔English data-contract mapping is in section 3.4.

---

## 1. Trigger points

1. **Before starting a new project**: initialize the collaborative workspace (create the management directory + fill in the initial information)
2. **Before taking over a long-idle project**: read the work files as needed (task-card-driven; this skill is not re-read)
3. **Legacy project onboarding** (already under way, no management structure): read `LEGACY_ONBOARDING.md` and carry it out

## 2. Workflow

```
① Confirm the workspace root {WORKSPACE_ROOT} (the user chooses once: default or custom; subfolders of the management directory are created automatically by the skill)
② Create the management directory (the universal first step, required by every project):
   MAP.md / STATE.md / REVIEWS.md / tasks\ / reports\ / INDEX.md / archives\ (including done\) / tools\
③ Fill in the initial information: replace the MAP placeholders (environment / rules / protocol / path registry, including [SKILL_SOURCE_PATH], [BACKUP_METHOD], [DECISION_MAKER] and the reports archive threshold)
④ Register the first task card (under tasks\, named after the work)
⑤ Run (the skill is never re-read after this; from here on work from the work files alone):
   read task card → do the work → end-of-work routing (overwrite update / move card) → INDEX entry
   (when tasks\ is empty, create a card on the user's instruction; no card = no active work)
   (with several cards: the user names a task → go to tasks\ and find the card with the same or a close name; if several cards share a name, ask the user)
```

## 3. Core protocol

### 3.1 Protocol quick-reference table

| Protocol | Content |
|---|---|
| Task-card-driven takeover | Read the matching task card (description / key points / files involved / code root path) → claim it in the card's "Claimed by" before starting → if that is enough, start directly; if not, read reports along "Last handoff"; **the card ends with an "end-of-work protocol memo"** (the end-of-work obligation travels with the card and is visible the moment you take over — no reliance on re-reading the skill, which stops an AI that only reads the card from skipping protocol duties) |
| End-of-work routing | **Unfinished → a card is mandatory** (including work with no card yet that exists only in the current conversation); has a next step → full handoff + overwrite-update the task card; no next step → simplified summary + **move the card to archives\done\** (never delete the card; keep the completion record); **end-of-work four-piece set: handoff → card update/move → INDEX → STATE (entry-level write)**, checking each item after it lands on disk |
| Progress anchor | While working, **overwrite at each landing point** into the card's "Progress anchor" line (single line, only for a card you claimed) — if a network/power/token outage cuts the work short before end-of-work, the card naturally keeps the latest landing point, and the next AI resumes along the anchor + the actual file state (`git status`); at a normal end-of-work the content has been absorbed into key points/handoff and the line is cleared to "—" — **the handoff format does not change at all**; for a cancelled task the anchor stays as it is when archived (traceable) |
| Next-step criterion | Has a next step = the user wants to continue / the work is not finished / there are leftovers; no next step = the user explicitly says "finished" / everything is cleared |
| Overwrite-style update | Task card / STATE are always overwritten to the latest; no appending, no snowballing; history goes to reports + INDEX; STATE is updated entry by entry during a parallel end-of-work (see 3.2) |
| Distill back to card | After reading reports, distill the increments back onto the card → every reports file is read at most once |
| INDEX entry | Add one row at every end-of-work (date + type + one-line summary + see reports\xxx.md); **[handoff]** read along the chain / **[done]** read only on review / **[dropped]** leave a trace so it is not redone by mistake |
| Human-read zone and AI zone | The human-read zone (3-line summary) is auto-generated from the AI zone — task ← first sentence of the description, status ← the status field, next step ← key point ① — rewritten in sync on an overwrite update, never aligned by subjective judgement |
| Minimal handoff | 6 blocks + block 7 "Task card update" (mandatory when a matching task card exists) |
| Archive red line | **Deleting or moving any file under reports\ or archives\ is forbidden** — the only exception is the end-of-work archiving flow (rolling archive past the threshold, moving completed cards), and after a move the matching INDEX row must be repointed; changes are recorded in three layers: **MAP records structure** (new paths / new branches), **reports record a summary** (when the project uses git, every "Changes" item carries a commit hash — `git show` gives the full diff when needed), **INDEX records the pointer row** (double-write, never lost) |
| Naming rules | reports `YYYY-MM-DD_topic_AI-tag.md` (the AI tag contains a short code: `{PLATFORM}-{AI_NAME}-{SHORT_CODE}`, 2-4 random characters; list the directory first to confirm there is no duplicate name); task cards are named after the work |
| Meta-management routing | The skill's own affairs (REVIEWS retrospectives, version-drift detection, recovery-action registration) are always appended to the workspace `REVIEWS.md`, and are **never written to reports\, never logged in INDEX** — project reports/INDEX hold project work records only |
| Concurrent-write rules | Summary: read-before-write · verify-after-write · STATE entry-level write · AI tag carries a short code · collision retry · cross-branch conflicts go to the manager (**details in 3.2**) |
| Gap filling | Summary: the skill source package is the authoritative source; if something is missing or outdated, copy and instantiate it from the source package; if data is lost, recover it along the INDEX/reports traces; whatever cannot be recovered is marked "data pending" and never faked (**details in 3.3**) |

### 3.2 Concurrent-write rules (details)

Read-before-write (read the latest before overwrite-writing STATE/a task card or append-writing INDEX) · verify-after-write (read back after writing to confirm it landed) · **STATE entry-level write** (during a parallel end-of-work each AI reads the latest first and updates only its own task's entry and the human-read zone — the "current progress" one-liner is overwritten by the last one to finish — every other entry stays as it is; blind whole-file overwrite is forbidden) · **AI tag carries a short code** (multiple instances on the same platform never collide) · **ID collision retry** (if verify-after-write finds the same ID already exists in the same branch → the later writer adds +1 to its ID, rewrites the row and leaves a trace in its own reports) · conflict resolution (different fields are merged and kept; for the same field, only within the same branch does the larger numeric ID overwrite the smaller; **across branches IDs are not compared and timestamps do not decide** — cross-platform clocks are untrustworthy; both sides leave a trace in their own reports and hand it to the manager for a decision, and timestamps are supporting evidence only, never the basis).

### 3.3 Gap filling (details)

The skill source package is the authoritative source: if a skill file in the project workspace is missing or outdated (the source package version is higher) → copy the template from the source package and instantiate it, refilling it (the source package path is in the MAP environment section "Skill source package path"); if a data file (task card / reports) is lost, recover it from INDEX/reports, and if INDEX is lost as well → mark it "data pending", never fake it; **task card lost** → among the recent INDEX rows find the nearest [handoff] row → read the latest reports along the handoff file column → rebuild the task card from reports (description / key points / files involved / last handoff) → create it anew under tasks\; **STATE corrupted** → restore it from the latest reports (the latest handoff record holds the current progress / next step); with any recovery action, log a line in **REVIEWS.md** in passing (meta-management routing, not into reports/INDEX).

### 3.4 Glossary (retained terms · plain language)

| Term | Plain language |
|---|---|
| task-card-driven | At takeover, read the matching task card first to locate the work; do not wander through the whole project |
| end-of-work routing | At end-of-work, route by "is there a next step": yes → full handoff; no → simplified summary + move the card to the archive |
| end-of-work four-piece set | The four things every end-of-work must do: handoff reports → card update/move → INDEX entry → STATE update |
| overwrite-style update | A file always carries the latest content, never appended history; history goes to reports/INDEX |
| minimal handoff | A handoff writes only what this task needs — no diff, no copied code |
| distill back to card | After reading reports, write the increments back into the card's key points, guaranteeing every reports file is read at most once |
| meta-management routing | The skill's own affairs are logged in REVIEWS.md, kept separate from project work records (reports/INDEX) |
| entry-level write | During a parallel end-of-work, STATE updates only its own task's entries; blind whole-file overwrite is forbidden |
| concurrent-write rules | Discipline for several AIs writing files at once: read the latest before writing, read back to confirm after writing, resolve conflicts by rule |
| dedup check first | Before creating the management directory, probe whether an instance for this project already exists; if so, merge — never start a second one |
| lightweight registration | When onboarding a legacy project, register only what is currently visible; no historical digging |
| progressive tidying | History is classified as work continues, recorded on demand |
| physical separation | The management directory lives outside the project's code, never mixed into the source tree |
| anchor | A reference path pointing at a concrete file/record (e.g. "Last handoff" pointing at a certain reports file) |
| double-write | INDEX writes both the main file and the archive file, so rows are never lost |

> **Chinese↔English data-contract mapping** (for a cross-language takeover, or when upgrading a workspace initialized with the Chinese package — the field names, markers and block titles below are the data contract, not prose):

| Chinese (v1.0.1) | English | Note |
|---|---|---|
| 编号 | ID | |
| 状态 | Status | |
| 描述 | Description | |
| 要点 | Key points | |
| 代码根路径 | Code root path | renamed from 工程锚点 in v1.0.1 |
| 涉及 | Files involved | |
| 承接 | Claimed by | |
| 进度锚点 | Progress anchor | |
| 上次交接 | Last handoff | |
| 已提炼 | Distilled | renamed from 最后折叠 in v1.0.1 |
| [接力] / [完成] / [废弃] | [handoff] / [done] / [dropped] | INDEX type markers |
| 进行中 / 待认领 / 已阻塞 | In progress / Unclaimed / Blocked | task card status values |
| 本次需求 / 本次涉及工程信息 / 改动点 / 验证结果 / 数据影响 / 下一步 | This request / Code context for this task / Changes / Verification / Data impact / Next step | the 6 handoff blocks |
| 任务卡更新（第 7 块） | Task card update (block 7) | |
| 技能源包 · 提炼回卡 · 人读区 + AI 区 · 项目地图（MAP） · 先查重 · 未建卡的工作 / 已建卡的工作 | skill source package · distill back to card · human-read zone + AI zone · project map (MAP) · dedup check first · work with no card yet / work already on a card | v1.0.1 terminology cleanup (legacy Chinese names → current) |
| 锚点组 · 派生视图 / 机械重写 · 内容级并发安全 · 树链式 | (merged into the "Last handoff" description) · (the human-read zone is auto-generated from the AI zone) · concurrent-write rules · division by module/branch | v1.0.1 terminology cleanup (continued; some legacy terms were removed rather than renamed) |

## 4. Initialization checklist

- [ ] Probed {WORKSPACE_ROOT} first for an existing management instance of this project (if there is one → merge / confirm the single original first; starting a second directory is forbidden)
- [ ] The workspace root {WORKSPACE_ROOT} has been confirmed with the user (default or custom)
- [ ] The management directory has been created: MAP / STATE / REVIEWS / tasks\ / reports\ / INDEX.md / archives\ (**including done\**) / tools\
- [ ] Every MAP placeholder has been replaced with the project's real information (**including [SKILL_SOURCE_PATH], [BACKUP_METHOD], [DECISION_MAKER]**; the rules-section settings are confirmed: INDEX main-file row count / reports archive threshold / periodic AI audit switch)
- [ ] The first task card has been created (with a human-read locator block + AI field block)
- [ ] Handoff template block 7 "Task card update" is ready
- [ ] INDEX.md has been initialized (header + type-marker explanation)
- [ ] Legacy project: lightweight registration completed per LEGACY_ONBOARDING.md (if applicable)

## 5. Management self-check (periodic / on demand)

- [ ] Is the takeover cost constant ≈ one task card ± 1 reports? (inflation points: are the task card / STATE overwrite-style?)
- [ ] Does the task card list hold only active work? Completed cards moved to archives\done\, dropped work traced?
- [ ] Are the INDEX type markers correct? Is the [handoff] chain continuous?
- [ ] Is end-of-work routing carried out (next step → update the card / no next step → move the card to archives\done\)?
- [ ] Are the human-read zone and AI zone updated in sync (no one-sided fork)?
- [ ] Have problems with the skill itself been logged in the workspace REVIEWS.md (meta-management closed loop: blocker → root cause → suggestion → disposition → distilled into the skill)?

## 6. Project viewing view (human eyes · platform-agnostic conventions)

- **Entry (three things for the manager)**: ① new project → quote this skill to initialize; ② view project → view an existing project (see below); ③ call tools → call the built-in tools / generated scripts directly (see tools\README for how to call them).
- **"View project" shows the whole directory structure first by default** (workspace directory tree: tasks / reports / INDEX / REVIEWS / archives / tools in one glance), so a human sees the whole picture before clicking into a place; "how to open / how to click" adapts to platform capability.
- **Two viewing granularities (recent vs full)**:
  - Recent → read the `INDEX.md` main file (only the most recent N=20 rows by default)
  - Full history → read `archives\INDEX_archived.md` only when the user explicitly asks for everything (complete records including archive breakpoints)
- **View directory by directory**:
  - Project overview: positioning + task distribution + current tasks + recent records + decision points + tools area + directory guide
  - Tools area: three-column table (tool / tool name / tool description)
  - All reports: read the `reports\` directory
  - Historical traceback: read the `archives\` directory
  - Decision-point detail: read the STATE decision-point section
  - Task-card detail: read the matching task card file
  - Meta-management detail (skill retrospectives / recovery records): read `REVIEWS.md`
- **Presentation conventions**: a platform that can open files/directories → provide an "open" entry; without that ability → the AI reads and outputs a table/list; without interactive selection → list everything and let the user pick by voice/text
- **INDEX row-count annotation and adjustment wording** (migrated from the INDEX template): the taking-over AI annotates the current row count of the INDEX main file in the handoff reports — below the configured value it shows the number only (e.g. "INDEX recent 16 rows"); at the configured value it adds a "can be changed" note; when the user wants to adjust, remind them: "The INDEX main file is currently configured for N rows and is full. If you want a different row count (e.g. 30/50/100), the archive file holds the complete records for traceback. Confirm the change?" → user confirms → change the MAP setting (the complete records in the archive file are unaffected, historical traceback stays unbroken).

## 7. Maintenance rules (the skill iterating on itself)

- **Single authoritative source**: `SKILL.md` is the **single source of truth** for the protocol; the "protocol overview" in `README.md` and the "Protocol" section of `MAP.template.md` are **derived snapshots** (their version numbers must match SKILL.md); `BLUEPRINT.md` holds design points only and carries no protocol detail, so it **does not take part in version syncing**
- **Protocol change flow**: change SKILL.md first (the authoritative source) → sync the README protocol overview + the MAP protocol section → increment the version consistently in all three, preventing version drift
- **Pass the protection zone first**: for any slimming / simplification / merging / field renaming, go through **section 8 "Change-protection zone"** item by item before touching anything
- **Retrospective before improvement**: log a skill improvement in the workspace REVIEWS.md first (blocker → root cause → suggestion → disposition → distilled into the skill), then land the change
- **Sync the copies after landing**: the skill source package (the entity the MAP "Skill source package path" points at) → each distribution copy (install location and release form are decided by the publisher, e.g. a .user_skills install copy, a ZIP release package; **with no distribution copy, maintaining the source package alone is enough**); when the source package version is higher than the project workspace version, prompt to pull the update — the source package's own disaster tolerance does not rely on distribution copies but on the backup registered in MAP "[BACKUP_METHOD]"

## 8. Change-protection zone (required reading before any update · important)

> This section is a hard gate for any later **update, slimming, simplification, merging or field renaming** of this skill package — its purpose is to stop "convenient editing" from breaking how features work together and from raising the takeover cost. Any update goes through this section item by item before anything is touched.

### A. Change gate (check each item before updating / slimming / simplifying / merging)

1. **Zero feature loss**: cut only duplicate copies, never unique information — the single original of anything cut must still exist and be locatable; if no original can be found, keep the text as it is
2. **Cross-impact check**: before changing/deleting/simplifying any protocol content, look up its **consumers** first — tools\ Checkpoints 1-7 and Recovery points 1-5, other protocol clauses, template fields that reference it. **Renaming a field or block first requires a grep across the whole package to list the sync set**, and every spot is synced before anything is touched; if a local simplification would break the cooperation with the check/recovery/handoff functions, do not do it at all (for interlocking examples and the change self-check see D in this section)
3. **Takeover cost must not rise**: files on the takeover path (task card → reports ±1 → STATE/MAP → INDEX) may only get thinner or stay the same, **never grow**; where content is turned into a pointer, high-frequency rules must stay readable in place (pointers cover only low-frequency detail); merging skills is allowed only when they share the same takeover path and do not add protocol entry files
4. **Three cost-attribution principles (snapshot / ledger / layering)**:
   - **Constant write path**: every field on the end-of-work path must be **mechanically derivable** (a local list, a single-row lookup, taking the first sentence — fillable correctly with your eyes closed); any field that needs a full inventory, a global scan or a cross-directory count is forbidden from entering the end-of-work flow — a field that is hard to fill in correctly will eventually be filled in wrongly, and a wrong number is worse than no number
   - **Snapshot vs ledger division of labour**: STATE = the current snapshot, the INDEX archive file = the full ledger; cumulative statistics (completed/dropped totals and other "period-end balances") belong to the ledger and are **queried on demand** — never move them back to high-frequency maintenance (a counter updated at every end-of-work); a change may move cost from a high-frequency path to a low-frequency one, **never the reverse**
   - **Main-file capacity is a ceiling**: the INDEX main-file row count N (default 20) is the **ceiling device for the default reading cost of a taking-over AI, not a capacity to be expanded** — it must not be raised, nor may the main file be made to carry more history, on the grounds of "more complete / more comprehensive / seeing more" (going from 20 rows to 50/100 looks like a better recent view but is in fact a tax on every taking-over AI); wanting more history → read the archive file on demand, and **the layered reading structure (main file = recent / archive = full) must never be merged**
5. **Authoritative-source flow**: change SKILL.md first (the authoritative source) → sync the README/MAP derived snapshots → versions consistent (see section 7)
6. **Retrospective before improvement**: log the motivation and the plan for a change in REVIEWS.md before landing it

> **Conflict means raise a flag (mandatory reminder duty)**: when the AI carrying out a change finds the proposed change conflicts with any gate/principle above, it MUST **proactively flag it to the user (pop-up / highlighted warning)** — stating which principle is in conflict, which function the change would harm and where the burden would land — and MUST NOT execute it without the user's explicit confirmation; it must not silently obey an instruction to "just do it", nor silently wave a change past the gate.

### B. Load-bearing structures (deleting / weakening / changing the semantics is forbidden — keep each item when updating)

1. **reports pointer chain**: task card "Last handoff" → reports "Next step" → INDEX [handoff] chain + the "Handoff file" column — the load-bearing wall of constant takeover cost
2. **INDEX double-write**: main file N rows + INDEX_archived.md full, rows never lost (moved in, not deleted)
3. **Distill back to card**: every reports file is read at most once with its increments written back to the card — which also serves as the disaster-tolerance layer against accidental deletion (what was read has already gone back to the card)
4. **Archive red line**: an AI never deletes or moves anything under reports\ or archives\ (the only exception is the end-of-work archiving flow, repointing the INDEX row after the move)
5. **Data honesty boundary**: whatever cannot be recovered is marked "data pending"; faking is forbidden
6. **Audit/recovery dependency list**: the 6+1 handoff block titles, the task card's "Last handoff", "Distilled", "Code root path", "Files involved", the ID rules (XXNNNN / numeric increase / collision retry), the MAP branch numbering registry and its three settings (INDEX main-file row count / reports archive threshold / periodic AI audit switch) — these are the **functional interfaces** of Checkpoints 1-7 and Recovery points 1-5, not restatements of the protocol; the slimming knife does not fall here
7. **Consistency between the version's authoritative source and the derived snapshots** (the basis of Checkpoint 6)

### C. Record and recovery safeguards (runtime, kept alongside any change)

- **Three-layer division of change records**: MAP = the structure ledger (new paths / new branches; branch registration is backed by Checkpoint 4) · reports = the change-summary ledger (attach a commit hash where git is available) · INDEX = the pointer ledger (double-write, never lost) — content accuracy originates in reports
- **MAP path-registry reconciliation**: Checkpoint 7 verifies that registry paths exist — after manually moving/renaming a directory, MAP must be updated, preventing "the map going silently stale"
- **Backup method registration**: the MAP environment section "[BACKUP_METHOD]" (git / periodic copy / none) — deleting a whole directory exceeds what the protocol can recover, and the backup is the last resort; the protocol registers this, it does not package an implementation
- **Source-package cross-restoration (like financial reconciliation)**: several records corroborate each other, and **what is being reconciled is consistency, not the direct restoration of information** — if a skill source package file is damaged/deleted → ① restore `SKILL.md` word for word from **any project workspace** (it was copied verbatim into the workspace at initialization, so it is the original); ② README/BLUEPRINT/LEGACY/tools sub-specs have no workspace copy → retrieve them per the MAP "[BACKUP_METHOD]" or a distribution copy, and mark "pending" rather than fake anything that cannot be retrieved; ③ after restoration run Checkpoint 6 to verify version consistency and record the recovery action in REVIEWS.md — reason from traces where reconciliation disagrees, allow a partial restoration, and never fill gaps from memory

### D. Interlocking chain warning (read at every change)

> This skill has **no isolated protocol line**. Many single features look like a few lines but are in fact the crossing point of several function points — deleting or rewriting "a few lines" breaks a function chain running somewhere else. Look at the examples first, then go through the six questions, at every change, with great care.

**Interlocking examples (looks like a few lines, is actually a node):**

| What it looks like | What it actually carries |
|---|---|
| MAP rules-section three settings (about 3 lines) | The operating basis of three features — INDEX truncation, reports archiving, the checks audit switch — plus the reconciliation input of Recovery point 5 |
| INDEX header "row-count annotation wording" (a 1-line pointer) | The source of Recovery point 5's behaviour ("prompt that it can be changed + point the breakpoint at the archive") — the wording original lives in section 6 of SKILL |
| Task card "Last handoff" field (1 line) | The takeover-chain entry + Checkpoint 5's anchor-existence check + the object of Recovery point 3's broken-link repair |
| Handoff 6+1 block titles (7 lines) | The block-by-block check target of Checkpoint 1's end-of-work gate |
| STATE "entry-level write" (1 line) | The guarantee that parallel end-of-work does not conflict + the evidence for Checkpoint 1's STATE ✓ |
| INDEX ID rules (2 lines) | The entire logical basis of Checkpoint 4 + the [handoff] chain continuing across archives |

**Six questions before a change (stop if you cannot answer them all):**
1. Which tools\ checkpoints/recovery points consume these lines as input or as a check target?
2. Which templates (HANDOVER / TASK_CARD / INDEX / STATE / MAP) reference them as fields or block titles?
3. Which derived snapshots (README / MAP protocol section) and other SKILL lines reference them?
4. After the change, does every function that depended on it still have an **equivalent path** to finish its job?
5. Will a taking-over AI have to read more because of this (does the takeover cost rise)?
6. Is the sync set complete, and has the change record been written to REVIEWS.md?

**Discipline**: if you cannot answer clearly "who consumes these lines", do not change them; when changing, **prefer too little over breaking a link** — better to keep one apparently redundant protocol line than to break one running link in the chain.

### E. Reconciliation mindset (design principle · required reading before changing anything about IDs / timestamps / anchors / evidence)

> **Layering principle**: a document protocol **does not, and cannot, supervise** an AI in real time — supervision is the job of the tools\ script layer (Checkpoints 1-7 are all deterministic functions). The document layer's job is to be **auditable after the fact**: every claim has at least two independent records corroborating it, so laziness, faking and mistakes are bound to surface in reconciliation. The protocol is not designed for "an AI will certainly follow the rules" but for "**breaking the rules is bound to leave a trace**".

> **Anti-incentive principle**: no conflict-resolution rule may **leave a profit in faking**. Lesson: the old "across branches the later timestamp wins" amounted to "whoever fakes a timestamp wins" — a referee rule that rewards cheating is a hole. The current design: timestamps are supporting evidence only, decisions go to the MAP [DECISION_MAKER], collisions are retried with a trace — so faking yields nothing.

**Four reconciliation anchors:**

| Anchor | Carrier | What it exposes |
|---|---|---|
| Time anchor | reports file-name date · INDEX row date · handoff timestamp | Reversed/backward time → suspicious (a supporting heuristic, never the decision) |
| ID anchor | `XXNNNN`: letters = a branch registered in MAP · digits = monotonic within the branch · collision retry leaves a trace | Unregistered branch / skipped number / duplicate number / reverse order → Checkpoint 4 |
| Identity anchor | AI tag `{PLATFORM}-{AI_NAME}-{SHORT_CODE}` | Impersonation / mixed authorship → compare the INDEX row with the card's "Claimed by" |
| Evidence anchor | the commit hash in "Changes" (where git is available) | A claimed change that never happened → `git show` against the original evidence |

> **ID rules are a reconciliation interface, not a formatting preference**: changing the ID format / increase rule / registration requirement means changing the entire logical basis of Checkpoint 4 and the way the [handoff] chain continues (see B.6) — it must first pass the A.2 cross-impact check, grepping the whole package for the sync set before anything is touched.

> The complete design blueprint is in `BLUEPRINT.md` (its 6 points are the authoritative quick-reference); the HTML edition `project-management-lite-blueprint.html` is a supplementary design document outside the package (this package is pure Markdown and does not carry it; a publisher only needs to place it outside the package).
