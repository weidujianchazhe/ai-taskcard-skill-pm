# Local script spec master document (SCRIPT_SPEC)

> **Purpose**: at project rollout the AI reads this file through, reads the sub-specs on demand (SPEC_protocol_audit / SPEC_recovery), confirms platform and modules with the user, then generates single-platform local scripts into the project workspace root.
> **Trigger**: when the user says "set up a local check script", "AI operations keep failing", "I need check/self-healing tools", the AI reads this file and runs the generation flow.
> **Relation to the skill**: this file is a skill source package spec (cross-platform, pure MD); generated scripts are local assets of the project workspace (single-platform implementation, not in the skill package, travel with the project).
> **Entry order**: custom\README.md (entry) → this file (master spec) → SPEC_protocol_audit.md / SPEC_recovery.md (sub-specs).
> **Revision (v1.0.1, 2026-09-09)**: generation granularity defaults to "one feature per script"; added the set·group execution framework with "script layer / execution layer separation" (see the end of section 2, Generation flow).

---

## 1. Capability map: what scripts can and cannot do

### What they can do reliably (filesystem/format layer — deterministic conclusions, automatically decidable)

| Capability | What it catches | Protocol anchor it relies on |
|---|---|---|
| End-of-work gate | Going through the motions on the four-piece set check, missing pieces | Distilled / Last handoff / ID |
| Drift detection | Version inconsistency across the three synchronized copies | Version line (v1.0.1) |
| ID audit | Unregistered branch, skipped numbers, collisions, illegal type | Branch numbering registry / XXNNNN |
| Naming audit | reports naming violations, duplicate names | YYYY-MM-DD_topic_AI-tag |
| Reference audit | Dangling anchor, INDEX pointing at something that does not exist | Code root path / Last handoff |
| Out-of-bounds changes | Files changed outside "Files involved" | Code root path / Files involved |
| Concurrent conflict | Another party writing in between read-before-write and verify-after-write | mtime / content hash |
| Recovery scaffolding | A rebuild draft after data loss | INDEX / reports (append-only) |
| Archive consistency | reports over the threshold, done reconciliation | archives conventions |

### What they cannot do (semantic layer — indeterminate conclusions, hard-judging forbidden)

| Capability | Why a script cannot | Disposition |
|---|---|---|
| Whether Key points really cover the reports content | semantic comparison | Output "to be verified", hand to the model/person |
| Whether the handoff content is real (done right, not just written) | format can only prove "written" | Output "to be verified" |
| Value judgement of drop / handoff / disposition | business judgement | Hand to the manager |

> **Iron rule 1**: a script outputs only three conclusions — [pass] / [problem] (definite violation) / [to be verified] (uncertain, hand to the model or person). Never hard-judge [to be verified] as [problem] or [pass].

### Three-layer audit strategy (scripts are not the only means)

1. **Script layer**: the modules of this master spec — catch format/file/completeness violations (cheap, can run daily).
2. **Model review layer**: feed the script's [to be verified] and suspicious [problem] items to the current AI with a "review prompt" to re-check the semantics (e.g. read the anchor reports and judge whether the card's Key points cover the key information) — no separate script; do it in conversation.
3. **Human final-arbitration layer**: if review is still inconclusive → list for the manager to decide (and write the REVIEWS blocker point; events are collected automatically).

---

## 2. Generation flow (AI rollout steps)

1. Read this file → read the matching sub-spec → ask the user three things:
   ① Platform and runtime environment: win + PowerShell? mac/linux + bash? Is python3 available?
   ② Which feature scripts to generate: default **one feature per script** — generate one per Checkpoint/Recovery point in the sub-spec (e.g. check_c1_end_of_work_gate, recover_r3_anchor_repair), each script independent, read-only by default, with the same interface contract; no big aggregate script
   ③ Whether whole-category/group execution is needed: an optional "runner" — two default sets by prefix (check_* protocol-audit set, recover_* recovery-aid set) + run_groups.json for custom cross-set grouping (see "generation granularity and execution framework" at the end)
   ④ Where results land: terminal only / write reports\check_date_topic_tag.md and register in INDEX / both
2. Generate the single-platform script → put it in the project workspace root (e.g. check_local.ps1 / check_local.sh / check_local.py).
3. Self-check once with sample paths → the output conforms to the "unified interface contract".
4. State the trigger: manual / automatic run after end of work / scheduled task (see tools\schedule).
5. If whole-category/cross-category batch execution is needed: provide/explain the runner per "generation granularity and execution framework" below; do not generate an aggregate script.

### Generation granularity and execution framework (script layer / execution layer separation)

- **Script layer (default: one feature per script)**: each Checkpoint/Recovery point = one independent script, named `<prefix>_<feature_point>_<topic>.ps1` (check_c1_end_of_work_gate, recover_r3_anchor_repair…); no aggregate script bundling multiple features — the cost of using one feature does not grow with the total number of tools.
- **Execution layer (optional orchestration, no code bundled)**:
  - Default whole sets: grouped automatically by filename prefix — `check_*` = protocol-audit set, `recover_*` = recovery-aid set; a whole set can be run member by member with one command;
  - Custom groups: a config file (run_groups.json) declares a higher-level grouping; members may be script names or set names (cross-set combinations supported, e.g. "pre-release self-check = check set + archive consistency");
  - Unified runner interface: `-Target <script_name|set_name|group_name>` for single/whole-set/group runs; executes member by member and aggregates exit codes (any member [problem]→1, only [to be verified]→2, all pass→0).

---

## 3. Unified interface contract (all generated scripts must obey)

