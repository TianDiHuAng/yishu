# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle140"; DATE="2026-11-24"
IDS=["female-saint-canopy-glass","st-stephen-glass-1230","st-peter-preaching-glass","adoration-magi-window-1516"]
ET,ST,PG=488,614,525
DECIS="""## D143 — Cycle140 中世纪彩绘玻璃 4 条（484 → 488；补彩窗类型）
`female-saint-canopy-glass`（华盖下女圣徒，1325–50，**核心**；华盖＝圣徒「位阶装置」）、
`st-stephen-glass-1230`（圣司提反受审，约1230–40，**核心**；原属库唐斯主教座堂大窗、残件反推整体）、
`st-peter-preaching-glass`（圣彼得布道，约1525–30，**核心**；主保圣人组窗＝教堂自我叙述）、
`adoration-magi-window-1516`（三王来拜，1516，**核心**；Marcillat 法国技艺→意大利工坊，技术转移）。
art-medieval 18→22。**自查**：overlay 一处节名误作「关系与争论」→ 构建前修正。
**如实保留截断**：三王来拜 summary 在希律处未补写。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（V&A）。
"""
REPORT=("- 中世纪彩绘玻璃 4 条（484 → 488，V&A）：华盖下女圣徒（华盖＝**圣徒位阶装置**）、圣司提反受审（原属**库唐斯**大窗、残件反推整体）、"
 "圣彼得布道（**主保圣人组窗＝教堂自我叙述**）、三王来拜（Marcillat 把**法国彩窗技艺**带入意大利、工坊学徒扩散＝技术转移）。"
 "一处 overlay 节名误写构建前已修正；三王来拜 summary 截断未补写。art-medieval 18→22。站点 521 → 525 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["中世纪彩窗（V&A）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["中世纪彩窗"],"gaps_found":{"entries":4},"network":"V&A","verdict":"art-medieval 18→22（总488）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle139":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle139":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **484**（L2 480 / L3 4 / L1 0） |","| 条目 | **488**（L2 484 / L3 4 / L1 0） |"),("| 来源 | **610**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **614**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **521**，站内断链 **0** |","| 页面 | **525**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **484** | L2 480 / L3 4 / **L1 0** |","| 条目总数 | **488** | L2 484 / L3 4 / **L1 0** |"),("| 来源库 | **610**（另 11 条预备来源未计入） |","| 来源库 | **614**（另 11 条预备来源未计入） |"),("| 站点页面 | **521** |","| 站点页面 | **525** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **484**（L2 480 / L3 4，**无 L1**） |","| 条目 | **488**（L2 484 / L3 4，**无 L1**） |"),("| 来源 | **610**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **614**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **521** |","| 站点页面 | **525** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)