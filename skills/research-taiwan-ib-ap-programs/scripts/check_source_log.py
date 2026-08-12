#!/usr/bin/env python3
import argparse, csv, sys
ap=argparse.ArgumentParser(); ap.add_argument("csv_file"); ns=ap.parse_args()
bad=[]
with open(ns.csv_file,encoding="utf-8-sig",newline="") as f:
    for i,row in enumerate(csv.DictReader(f),2):
        missing=[k for k in ("source_url","check_date") if not row.get(k,"").strip()]
        if missing: bad.append((i,missing))
for row,fields in bad: print(f"row {row}: missing {', '.join(fields)}")
sys.exit(1 if bad else 0)
