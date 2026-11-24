# -*- coding: utf-8 -*-
"""Cycle101 收尾：D104（199条全量复核 0 问题 + 修校验器世纪换算）。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D104 — Cycle101 全量复核（199 条机构来源）0 问题；修校验器「世纪换算」两处误报
- **背景**：条目已达 344，其中 **199 条**带机构 API 记录。用已修好的 `qc_sample_c56.py` 做**全量**复核（`QC_ALL=1`）。
- **结果**：**受检 199 条、尺寸核对 139 项、命中 139 项、问题 0**。本轮**无真实数据错误**——如实记录。
- **两处校验器误报（均是「1100s ↔ 12世纪」等价问题）**：
  1. 记录 `creation_date="1100s"` 提取年份 `1100`，而条目正文写「12世纪」，字面不匹配 → 误报 3 条（kofukuji/khmer-naga/burmese）。
  2. 修法：把年份同时换算为**两种世纪写法**（`n//100` 与 `n//100+1`）作为候选——`1100`→「11世纪/12世纪」，`1250`→「12世纪/13世纪」，覆盖博物馆「NN00s＝下一世纪」的惯用义，同时不误伤严格纪年。
- **意义**：这是本会话**第三次**「先修工具再信结论」（前两次 D058 汇总行、D082 尺寸提取）。不改工具则本轮会虚报 3 条年代不符。
- **可逆方式**：纯工具改动，无数据变更。
- **代价**：`qc_sample_c56.py` 仍为**按需联网**工具，不进离线体检；世纪候选放宽到两种写法，理论上可能漏掉极个别真错，但配合 R2/R3 硬规则可兜底。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle101","date":"2026-11-24","status":"completed",
 "gap_methods":["344 条中 199 条机构来源全量复核"],"network":"partial: museum APIs ok",
 "new_entries":0,"fixes":1,
 "qc":{"entries_checked":199,"dim_checks":139,"dim_hits":139,"issues":0},
 "checker_fix":"世纪换算（NN00s→下一世纪）两种候选，消除 3 处误报",
 "entries_total":344,"sources_total":473,"pages":381,
 "check_result":"errors=0","check_links_result":"broken=0(381页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle101","date":"2026-11-24","methods_used":["全量机构来源复核"],
 "gaps_found":{},"network":"partial (museum APIs)",
 "verdict":"199 条全量复核：139/139 命中、0 真问题；修校验器世纪换算；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle101"' not in t:
    block=('if cyc=="cycle101":\n'
           '    L.append("- **全量复核**：344 条中 **199 条机构来源**逐条重抓记录，**尺寸核对 139 项、139 项命中、0 真问题**（本轮无真实错误，如实记录）。'
           '修校验器**两处世纪换算误报**：记录 `1100s` 提取 `1100` 而正文写「12世纪」不匹配——改为对年份同时给出**两种世纪写法**'
           '（`n//100` 与 `n//100+1`），覆盖博物馆「NN00s＝下一世纪」的惯用义。这是本会话**第三次**「先修工具再信结论」'
           '（前两次 D058 汇总行、D082 尺寸提取）。站点仍 381 页，体检 12/12。")\n')
    anchor='if cyc=="cycle100":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])