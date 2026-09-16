# Static validation asset (v1.2.0)

This is a **static, read-only checklist**, not a runtime or watcher. It validates the English source package before release; it does not create or modify a project workspace.

## Required checks

- [ ] Every synchronized document reports `v1.2.0`; `SKILL.md` frontmatter reports `1.2.0`.
- [ ] `SKILL.md` states the protocol/template/script-generation boundary and no default runtime.
- [ ] `TASK-ID`, `EVENT-ID`, and `DESIGN-ID` are stable, immutable, and lifecycle transitions emit events.
- [ ] Role/permission and mode matrices are present; triggers are explicit.
- [ ] Completion gate is blocking and checks the four-piece set plus revision/hash evidence.
- [ ] Initialization lists `archives\INDEX_archived.md`; PowerShell and bash examples create it.
- [ ] Archive index is immutable, append-only, canonical, single-writer, pointer-based, and has a failure path.
- [ ] Revision, exact UTF-8 SHA-256, CAS, atomic same-directory writes, single-writer boundaries, and conflict files are specified.
- [ ] STATE entry-level concurrency boundaries are explicit.
- [ ] Recovery records raw/normalized SHA-256, encoding/BOM, source proof, revision, and normalization algorithm.
- [ ] No generated runtime, daemon, watcher, scheduler, or project implementation is included in `skill-en`.

## Manual result

Record the date, reviewer, and any `[problem]` or `[to be verified]` findings in the release task or project `REVIEWS.md`; do not alter the source package from this checklist.
