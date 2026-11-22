# -*- coding: utf-8 -*-
"""阶段0静态自检：来源id存在且verified、related指向存在、id规范、必填非空、无重复。"""
import json, os, sys, re
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catalog import entries, UNITS
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
S=json.load(open(os.path.join(ROOT,"data","sources.json"),encoding="utf-8"))["sources"]
sm={s["id"]:s for s in S}
es=entries(); ids={e["id"] for e in es}
errs=[]
for e in es:
    if not re.fullmatch(r"[a-z0-9-]+", e["id"]): errs.append(("ID_FORMAT",e["id"],""))
    if e["unit"] not in UNITS: errs.append(("UNIT",e["id"],e["unit"]))
    for f in ("title","kind","def","when","overview","tier","era","region","medium"):
        if not e.get(f): errs.append(("EMPTY",e["id"],f))
    for s in e["sources"]:
        if s not in sm: errs.append(("SRC_MISSING",e["id"],s))
        elif not sm[s]["verified"]: errs.append(("SRC_UNVERIFIED",e["id"],s))
    for r in e["related"]:
        if r not in ids: errs.append(("REL_MISSING",e["id"],r))
# 重复id
seen=set()
for e in es:
    if e["id"] in seen: errs.append(("DUP_ID",e["id"],""))
    seen.add(e["id"])
# 重复标题
seen=set()
for e in es:
    if e["title"] in seen: errs.append(("DUP_TITLE",e["title"],""))
    seen.add(e["title"])
print("errors:",len(errs))
for x in errs: print(" ",x)
