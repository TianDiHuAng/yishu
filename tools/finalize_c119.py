# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle119"; DATE="2026-11-24"
IDS=["ilkhanid-flying-birds-bowl","canopic-jar-26","amenemhat-statue","minemheb-statue"]
ET,ST,PG=412,540,449
DECIS="""## D122 — Cycle119 埃及/伊斯兰 4 条（408 → 412）
`ilkhanid-flying-birds-bowl`（伊尔汗飞鸟碗，1280—1400，**核心**；中国母题入波斯、凤=simurgh、中亚至埃及外销/仿制）、
`canopic-jar-26`（26王朝卡诺普罐，**核心**；荷鲁斯四子器官配对，豺头 Duamutef 护胃）、
`amenemhat-statue`（阿门涅姆赫特三世像，**核心**；无铭凭面容鉴定、超大双耳=听愿、双手平贴护肢）、
`minemheb-statue`（米奈赫布像，**核心**；像中像跪捧狒狒托特，营建首长衔=功绩碑）。
**写前查重**通过。埃及 6→10、伊斯兰 25→29、古代 26→30。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）。
"""
REPORT=("- 埃及/伊斯兰 4 条（408 → 412，CMA）：伊尔汗飞鸟碗（中国母题入波斯，凤=simurgh，中亚至埃及外销/仿制）、"
 "26王朝卡诺普罐（荷鲁斯四子器官配对、豺头=Duamutef 护胃）、阿门涅姆赫特三世像（无铭凭面容鉴定、超大双耳=听愿、双手平贴护肢）、"
 "米奈赫布像（**像中像**跪捧狒狒托特、「庆典神庙营建首长」衔=功绩碑）。埃及 6→10、古代 26→30。站点 445 → 449 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["埃及/伊斯兰（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["埃及/伊斯兰"],"gaps_found":{"entries":4},"network":"CMA","verdict":"总412；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle118":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle118":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **408**（L2 404 / L3 4 / L1 0） |","| 条目 | **412**（L2 408 / L3 4 / L1 0） |"),("| 来源 | **537**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **540**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **445**，站内断链 **0** |","| 页面 | **449**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **408** | L2 404 / L3 4 / **L1 0** |","| 条目总数 | **412** | L2 408 / L3 4 / **L1 0** |"),("| 来源库 | **537**（另 11 条预备来源未计入） |","| 来源库 | **540**（另 11 条预备来源未计入） |"),("| 站点页面 | **445** |","| 站点页面 | **449** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **408**（L2 404 / L3 4，**无 L1**） |","| 条目 | **412**（L2 408 / L3 4，**无 L1**） |"),("| 来源 | **537**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **540**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **445** |","| 站点页面 | **449** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)