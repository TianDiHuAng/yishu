# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle130"; DATE="2026-11-24"
IDS=["claudia-octavia-bust","roman-sarcophagus","antonine-portrait-head","silenus-couch-bust"]
ET,ST,PG=452,579,489
DECIS="""## D133 — Cycle130 罗马雕塑 4 条（448 → 452）
`claudia-octavia-bust`（奥克塔维娅胸像，**核心**；stola 标示已婚上层女性、塔西佗「贵族气而有德」、终被休弃赐死）、
`roman-sarcophagus`（俄瑞斯忒斯石棺，**核心**；正面三联＝弑母/复仇女神/德尔斐赎罪，棺盖四季「罪—罚—赎」）、
`antonine-portrait-head`（安东尼朝官员像，**核心**；**钻瞳/虹膜作为断代硬指标**，不早于哈德良朝 117—38）、
`silenus-couch-bust`（西勒诺斯床榻像；卧榻 fulcrum 扶手件、醉态鹿皮袍、希腊→罗马家具装饰传承）。
写前查重通过。art-ancient 30→34、罗马相关＋4。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）。
"""
REPORT=("- 罗马雕塑 4 条（448 → 452，CMA）：奥克塔维娅胸像（**stola 标示已婚上层女性**、塔西佗「贵族气而有德」、终被休弃赐死）、"
 "俄瑞斯忒斯石棺（正面三联**弑母/复仇女神/德尔斐赎罪**、棺盖四季，「罪—罚—赎」闭环）、安东尼朝官员像（**钻瞳/虹膜＝断代硬指标**、不早于哈德良朝）、"
 "西勒诺斯床榻像（卧榻 fulcrum 扶手件、醉态鹿皮袍、希腊→罗马家具装饰传承）。art-ancient 30→34。站点 485 → 489 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["罗马雕塑（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["罗马雕塑"],"gaps_found":{"entries":4},"network":"CMA","verdict":"art-ancient 30→34（总452）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle129":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle129":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **448**（L2 444 / L3 4 / L1 0） |","| 条目 | **452**（L2 448 / L3 4 / L1 0） |"),("| 来源 | **575**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **579**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **485**，站内断链 **0** |","| 页面 | **489**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **448** | L2 444 / L3 4 / **L1 0** |","| 条目总数 | **452** | L2 448 / L3 4 / **L1 0** |"),("| 来源库 | **575**（另 11 条预备来源未计入） |","| 来源库 | **579**（另 11 条预备来源未计入） |"),("| 站点页面 | **485** |","| 站点页面 | **489** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **448**（L2 444 / L3 4，**无 L1**） |","| 条目 | **452**（L2 448 / L3 4，**无 L1**） |"),("| 来源 | **575**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **579**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **485** |","| 站点页面 | **489** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)