#!/usr/bin/env python3
from pathlib import Path
import subprocess
import sys
import re


def main() -> int:
    root = Path(__file__).resolve().parent.parent
    failures = []

    required = [
        root / ".github" / "copilot-instructions.md",
        root / ".github" / "agents" / "frontend-ui.agent.md",
        root / "reference-standards" / "styles-standard.css",
        root / "examples" / "basic-guide.html",
    ]
    for path in required:
        if not path.exists():
            failures.append(f"Falta archivo obligatorio: {path.relative_to(root)}")

    skill_root = root / ".github" / "skills"
    skills = sorted(skill_root.glob("*/SKILL.md"))
    if not skills:
        failures.append("No se encontraron skills en .github/skills")
    for skill in skills:
        text = skill.read_text(encoding="utf-8")
        if not text.startswith("---\n"):
            failures.append(f"Skill sin frontmatter: {skill.relative_to(root)}")
        if not re.search(r"^name:\s+[a-z0-9-]+\s*$", text, flags=re.M):
            failures.append(f"Skill con name inválido: {skill.relative_to(root)}")
        if not re.search(r"^description:\s+.+$", text, flags=re.M):
            failures.append(f"Skill sin description: {skill.relative_to(root)}")

    validator = root / "scripts" / "style_validator.py"
    html_files = list((root / "reference-standards").glob("*.html")) + list((root / "examples").glob("*.html"))
    for html in html_files:
        result = subprocess.run([sys.executable, str(validator), "--file", str(html)], capture_output=True, text=True)
        if result.returncode != 0:
            failures.append(f"Validación falló para {html.relative_to(root)}:\n{result.stdout.strip()}")

    if failures:
        for failure in failures:
            print(f"FAIL: {failure}")
        print(f"RESULT: FAIL ({len(failures)} problemas)")
        return 1

    print(f"PASS: {len(skills)} skills detectadas")
    print(f"PASS: {len(html_files)} HTML validados")
    print("RESULT: PASS")
    return 0


if __name__ == "__main__":
    sys.exit(main())
