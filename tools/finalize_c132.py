# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle132"; DATE="2026-11-24"
IDS=["daniel-lions-relief","byzantine-ivory-plaque","ottonian-mission-apostles","lion-basilisk-capital"]
ET,ST,PG=460,587,497
DECIS="""## D135 — Cycle132 中世纪 4 条（456 → 460）
`daniel-lions-relief`（但以理狮坑柱头，**核心**；信仰得救叙事＋圣艾尼昂教堂建筑语境）、
`byzantine-ivory-plaque`（拜占庭「斯特罗加诺夫」象牙，**核心**；宝座圣母可溯6世纪、超自然孩童＝道成肉身）、
`ottonian-mission-apostles`（奥托差遣使徒板，**核心**；基督持书、或原为福音书封中央装饰＝媒介自指）、
`lion-basilisk-capital`（狮与蛇怪柱头；蛇怪半鸡半蛇、一瞥致死、魔鬼象征为基督践踏）。
`art-medieval` 14→18。写前查重通过。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）。
"""
REPORT=("- 中世纪 4 条（456 → 460，CMA）：但以理狮坑柱头（信仰得救叙事＋圣艾尼昂教堂建筑语境）、拜占庭「斯特罗加诺夫」象牙"
 "（宝座圣母可溯6世纪、**超自然孩童＝道成肉身**）、奥托差遣使徒板（基督持书、或原为**福音书封**中央饰＝媒介自指）、"
 "狮与蛇怪柱头（蛇怪半鸡半蛇、一瞥致死、**魔鬼象征为基督践踏**）。art-medieval 14→18。站点 493 → 497 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["中世纪（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["中世纪"],"gaps_found":{"entries":4},"network":"CMA","verdict":"art-medieval 14→18（总460）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle131":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle131":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **456**（L2 452 / L3 4 / L1 0） |","| 条目 | **460**（L2 456 / L3 4 / L1 0） |"),("| 来源 | **583**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **587**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **493**，站内断链 **0** |","| 页面 | **497**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **456** | L2 452 / L3 4 / **L1 0** |","| 条目总数 | **460** | L2 456 / L3 4 / **L1 0** |"),("| 来源库 | **583**（另 11 条预备来源未计入） |","| 来源库 | **587**（另 11 条预备来源未计入） |"),("| 站点页面 | **493** |","| 站点页面 | **497** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **456**（L2 452 / L3 4，**无 L1**） |","| 条目 | **460**（L2 456 / L3 4，**无 L1**） |"),("| 来源 | **583**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **587**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **493** |","| 站点页面 | **497** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)