- **Exit codes**: 0 = all pass; 1 = has [problem] (definite violation); 2 = has [to be verified]; 3 = the script's own error
- **Output**: print [pass] / [problem] / [to be verified] in sections + "file or line: specific description" + a fix suggestion with each problem; never silent
- **Read-only by default**: except for write operations explicitly marked in SPEC_recovery, never change files; repair-type output is suggestions only, executed after user confirmation
- **Platform self-check**: the script probes the platform at the start (win/mac/linux + available shell); the path separator follows the platform; if no legal runtime environment is detected → exit code 3 and report not applicable
- **Boundary discipline**: any "semantic judgement" always goes to [to be verified], never disguised as [problem]
- **Resource restraint**: scripts are lightweight by default — plain text/file checks, no heavy dependencies; on a performance-limited host use incremental/sampled runs (check only the most recent N entries, skip the full git diff) to avoid slowing the management session

---

## 4. Platform adaptation table (select at generation time per the detected platform)

| Capability | PowerShell (win) | bash (mac/linux) | python3 (cross-platform, optional) |
|---|---|---|---|
| File existence | Test-Path | test -e | os.path.exists |
| Modification time | (Get-Item).LastWriteTime | stat -c %Y | os.path.getmtime |
| Content hash | Get-FileHash -Algorithm SHA256 | sha256sum | hashlib.sha256 |
| Regex extraction | -match / -replace | grep -E / sed -E | re |
| Directory recursion | Get-ChildItem -Recurse | find | os.walk |
| Text write | Set-Content -Encoding UTF8 | cat > | open(..., encoding=...) |

> Path separator: Windows uses \, POSIX uses /; hard-coding separators inside a script is forbidden; join with platform APIs.
> Chinese content: always UTF-8; in PowerShell mind the encoding parameter (e.g. -Encoding UTF8).

---

## 5. Sub-spec index

| Sub-spec | Purpose | Content |
|---|---|---|
| SPEC_protocol_audit.md | Protocol audit (checks primary) | End-of-work gate / out-of-bounds changes / concurrent conflict / ID and INDEX / naming and references / version drift / registry reconciliation |
| SPEC_recovery.md | Self-healing aids (recovery primary) | Card-rebuild scaffolding / STATE recovery / broken-anchor repair / stale version / archive consistency |

> The "Boundaries" field of every Checkpoint marks what is [to be verified] (needs model/human review); do not hard-judge beyond bounds.
## 6. Continuous operation and automation boundaries

> Can scripts "run continuously and fully automate the management and audit of the AI"? The answer is layered — the deterministic layer can be fully unattended; the semantic layer never can. This section is the boundary that must be obeyed when generating resident/scheduled scripts.

### What can be "thorough + continuous + unattended" (deterministic layer)

| Continuous task | What it catches | Defect it addresses |
|---|---|---|
| File-watchdog | Concurrent write conflicts, out-of-bounds changes, files changed without going through end-of-work routing | Reliance on discipline |
| Invariant checks | Monotonic IDs, naming conformance, complete anchors, version drift, archive consistency | Format-layer laziness |
| End-of-work gate | Claims end of work → force the four-piece set verification; cannot leave until it passes | Ticking without doing |
| Automatic anomaly collection | Recovery actions/violations → automatically recorded as REVIEWS blocker points | REVIEWS planted in only 3 places |
| Maintenance reminders | reports over the threshold, INDEX reaching N lines → automatic reminder | Missed archiving |

### What cannot be fully automated (semantic layer = the ceiling)

| Can never audit | Why |
|---|---|
| Whether code/document changes are right (whether they really solved the task) | correctness is an open problem |
| Whether Key points really cover the reports content (whether distillation really happened) | semantic comparison |
| Whether the "verification passed" written in the handoff was really verified | format proves only "written", not "done" |
| Value judgement of drop/handoff/disposition | business judgement |

> Root cause: a script is a deterministic function, semantics is an open problem. Any "automatic semantic audit" is in essence introducing one more model, and that model will also cut corners/make mistakes — so the semantic layer is forever semi-automatic and must ultimately be arbitrated by a human.

### The correct architecture for continuous operation (three layers, not a single script looping forever)

```
Trigger: scheduled (cron/scheduled task) + event (after end of work) + manual
  ↓
Script layer (continuous · read-only · cheap · fully automatic) ── deterministic checks, producing [pass]/[problem]/[to be verified]
  ↓
Model review layer (periodic batch · anomaly-triggered · has a cost) ── reviews only [to be verified] and suspicious [problem]
  ↓
Human final-arbitration layer (exceptions · low frequency) ── decides drop/disposition, records REVIEWS
```

**Alerting and restraint principles**:
- Scripts are neither silent nor a screen flood — stay quiet when everything passes, report only differences;
- Accumulated [to be verified] items are fed to the model in batches, not one by one to a human;
- The watchdog runs incrementally/sampled, not a full scan (echoing "resource restraint").
- Pending human arbitration = asynchronous queueing, non-blocking: arbitration items are only recorded, no shutdown, and applied retroactively after the human rules in batch; the only blocking point is the "end-of-work gate", and it occurs at the end-of-work boundary (the work is done, the question is whether you may clock off), not as a mid-work interruption. Audit is a bypass, not the main chain.

### Hard constraints on generated scripts at rollout

1. Resident/scheduled scripts handle only the "deterministic layer"; on any semantic judgement always mark [to be verified] and never pretend to be able to audit it.
2. "Continuous" depends on the host's background scheduling capability; a platform without it degrades to "run once automatically at the end of every session" (pseudo-continuous, but it still has gate value).
3. The value of a fully automatic script is not "thoroughness" but "freeing human attention from watching format to auditing semantics only".
