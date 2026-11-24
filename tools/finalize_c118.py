# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle118"; DATE="2026-11-24"
IDS=["hevajra-buddhist","palanquin-hook-angkor","garuda-lintel-khmer","baphuon-kneeling-figure"]
ET,ST,PG=408,537,445
DECIS="""## D121 — Cycle118 东南亚再补 4 条（404 → 408）
`hevajra-buddhist`（喜金刚，约1200，**核心**；八面十六臂四腿，左持神右持兽，阇耶跋摩七世东门巨像线索）、
`palanquin-hook-angkor`（帕輿钩，1175—1230；伽楼多面钩端，环—座—杠复合装置）、
`garuda-lintel-khmer`（伽楼多楣饰，875—925，**核心**；按蛇尾+印度母题高棉化）、
`baphuon-kneeling-figure`（Baphuon 期跪像，1010—80；第三眼=信徒取神外观，五官原嵌银）。
**自查**：写 tuple 时发现 `garuda-lintel-khmer` 自引用，**构建前已修正**为 palanquin-hook-angkor（避免 R19 报错）。
**如实保留截断**：喜金刚「右手第八动物」句**截断未补写**；帕輿钩「虔敬与成功图像」句截断。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）；东南亚 4→8 条（Hevajra/輿钩/楣/跪像跨雕塑与金属器）。
"""
REPORT=("- 东南亚再补 4 条（404 → 408，CMA）：喜金刚（约1200）、帕輿钩（1175—1230）、伽楼多楣饰（875—925）、Baphuon 期跪像（1010—80）。"
 "①喜金刚**八面十六臂**、左持神右持兽，**阇耶跋摩七世东门巨像**见其仪式政治（第八动物句截断未补）；②帕輿钩为**环—座—杠**复合装置、钩端伽楼多面；"
 "③伽楼多楣饰**按蛇尾**、印度母题**高棉化**；④Baphuon 跪像**第三眼＝信徒取神外观**、五官原嵌银。"
 "构建前自查发现楣饰自引用并已修正。站点 441 → 445 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["东南亚续深（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"self_ref_fixed":"garuda-lintel-khmer 构建前修正自引用",
 "new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["东南亚续深"],"gaps_found":{"entries":4},"network":"CMA","verdict":"东南亚 8（总408）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle117":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle117":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **404**（L2 400 / L3 4 / L1 0） |","| 条目 | **408**（L2 404 / L3 4 / L1 0） |"),("| 来源 | **533**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **537**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **441**，站内断链 **0** |","| 页面 | **445**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **404** | L2 400 / L3 4 / **L1 0** |","| 条目总数 | **408** | L2 404 / L3 4 / **L1 0** |"),("| 来源库 | **533**（另 11 条预备来源未计入） |","| 来源库 | **537**（另 11 条预备来源未计入） |"),("| 站点页面 | **441** |","| 站点页面 | **445** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **404**（L2 400 / L3 4，**无 L1**） |","| 条目 | **408**（L2 404 / L3 4，**无 L1**） |"),("| 来源 | **533**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **537**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **441** |","| 站点页面 | **445** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)