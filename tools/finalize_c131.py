# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle131"; DATE="2026-11-24"
IDS=["qianlong-carved-lacquer-scrollbox","ming-side-table-everted","ming-lohan-armchairs","kang-table-dragons"]
ET,ST,PG=456,583,493
DECIS="""## D134 — Cycle131 中国家具/漆器 4 条（452 → 456）
`qianlong-carved-lacquer-scrollbox`（乾隆剔红龙纹卷轴盒，**核心**；五爪龙唯帝王、藏11位宠妃像、苏州承制、**1787造办处记录反证年代**）、
`ming-side-table-everted`（明式翘头案，**核心**；榫卯框架、云头角牙、翘头「正式化」或作供案）、
`ming-lohan-armchairs`（黄花梨圈背椅，**核心**；席地→高足、苏作极简、靠背七块木·榫卯源见河姆渡）、
`kang-table-dragons`（云龙纹炕桌，**核心**；火炕坐卧→炕桌尺度、南传木榻、明清用黄花梨）。
置于 `art-asia`（东亚，现含中国家具/漆器）。写前查重通过。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）。
"""
REPORT=("- 中国家具/漆器 4 条（452 → 456，CMA）：乾隆剔红龙纹卷轴盒（**五爪龙唯帝王**、藏11位宠妃像、苏州承制、**1787造办处记录反证年代**）、"
 "明式翘头案（**榫卯框架**、云头角牙、翘头「正式化」或作供案）、黄花梨圈背椅（席地→高足、**苏作极简**、靠背七块木·榫卯源见**河姆渡**）、"
 "云龙纹炕桌（**火炕坐卧→炕桌尺度**、南传木榻、明清用黄花梨）。站点 489 → 493 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["中国家具/漆器（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["中国家具/漆器"],"gaps_found":{"entries":4},"network":"CMA","verdict":"总456；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle130":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle130":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **452**（L2 448 / L3 4 / L1 0） |","| 条目 | **456**（L2 452 / L3 4 / L1 0） |"),("| 来源 | **579**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **583**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **489**，站内断链 **0** |","| 页面 | **493**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **452** | L2 448 / L3 4 / **L1 0** |","| 条目总数 | **456** | L2 452 / L3 4 / **L1 0** |"),("| 来源库 | **579**（另 11 条预备来源未计入） |","| 来源库 | **583**（另 11 条预备来源未计入） |"),("| 站点页面 | **489** |","| 站点页面 | **493** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **452**（L2 448 / L3 4，**无 L1**） |","| 条目 | **456**（L2 452 / L3 4，**无 L1**） |"),("| 来源 | **579**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **583**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **489** |","| 站点页面 | **493** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)