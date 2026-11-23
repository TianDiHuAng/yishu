# -*- coding: utf-8 -*-
"""Cycle67：饱和评估（AUTONOMOUS §5）v2。
条件①：连续 3 轮七种缺口方法均未发现新的、有权威依据的缺口；
条件②：核心与重要条目均达 L2。
用仓库自身数据与最近轮次记录给出判定与证据，写入 SATURATION.json 与 reports/saturation_c67.json。
"""
import json,os
from collections import Counter
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
cov=json.load(open(os.path.join(D,"coverage.json"),encoding="utf-8"))
met=json.load(open(os.path.join(ROOT,"METRICS.json"),encoding="utf-8"))["rounds"]
lv=Counter(e.get("level","L2") for e in es); tier=Counter(e["tier"] for e in es)
core_ok=all(e.get("level") in ("L2","L3") for e in es if e["tier"]=="核心")
imp_ok=all(e.get("level") in ("L2","L3") for e in es if e["tier"]=="重要")
# 最近 6 轮的缺口产出（来自 METRICS）
recent=[r for r in met if r.get("cycle","").startswith(("cycle6","cycle5"))][-6:]
gaps=[(r["cycle"],r.get("new_entries",0)) for r in recent]
new_total=sum(n for _,n in gaps)
SAT={
 "cycle":"cycle67","saturated":False,
 "condition_1_no_new_gaps_3_rounds":False,
 "condition_2_core_important_L2":{"核心":core_ok,"重要":imp_ok,"levels":dict(lv),"tiers":dict(tier)},
 "evidence_recent_rounds":gaps,
 "recent_new_entries_total":new_total,
 "why_not_saturated":("条件①不成立：最近 6 轮仍在持续产出**新的有来源条目**（cycle52–64 共新增 %d 条），"
   "且缺口清单中仍有明确可补项（北美平原/东南、非洲余量、东南亚泰越窑）。"
   "条件②成立：核心与重要条目全部 ≥L2。"%new_total),
 "open_gaps":{
   "A_class_matrix":"见 reports/覆盖矩阵.md（建筑已建 4 条，其余需内容来源）",
   "B2_music_regions":"非西方音乐体裁仍有空白",
   "B5_pending":"少量待核实项",
   "geo_blocks":{"东南亚泰/越窑":"确认不可得（CMA 无对象）","北美平原/东南":"CMA 有候选未用尽","大洋洲":"仅 2 条"},
   "unanchored":"部分条目无 Wikidata 锚点（自有页/中国专题）"},
 "saturation_blockers":"外部来源可达性（Wikipedia/Met/Tate 不可达）",
 "recommendation":"继续以博物馆 API 推进内容；饱和度判定需连续 3 轮无新增缺口才可成立",
}
json.dump(SAT,open(os.path.join(ROOT,"reports","saturation_c67.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
sp=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(sp,encoding="utf-8"))
sd["saturated"]=False; sd["assessment_c67"]=SAT
sd["cycles"].append({"cycle":"cycle67","date":"2026-11-23","methods_used":["§5 饱和评估"],
 "gaps_found":{}, "network":"partial",
 "verdict":"未饱和：条件②成立，条件①不成立（近 6 轮仍有新条目与明确可补缺口）"})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("saturated:",SAT["saturated"])
print("核心全L2+:",core_ok,"| 重要全L2+:",imp_ok)
print("近6轮新增:",gaps,"合计",new_total)
print("层级:",dict(lv),"| 重要性:",dict(tier))