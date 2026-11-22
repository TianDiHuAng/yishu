# -*- coding: utf-8 -*-
"""Cycle7（本地）v2：数据驱动的矩阵空白格分类。
域：艺术（绘画/雕塑/建筑/书法/综合） vs 音乐（音乐体裁）。
规则：该地区在该域内**已有其他媒介的条目**却缺此媒介 → A（应补）；该地区在该域内完全无条目 → B（暂不构成缺口，可能超出本库范围）。
"""
import json,os
from collections import Counter
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
g=json.load(open(os.path.join(ROOT,"reports","gaps_cycle6final.json"),encoding="utf-8"))
ART={"绘画","雕塑","建筑","书法","综合"}

def domain(m): return "art" if m in ART else "music"
region_media=Counter()
region_domain=Counter()
for e in es:
    for m in set(e["medium"].split(",")):
        region_media[(e["region"],m)]+=1
        region_domain[(e["region"],domain(m))]+=1

rows=[]
EAST_ASIA={"中国","日本","东亚","南亚","东南亚"}
for region,medium in g["matrix_blank"]:
    d=domain(medium)
    # 修正规则：书法只在东亚/南亚文化圈构成缺口；"综合"是兜底标签不作补盲目标
    if medium=="书法" and region not in EAST_ASIA: cls="B"
    elif medium=="综合": cls="B"
    else: cls="A" if region_domain.get((region,d),0)>0 else "B"
    rows.append({"region":region,"medium":medium,"domain":d,"class":cls,
                 "region_domain_entries":region_domain.get((region,d),0)})
A=[r for r in rows if r["class"]=="A"]
A.sort(key=lambda r:r["region_domain_entries"],reverse=True)
B=[r for r in rows if r["class"]=="B"]

L=["# 覆盖矩阵空白格分类（Cycle 7，本地数据驱动）","",
   "空白格共 **%d**：A 类（该地区在本域已有条目、却缺此媒介，**应补**）**%d** 个；B 类（该地区在本域完全无条目，暂不构成缺口）**%d** 个。 "%(len(rows),len(A),len(B)),
   "分类为**本库范围判断**而非学界定论；A 类仍需联网核验来源后方可新增，不得据本表直接写作。 ","",
   "## A 类补盲目标（按该地区本域条目数降序）","","| 地区 | 缺失媒介 | 该地区本域现有条目 |","|---|---|---|"]
for r in A: L.append("| %s | %s | %d |"%(r["region"],r["medium"],r["region_domain_entries"]))
L+=["","## B 类（%d 个，暂不处理）"%len(B),""]
from collections import defaultdict
byreg=defaultdict(list)
for r in B: byreg[r["region"]].append(r["medium"])
for k,v in sorted(byreg.items(), key=lambda kv:-len(kv[1]))[:15]:
    L.append("- %s：%s"%(k,"、".join(sorted(set(v)))))
open(os.path.join(ROOT,"reports","matrix_targets_c7.md"),"w",encoding="utf-8").write("\n".join(L))
json.dump({"total":len(rows),"A":A,"B_count":len(B)},
          open(os.path.join(ROOT,"reports","matrix_targets_c7.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("blank=%d  A(应补)=%d  B=%d"%(len(rows),len(A),len(B)))
print("A top12:",[(r["region"],r["medium"]) for r in A[:12]])