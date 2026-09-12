# Scheduled task spec (schedule\)

> Reminders / periodic checks / periodic reporting. **Implementation relies on each platform's scheduling capability** (this skill only holds the spec, no bundled implementation).

## Purpose

| Type | Example | Related |
|---|---|---|
| Scheduled reminder | meeting reminder, deadline reminder | — |
| Periodic check | daily/weekly project status check | wired to the `checks\` switch (off by default; runs only when enabled) |
| Periodic reporting | daily/weekly report generation | see `report\` |

## Conventions

1. When a scheduled task fires, state explicitly in the execution instruction "this request was triggered by scheduled task [TASK_NAME]"
2. Periodic checks obey the `checks\` switch: off by default; only after the manager enables it does the AI run them periodically
3. Records produced on a schedule settle under the existing protocol (reports\ + INDEX + STATE); do not build a separate system
4. Do not write scheduling implementations into the skill — each platform uses its own scheduling capability; the output only needs to align with this protocol
5. **Platform has no scheduling capability** → read the `custom\` guide and generate a local script (Windows scheduled task / Linux cron)
