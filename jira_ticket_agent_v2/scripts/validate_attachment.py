#!/usr/bin/env python3
import sys
from pathlib import Path

def main():
    p=Path(sys.argv[1])
    if not p.exists() or p.stat().st_size==0:
        print("FAIL: archivo inexistente o vacio"); return 2
    ext=p.suffix.lower()
    if ext in {'.png','.jpg','.jpeg','.webp'}:
        try:
            from PIL import Image
            with Image.open(p) as im:
                im.verify()
            with Image.open(p) as im:
                print(f"PASS: imagen {im.format} {im.size[0]}x{im.size[1]}")
            return 0
        except Exception as e:
            print(f"FAIL: imagen invalida: {e}"); return 2
    print(f"PASS_METADATA: archivo {p.name} size={p.stat().st_size}")
    return 0
if __name__=='__main__': raise SystemExit(main())
