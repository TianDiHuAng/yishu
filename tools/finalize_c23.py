# -*- coding: utf-8 -*-
"""Cycle23 收尾：D027 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D027 — Cycle23 实体锚点 pass2：用「条目 id（英文 slug）」比对实体英文标签
- **决定**：歧义组改用 pass2 规则——把条目 id（如 greek-art、abstract-expressionism）规范化后与实体英文标签比对，相等或互为子串且描述含类型词才算命中；再经**人工逐条确认**，采纳 12 条、拒绝 3 条。
- **理由**：pass1 只比对中文标题，凡实体缺中文标签即判歧义（40 条），浪费了大量可靠命中。条目 id 本身是英文 slug，是天然的第二把钥匙；同时该规则天然排除中文论文类实体（其标签与 id 不同名）。
- **人工确认不可省略**：15 个初命中里有 3 个必须拒绝——
  - romanesque → Q46261 是『建筑』实体，条目为跨媒介艺术风格；
  - renaissance → Q23731823 竟是**法国政党**（纯字符串巧合）；
  - baroque-music → Q3328590 是『法国巴洛克音乐』，比条目窄。
  这三例证明机器匹配到位后**仍需人眼**，否则会把锚点挂在错误实体上。
- **可逆方式**：删除 wd-anchor-* 来源与覆盖层引用即可。
- **代价**：锚点总数 21 → 33（12 条新增）；仍余 28 条未锚定（含 43→ 无候选与部分歧义），已记录待人工处理。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle23","date":"2026-11-22","status":"completed",
 "gap_methods":["实体锚定 pass2(id↔英文标签)+人工确认"],"network":"partial: wikidata ok",
 "new_entries":0,"upgrades":0,"reviews":15,"fixes":0,
 "entity_pass2":{"hits":15,"adopted":12,"rejected":3},
 "rejected_examples":"romanesque→建筑实体; renaissance→法国政党; baroque-music→法国巴洛克音乐(过窄)",
 "new_sources":12,"sources_total":240,"anchors_total":33,
 "check_result":"errors=0","check_links_result":"broken=0(175页)","audit_all":"7/7 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle23","date":"2026-11-22","methods_used":["实体锚定pass2"],
 "gaps_found":{"anchors":12},"network":"partial",
 "verdict":"pass2 采纳 12 条锚点（拒绝 3 条误配，已写明原因）；锚点累计 33；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle23"' not in t:
    block=('if cyc=="cycle23":\n'
           '    L.append("- 本轮特别说明：针对上轮 40 条歧义项，改用 **pass2 规则**——拿条目 id（本身是英文 slug）'
           '去比对实体的**英文标签**，相等或互为子串且描述含类型词才算命中，再**人工逐条确认**：'
           '初命中 15 条，**采纳 12 条、拒绝 3 条**。拒绝示例很有说服力：'
           'romanesque 命中「罗马式建筑」实体（条目是跨媒介风格）、renaissance 命中**法国政党**、'
           'baroque-music 命中「法国巴洛克音乐」（比条目窄）——证明机器匹配到位后仍需人眼把关。'
           '锚点总数 21→**33**，来源 228→240，站点仍 175 页。")\n')
    anchor='if cyc=="cycle22":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 22 已完成** → 下轮 **Cycle 23**",
              "- 当前轮次：**Cycle 23 已完成** → 下轮 **Cycle 24（体检轮）**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")