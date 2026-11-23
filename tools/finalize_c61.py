# -*- coding: utf-8 -*-
"""Cycle61 收尾：D065 + METRICS/SATURATION/REPORT。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D065 — Cycle61 表格窄屏溢出：215 个表格统一包裹可滚动容器（并立检查防回归）
- **事实**：全站 **215 个表格**（分布 211 页）**都没有横向滚动容器**；CSS 只有 `table{width:100%}`。其中 `sources.html` 的表有 **7 列**、单元格文字最长 **113 字符**，条目页来源表 **5 列**且含长 URL——窄屏下必然挤压或溢出。
- **决定（三步）**：
  1. `gen_site.py` 增加**生成后处理** `postprocess_tables()`：把每个 `<table>…</table>` 包进 `<div class='table-wrap'>`，幂等（已包裹则跳过）；本次覆盖 **211 页 / 215 个表格**。
  2. CSS 增补：`.table-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch}`、`th,td{word-break:break-word;overflow-wrap:anywhere}`（长 URL 可断）。
  3. `usability_c60.py` **新增第 9 项检查**：`<table>` 数不得超过 `class='table-wrap'` 数。
- **验证**：修后 `表格 215 ｜包裹 215`、可用性问题 0；**注入测试**——手工去掉 `sources.html` 的一个包裹 → 报 `unwrapped_table 1 例 ['sources.html']` 且 **rc=1**；还原 → **rc=0**。
- **两个实现坑（记下来）**：
  1. 首次插入调用因判断条件写成 `if "postprocess_tables()" not in s` 而被**函数定义本身**命中，调用没插上（生成后看不到「表格容器包裹」那行才发现）——改为以 `_wrapped=` 作标记；
  2. 后处理的正则用了 `(?<!<div …>)` 前瞻否定，第二次运行仍重复包裹，改为**按页内含 `class='table-wrap'` 即整页跳过**（幂等更可靠）。
- **可逆方式**：删除 `postprocess_tables()` 与两条 CSS，回退可用性第 9 项。
- **代价**：每页多一层 div；页面体积略增（约每表 +34 字节）。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle61","date":"2026-11-23","status":"completed",
 "gap_methods":["窄屏溢出审计（表格）"],"network":"partial",
 "new_entries":0,"fixes":3,
 "tables":{"total":215,"pages":211,"wrapped_after":215,"max_cols":7,"longest_cell":113},
 "fixes_detail":["gen_site 后处理包裹 .table-wrap（幂等）","CSS overflow-x:auto + word-break","usability 新增 unwrapped_table 检查"],
 "guard_test":"去包裹 → rc=1；还原 → rc=0",
 "impl_pitfalls":["调用插入条件被函数定义命中","正则前瞻失败导致重复包裹→改为整页跳过"],
 "entries_total":208,"sources_total":339,"pages":243,
 "check_result":"errors=0","check_links_result":"broken=0(243页)","audit_all":"11/11 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle61","date":"2026-11-23","methods_used":["表格溢出审计"],
 "gaps_found":{"unwrapped_tables":215},"network":"partial",
 "verdict":"215 表统一包裹 + 断词；新增检查；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle61"' not in t:
    block=('if cyc=="cycle61":\n'
           '    L.append("- 接着查**窄屏溢出**：全站 **215 个表格（211 页）都没有横向滚动容器**，'
           '`sources.html` 更是 **7 列、单元格最长 113 字符**，条目页来源表 5 列且含长 URL——窄屏必挤压。'
           '修法三步：`gen_site` 增加**生成后处理**把每个表格包进 `.table-wrap`（幂等，本次覆盖 211 页/215 表）；'
           'CSS 加 `overflow-x:auto` 与 `word-break`；可用性审计**新增第 9 项**（表数不得多于包裹数）。'
           '注入测试：去掉 `sources.html` 一个包裹 → 报 `unwrapped_table` 且 rc=1，还原 rc=0。'
           '两个实现坑也记了：调用插入条件被**函数定义自身**命中导致没插上；正则前瞻不幂等导致重复包裹。站点 243 页，体检 11/11。")\n')
    anchor='if cyc=="cycle60":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])