# -*- coding: utf-8 -*-
"""缺口发现工具：覆盖矩阵空格/稀疏格、悬空引用、深度缺口、待核实清单、孤儿页。
输出 reports/gaps_cycleN.json 供 BACKLOG 排序使用。"""
import json, os, re, glob, sys
from collections import defaultdict, Counter
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
cycle=sys.argv[1] if len(sys.argv)>1 else "auto"
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
byid={e["id"]:e for e in es}
ids=set(byid)

gaps={"cycle":cycle,"matrix_blank":[],"matrix_sparse":[],"dangling":[],
      "depth_core_l1":[],"depth_important_l1":[],"pending":[],"orphan":[]}

# 1) 覆盖矩阵（时期带 × 地区 × 媒介）
def band(e):
    w=e["when"]
    if re.search(r"旧石器|新石器|公元前|战国|先秦|远古|商周",w): return "古代"
    if re.search(r"中世纪|拜占庭|罗马式|哥特|5—15|5—14",w): return "中世纪"
    if re.search(r"14—16|15世纪|16世纪|唐代|宋代|元代|明代|汉|唐|宋|元|明",w): return "文艺复兴/宋元明"
    if re.search(r"17|18|19|清",w): return "17—19世纪"
    if re.search(r"20|当代|至今|19末",w): return "20世纪—当代"
    return "跨期/术语"
bands=["古代","中世纪","文艺复兴/宋元明","17—19世纪","20世纪—当代","跨期/术语"]
regions=sorted({e["region"] for e in es})
medias=sorted({m for e in es for m in e["medium"].split(",")})
grid=defaultdict(list)
for e in es:
    for m in e["medium"].split(","): grid[(band(e),e["region"],m)].append(e["id"])
# 空格：某地区×媒介完全无条目（列前20）
for r in regions:
    for m in medias:
        if not any(grid.get((b,r,m)) for b in bands):
            gaps["matrix_blank"].append([r,m])
# 稀疏格：1条
for (b,r,m),v in grid.items():
    if len(v)==1: gaps["matrix_sparse"].append([b,r,m,v[0]])

# 2) 悬空引用：related 指向不存在的id（check已覆盖，这里再列正文提及的书名号条目名）
titles={e["title"] for e in es}
for e in es:
    for r in e.get("related",[]):
        if r not in ids: gaps["dangling"].append([e["id"],r])

# 3) 深度缺口
for e in es:
    lv=e.get("level","L1")
    if lv=="L1" and e["tier"]=="核心": gaps["depth_core_l1"].append(e["id"])
    if lv=="L1" and e["tier"]=="重要": gaps["depth_important_l1"].append(e["id"])

# 4) 待核实清单（L2的待核实节 + coverage needs_verification）
for e in es:
    pending=e.get("pending_notes") or ""
    sec_pending=e.get("sections",{}).get("待核实","")
    if pending or (sec_pending and "待核实" not in sec_pending[:6]):
        gaps["pending"].append({"id":e["id"],"level":e.get("level","L1"),
            "coverage_note":pending[:100],"section_len":len(sec_pending)})

# 5) 孤儿页：无入链
inbound=Counter(r for e in es for r in e.get("related",[]))
for e in es:
    if inbound[e["id"]]==0: gaps["orphan"].append(e["id"])

out=os.path.join(ROOT,"reports","gaps_%s.json"%cycle)
json.dump(gaps,open(out,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("gaps: matrix_blank=%d sparse=%d dangling=%d coreL1=%d impL1=%d pending=%d orphan=%d"%(
 len(gaps["matrix_blank"]),len(gaps["matrix_sparse"]),len(gaps["dangling"]),
 len(gaps["depth_core_l1"]),len(gaps["depth_important_l1"]),len(gaps["pending"]),len(gaps["orphan"])))
print("->",out)
