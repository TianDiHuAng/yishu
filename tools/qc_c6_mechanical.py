# -*- coding: utf-8 -*-
"""Cycle6 质量闸（机械部分）：L3 块的来源id有效性、data数值是否真出自条目自身事实、
holder 是否为泛称（禁具体人名）、issue 是否能在条目 sections 找到对应依据。"""
import json,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
src={s["id"]:s for s in json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))["sources"]}
GENERIC=("所引","来源","通说","部分","研究者","批评","支持","学界","本条","页面","记载","作者","评论")
problems=[]
checked=0
for eid,e in es.items():
    l3=e.get("l3")
    if not l3: continue
    checked+=1
    body="".join(e.get("sections",{}).values())+e.get("when","")+e.get("overview","")+e.get("def","")
    # 1) 来源id 有效
    for d in l3.get("data",[]):
        m=re.search(r"来源[:：]\s*([a-z0-9-]+(?:\s*[,、]\s*[a-z0-9-]+)*)",d.get("note",""))
        if m:
            ids=re.split(r"[,、\s]+",m.group(1))
            for sid in ids:
                sid=sid.strip()
                if not sid: continue
                if sid not in src: problems.append((eid,"来源id不存在",sid))
                elif not src[sid]["verified"]: problems.append((eid,"来源未核验",sid))
        else:
            problems.append((eid,"data缺来源标注",d.get("label","")[:20]))
    # 2) data 数值是否出自条目自身事实（4位年份/2-4位数字）
    for d in l3.get("data",[]):
        val=str(d.get("value",""))
        for num in re.findall(r"\d{2,4}",val):
            if num not in body:
                problems.append((eid,"data数值不在条目事实中",num))
    # 3) holder 泛称检查
    for c in l3.get("controversies",[]):
        for v in c.get("views",[]):
            h=v.get("holder","")
            if not any(g in h for g in GENERIC):
                problems.append((eid,"holder疑似具体人名",h[:24]))
    # 4) issue 与 sections 的依据（关键词重叠）
    secs="".join(e.get("sections",{}).values())
    for c in l3.get("controversies",[]):
        iss=c.get("issue","")
        keys=[k for k in re.findall(r"[\u4e00-\u9fff]{2,4}",iss) if k in secs]
        if not keys: problems.append((eid,"issue在sections无关键词依据",iss[:30]))
print("L3 entries checked:",checked,"problems:",len(problems))
for p in problems[:40]: print("  ",p)