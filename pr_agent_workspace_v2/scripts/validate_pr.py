#!/usr/bin/env python3
import argparse, json, re, sys
from pathlib import Path

TITLE_RE = re.compile(r"^\[[A-Z0-9]+-[0-9]+\] - PR DEVELOP$")
BODY_RE = re.compile(r"^feat\([A-Z0-9]+-[0-9]+\): .+")
PASS_CONCLUSIONS = {"success", "passed"}


def first_nonempty(text):
    for line in (text or "").splitlines():
        if line.strip():
            return line.strip()
    return ""


def validate(data):
    checks = []
    def add(name, result, reason): checks.append({"check": name, "result": result, "reason": reason})

    title = data.get("title", "")
    body = first_nonempty(data.get("body", ""))
    add("Title", "PASS" if TITLE_RE.fullmatch(title) else "FAIL", title or "missing")
    add("Description", "PASS" if BODY_RE.match(body) else "FAIL", body or "missing")
    add("State", "PASS" if str(data.get("state", "")).upper() == "OPEN" else "FAIL", str(data.get("state", "missing")))
    add("Base branch", "PASS" if data.get("base_ref") == "develop" else "FAIL", str(data.get("base_ref", "missing")))
    add("Draft", "PASS" if data.get("draft") is False else "FAIL", str(data.get("draft", "missing")))

    mergeable = data.get("mergeable")
    add("Mergeable", "PASS" if mergeable is True else ("FAIL" if mergeable is False else "UNKNOWN"), str(mergeable))

    status_checks = data.get("status_checks")
    if status_checks is None:
        add("Required checks", "UNKNOWN", "not provided")
    else:
        failed = [c.get("name", "unnamed") for c in status_checks if c.get("required", True) and str(c.get("conclusion", "")).lower() not in PASS_CONCLUSIONS]
        add("Required checks", "FAIL" if failed else "PASS", ", ".join(failed) if failed else "all required checks passed")

    required = data.get("required_approvals")
    approvals = data.get("approvals")
    if required is None or approvals is None:
        add("Approvals", "UNKNOWN", "approval requirement/count not provided")
    else:
        add("Approvals", "PASS" if approvals >= required else "FAIL", f"{approvals}/{required}")

    threads = data.get("unresolved_review_threads")
    if threads is None:
        add("Review threads", "UNKNOWN", "not provided")
    else:
        add("Review threads", "PASS" if threads == 0 else "FAIL", f"{threads} unresolved")

    sec = data.get("security_blockers")
    if sec is None:
        add("Security / Dependabot", "UNKNOWN", "not provided")
    else:
        add("Security / Dependabot", "PASS" if sec == 0 else "FAIL", f"{sec} blocker(s)")

    results = [c["result"] for c in checks]
    if "FAIL" in results:
        decision = "NOT READY TO MERGE"
    elif "UNKNOWN" in results:
        decision = "READY WITH CONDITIONS"
    else:
        decision = "READY TO MERGE"
    return checks, decision


def main():
    p = argparse.ArgumentParser()
    p.add_argument("input")
    args = p.parse_args()
    data = json.loads(Path(args.input).read_text(encoding="utf-8"))
    checks, decision = validate(data)
    print("PR VALIDATION RESULT")
    for c in checks:
        print(f"{c['check']:<24} {c['result']:<8} {c['reason']}")
    print(f"\nMerge recommendation: {decision}")
    return 0 if decision == "READY TO MERGE" else (3 if decision == "READY WITH CONDITIONS" else 2)

if __name__ == "__main__":
    sys.exit(main())
