#!/usr/bin/env python3
from pathlib import Path


def main() -> int:
    root = Path(__file__).resolve().parents[1]
    required = [
        root / ".github/agents/functional-test-engineer.agent.md",
        root / ".github/copilot-instructions.md",
        root / "reference-standards/testing-standard.md",
        root / "reference-standards/flask-functional-testing-reference.md",
        root / "reference-standards/coverage-standard.md",
        root / "demo_shop/app.py",
        root / "demo_shop/domain.py",
        root / "tests/test_domain.py",
        root / "tests/test_flask_functional.py",
    ]
    missing = [str(p.relative_to(root)) for p in required if not p.exists()]
    skills = list((root / ".github/skills").glob("*/SKILL.md"))
    if missing:
        print("FAIL: missing required files")
        for item in missing:
            print(" -", item)
        return 2
    if len(skills) != 4:
        print(f"FAIL: expected 4 skills, found {len(skills)}")
        return 2
    print("PASS: workspace structure valid")
    print(f"PASS: {len(skills)} skills detected")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
