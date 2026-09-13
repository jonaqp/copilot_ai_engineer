#!/usr/bin/env python3
from __future__ import annotations
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


def main() -> int:
    path = Path(sys.argv[1] if len(sys.argv) > 1 else "coverage.xml")
    if not path.exists():
        print(f"FAIL: coverage report not found: {path}")
        return 2

    root = ET.parse(path).getroot()
    rows = []
    for cls in root.findall(".//class"):
        filename = cls.attrib.get("filename", "unknown")
        rate = float(cls.attrib.get("line-rate", "0")) * 100
        missing = []
        for line in cls.findall("./lines/line"):
            if int(line.attrib.get("hits", "0")) == 0:
                missing.append(line.attrib.get("number", "?"))
        rows.append((rate, filename, missing))

    print("Coverage gap report")
    print("=" * 72)
    for rate, filename, missing in sorted(rows):
        status = "PRIORITY" if rate < 70 else "REVIEW" if rate < 80 else "OK"
        preview = ",".join(missing[:15]) if missing else "-"
        if len(missing) > 15:
            preview += ",..."
        print(f"{status:8} {rate:6.2f}%  {filename:28} missing: {preview}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
