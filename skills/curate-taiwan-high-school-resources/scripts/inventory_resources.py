#!/usr/bin/env python3
import argparse, csv, hashlib
from pathlib import Path

def sha256(path):
    h=hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda:f.read(1024*1024),b""): h.update(block)
    return h.hexdigest()

ap=argparse.ArgumentParser(); ap.add_argument("root"); ap.add_argument("--output",default="manifest.csv"); ns=ap.parse_args()
root=Path(ns.root).resolve(); out=Path(ns.output)
rows=[]
for p in sorted(x for x in root.rglob("*") if x.is_file() and x.resolve()!=out.resolve()):
    rows.append({"path":p.relative_to(root).as_posix(),"filename":p.name,"bytes":p.stat().st_size,"sha256":sha256(p),"subject":"","topic":"","grade":"","language":"","source_url":"","access_basis":"","license":"","redistribution":"needs-review","decision":"needs-review"})
with out.open("w",newline="",encoding="utf-8-sig") as f:
    w=csv.DictWriter(f,fieldnames=rows[0].keys() if rows else ["path","filename","bytes","sha256","subject","topic","grade","language","source_url","access_basis","license","redistribution","decision"]); w.writeheader(); w.writerows(rows)
print(f"Wrote {len(rows)} records to {out}")
