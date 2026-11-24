# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle143"; DATE="2026-11-24"
IDS=["gaur-tile-panel","iran-mihrab-1307","iznik-stele-1560","isfahan-tile-1450"]
ET,ST,PG=500,626,537
DECIS="""## D146 — Cycle143 伊斯兰釉砖 4 条（496 → 500；**达到 500 条目**）
`gaur-tile-panel`（孟加拉高尔釉砖板，**核心**；自废墟取出后**任意拼合**、拟屋正面＝展示产物）、
`iran-mihrab-1307`（伊朗米哈拉布残段，1307，**核心**；龛形＋浮雕阿铭＋描金珐琅）、
`iznik-stele-1560`（伊兹尼克立碑砖，**核心**；双面花饰、1550s 确立配色，**「谜样」用途未明不臆测**）、
`isfahan-tile-1450`（伊斯法罕马赛克砖，**核心**；**裁切拼装＋六色单元**、莲纹蒙古征服后传入）。
art-islamic 41→45。**如实保留截断/无 summary**：O82264/O86037 无 summary，O86037 来源句、O85357 中央纹处截断，均未补写。
**500 是数量里程碑，不等于覆盖均衡**；未写 ALL_DONE，饱和见 SATURATION.json（仍 false）。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（V&A）。
"""
REPORT=("- 伊斯兰釉砖 4 条（496 → **500**，V&A）：孟加拉**高尔砖板**（废墟取出后**任意拼合**＝展示产物）、伊朗**米哈拉布残段**（1307；浮雕阿铭＋描金）、"
 "**伊兹尼克立碑砖**（双面花饰、1550s 配色，「谜样」用途未明不臆测）、**伊斯法罕马赛克砖**（裁切拼装＋六色单元、莲纹蒙古征服后传入）。"
 "**达到 500 条目里程碑**（537 页）。O82264/O86037 无 summary；多处截断未补写。art-islamic 41→45。站点 533 → 537 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["伊斯兰釉砖（V&A）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"milestone":"500 entries","new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["伊斯兰釉砖"],"gaps_found":{"entries":4},"network":"V&A","verdict":"达到500条目；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle142":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle142":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **496**（L2 492 / L3 4 / L1 0） |","| 条目 | **500**（L2 496 / L3 4 / L1 0） |"),("| 来源 | **622**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **626**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **533**，站内断链 **0** |","| 页面 | **537**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **496** | L2 492 / L3 4 / **L1 0** |","| 条目总数 | **500** | L2 496 / L3 4 / **L1 0** |"),("| 来源库 | **622**（另 11 条预备来源未计入） |","| 来源库 | **626**（另 11 条预备来源未计入） |"),("| 站点页面 | **533** |","| 站点页面 | **537** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **496**（L2 492 / L3 4，**无 L1**） |","| 条目 | **500**（L2 496 / L3 4，**无 L1**） |"),("| 来源 | **622**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **626**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **533** |","| 站点页面 | **537** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)