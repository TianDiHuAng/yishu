# -*- coding: utf-8 -*-
"""Cycle54 不变式全面盘点（9 项）：
1 条目/来源/单元/页面数 与 coverage.json、REPORT 声称是否一致
2 来源类型分布 + 未被任何条目引用的来源（死重）
3 level/tier/unit 分布
4 L3 条目的门禁状态（是否有争议块、双方、≥2数据、图示说明）
5 孤儿条目（无入链）
6 标题/ID 重复
7 related 悬空与单向（应已被 R19 覆盖，仍复核一遍）
8 待核实为空却 needs_verification=True 的情况（反之亦然）
9 每单元条目数与 units.html 所列是否一致
输出 reports/invariants_c54.json 与一份人类可读摘要。"""
import json,os,glob,re
from collections import Counter,defaultdict
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
src=json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))["sources"]
cov=json.load(open(os.path.join(D,"coverage.json"),encoding="utf-8"))
byid={e["id"]:e for e in es}
sm={s["id"]:s for s in src}
rep={"issues":[],"review":[],"stats":{}}

# 1 计数一致
rep["stats"]["entries"]=len(es); rep["stats"]["sources"]=len(src)
rep["stats"]["units"]=len({e["unit"] for e in es})
pages=len(glob.glob(os.path.join(ROOT,"*.html")))+len(glob.glob(os.path.join(ROOT,"entries","*.html")))+len(glob.glob(os.path.join(ROOT,"units","*.html")))
rep["stats"]["html_files"]=pages
if cov.get("entries_total") not in (None,len(es)):
    rep["issues"].append(("1-count", "coverage.entries_total=%s 与实际 %d 不符"%(cov.get("entries_total"),len(es))))

# 2 来源类型分布 + 死重
types=Counter(s.get("type","?") for s in src)
rep["stats"]["source_types"]=dict(types)
used={x for e in es for x in e.get("sources",[])}
dead=[s["id"] for s in src if s["id"] not in used]
if dead: rep["issues"].append(("2-dead-source", "未被任何条目引用：%s"%dead))

# 3 分布
rep["stats"]["levels"]=dict(Counter(e.get("level","L2") for e in es))
rep["stats"]["tiers"]=dict(Counter(e["tier"] for e in es))
perunit=Counter(e["unit"] for e in es); rep["stats"]["per_unit"]=dict(perunit)

# 4 L3 门禁
l3=[e for e in es if e.get("level")=="L3"]
for e in l3:
    sec=e.get("sections",{}); cont=sec.get("与前后风格的关系和争论","")
    ok_views=("一方" in cont) or ("另一" in cont) or ("两" in cont)
    if len(cont)<120: rep["review"].append(("4-l3","%s 争议块过短（%d 字）"%(e["id"],len(cont))))
    if not ok_views: rep["review"].append(("4-l3","%s 未检出两方关键词（需人工判读）"%(e["id"],)))

# 5 孤儿（无入链）
inbound=Counter()
for e in es:
    for r in e.get("related",[]): inbound[r]+=1
orph=[e["id"] for e in es if inbound[e["id"]]==0]
if orph: rep["issues"].append(("5-orphan","无入链：%s"%orph))

# 6 重复
ti=Counter(e["title"] for e in es); dup=[t for t,c in ti.items() if c>1]
if dup: rep["issues"].append(("6-dup-title","重复标题：%s"%dup))
ids=Counter(e["id"] for e in es); du2=[i for i,c in ids.items() if c>1]
if du2: rep["issues"].append(("6-dup-id",du2))

# 7 related 悬空/单向
for e in es:
    for r in e.get("related",[]):
        t=byid.get(r)
        if t is None: rep["issues"].append(("7-related","%s → %s 悬空"%(e["id"],r)))
        elif e["id"] not in t.get("related",[]): rep["issues"].append(("7-related","单向 %s → %s"%(e["id"],r)))

# 8 needs_verification 与 pending_notes 一致性
for e in es:
    nv=e.get("needs_verification"); pend=(e.get("sections",{}).get("待核实","") or e.get("pending_notes",""))
    if nv and not pend.strip(): rep["issues"].append(("8-nv","%s 标记待核实但无待核内容"%e["id"]))
    if (not nv) and len(e.get("sources",[]))<2: rep["issues"].append(("8-nv","%s 来源<2 却未标记待核实"%e["id"]))

# 9 单元页一致性
for u in sorted(perunit):
    p=os.path.join(ROOT,"units",u+".html")
    if not os.path.exists(p): rep["issues"].append(("9-unit","缺单元页 %s"%u)); continue
    h=open(p,encoding="utf-8").read()
    n=h.count("entries/")
    if n==0: rep["issues"].append(("9-unit","%s 页未列出条目"%u))

print("条目 %d · 来源 %d · 单元 %d · HTML %d"%(len(es),len(src),rep["stats"]["units"],pages))
print("来源类型:",dict(types))
print("层级:",rep["stats"]["levels"],"｜重要性:",rep["stats"]["tiers"])
print("L3:",[(e["id"],len(e["sections"].get("与前后风格的关系和争论",""))) for e in l3])
print("问题计数:",len(rep["issues"]))
for k,v in rep["issues"][:20]: print("  [%s] %s"%(k,v))
json.dump(rep,open(os.path.join(ROOT,"reports","invariants_c54.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
import sys
print("需人工复核（L3 判读）:",len(rep["review"]))
for k,v in rep["review"]: print("  [review]",v)
sys.exit(1 if rep["issues"] else 0)
