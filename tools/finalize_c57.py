# -*- coding: utf-8 -*-
"""Cycle57 收尾：D061 + METRICS/SATURATION/REPORT。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D061 — Cycle57 `when` 抽查：**放弃一个坏启发式**，改用一条结构性硬规则 R21
- **原计划**：核对 `when` 与正文年份是否自洽。**实现后立刻失效**：全库 200 条中 55 条被标"需复核"、41 条"重点"，逐条看下去几乎全是**设计性误报**：
  1. **馆藏号被当成年代**：`1918`、`1043`、`1979`、`1962`、`328` 等来自「藏（1918.328）」这类上下文；
  2. **人物条目的 `when` 是生卒年**（如 1834—1917），而正文必然出现老师、作品、展览的年份（1853、1863、1874…）——这是**正常**的，不是矛盾；
  3. **流派条目的 `when` 是风格存续期**（约1870—1890），正文出现该流派的具体展览年份亦属正常。
  → 结论：**「年份集合包含关系」不是可用的不变量**。此路放弃，并在本条记录原因，避免后人重复踩坑。
- **改为结构性检查（R21）**：`when` 字段**不得含拉丁字母**（本站统一中文表述）。据此发现并修正 **6 条**：`约1940s—1950s` → `约1940年代—1950年代`；`约1950s—1970s`、`约1960s—1970s`、`约1960s—至今` 同理；`early 1830s（系列作于1829—1833年）` → `1830年代初（…）`；`热释光测年 20—620 CE` → `热释光测年 公元20—620年`。
- **顺带核对**：另有 10 条 `when` 长度 <3（`历代`、`汉代`），逐一查看后确认**合法**（术语条目如写意、工笔、隶书本就跨朝代），不属缺陷。
- **验证**：R21 **注入测试**——把 `pop-art` 的 when 改成 `约1950s` 并写入 `site_entries.json` → `[R21] pop-art: when 含拉丁字母`，还原后 errors=0。（第一次注入错误地改了 `entries.json`，而 check 读的是 `site_entries.json`，故未触发——**注入测试本身也要确认数据源**。）
- **可逆方式**：删除 R21 与 6 条 when 的规范化。
- **代价**：`when` 表述统一为中文，英文材料原文（如 `early 1830s`）改置于正文说明。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle57","date":"2026-11-23","status":"completed",
 "gap_methods":["when 字段抽查（先启发式后结构性）"],"network":"partial",
 "new_entries":0,"fixes":6,
 "abandoned_heuristic":{"name":"when 与正文年份集合包含关系","false_positives":"55 命中中 41 为设计性误报",
   "causes":["馆藏号被当年代(1918/1043/1979)","人物生卒 vs 事件年份","流派存续期 vs 展览年份"]},
 "new_rule":"R21 when 不得含拉丁字母（注入测试通过）",
 "normalized":["约1940s→约1940年代","约1950s→约1950年代","约1960s→约1960年代","early 1830s→1830年代初","20—620 CE→公元20—620年"],
 "false_alarm_avoided":"10 条 when 长度<3（历代/汉代）为合法，未改",
 "checks_r":21,"entries_total":200,"sources_total":331,"pages":235,
 "check_result":"errors=0","check_links_result":"broken=0(235页)","audit_all":"10/10 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle57","date":"2026-11-23","methods_used":["when 抽查"],
 "gaps_found":{"when_formatting":6},"network":"partial",
 "verdict":"弃用坏启发式，改立 R21；6 条 when 规范化；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle57"' not in t:
    block=('if cyc=="cycle57":\n'
           '    L.append("- 本轮**放弃了一个坏启发式**：原想核对「when 与正文年份自洽」，实现后 200 条里 55 条被标、41 条「重点」，'
           '逐条看几乎全是**设计性误报**——馆藏号（1918/1043/1979）被当成年代、人物 `when` 是生卒年而正文必有师承与作品年份、'
           '流派 `when` 是存续期而正文必有展览年份。结论：**年份集合包含关系不是可用的不变量**，此路放弃并记入 D061。'
           '改用**结构性硬规则 R21**：`when` 不得含拉丁字母 → 修正 **6 条**（约1940s→1940年代、early 1830s→1830年代初、'
           '20—620 CE→公元20—620年 等）；另有 10 条长度<3（历代/汉代）经核为**合法**，未动。'
           'R21 经注入测试（改 site_entries 后报错、还原后 0 错误）——顺带发现**第一次注入改错数据源**（entries.json 而非 site_entries.json）。'
           '硬规则增至 **R1–R21**，站点 235 页，体检 10/10。")\n')
    anchor='if cyc=="cycle56":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])