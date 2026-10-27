#!/usr/bin/env python3
"""Rebaixa os originais das fotografias de acervo a partir de assets/credits.json.

Os originais (14 MB) ficam fora do git: são insumo, não entregável. Este script
os traz de volta para que `tools/build-assets.py` possa rodar.
"""
import json, os, sys, urllib.request

CREDITS = "assets/credits.json"

def main():
    if not os.path.exists(CREDITS):
        sys.exit(f"falta {CREDITS}")
    items = json.load(open(CREDITS))
    if isinstance(items, dict):
        items = items.get("items", list(items.values()))
    for it in items:
        dest, url = it["file"], it["image"]
        if os.path.exists(dest):
            print(f"  já existe  {dest}")
            continue
        os.makedirs(os.path.dirname(dest), exist_ok=True)
        req = urllib.request.Request(url, headers={"User-Agent": "connect-air-build/1.0"})
        with urllib.request.urlopen(req) as r, open(dest, "wb") as f:
            f.write(r.read())
        print(f"  baixado   {dest}  ({os.path.getsize(dest)//1024} KB)")

if __name__ == "__main__":
    main()
