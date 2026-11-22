# -*- coding: utf-8 -*-
"""Cycle22 收尾：D026 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG（全部避免反引号与 ASCII 引号）。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D026 — Cycle22 实体锚点（identity anchor）与「实体对照」页
- **决定**：
  1. 为 104 条尚无 Wikidata 关联的条目做两阶段匹配（先检索候选、再分块批量取标签/描述），严格规则：标签规范化后与标题相等或互为子串，且实体描述含该类条目的类型词 → 命中 21 条。
  2. 命中项登记为**身份锚点来源**（type = 权威结构化数据（身份锚点）），并在站点新增**实体对照页** entities.html，公开列出 条目 ↔ QID。
  3. 明确写入来源说明：身份锚点**不作为事实依据**，条目的年代/风格/评价仍以原来源为准。
- **理由**：内容来源不可达期间，能做的可靠增量是「把条目锚定到权威结构化实体」，便于读者核对，也便于将来恢复网络后按 QID 精准补事实。若把锚点当事实依据，就会滑向单源断言，故必须在来源类型与页面上双重声明。
- **可逆方式**：删除 wd-anchor-* 来源与对应 overlay 的该来源项，并停用 entities.html 生成函数即可。
- **代价**：41 → 62 条条目具备 Wikidata 关联（41 原有 + 21 锚点）；精确匹配率 21/104 偏低，其余 40 条歧义、43 条无候选，已记录在 reports/entity_map_c22.json 供后续人工确认。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle22","date":"2026-11-22","status":"completed",
 "gap_methods":["实体锚定(Wikidata 两阶段批量匹配)"],"network":"partial: wikidata ok",
 "new_entries":0,"upgrades":0,"reviews":104,"fixes":0,
 "entity_mapping":{"candidates":104,"matched":21,"ambiguous":40,"none":43},
 "new_sources":21,"sources_total":228,
 "site_pages":{"entities.html":175},
 "check_result":"errors=0","check_links_result":"broken=0(175页)","audit_all":"7/7 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle22","date":"2026-11-22","methods_used":["实体锚定"],
 "gaps_found":{"anchors":21},"network":"partial",
 "verdict":"21 条目新增 Wikidata 身份锚点 + 实体对照页；40 歧义/43 无候选已记录；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle22"' not in t:
    block=('if cyc=="cycle22":\n'
           '    L.append("- 本轮特别说明：把 104 条尚未关联 Wikidata 的条目做**两阶段批量匹配**'
           '（先检索候选、再按 50 个一组批量取标签与描述，避免逐条抓取超时）：'
           '**命中 21 条**、歧义 40 条、无候选 43 条。命中项登记为**身份锚点来源**（明确声明不作事实依据），'
           '并在站点新增**实体对照页** entities.html（21 条映射，公开可核对）。'
           '匹配率偏低如实记录在 reports/entity_map_c22.json（歧义项多为中文标签缺失或同名条目）。'
           '来源 207→228，站点 174→175 页。")\n')
    anchor='if cyc=="cycle21":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 21 已完成** → 下轮 **Cycle 22**",
              "- 当前轮次：**Cycle 22 已完成** → 下轮 **Cycle 23**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")