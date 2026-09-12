# archives\ (archive)

> In only, never out: content moved into this directory is never deleted. Keep this directory — do not delete it.

## Archived content

| Subdirectory/file | Source | Trigger |
|---|---|---|
| `reports\` (archived handoff files) | old handoff records under reports\ | rolling archive once the count reaches the MAP "reports archive threshold" (default 20) |
| `done\` (completed-card archive) | completed task cards under tasks\ | moved in during a completion-type end-of-work |
| `INDEX_archived.md` (INDEX archive file) | historical rows of INDEX.md | double-write mechanism — the main file keeps N rows, this file stores every row |
