# Legacy Project Onboarding Guide (Attached Skill File · For Projects Already Underway)

> **What this file is**: a standalone attached onboarding file, serving legacy projects that "have already been worked on for a while but have not yet established a project management structure".
> **Its relation to the main skill**: it stands alone; it is not written into the main skill protocol (SKILL.md / README / blueprint / templates) and is not part of the main skill's required-reading flow.
> **Who reads it**: the AI or the project manager of a project already underway — read this file separately, understand the way the project is managed, create the management structure, lightweight-register the current information, then manage normally under the main skill.

---

## 1. Applicable scenarios

The project already has real work output (code / documents / multiple rounds of conversation history), but has the following gaps:

| Gap | Symptom |
|---|---|
| No skill master table | There is no SKILL.md, so the AI does not know the management protocol |
| No directory master table | There is no MAP.md, so the AI cannot find its way |
| No work task flow | There is no tasks\, so the AI does not know what to do or who is doing it |
| No work records | There is no reports\ / INDEX.md, so history cannot be traced |

At this point the AI reads this file, executes the "onboarding flow", and brings the project into the project management system.

---

## 2. Creation is the universal first step; legacy projects only add "lightweight registration"

| Stage | Normal project (uses this skill from day one) | Legacy project (adopts this skill midway) |
|---|---|---|
| Read the skill | Read once at initialization | Read once at onboarding |
| Create management directories | **Also required** (startup information is right at hand) | **Also required** (creation dominates) |
| History tidying | Not needed (no history) | **Lightweight registration**: register only the key information visible in the current session, **no deep tidying analysis** |

> **Key points**:
> 1. **Creation is the universal first step**: any project adopting this skill first creates the management directories (MAP / STATE / tasks\ / reports\ / INDEX); only after that does management of the whole project begin — there is no "read-directly" starting point.
> 2. **Legacy projects do not do deep tidying**: thinking deeply to analyze history is a massive undertaking (the deeper the project, the more terrifying) — so onboarding **only does lightweight registration** (information directly visible in the current session), with no deep digging into history.
> 3. **History relies on progressive tidying**: do not tidy all at once; classify as you go during subsequent work (see "Progressive tidying mechanism"); backfill historical gaps by tracing them back as needed.
> 4. **The skill is not read repeatedly**: once creation is complete, the AI runs only from the created work files (task cards / MAP / reports) and does not need to read the skill itself again.

---

## 3. Execution flow (dedup check first + five steps: light registration → build structure → backfill → first record → run)

### Step 0: dedup check first — does a management instance for this project already exist (v1.2.0 prerequisite, mandatory)

Before onboarding begins, first probe under `{WORKSPACE_ROOT}` (and the visible scope of the skill source package) for **whether a management directory / workspace for this project already exists**:
- Already exists → **first merge or confirm the single authoritative copy** (continue managing from that copy; backfill historical gaps progressively under the existing protocol); **starting another new management directory is forbidden** — two management directories for the same project cause state splitting (higher read cost and error rate);
- Does not exist → continue with normal onboarding.

> Trigger point: whether it is new-project initialization or legacy onboarding, do this step first, before copying templates / creating directories.

### Step 1: lightweight registration of the current information (no deep tidying)

Register only the key information **directly visible in the current session**, forming an "initial information list":

- **What the project is**: one-line positioning + tech stack + code path + boundaries not involved
- **Work currently in progress**: what is being done / unfinished (this is the raw material for task cards)
- **Decision points pending confirmation**: questions left unresolved in the session, items waiting for the user's call
- **Known limitations / issues**: bugs, environment limits, leftover risks
- **Key milestones** (optional): major changes that can be evidenced, one line is enough

> **No deep tidying**: do not dig into historical details or do full-scale analysis — deep thinking is a massive undertaking; leave it to the "progressive tidying mechanism" to backfill as needed. Mark the parts of the history that cannot be reconstructed as "to be tidied as needed"; do not force one-shot completion.

### Step 2: create the project management directory structure

Create it in the workspace per the main skill standard — **the file composition is exactly the same as "workspace file list" in section 3 of README** (new-project initialization and legacy onboarding share one and the same list, producing no second workspace composition): instantiate the four templates MAP / STATE / INDEX / REVIEWS, copy SKILL.md and the entry files of tasks\ / reports\ / archives\ / tools\ as is, and create the empty directories tasks\, reports\, archives\done\.

### Step 3: backfill the initial state (lightweight, only currently visible information)

