# [TASK_NAME] task card

> File name: named after the work under tasks\ (a short Chinese or English name is fine — by default follow the user's communication language: Chinese if mostly Chinese, English if mostly English; follow the user's instruction if given).

━━━ Human-read locator ━━━
Project: [PROJECT_NAME] · Module: [MODULE]
Task: [ONE_LINE_TASK_LOCATOR]
Status: [In progress / Unclaimed / Blocked] · Next step: [NEXT_STEP]
━━━━━━━━━━━━━━━━

- **ID**: [XXNNNN, e.g. EX0001 — two-letter branch + four-digit sequence]
- **Status**: [In progress / Unclaimed / Blocked]
- **Description**: [what is to be done now, the latest description for this round]
- **Key points**: [1-3 complete actionable steps for the current task (what to do + in which file), overwrite-style, keeping the latest]
  - ① [key point 1]
  - ② [key point 2]
- **Code root path**: [absolute project path (the code source root), e.g. F:\code\project; a cold-start AI locates the code from this without reading MAP first]
- **Files involved**: [list of file paths involved, comma-separated; relative to "Code root path", or absolute paths directly]
- **Claimed by**: [AI tag, e.g. {PLATFORM}-{AI_NAME}-{SHORT_CODE} (short code 2-4 random characters, so multiple instances on the same platform do not collide); "—" if unclaimed]
- **Progress anchor**: [resume-from-breakpoint anchor — how far it got / which files changed / how far verification went, one line; "—" if not started]
- **Last handoff**: [path(s) under reports\, one or more (trunk/branches), comma-separated — the takeover-chain entry; "—" if none]
- **Distilled**: [names of the reports files whose increments have been distilled back into the key points (distill back to card); "—" if no reports were read this round]

---

> Update: unfinished → a card is mandatory (including work with no card yet that exists only in the current conversation); the human-read zone is auto-generated from the AI zone — task line ← first sentence of the description, status line ← the status field, next step ← key point ① ("—" if there is no key point), rewritten in sync on an overwrite update; completed → write a summary and move the card to archives\done\ (never delete the card; keep the completion record).
> **How to write the progress anchor (resume from breakpoint)**: while working, **overwrite at each landing point** — every time a sub-step is finished or a verification passes, rewrite this line (single-line overwrite, only for a card you claimed, so there is no concurrency conflict); if a network/power/token outage cuts the work short before end-of-work, the card naturally keeps the latest landing point and the next AI resumes along the anchor + the actual file state (`git status`); at a normal end-of-work the anchor content has been absorbed into key points/handoff → clear it to "—", and **the handoff format does not change at all**; for a card archived directly because the task was cancelled, the anchor stays as it is (a traceable interruption record).
> **Field quality bar**: key points = actionable steps (what + where; no empty phrases like "keep optimizing"); files involved = concrete file paths (no "related files"); code root path = an absolute path (cold start locates from it without reading MAP first); last handoff = "—" only when there is no handoff; distilled = reports that were read must have their increments distilled back into the key points, otherwise the next AI has to re-read the same file.
> **End-of-work protocol memo** (full protocol in the workspace SKILL.md core protocol / MAP protocol section): end-of-work four-piece set = ① handoff reports (named `YYYY-MM-DD_topic_your-AI-tag.md`, list the directory first to avoid duplicate names) → ② update this card (or move it to archives\done\ when completed) → ③ add one INDEX row → ④ STATE entry-level write; **new files / new paths / new branches must be registered in MAP** (register a new branch letter before using it); files under reports\ and archives\ must not be deleted or moved; the skill's own affairs go to REVIEWS.md, never into reports/INDEX.
