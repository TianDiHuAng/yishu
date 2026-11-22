# -*- coding: utf-8 -*-
"""Cycle33 收尾：D036 + METRICS/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D036 — Cycle33 饱和评估：**未饱和**，且明确"不是缺口没了，是来源进不来"
- **决定**：按 §5 两个条件正式评估，结论 **saturated=false**，理由写进 `reports/saturation_assessment_c33.json`：
  - 条件①（连续 3 轮七种方法找不到新缺口）**不成立**：最近三轮仍在发现新的、有权威依据的缺口（Cycle31 锚定 14 条、Cycle32 锚定 4 条；Cycle19 新发现 B2 类 22 项）。
  - 条件②（核心与重要条目均达 L2）**成立**：核心 48、重要 85 全部 ≥L2，全库 145 条无 L1。
- **当前开放缺口（如实登记）**：A 类矩阵 58 项（建筑已建 3 条）、B2 音乐地区 22 项、B5 待核实 5 项、未锚定条目 27 条（其中 11 条为自有页面，本无实体）。
- **性质说明**：上述缺口**填不了的原因只有一个**——内容来源（Wikipedia/Met/Tate）在本构建环境不可达；Wikidata 只能做身份锚定与结构化事实，无法支撑风格/体裁/评价类陈述。这是**外部阻塞**，不是质量问题。
- **可逆方式**：来源恢复后按 `next_actions_if_unblocked` 逐项推进即可，无需改动架构。
- **代价**：饱和判定推迟；项目以"结构完成 + 已知缺口登记"状态运行。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle33","date":"2026-11-22","status":"completed",
 "gap_methods":["F体检(第七次)","饱和评估(§5)"],"network":"partial",
 "new_entries":0,"upgrades":0,"reviews":145,"fixes":0,
 "healthcheck":{"audit":"8/8","dead":0,"duplicates":0,"contradictions":0,"orphans":0,
   "bad_anchors":0,"sitemap":"一致","contrast":"AA","oneway":0,"render_mismatch":0,"html_struct":0},
 "liveness":{"wd_sources":120,"http_200":120,"failed":0},
 "saturation_assessment":{"saturated":False,"core_L2plus":True,"important_L2plus":True,
   "open_gaps":{"A":58,"B2":22,"B5":5,"unanchored":27}},
 "check_result":"errors=0","check_links_result":"broken=0(176页)","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle33"' not in t:
    block=('if cyc=="cycle33":\n'
           '    L.append("- 本轮为**体检轮 + 饱和评估**。八步体检全通过；**120 条 Wikidata 来源 120/120 返回 200**。'
           '按 §5 两个条件正式评估饱和：条件②（核心48/重要85 全部≥L2、全库无 L1）**成立**；'
           '但条件①（连续3轮无新缺口）**不成立**——最近三轮仍发现新缺口（Cycle31 锚定14、Cycle32 锚定4）。'
           '故 **saturated=false**，并登记开放缺口：A类58、B2音乐地区22、B5待核实5、未锚定27（含自有页11）。'
           '性质说明写得很直白：**不是缺口没了，是内容来源进不来**；Wikidata 只能做身份锚定与结构化事实，'
           '撑不起风格/体裁/评价类陈述。这是外部阻塞，不是质量问题。")\n')
    anchor='if cyc=="cycle32":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 32 已完成** → 下轮 **Cycle 33（体检轮）**",
              "- 当前轮次：**Cycle 33（体检轮+饱和评估）已完成** → 下轮 **Cycle 34**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")