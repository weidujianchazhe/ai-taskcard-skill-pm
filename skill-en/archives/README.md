# archives\ (archive)

> Version v1.2.1 · Protocol/template specification only; no default runtime or automatic archive writer is implied.

> In only, never out: content moved into this directory is never deleted. Keep this directory — do not delete it.

## Archived content

| Subdirectory/file | Source | Trigger |
|---|---|---|
| `reports\` (archived handoff files) | old handoff records under reports\ | rolling archive once the count reaches the MAP "reports archive threshold" (default 20) |
| `done\` (completed-card archive) | completed task cards under tasks\ | moved in during a completion-type end-of-work |
| `INDEX_archived.md` (INDEX archive file) | canonical historical rows of INDEX.md | created at initialization; append and verify the hash first, then CAS-update the main file; on failure keep the main file and write `CONFLICT_*.md` |

> Archive algorithm: read and hash the source, acquire the single-writer/CAS boundary, append, verify exact UTF-8 SHA-256 bytes, then atomically update the bounded active index. Any failure leaves the source and prior index untouched and produces a conflict/quarantine file for manager review.
