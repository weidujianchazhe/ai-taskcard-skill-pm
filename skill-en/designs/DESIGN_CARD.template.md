# [Design topic] Design card

> Version v1.2.0

- **DESIGN-ID**: `DSN-YYYYMMDD-XXXXXX` (immutable after creation)
- **Status**: draft / review / approved / rejected / retired
- **Proposer**: [AI identity]
- **Approver**: [manager; `—` until approved]
- **Approval EVENT-ID**: [EVT-...; `—` until approved]
- **Affected mode**: light / standard / coordination
- **Scope and invariants**: [goal, non-goals, protocol constraints]
- **Role/permission changes**: [owner, audit, and arbitration responsibilities]
- **Migration and rollback**: [file set, compatibility, failure handling]
- **Verification evidence**: [checks/fixtures/commands and results]

## Lifecycle gates

1. Draft -> review: complete scope, permissions, migration, and verification evidence.
2. Review -> approved/rejected: the manager records an approval or rejection EVENT-ID; no execution card may be generated before approval.
3. Approved -> execution card: every execution card links this DESIGN-ID and receives a new TASK-ID.
4. Approved -> retired: the manager records a retirement EVENT-ID; existing execution cards are not rewritten.
