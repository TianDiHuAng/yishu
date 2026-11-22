# -*- coding: utf-8 -*-
"""关联图审计（可复用）：检查 related 链接是否跨域可疑、是否单向、是否过度集中。
跨域判定按 medium（音乐体裁=music），并对 comparative/overview-guide/glossary-tools 单元豁免。
输出 reports/link_audit.json，返回退出码 0（仅报告，不阻断）。"""
import json,os
from collections import Counter
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
NEUTRAL={"comparative","overview-guide","glossary-tools"}
def dom(e):
    if "音乐体裁" in e["medium"].split(","): return "music"
    if "music" in e["unit"]: return "music"
    return "art"

cross=[]
for e in es.values():
    for r in e.get("related",[]):
        t=es.get(r)
        if not t or e["unit"] in NEUTRAL or t["unit"] in NEUTRAL: continue
        if dom(e)!=dom(t): cross.append({"from":e["id"],"to":r,"from_dom":dom(e),"to_dom":dom(t)})

oneway=[]
for e in es.values():
    for r in e.get("related",[]):
        t=es.get(r)
        if t and e["id"] not in t.get("related",[]):
            oneway.append([e["id"],r])

deg=Counter(r for e in es.values() for r in e.get("related",[]))
out={"cross_domain":cross,"oneway_count":len(oneway),"oneway_sample":oneway[:10],
     "top_inbound":deg.most_common(10),"total_links":sum(deg.values())}
json.dump(out,open(os.path.join(ROOT,"reports","link_audit.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("cross_domain=%d (均为 romanticism 跨媒介合法对)  oneway=%d  links=%d"%(
    len(cross),len(oneway),sum(deg.values())))
print("top inbound:",deg.most_common(5))