# Self-healing aids script spec (SPEC_recovery)

> **Purpose**: generate "recovery aids" local scripts. Read-only by default + output "drafts/suggestions"; any write operation (persisting a rebuilt file, etc.) must have user confirmation before it runs.
> **Proof requirement (v1.2.0)**: recovery output records raw and normalized SHA-256, UTF-8 encoding/BOM, source pointer/revision, and normalization algorithm. Raw bytes remain authoritative; unknown proof is `data pending`, never fabricated.
> **Trigger**: when data files are lost / STATE is corrupt / anchors are broken / the version is stale / history must be inspected, the AI reads this file to generate a script or directly executes its logic.
> **Generation granularity**: each Recovery point = one independent script (recover_<recovery_point>_<topic>.ps1, default one feature per script); whole-set/group execution is orchestrated by the runner (see SCRIPT_SPEC "generation granularity and execution framework").

---

## Recovery point 1: task card rebuild scaffolding

**Purpose**: when a task card is lost, hand "what a machine can do" to the script and leave the semantic part to the AI.
**Input**: INDEX.md, reports\, archives\.
**Logic**:
```
Recent INDEX rows → find the most recent [handoff] row → take its "handoff file" column → walk the chain to list candidate reports (by date, newest first)
Generate a "task card rebuild draft": title/ID suggestion (branch registry + increment) / Last handoff (most recent handoff file candidates) / Files involved (paths extracted from reports) filled automatically
Description / Key points / Distilled → left blank + marked ⚠to be filled by the AI (requires reading the candidate reports to complete the semantics)
The card tail carries the "end-of-work protocol quick note" (copied verbatim from the TASK_CARD.template card tail, so a rebuilt card does not decouple from the protocol)
Progress anchor → fill "—" (the mid-way landing point cannot be inferred during a rebuild; fabrication forbidden)
```
**Output**: the draft to the terminal (or written to tasks\ after user confirmation).
**Boundaries**: rebuilt content is inferred from reports → the draft's semantic fields must be marked "to be confirmed"; landing it directly as a formal card is forbidden.

---

## Recovery point 2: STATE recovery aids

**Purpose**: rebuild the skeleton from the latest reports when STATE is corrupt.
**Logic**:
```
Read the latest reports containing "Next step" (by [handoff] anchor or reverse chronological order)
Extract: current progress / tasks in progress / decision points → generate a STATE draft (human-read zone 3 lines + AI zone skeleton)
```
**Output**: a draft (written over STATE.md after AI/user confirmation).
**Boundaries**: incomplete reports → the draft marks the gaps "to be tidied on demand"; do not fabricate.

---

## Recovery point 3: broken-anchor repair

**Purpose**: give repair suggestions when the card's "Last handoff" points at something that does not exist (archived/deleted by mistake).
**Logic**:
```
Scan all active cards → parse each "Last handoff" anchor → does the target exist?
Does not exist → find the actual location in INDEX (main + archive) by topic/time (it may have moved into archives\) → output "suggest changing the anchor to X"
```
**Output**: broken-link list + suggested new anchors ([to be verified]: change the card only after AI confirmation).
**Boundaries**: no matching file found → mark the suggestion "data pending"; do not forge an anchor.

---

## Recovery point 4: stale version detection (source package vs workspace)

**Purpose**: source package version > workspace → prompt to pull the update (corresponds to "gap filling: missing or stale").
**Input**: MAP environment section "skill source package path" (filled "—" or unregistered → prompt to register it first).
**Logic**:
```
Compare the version lines of each protocol file (SKILL/README/MAP) in the workspace vs the source package
Source package higher → [problem]: list the stale files + the "copy the template from the source package, instantiate and refill" steps
```
**Output**: stale list + update steps (write operations need user confirmation).
**Boundaries**: no source package path → output the prompt "register the skill source package path first"; not counted as a violation.

---

## Recovery point 5: archive consistency

**Purpose**: reports over the threshold, completed-card reconciliation, INDEX main file truncation breakpoint.
**Logic**:
```
reports\ count > MAP rules section "reports archive threshold" (default 20) → list the N oldest entries and suggest moving them to archives\ (by month)
No cards in tasks\ but cards in archives\done\: check whether INDEX has corresponding [done] lines
INDEX main file reaches N lines → prompt "can change" + point the breakpoint position at archives\INDEX_archived.md
```
**Output**: suggestion list (moving/registering are write operations and need user confirmation).
**Boundaries**: whether to archive is a maintenance decision → the script only lists candidates; it never moves anything automatically.

---

> **General boundary**: all "write" actions in this spec (persisting a draft, moving files, updating anchors) output suggestions by default and need user confirmation; "semantic filling" (Description / Key points / summary) always goes to [to be verified] and is completed by the current AI after reading the source files.
> **Recovery registration (meta-management routing)**: after any recovery action completes, append one blocker point line in the workspace `REVIEWS.md` — do not write to reports\, do not register in INDEX.
