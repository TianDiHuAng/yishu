# -*- coding: utf-8 -*-
"""Cycle25 收尾：D028 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D028 — Cycle25 新增「站点状态」页（status.html）与 pass3 精确锚定
- **决定**：
  1. 新增 `status.html`：公开呈现条目数/层级分布/重要性分布/来源构成（事实来源 vs 身份锚点）/校验方式与**已知缺口**，与 entities.html 一起构成透明度页面。
  2. 对 71 条未锚定条目做 pass3（要求 norm(id) 与英文标签**完全相等**且描述含类型词）：仅命中 1 条（serialism → Q507246），照实际采纳。
- **理由**：Cycle22/23 的锚点已到 33 条，但站点此前没有一处集中说明"我们有哪些缺口、锚点是什么性质"。状态页把这些**主动摆出来**，比藏在 reports/ 里更符合"诚实标注"的项目立场。pass3 之所以只命中 1 条，是因为多数条目（宋/元/明/清绘画、书法、中国音乐等）在 Wikidata 中并无对应英文实体——**这本身是信息**，说明这些条目的锚定只能靠中文标签或人工指定。
- **可逆方式**：删除 build_status 函数与导航项即可。
- **代价**：状态页数据来自构建时的 JSON（每次 gen_site 重新计算），若报告与数据不同步会显示旧缺口数；已在页面注明"具体数值见 reports/"。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle25","date":"2026-11-22","status":"completed",
 "gap_methods":["实体锚定pass3(精确)","站点透明度补全"],"network":"partial: wikidata ok",
 "new_entries":0,"upgrades":0,"reviews":71,"fixes":0,
 "entity_pass3":{"tested":71,"matched":1},
 "site_pages":{"status.html":176},
 "new_sources":1,"sources_total":241,"anchors_total":34,
 "check_result":"errors=0","check_links_result":"broken=0(176页)","audit_all":"7/7 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle25","date":"2026-11-22","methods_used":["pass3锚定","状态页"],
 "gaps_found":{"anchors":1},"network":"partial",
 "verdict":"pass3 仅1条精确命中；新增 status.html 公开缺口与来源构成；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle25"' not in t:
    block=('if cyc=="cycle25":\n'
           '    L.append("- 本轮特别说明：两件事。①对 71 条未锚定条目做 **pass3 最高精度匹配**'
           '（要求条目 id 与实体英文标签完全相等），只命中 **1 条**（serialism → Q507246）并照实采纳；'
           '命中率极低本身是信息——宋/元/明/清绘画、书法、中国音乐等条目在 Wikidata 中并无对应英文实体，锚定只能靠中文标签或人工指定。'
           '②新增**站点状态页** status.html：公开条目数、层级与重要性分布、来源构成（事实来源 43 / 身份锚点 34）、'
           '校验方式，以及**已知缺口**（A类58、B2候选22、待核实项、Wikipedia/Met/Tate 不可达）——'
           '把短板主动摆在读者面前，而不是藏在报告里。站点 175→176 页。")\n')
    anchor='if cyc=="cycle24":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 24（体检轮）已完成** → 下轮 **Cycle 25**",
              "- 当前轮次：**Cycle 25 已完成** → 下轮 **Cycle 26**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")