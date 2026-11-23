# -*- coding: utf-8 -*-
"""Cycle41（同批扩充）收尾：D044 + METRICS/SATURATION/REPORT/PROGRESS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D044 — Cycle41 第二批扩充：以馆方传记正文新增 5 位人物（149 → 154）
- **决定**：用 Cleveland 艺术家记录中的**馆方撰写的传记正文**（1000–4800 字符不等），新增 5 位缺席的重要人物：
  `manet`（1832—1883，核心）、`turner`（1775—1851，核心）、`constable`（1776—1837，重要）、`courbet`（1819—1877，核心）、`ingres`（1780—1867，重要）。条目 149 → **154**。
- **双源情况（如实）**：
  - `manet`：CMA 传记 + **V&A《洛拉·德·瓦朗丝》(1863–64, O652344)** → 两机构；
  - `constable`：CMA 传记 + **V&A《汉普斯特德布兰奇山池塘》(1819, O84528)** → 两机构；
  - `courbet`：CMA 传记 + **V&A《圣德尼堡风景》(1873, O81593)** → 两机构；
  - `turner`、`ingres`：**仅 CMA**（V&A 检索命中的同名者非其本人作品；Ingres 命中为「仿安格尔」之作）→ 已按 R10 标 `needs_verification`，并在待核实首条写明。
- **写作纪律**：只写传记与其藏品记录能支撑的内容——学艺经历、展览与任职、技法与题材演变、可查的争议事件（马奈与沙龙体制、库尔贝与公社、安格尔与德拉克洛瓦之争、透纳与康斯太勃尔并置）。人物评价性断语若仅一处转引，均在待核实注明「系该馆转引，未核原刊」。
- **可逆方式**：删除 5 条 overlay 与 catalog 元组，重跑 `build_scope.py`。
- **代价**：`turner`、`ingres` 带 `needs_verification`；V&A 藏品仅能佐证「该艺术家有此作品」，不核对生卒年，这一点已在条目中写明，未当作"双源核对"使用。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle41","date":"2026-11-23","status":"completed",
 "gap_methods":["馆方传记正文（CMA 艺术家记录）","V&A 藏品核验"],"network":"partial: museum APIs ok",
 "new_entries":5,"new_entry_ids":["manet","turner","constable","courbet","ingres"],
 "dual_institution":["manet","constable","courbet"],"single_institution_flagged":["turner","ingres"],
 "new_sources":8,"sources_total":291,"entries_total":154,"pages":185,
 "check_result":"errors=0","check_links_result":"broken=0(185页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle41","date":"2026-11-23","methods_used":["馆方传记","V&A核验"],
 "gaps_found":{"entries":5},"network":"partial (museum APIs)",
 "verdict":"新增 5 人物（154）；3 双机构 / 2 单机构已标记；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle41"' not in t:
    block=('if cyc=="cycle41":\n'
           '    L.append("- 同批第二次扩充：用 Cleveland 馆方撰写的**艺术家传记正文**新增 5 位缺席人物——'
           '马奈、透纳、康斯太勃尔、库尔贝、安格尔（149 → 154）。'
           '双源如实：马奈 / 康斯太勃尔 / 库尔贝各有 V&A 藏品记录作第二机构；'
           '透纳与安格尔仅 CMA（V&A 命中同名者非本人作品、Ingres 命中为仿作），已标 needs_verification。'
           '写作只取传记与藏品能支撑的事实（学艺、展览、任职、技法演变、可查争议），'
           '转引性评语一律注明「系该馆转引，未核原刊」。站点 180 → 185 页，八步体检 8/8。")\n')
    anchor='if cyc=="cycle40":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
PP=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PP,encoding="utf-8").read()
for a,b in [("| 条目 | 149（L2 143 / L3 6 / L1 0） |","| 条目 | 154（L2 148 / L3 6 / L1 0） |"),
            ("| 来源 | 283（全部 verified；隔离区 5 条不可核验） |","| 来源 | 291（全部 verified；隔离区 5 条不可核验） |"),
            ("| 页面 | 180，站内断链 **0** |","| 页面 | 185，站内断链 **0** |")]:
    if a in s2: s2=s2.replace(a,b)
io.open(PP,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-150:])