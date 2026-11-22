# -*- coding: utf-8 -*-
"""Cycle12：单向关联审校。对每条 A→B 且 B 未指向 A 的链接，按"是否同单元/同域"分类：
same_unit（补反向最安全）、same_domain（可补）、cross_domain（不补，除非跨媒介专题）。
输出 reports/oneway_audit.json 与统计。仅生成报告，**不自动改动数据**。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
NEUTRAL={"comparative","overview-guide","glossary-tools"}
def dom(e):
    if "音乐体裁" in e["medium"].split(","): return "music"
    if "music" in e["unit"]: return "music"
    return "art"
rows=[]
for e in es.values():
    for r in e.get("related",[]):
        t=es.get(r)
        if not t: continue
        if e["id"] in t.get("related",[]): continue
        if e["unit"]==t["unit"]: cls="same_unit"
        elif dom(e)==dom(t) or e["unit"] in NEUTRAL or t["unit"] in NEUTRAL: cls="same_domain"
        else: cls="cross_domain"
        rows.append({"from":e["id"],"to":r,"class":cls,"from_unit":e["unit"],"to_unit":t["unit"]})
from collections import Counter
c=Counter(x["class"] for x in rows)
json.dump({"total_oneway":len(rows),"by_class":dict(c),"rows":rows},
          open(os.path.join(ROOT,"reports","oneway_audit.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("单向关联总计 %d：%s"%(len(rows),dict(c)))
print("same_unit 示例:",[(x["from"],x["to"]) for x in rows if x["class"]=="same_unit"][:6])
print("same_domain 示例:",[(x["from"],x["to"]) for x in rows if x["class"]=="same_domain"][:6])