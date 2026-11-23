# -*- coding: utf-8 -*-
"""Cycle50 巡检：覆盖层是否携带"基础字段"并覆盖了 catalog 的真值。
基础字段 = id/title/kind/unit/era/region/medium/tier/def/when/overview
（related 与 sources 已在 D021/D052 改为并集，故不在本次风险清单内，但仍列出是否出现）。
输出每一处 值 不一致（catalog 值 vs overlay 值）。"""
import json,os,glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
base={e["id"]:e for e in json.load(open(os.path.join(D,"entries.json"),encoding="utf-8"))["entries"]}
RISK=["title","kind","unit","era","region","medium","tier","def","when","overview","related","sources"]
carriers={k:[] for k in RISK}
mismatch=[]
for p in sorted(glob.glob(os.path.join(D,"l2","*.json"))):
    o=json.load(open(p,encoding="utf-8")); eid=o.get("id")
    b=base.get(eid)
    if not b: mismatch.append({"id":eid,"field":"__no_base__","catalog":None,"overlay":"overlay 存在但 catalog 无此条目"}); continue
    for k in RISK:
        if k in o:
            carriers[k].append(eid)
            if k in ("related","sources"): continue  # 已改为并集
            if o[k]!=b.get(k):
                mismatch.append({"id":eid,"field":k,"catalog":b.get(k),"overlay":o[k]})
print("覆盖层中出现的基础字段（条目数）：")
for k in RISK:
    if carriers[k]: print("  %-9s %d"%(k,len(carriers[k])))
print()
print("值不一致（会被 update 覆盖）：",len(mismatch))
for m in mismatch[:20]: print("  ",m["id"],"|",m["field"],"| catalog:",str(m["catalog"])[:40],"| overlay:",str(m["overlay"])[:40])
json.dump({"carriers":{k:v for k,v in carriers.items() if v},"mismatch":mismatch},
          open(os.path.join(ROOT,"reports","overlay_field_audit_c50.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)