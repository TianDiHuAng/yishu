# -*- coding: utf-8 -*-
"""Cycle36 收尾：D039 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D039 — Cycle36 B5 收尾：用 Wikidata 时间声明尝试解决剩余 5 项，得到「1 个真实差异 + 1 个备查事实 + 3 个仍无解」
- **背景**：B5 剩余 5 项待核：realism 的 1840—1870、romanesque 的终点 1150、donatello 的"解剖准确性"、草书年代、张旭作品。
- **结果**（证据存 `reports/b5_wd_attempt_c36.json`）：
  1. **romanesque：得到真实差异**——Wikidata 实体 `Romanesque art (Q46805)` 记 **P580=1000 / P582=1200**，而本条目正文采「约1000—1150」，**终点相差 50 年**。且本条的 1150 源自早期种子、从未获独立来源支撑。
  2. **张旭：得到备查事实**——`Zhang Xu (Q717343)`（Chinese calligrapher）记 **生年 670**；但条目的待核问题是"具体作品名称"，仍无解。
  3. realism 年代、草书年代、donatello 术语：Wikidata 无可用声明（检索无候选或无时间属性），维持待核。
- **处置原则**：**不据单一结构化来源改动正文与 when**。差异与备查事实一律写入"待核实"的复核记录节：
  - romanesque 明确写"不据单一来源改动正文，差异待第三来源判定"；
  - cursive-script 写"仅登记备查"。
- **理由**：这正是双源规则的意义——Wikidata 能给出一个数值 ≠ 可以改正文。**发现差异比抹平差异更有价值**：读者现在能看到"我们的 1150 与结构化数据的 1200 不一致，且 1150 无来源"。
- **可逆方式**：从两条目待核实中删除对应句子。
- **代价**：romanesque 的断代悬置（正文仍写 1150，标注了差异），需第三来源才能定夺。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle36","date":"2026-11-22","status":"completed",
 "gap_methods":["B5复核(Wikidata时间声明)"],"network":"partial: wikidata ok",
 "new_entries":0,"upgrades":0,"reviews":5,"fixes":0,
 "b5_result":{"romanesque":"差异：WD 1000–1200 vs 条目 1000—1150","zhangxu":"备查：生年670（作品名仍无解）",
   "unresolved":["realism 1840-1870","donatello 术语","草书年代"]},
 "check_result":"errors=0","check_links_result":"broken=0(176页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle36","date":"2026-11-22","methods_used":["B5 Wikidata尝试"],
 "gaps_found":{"discrepancy":1,"fact":1,"unresolved":3},"network":"partial",
 "verdict":"B5：1 差异（romanesque 断代）+1 备查（张旭生年）+3 仍无解；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle36"' not in t:
    block=('if cyc=="cycle36":\n'
           '    L.append("- 本轮把 B5 剩余 5 项用 Wikidata **时间声明**再核一遍，结果是「1 个真实差异 + 1 个备查事实 + 3 个仍无解」：'
           '①**romanesque 发现断代差异**——Wikidata『Romanesque art』(Q46805) 记 P580=1000 / P582=1200，'
           '本条目正文采「约1000—1150」，**终点差 50 年**，而 1150 本身源自早期种子、从未有独立来源；'
           '②张旭实体给出**生年 670**，但条目待核的是"作品名称"，仍无解；'
           '③realism 年代、草书年代、donatello 术语无可用声明。'
           '处置：**一律不据单一结构化来源改正文**，差异与备查事实写进复核记录，并注明"待第三来源判定"。'
           '发现差异比抹平差异更有价值。")\n')
    anchor='if cyc=="cycle35":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 35 已完成** → 下轮 **Cycle 36**",
              "- 当前轮次：**Cycle 36 已完成** → 下轮 **Cycle 37（体检轮）**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")