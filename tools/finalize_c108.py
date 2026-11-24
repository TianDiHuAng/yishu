# -*- coding: utf-8 -*-
"""Cycle108 收尾：D111 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D111 — Cycle108 V&A 再补 4 条（368 → 372；日版画＋伊斯兰金属/釉砖）
新增 `hiroshige-satta-sea`（广重《骏河萨埵海》，1858，**核心**）、`hokusai-kingfisher-print`（北斋《翠鸟·鸢尾·石竹》，约1834，**核心**）、
`mamluk-inlaid-basin`（马穆鲁克错金银铜盆，约1250—1350，**核心**）、`iznik-tile-panel-edirne`（伊兹尼克六砖板，1570—74，**核心**）。
四处要点：①日本版画是**画师/雕版师/印工依出版商指令分工**的**商业产品**，本幅以**巨浪＋富士**构图；
②北斋花鸟画以**静态花鸟＋汉诗/和歌**显中国影响，属**中判**；
③马穆鲁克铜盆以**苏卢斯铭＋骑者/月神圆章**构成整饰系统，错金银；
④伊兹尼克六砖板原为**龛形板顶部**，或装**埃迪尔内皇宫**，是**建筑表皮单元**而非独立画。
**如实保留资料截断**：广重（「19世纪日本…」）、伊兹尼克（「显示了…」）两处 V&A 说明**截断，未补写**。
**QC** 未单跑（尺寸已在正文按 Height/Width 精确写出）；audit 12/12、check errors=0、links 0。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条 V&A 来源。
代价：均单一机构（V&A）；日本版画与伊斯兰金属/釉砖由此具象化，仍属点状。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle108","date":"2026-11-24","status":"completed",
 "gap_methods":["V&A：日本版画+伊斯兰金属/釉砖"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":["hiroshige-satta-sea","hokusai-kingfisher-print","mamluk-inlaid-basin","iznik-tile-panel-edirne"],
 "new_sources":4,"sources_total":501,"entries_total":372,"pages":409,
 "check_result":"errors=0","check_links_result":"broken=0(409页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle108","date":"2026-11-24","methods_used":["V&A 日本版画/伊斯兰装饰艺术"],
 "gaps_found":{"entries":4},"network":"V&A 200","verdict":"总372；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle108"' not in t:
    block=('if cyc=="cycle108":\n'
           '    L.append("- V&A 再补 4 条（368 → 372）：广重《骏河萨埵海》（1858）、北斋《翠鸟·鸢尾·石竹》（约1834）、马穆鲁克错金银铜盆、伊兹尼克六砖板。'
           '①日本版画是**画师/雕版/印工依出版商指令分工**的商业产品，本幅以**巨浪＋富士**构图；②北斋花鸟以**静态花鸟＋汉诗/和歌**显中国影响（中判）；'
           '③马穆鲁克铜盆以**苏卢斯铭＋骑者/月神圆章**整饰、错金银；④伊兹尼克砖板原为**龛形板顶部**、或装**埃迪尔内皇宫**、为**建筑表皮单元**。'
           '**如实保留两处资料截断**（广重「19世纪日本…」、伊兹尼克「显示了…」）。站点 405 → 409 页，体检 12/12。")\n')
    anchor='if cyc=="cycle107":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **368**（L2 364 / L3 4 / L1 0） |","| 条目 | **372**（L2 368 / L3 4 / L1 0） |"),
    ("| 来源 | **497**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **501**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **405**，站内断链 **0** |","| 页面 | **409**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **368** | L2 364 / L3 4 / **L1 0** |","| 条目总数 | **372** | L2 368 / L3 4 / **L1 0** |"),
    ("| 来源库 | **497**（另 11 条预备来源未计入） |","| 来源库 | **501**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **405** |","| 站点页面 | **409** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **368**（L2 364 / L3 4，**无 L1**） |","| 条目 | **372**（L2 368 / L3 4，**无 L1**） |"),
    ("| 来源 | **497**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **501**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **405** |","| 站点页面 | **409** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])