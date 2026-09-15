#!/usr/bin/env python3
from __future__ import annotations
import re
import subprocess
import sys
from pathlib import Path


def scan_trivial_asserts() -> list[str]:
    findings = []
    pattern = re.compile(r"\bassert\s+(True|1\s*==\s*1)\b")
    for path in Path("tests").glob("test_*.py"):
        text = path.read_text(encoding="utf-8")
        for lineno, line in enumerate(text.splitlines(), 1):
            if pattern.search(line):
                findings.append(f"{path}:{lineno}: {line.strip()}")
    return findings


def main() -> int:
    findings = scan_trivial_asserts()
    if findings:
        print("FAIL: trivial assertions detected")
        for item in findings:
            print(" -", item)
        return 2

    cmd = [
        sys.executable,
        "-m",
        "pytest",
        "--cov=demo_shop",
        "--cov-branch",
        "--cov-report=term-missing",
        "--cov-report=xml:coverage.xml",
        "--cov-fail-under=80",
    ]
    print("Running:", " ".join(cmd))
    result = subprocess.call(cmd)
    if result != 0:
        print("RESULT: FAIL")
        return result
    print("RESULT: PASS - tests green and coverage >= 80%")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
