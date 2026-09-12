**English** | [简体中文](README.md)

# AI-Relay Project Management Lite (ai-taskcard-skill-pm)

> **Last updated: 2026-09-12** (version v1.0.1)
>
> A general-purpose "cross-obstacle" project-management skill: **task-card-driven lightweight takeover · overwrite-style state · end-of-work routing handoff · INDEX type markers**.
> Supports multi-AI / cross-platform / cross-time / cross-project relay — crossing platform, AI, time and project obstacles, so the taking-over side understands the work at a lower reading cost and with fewer errors.

**Core philosophy: a project may be complex and heavy, the taking-over AI reads only what it needs — the burden does not grow with project size.**

Inspired by 《为什么越改越偏？》("Why Does It Drift Further With Every Revision?") — the bigger the project, the heavier a full read; this skill lets the AI read only "one task card ± 1 handoff" at takeover instead of being crushed by the project's entire backlog.

---

## Language versions / 语言版本

| Language | Skill package | README | Install |
|---|---|---|---|
| **English** | [`skill-en/`](skill-en/) | this file | copy `skill-en/` into your skills directory |
| **简体中文** | [`skill/`](skill/) | [README.md](README.md) | 复制 `skill/` 到技能目录 |

The two packages are **fully self-contained and structurally identical** — same file names, same relative paths, same protocol version (`v1.0.1`). They are two language editions of one protocol, not two different skills.

> **Do not mix languages inside a single workspace.** Task-card field names, INDEX type markers and handoff block titles are the data contract, and they are fixed per language. A workspace is initialized in one language and stays in it. When a handoff really must cross languages, map field by field with the Chinese↔English term table in `SKILL.md` section 3.4.

## 1. Features

| Feature | Description |
|---|---|
| **Task-card-driven takeover** | Takeover reads only the matching task card (description / key points / files involved / code root path / last handoff) — precise arrival, no wandering through the whole project |
| **Overwrite-style state** | Task card / STATE are always overwritten to the latest; no appending, no snowballing; history goes to reports + INDEX |
| **End-of-work four-piece set** | Handoff → card update/move → INDEX entry → STATE sync, a closed loop with nothing missed (unfinished work must have a card; completed work is moved to `archives\done\`, never deleted) |
| **Human-read zone + AI zone** | Human-read zone (3-line summary, auto-generated from the AI zone) + AI work coordinates — one glance tells a human where the task stands |
| **Meta-management routing** | The skill's own affairs (retrospective / version / recovery registration) go to the workspace `REVIEWS.md` and never pollute project reports/INDEX |
| **Legacy project onboarding** | For projects already under way: "lightweight registration + progressive tidying", no deep historical reorganization (LEGACY_ONBOARDING.md) |
| **Platform-agnostic** | Pure files + pure protocol, no dependency on any platform's private API, skill system or SDK |

## 2. Requirements

**A local filesystem plus command/file execution ability** (able to create the management directory on disk and read/write task cards and handoff files).

Platforms are judged by capability dimension, not enumerated by name — any platform with the above abilities (harness-style / IDE agent / desktop workspace agent, etc.) is automatically compatible. Scenarios without local file ability (web chat / mobile app / pure conversation / raw API calls) do not qualify.

## 3. Directory structure

```
skill-en/                             # English skill package (copy into your skills directory to use)
├── SKILL.md                # Skill entry (positioning/triggers/workflow/initialization checklist/self-check)
├── README.md               # Template guide (read by the AI at runtime)
├── BLUEPRINT.md            # Design blueprint pointer
├── MAP.template.md         # Project map skeleton (→ instantiate as MAP.md)
├── STATE.template.md       # Current-state snapshot skeleton (→ instantiate as STATE.md)
├── INDEX.template.md       # Record-index skeleton (→ instantiate as INDEX.md)
├── LEGACY_ONBOARDING.md    # Legacy project onboarding guide (companion file)
├── REVIEWS.template.md     # Skill retrospective (meta-management loop: blocker/suggestion/disposition)
├── tasks\TASK_CARD.template.md   # Task card skeleton
├── reports\HANDOVER.template.md  # Minimal handoff template
├── archives\README.md     # Archive notes (in only, never out)
└── tools\                 # Optional tools area (checks/visualize/schedule/report/custom)
```

Workflow: copy `skill-en/` into your skills directory → for a new project read `SKILL.md` to initialize; for a legacy project read `LEGACY_ONBOARDING.md` to onboard.

## 4. Installation

| Environment | How |
|---|---|
| **Doubao** | copy `skill-en/` into your skills directory (e.g. `.user_skills\`) |
| **Claude Code and other environments that support SKILL.md** | copy `skill-en/` into your skills directory |
| **Plain-document use** | read `skill-en/SKILL.md` directly and follow the protocol (works with any LLM) |

> Skill name: the English package declares `name: AI-Relay-project-management-lite` in its frontmatter. If your platform requires the installed folder name to match the skill name, rename the copied folder accordingly. Note that some platforms (Claude Code and similar) only accept lowercase letters, numbers and hyphens in a skill name — if yours rejects mixed case, use `ai-relay-project-management-lite` instead.

## 5. Quick start

1. **New project**: read `SKILL.md` → confirm the workspace root `{WORKSPACE_ROOT}` (once) → the management directory is created automatically → fill in the `MAP.md` placeholders → create the first task card under `tasks\` → start working from the task card
2. **Legacy project** (already under way, no management structure): read `LEGACY_ONBOARDING.md` → create the management directory + lightweight registration of the current state → progressively tidy the history

Core loop (runtime): **read task card → do the work → end-of-work four-piece set (handoff → card update/move → INDEX → STATE)**

## 6. Design blueprint

The full design blueprint is in [`project-management-lite-blueprint.html`](project-management-lite-blueprint.html) (design decisions, reading model, acceptance checklist). The Chinese blueprint is in `项目管理轻量化工作分配蓝图.html`.

## 7. License

MIT License (see [LICENSE](LICENSE)).

## Credits

- Author: 如天之星
- Origin: the project was inspired by the article 《为什么越改越偏？》("Why Does It Drift Further With Every Revision?")
