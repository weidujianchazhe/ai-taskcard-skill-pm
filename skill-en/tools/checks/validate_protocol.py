"""Read-only structural validation for the v1.2.1 skill package."""

from pathlib import Path
import re
import sys


ROOT = Path(__file__).resolve().parents[2]
REQUIRED = {
    "SKILL.md": ("version: 1.2.1", "TASK-ID", "EVENT-ID", "DESIGN-ID",
                 "coordination", "RAW-SHA256", "NORMALIZED-SHA256",
                 "compare-and-swap", "blocks completion"),
    "README.md": ("Version v1.2.1", "archives\\INDEX_archived.md"),
    "MAP.template.md": ("Version v1.2.1", "STATE character limit",
                        "single logical writer", "coordination"),
    "INDEX.template.md": ("Version v1.2.1", "immutable", "EVENT-ID"),
    "STATE.template.md": ("Version v1.2.1", "revision", "NORMALIZED-SHA256"),
    "tasks/TASK_CARD.template.md": ("TASK-ID", "DESIGN-ID", "EVENT-ID"),
    "reports/HANDOVER.template.md": ("EVENT-ID", "TASK-ID", "concurrency metadata"),
    "archives/README.md": ("archive algorithm", "CONFLICT_", "CAS"),
    "designs/DESIGN_CARD.template.md": ("DESIGN-ID", "approved", "TASK-ID"),
}


def main() -> int:
    errors = []
    for relative, terms in REQUIRED.items():
        path = ROOT / relative
        if not path.is_file():
            errors.append(f"missing file: {relative}")
            continue
        text = path.read_text(encoding="utf-8")
        for term in terms:
            if term.lower() not in text.lower():
                errors.append(f"{relative}: missing {term}")

    versions = []
    for path in (ROOT / "SKILL.md", ROOT / "README.md", ROOT / "MAP.template.md",
                 ROOT / "INDEX.template.md", ROOT / "STATE.template.md",
                 ROOT / "reports" / "HANDOVER.template.md"):
        if path.is_file():
            versions.extend(re.findall(r"v1\.\d+\.\d+", path.read_text(encoding="utf-8")))
    if versions and set(versions) != {"v1.2.1"}:
        errors.append(f"version drift: {sorted(set(versions))}")

    if errors:
        print("\n".join(f"[FAIL] {error}" for error in errors))
        return 1
    print("[PASS] v1.2.1 protocol structure, IDs, modes, archive and concurrency metadata")
    return 0


if __name__ == "__main__":
    sys.exit(main())
