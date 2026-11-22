# -*- coding: utf-8 -*-
"""Cycle33（体检轮）：饱和评估（AUTONOMOUS §5）。
判定条件：①连续3轮七种缺口方法均找不到新的、有权威依据的缺口；②核心与重要条目均达 L2。
本轮给出明确定论与依据，写入 SATURATION.json 与 reports/saturation_assessment_c33.md。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
lv={}
for e in es: lv[e.get("level","L2")]=lv.get(e.get("level","L2"),0)+1
core_ok=all(e.get("level") in ("L2","L3") for e in es if e["tier"]=="核心")
imp_ok=all(e.get("level") in ("L2","L3") for e in es if e["tier"]=="重要")
matrix=json.load(open(os.path.join(ROOT,"reports","matrix_b_review_c19.json"),encoding="utf-8"))
tgt=json.load(open(os.path.join(ROOT,"reports","matrix_targets_c7.json"),encoding="utf-8"))
A=len(tgt["A"]); B2=matrix["B2"] if isinstance(matrix["B2"],int) else len(matrix["B2"])
SAT={
 "cycle":"cycle33","saturated":False,
 "condition_1_all_core_important_L2":{"核心":core_ok,"重要":imp_ok,"levels":lv},
 "condition_2_no_new_gaps_3_rounds":False,
 "open_gaps":{
   "A_class_matrix":"A 类空白格 %d 项（建筑已建 3 条，其余需可核验内容来源）"%A,
   "B2_music_regions":"B2 候选缺口 %d 项（非西方音乐体裁，需内容来源）"%B2,
   "pending_verification":"B5 剩余 5 项待第二来源",
   "unanchored_entries":"27 条无 Wikidata 锚点（自有页 11 无需、中国专题 11 无匹配实体、被拒 5）",
 },
 "reason_not_saturated":"条件①不成立：最近三轮仍在发现**新的、有权威依据的缺口**（Cycle31 锚定 14 条、Cycle32 锚定 4 条、Cycle19 发现 B2 类 22 项）。这些缺口当前**无法填补**并非因为缺口不存在，而是因为内容来源（Wikipedia/Met/Tate）在本构建环境不可达。",
 "blocker":"外部来源可达性（非项目质量问题）",
 "maintenance_ready":True,
 "next_actions_if_unblocked":["按 A 类清单补建筑（南亚/日本/伊斯兰等，≥2 来源）","补 B2 音乐地区空白（甘美兰/印度古典/雅乐等）","B5 剩余 5 项复核","为 27 条未锚定条目人工指定 QID 或确认无需锚定"],
}
json.dump(SAT,open(os.path.join(ROOT,"reports","saturation_assessment_c33.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 同步 SATURATION.json（保留历史 cycles）
sp=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(sp,encoding="utf-8"))
sd["saturated"]=False
sd["zero_gap_streak"]=0
sd["maintenance_mode"]=False
sd["assessment_c33"]=SAT
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("saturated?",SAT["saturated"],"| core_L2+:",core_ok,"imp_L2+:",imp_ok)
print("open gaps: A=%d B2=%d B5=5 unanchored=27"%(A,B2))