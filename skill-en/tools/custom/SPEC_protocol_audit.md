# Protocol audit script spec (SPEC_protocol_audit)

> **Purpose**: generate "protocol audit" local scripts (checks primary, read-only by default). At rollout the AI maps each Checkpoint to platform commands (see the SCRIPT_SPEC platform adaptation table).
> **Trigger**: automatic run after end of work / manual run by the manager / periodic check (the tools\checks switch).
> **Generation granularity**: each Checkpoint = one independent script (check_<checkpoint>_<topic>.ps1, default one feature per script); whole-set/group execution is orchestrated by the runner (see SCRIPT_SPEC "generation granularity and execution framework").

---

## Checkpoint 1: end-of-work gate (four-piece set authenticity)

**Purpose**: catch going through the motions on the "End-of-work check (4/4)" tick.
**Input**: the most recent handoff reports (or one the user specifies).
**Logic**:
```
Read reports → verify all 6+1 block titles present (This request / Code context for this task / Changes / Verification / Data impact / Next step / Task card update)
Parse the "Task card update" block → target card (update, or move the card to archives\done\)
Card ✓: the target card exists; and if this session's anchor is not "—" → the card's "Distilled" is not "—" and is not earlier than the anchor (filename/time comparison)
INDEX ✓: INDEX.md contains this session's ID line; ID = registered branch + numeric increment (see Checkpoint 4)
STATE ✓: STATE.md shows evidence of this session's write (mtime/hash change, or "last update" ≥ handoff time)
Card-move type: the card is already in archives\done\ and INDEX has a [done] line
```
**Output**: for each piece [pass]/[problem]; problems carry "which piece is missing + suggested action".
**Boundaries**: whether the handoff content is true → [to be verified] (the script checks only "whether the pieces are complete and the fields filled", not "whether it was done right").
**Note**: "handoff ✓ exists" passes trivially (skipped in the old version) — this spec instead verifies that all 6+1 block titles are present, closing the "tick even when there is only an empty file" hole.

---

## Checkpoint 2: out-of-bounds changes (careless moves)

**Purpose**: catch changes to files outside the task card's "Files involved".
**Input**: active task card + Code root path (the card's "Code root path" field or MAP).
**Logic**:
```
Parse the "Files involved" field → allowed file/directory list
git available: take the actual changes from git status/diff → difference set (actual - allowed) = out of bounds
no git: approximate with an mtime window (files changed inside the time window); mark the result "approximate"
```
**Output**: list of out-of-bounds files [problem].
**Boundaries**: approximate result without git → mark "approximate"; files inside allowed directories → not out of bounds.

---

## Checkpoint 3: concurrent conflict (two AIs writing one file)

**Purpose**: how well read-before-write/verify-after-write is carried out.
**Input**: STATE.md / the target task card + the moment the write occurred.
**Logic** (to hook into the end-of-work script at rollout):
```
Before the overwrite write: record mtime + content hash
After the write: re-read mtime/hash → inconsistent with before the write → someone interleaved a write (conflict)
```
**Output**: [pass] or [problem] (suspected conflict + a suggestion to handle it per the conflict arbitration rules).
**Boundaries**: meaningful only if run immediately after the AI declares a write; a pure post-hoc audit can only look at hash changes → [to be verified]. Timestamps are corroborating evidence only — cross-branch conflicts are not arbitrated by timestamp (cross-platform clocks are untrustworthy); both sides leave a trace in reports and hand it to the manager; corroborating heuristic: increasing IDs + non-decreasing timestamps = normal, reversed order makes the timestamp suspect (flag for human attention; not grounds for a ruling).

---

## Checkpoint 4: ID and INDEX integrity

**Purpose**: ID system conformance (format validation is the core asset against corner-cutting).
**Input**: the full INDEX.md text (including the archive breakpoint), MAP Branch numbering registry.
**Logic**:
```
ID format: two letters + 4~5 digits
Same branch: digits strictly increasing (compare numerically, EX10000 > EX9999, not as strings)
Branch letters: must exist in the MAP "Branch numbering registry" (unregistered = [problem])
Type markers: ∈ {[handoff], [done], [dropped]}
[handoff] chain: at the main file's truncation point → the next hop continues in archives\INDEX_archived.md (a chain is not judged a violation; pointing at the archive is enough)
Handoff column: the file it points at exists (reports\ or archives\)
```
**Output**: list of violating lines [problem]; uncertain ownership/value → [to be verified].
**Boundaries**: whether an ID corresponds to "work actually done" → [to be verified] (format can only prove the sequence is conformant).

---

## Checkpoint 5: naming and reference integrity

**Purpose**: reports naming conformance + no dangling anchors.
**Logic**:
```
reports\*.md filenames match the date_topic_AI-tag convention (per the MAP naming convention; the AI tag contains "-")
tasks\ active card "Last handoff" anchors → the target exists (reports\ or archives\)
Template files are not modified as if they were work files
```
**Output**: [problem] list.
**Boundaries**: whether the topic wording is apt → [to be verified].

---

## Checkpoint 6: version drift (three-way sync + source package)

**Purpose**: SKILL/README/MAP version lines inconsistent = changed without syncing.
**Logic**:
```
Read SKILL.md frontmatter version, the "version vX" lines in README.md / MAP.template.md (BLUEPRINT does not take part in version sync — it records design key points only; no version line means no alarm)
When the source package path exists (MAP environment section "skill source package path"): compare workspace vs source package
Any inconsistency → [problem]: which copy is old / which version field is missing
```
**Output**: [problem] list + the suggestion "sync the 3 places per the SKILL.md maintenance spec and bump the version".
**Boundaries**: content drift but the version number happens to match → [to be verified] (recommend model review).

---

## Checkpoint 7: path registry reconciliation (MAP vs the actual filesystem)

**Purpose**: catch "stale map" — registry paths have been moved/renamed/deleted, MAP silently goes invalid, and every AI that follows the map to find files gets lost with no alarm.
**Input**: all MAP Path registry rows + the environment section's "skill source package path" and "workspace backup method".
**Logic**:
```
Take each registry path row by row → verify existence (directory/file)
Does not exist → [problem]: list the dead rows + suggest "update that row in the MAP registry" (the update is a write operation and needs user confirmation)
Skip rules (not counted as problems): ① template placeholder rows (e.g. `[NEW_PATH]`) — skip; ② rows marked "created at first archive / created at first X" for deferred creation (e.g. archives\INDEX_archived.md) — when they do not exist, downgrade to a [to be verified] note ("not yet created, which is normal"), do not report [problem]
The "skill source package" row: verify against the environment section's "skill source package path" (filled "—" / unregistered → skip, not counted as a problem)
File integrity inside reports\ / archives\ → belongs to Checkpoint 4 (handoff column existence) and Recovery point 5 (reconciliation); here verify only that the directories themselves exist
```
**Output**: list of dead paths [problem].
**Boundaries**: the path exists but the content is empty/corrupt → [to be verified] (the script checks existence only, not content); accidental deletion of a whole directory is a recovery problem → route to Recovery points 1-3 + fall back per the MAP "backup method".
