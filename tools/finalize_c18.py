# -*- coding: utf-8 -*-
"""Cycle18 收尾：D023 + METRICS/SATURATION + REPORT 块 + PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEC=os.path.join(ROOT,"DECISIONS.md")
io.open(DEC,"a",encoding="utf-8").write("""
## D023 — Cycle18 新增「高棉建筑」（A 类建筑缺口第二条，双内容来源）
- **决定**：新建 `khmer-architecture`（高棉建筑），归 `art-asia`，medium=建筑；来源 = `enc-khmer-art`（高棉艺术，论述吴哥建筑）+ `enc-angkor`（吴哥，论述建筑群与象征）+ `wd-angkor-wat`（实体身份）。
- **理由**：与 Cycle17 的哥特/罗马式不同，本条拥有**两个确实论述建筑的已核验内容来源**（不止是身份确认），因此其形制描述有真正的双源基础。中国建筑仍只有 Wikidata 一条可核验来源 → 继续不建。
- **过程中修正的一处不诚实**：初稿写「19世纪后被重新发现与研究」，但所引来源并未支撑该年份，已删去并改为「近现代被重新记录与研究（具体年代待核实）」，同时在待核实记明原委。
- **可逆方式**：从 catalog.py 删除该行、从 sources.json 删除 `wd-angkor-wat`、删除 l2 覆盖层即可。
- **代价**：与既有 `khmer-art`、`angkor` 主题邻近，已在 `related` 互链区分（一个艺术门类、一个建筑群实例、一个建筑传统）。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle18","date":"2026-11-22","status":"completed",
 "gap_methods":["B2矩阵A类(建筑,第二条)","B5核验"],"network":"partial: wikidata ok; 新通道扫描无可用",
 "new_entries":1,"upgrades":0,"reviews":1,"fixes":1,
 "new_sources":1,"sources_total":205,
 "honesty_fix":"删去来源未支撑的「19世纪后重新发现」表述并记明原委",
 "check_result":"errors=0","check_links_result":"broken=0(174页)","audit_all":"6/6 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle18","date":"2026-11-22","methods_used":["B2补盲","B5核验"],
 "gaps_found":{"建筑缺口":1},"network":"partial",
 "verdict":"高棉建筑（双内容来源）建成；中国建筑仍单源不建；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle18"' not in t:
    block=('if cyc=="cycle18":\n'
           '    L.append("- 本轮特别说明：A 类建筑缺口推进第二条——新建 **高棉建筑**，其形制描述拥有 **两个确实论述建筑的已核验内容来源**（高棉艺术、吴哥）外加 Wikidata 身份来源，'
           '因此比 Cycle17 的哥特/罗马式（Wikidata 仅确认身份）基础更实。**中国建筑仍只差第二来源，继续不建**。'
           '过程中主动修正一处不诚实：初稿「19世纪后被重新发现」在所引来源中无支撑，已删去并改写为「近现代被重新记录与研究（具体年代待核实）」，并在待核实记明原委。'
           '条目 144→**145**，站点 173→**174** 页，孤儿 0，check/links/audit 全通过。")\n')
    anchor='if cyc=="cycle17":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 17 已完成** → 下轮 **Cycle 18**",
              "- 当前轮次：**Cycle 18 已完成** → 下轮 **Cycle 19**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")