# -*- coding: utf-8 -*-
"""Cycle66 收尾：D070（否定结论）+ METRICS/SATURATION/REPORT。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D070 — Cycle66 否定结论：**「年份集合包含」类检查在本语料上不可作为硬性不变量**（第三次验证）
- **本轮尝试**：核对 `def`/`overview`（短文本）与 `when` 的年份是否冲突。
- **三轮口径演进与结果**：
  1. 初版（所有 2–4 位数字）：47 项"冲突"；**馆藏号**（1918.328 的 328、1933.220 的 220、1948.306 的 306…）与**人物生卒 vs 事件年份**（1775—1851 vs 1819 意大利之行）大量污染。
  2. 收窄到**四位年**：14 项。
  3. 逐条人工判读 14 项，**全部为合理内容**：
     | 类型 | 例 |
     |---|---|
     | 语境年份（正文确实要提的时代事件） | turner 的 1819 意大利之行；kongo-crucifix 的 1491 改宗；navajo 的 1540 西班牙人入西南、1860s Bosque Redondo；hopi 的 1500s 西班牙原型 |
     | 馆藏号误伤 | joseon 的 1981.3、inuit 的 1972.1054 |
     | 人物生卒（艺人） | inuit 的 1928—1998 |
- **结论（重要）**：**「年份集合包含关系」在本语料上不是有效不变量**。原因不是数据脏，而是**这个知识库的正文本来就要写大量他指年份**（师承、事件、来源史、馆藏号）。三次尝试（Cycle57 的 when↔正文、Cycle60 前的 when↔body、本轮 def/overview）都在同一处折戟。
- **决定**：**停止**在此方向再投入。保留两条**真正可工作的**年份类校验：
  1. **机构记录 ↔ 正文尺寸/年代**逐条比对（Cycle56，55 条 36/36 命中）；
  2. **R21**：`when` 不得含拉丁字母（表述规范）。
  本轮的 `def_overview_c66.py` 保留为**离线咨询工具**（输出供人读），**不接入 `audit_all`**，以免制造假警报。`def`/`overview` 的**空字段与复制粘贴**检查（B、C 两项）均 0 问题，可保留。
- **可逆方式**：无需回退（未改动数据）。
- **代价**：少了一个想象中的护栏；换来的是**不再浪费时间与假警报**。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle66","date":"2026-11-23","status":"completed",
 "gap_methods":["def/overview 与 when 年份一致性"],"network":"partial",
 "new_entries":0,"fixes":0,
 "result":"negative：47→14→人工判读 14 项全为合理内容（语境年份/馆藏号/艺人年）",
 "verdict":"年份集合包含不可作不变量（第三次验证），停止投入；保留可工作的两项（机构记录比对、R21）",
 "b_check_empty":0,"c_check_duplicate":0,"audit_steps":12,
 "entries_total":216,"sources_total":347,"pages":251,
 "check_result":"errors=0","check_links_result":"broken=0(251页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle66","date":"2026-11-23","methods_used":["def/overview 年份核查"],
 "gaps_found":{},"network":"partial",
 "verdict":"否定结论：年份集合包含不可作不变量（第三次），停止投入；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle66"' not in t:
    block=('if cyc=="cycle66":\n'
           '    L.append("- 本轮得到一个**否定结论**：核对 `def`/`overview` 与 `when` 的年份一致性，'
           '口径从「全部 2–4 位数字」（47 项）收窄到「仅四位年」（14 项），**逐条人工判读后 14 项全部合理**——'
           '要么是正文必须交代的**语境年份**（透纳 1819 意大利之行、刚果十字架 1491 改宗、纳瓦霍 1540 西班牙人入西南、'
           '1860s Bosque Redondo、霍皮 1500s 西班牙原型），要么是**馆藏号误伤**（1981.3、1972.1054）与艺人年（1928—1998）。'
           '这已是**第三次**在同一处折戟（Cycle57 的 when↔正文、更早的 when↔body）。结论：**「年份集合包含」在本语料上不是有效不变量**，'
           '原因是这个知识库的正文本来就要写大量他指年份。决定**停止投入**，只保留两条真正可工作的校验：'
           '机构记录 ↔ 正文尺寸/年代（36/36）与 R21 表述规范；本脚本降级为**离线咨询工具**，不接入体检以免制造假警报。'
           '（`def`/`overview` 空字段与复制粘贴两项为 0 问题。）")\n')
    anchor='if cyc=="cycle65":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])