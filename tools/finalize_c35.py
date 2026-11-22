# -*- coding: utf-8 -*-
"""Cycle35 收尾：D038 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D038 — Cycle35 条目页「来源构成」徽标（让证据强度可读）
- **决定**：每个条目页标题区新增徽标，形如「3 来源：内容 2 · 结构化 1 · 锚点 0」，三类来源分别统计：
  内容来源（百科/机构页）、结构化事实（Wikidata 事实条目）、身份锚点（仅确认实体身份）。
- **理由**：此前读者只能看到"来源"表格里的逐条类型，**看不出整体证据结构**——例如"2 条百科 + 1 个锚点"与"2 条百科 + 1 个结构化事实"的证据强度并不相同，但页面上毫无差别。徽标把这一差别显性化，也与 D034/D026 的口径规则呼应。
- **实测分布（145 条）**：内容+锚点 77 · 内容+结构化 41 · 仅内容 27；**无任何条目只靠结构化/锚点**（即不存在"没有内容来源"的条目）。
- **可逆方式**：删除 `source_profile()` 与徽标拼接即可。
- **代价**：徽标占用标题区一行空间；统计口径若调整需同步 `source_profile` 的类型判定。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle35","date":"2026-11-22","status":"completed",
 "gap_methods":["站点信息增强"],"network":"probe: wiki/met/tate 000; wikidata 200",
 "new_entries":0,"upgrades":0,"reviews":145,"fixes":0,
 "ui_change":"条目页新增来源构成徽标（内容/结构化/锚点）",
 "badge_distribution":{"content+anchor":77,"content+structured":41,"content_only":27},
 "check_result":"errors=0","check_links_result":"broken=0(176页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle35","date":"2026-11-22","methods_used":["站点信息增强"],
 "gaps_found":{},"network":"wiki blocked / wikidata ok",
 "verdict":"来源构成徽标；网络仍只通 Wikidata；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle35"' not in t:
    block=('if cyc=="cycle35":\n'
           '    L.append("- 网络探针：Wikipedia/Met/Tate 仍 000（不可达），Wikidata 200 —— 内容建设继续受阻。'
           '本轮做**条目页来源构成徽标**：标题区显示「N 来源：内容 a · 结构化 b · 锚点 c」，'
           '让读者一眼看出证据结构差异（「2 百科+1 锚点」与「2 百科+1 结构化事实」强度并不相同）。'
           '实测分布：内容+锚点 77、内容+结构化 41、仅内容 27 —— **没有条目只靠结构化或锚点撑着**。'
           '过程中修了一次锚点没对上的补丁（与 Cycle29 同类问题），已用精确匹配替换。")\n')
    anchor='if cyc=="cycle34":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 34 已完成** → 下轮 **Cycle 35**",
              "- 当前轮次：**Cycle 35 已完成** → 下轮 **Cycle 36**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")