| File | Backfilled content |
|---|---|
| `SKILL.md` | Copy the skill source package protocol entry (skill entry / triggers / flow / initialization checklist) — the MAP reference "for the collaboration protocol see SKILL.md" points to this file |
| `MAP.md` | Environment / rules / protocol / path registry (four fixed blocks; the environment block contains the [SKILL_SOURCE_PATH], [BACKUP_METHOD] and [DECISION_MAKER] placeholders; the rules block confirms three settings: INDEX row count / reports archive threshold / AI periodic-check switch) |
| `STATE.md` | Write the current-state summary of the "initial information list" (human-read zone + AI zone) |
| `REVIEWS.md` | Copy REVIEWS.template.md and instantiate it (the landing point for meta-management records — skill retrospectives / recovery registrations go here, not into reports/INDEX) |
| `INDEX.md` | Create only a few key `[done]` rows (milestones that can be evidenced); do not create the rest of the history — leave it for progressive tidying |
| `tasks\` | Create task cards for **work currently in progress** (Description + Key points + Files involved + Claimed by); write unresolved decision points into the task card's Key points |
| `tools\README.md` | Copy the skill source package tools-area entry (overview + three iron rules + built-in tool table); pull the sub-specs (checks/visualize/schedule/report) from the skill source package only when they are used |

### Step 4: create the first record (onboarding anchor)

Write one **onboarding record** in `reports\`:

```
# Onboarding record YYYY-MM-DD
- Event: this project was brought under project management via the "Legacy Project Onboarding Guide"
- Source: the historical information comes from session summaries (as of YYYY-MM-DD), not item-by-item work records
- Known gaps: the parts of the history that cannot be fully reconstructed (e.g. [xxx]), marked as to be filled in
- From here on: run under the main skill protocol (task-card-driven / end-of-work routing / overwrite-style update)
```

At the same time, mark the type `[handoff]` on the corresponding `INDEX.md` row of that record (as the starting point of the new management cycle).

### Step 5: enter normal operation (creation complete, the skill is no longer read)

- At this point the management files are **fully created** and the project enters normal operation: read task card → do the work → end-of-work routing, overwrite-style update, distill back to card
- **Do not read the skill again** (SKILL.md / this file): the AI runs only from the created work files (task card / MAP / reports)
- Mark historical gaps as "to be filled in" in STATE; when needed, confirm with the user to fill them in
- This file has completed its mission (unless a new project needs onboarding again)

---

## 4. Progressive tidying mechanism (classify while working · backfill history as needed)

**No one-shot deep tidying**; bring the project to standard gradually through the following:

1. **New work is standardized as it happens**: from the onboarding date, every end-of-work classifies automatically — write handoff / summary (reports\) → update INDEX ([handoff]/[done]/[dropped]) → overwrite-update STATE → update task card. Newly generated information is standardized from day one.
2. **Backfill history as needed**: when a stretch of history needs to be traced / reviewed, tidy it then and backfill it into INDEX / STATE — backfill one stretch at a time, never all at once, avoiding the huge cost of deep thinking.
3. **Key lessons settle gradually**: historical decisions, constraints and lessons found during work are backfilled into task card Key points or STATE as you go, accumulating over time.
4. **Archiving happens naturally**: when the number of reports reaches the "reports archive threshold" in the MAP rules block (default 20), roll-archive per the existing rules, and the old history is brought into standard management along with it.

> **Effect**: the onboarding cost is low (not terrifying because of deep tidying), and every day afterward is progressive tidying — the more the project runs, the more standardized it becomes, and the tidying cost is spread across daily work.

---

## 5. Boundaries and cautions

1. **Do not fabricate history**: register only information that can be evidenced in the session; mark anything unevidenced as "to be tidied as needed"
2. **Do not mix it into the main skill**: this file is distributed independently and does not modify SKILL.md / README / blueprint / templates; the main skill's required-reading flow is unchanged
3. **One-time onboarding**: once onboarding is complete, run under the main skill; this file is used only for "a legacy project's first onboarding"
4. **Catch the decision points**: questions awaiting user confirmation in the current session must be folded into STATE decision points or task card Key points at onboarding time — onboarding catches them, with nothing missed
5. **Confidence labeling**: history registered from a session is labeled "from session summaries (not verified item by item)"; formal work records are labeled "formal record" — the two can be distinguished in INDEX
6. **Do not force one-shot tidying**: it is allowed for historical gaps to persist for a long time (marked "to be tidied as needed"); backfill only when that stretch of history is needed; complete tidying is not a prerequisite for onboarding
