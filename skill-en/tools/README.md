# Optional tools area (tools\)

> **Pull on demand, not on the takeover path**: an AI taking over work does not need to read this directory; read the matching tool spec only for a concrete need (check / diagram / schedule / report).

## Built-in tools

| Tool | Purpose | Trigger |
|---|---|---|
| `checks\` | Project checks (mainly human-triggered; the AI periodic sweep switch defaults to off) | When the project manager has a need |
| `visualize\` | Visualization spec (platform-agnostic) | When a diagram/chart is needed to express structural relations |
| `schedule\` | Scheduled tasks (reminders / periodic checks / periodic reporting) | When scheduling capability is needed |
| `report\` | Report generation (daily/weekly report data pull) | When a report is needed |
| `custom\` | Local script generation guide (user-defined scripts) | When AI operations on a platform repeatedly fail |

## Anti-runaway rules (three iron rules)

1. **Pull on demand**: read the matching tool spec only when needed; do not preload
2. **Not on the takeover path**: tool specs are not added to the must-read takeover flow
3. **Specs only, no platform implementations**: protocols are registered; implementation relies on each platform's native capability (no implementation bundled)

## Invocation (the manager can invoke directly)

- Tools can be **invoked directly**: in any session (a new session / a session whose work is paused or terminated) the manager simply says "invoke tool X / generate the weekly report / check the records / run the local script"; the AI reads the matching spec or runs an already-generated script, with no need to browse the directory first.
- Already-generated custom scripts (in the project workspace root, e.g. check_local.ps1 / check_local.sh) and built-in tool specs are both directly invocable tools.
- Context-independent: invoking a tool only reads workspace files and does not interrupt other sessions that are working.
- Difference from "view project": viewing a project is "browse the directory → discover tools → only then decide"; invoking a tool is "already know which tool → invoke directly".

## Adding tools (if extension is needed)

- Following the three iron rules above, add a subdirectory + spec file under `tools\`, and register it in this README
- Do not add tools that "the platform natively already does" (such as search/translation/writing/minutes transcription/Q&A — their output settles naturally under the existing protocol)
- If discipline problems repeatedly occur on some platform, add a local check script for that platform (single-platform implementation, not in the skill package); the skill side only does protocol registration
