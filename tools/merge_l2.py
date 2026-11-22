# -*- coding: utf-8 -*-
"""合并层：data/entries.json(L1种子) + data/l2/*.json(L2/L3覆盖) -> data/site_entries.json
并据合并结果刷新 data/coverage.json 的 level/status/来源计数。
幂等，可重复运行。
"""
import json, os, glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
S=json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))["sources"]
S_BY_ID={s["id"]:s for s in S}
verified={s["id"] for s in S if s["verified"]}

seed=json.load(open(os.path.join(D,"entries.json"),encoding="utf-8"))["entries"]
merged={e["id"]:dict(e) for e in seed}
# 来源修复层：替换重复来源id（须在L2覆盖之前应用）
fixes_p=os.path.join(D,"source_fixes.json")
if os.path.exists(fixes_p):
    for eid,srcs in json.load(open(fixes_p,encoding="utf-8")).items():
        if eid in merged: merged[eid]["sources"]=list(srcs)
l2dir=os.path.join(D,"l2"); os.makedirs(l2dir,exist_ok=True)
for p in sorted(glob.glob(os.path.join(l2dir,"*.json"))):
    ov=json.load(open(p,encoding="utf-8"))
    eid=ov["id"]
    if eid not in merged: continue
    base=list(merged[eid].get("sources",[]))
    merged[eid].update(ov)
    # 来源并集：覆盖层只增不删
    merged[eid]["sources"]=list(dict.fromkeys(base+list(ov.get("sources",[]))))

entries=list(merged.values())
# 全局去重：来源id不得重复（保持顺序）
for e in entries:
    if "sources" in e:
        e["sources"]=list(dict.fromkeys(e["sources"]))
json.dump({"entries":entries},open(os.path.join(D,"site_entries.json"),"w",encoding="utf-8"),
          ensure_ascii=False,indent=2)

cov=json.load(open(os.path.join(D,"coverage.json"),encoding="utf-8"))
for e in entries:
    c=cov["entries"].get(e["id"])
    if not c: continue
    lv=e.get("level","L1")
    c["level"]=lv
    c["status"]={"L1":"seeded","L2":"written_l2","L3":"written_l3"}.get(lv,"seeded")
    c["sources_count"]=len(e.get("sources",[]))
    nver=sum(1 for s in set(e.get("sources",[])) if s in verified)
    c["verified_sources_count"]=nver
    # WORKFLOW双源规则：≥2个不同verified来源id即通过
    c["needs_verification"]=nver<2
    c["pending_notes"]=("关键事实需≥2个verified来源，当前%d个"%nver) if nver<2 else ""
    # TASK独立性关注：单独记录，不混入 needs_verification（避免比例失真）
    srcs=[s for s in e.get("sources",[]) if s in verified]
    authors={S_BY_ID[s]["author"] for s in srcs if s in S_BY_ID}
    from urllib.parse import urlparse
    hosts={urlparse(S_BY_ID[s]["url"]).netloc for s in srcs if s in S_BY_ID}
    c["source_independence_ok"]=(nver>=2 and len(authors)>=2 and len(hosts)>=2)
    c["last_update"]="2026-11-22"
json.dump(cov,open(os.path.join(D,"coverage.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)

from collections import Counter
cnt=Counter(e.get("level","L1") for e in entries)
print("merged entries=%d levels=%s"%(len(entries),dict(cnt)))
