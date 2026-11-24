# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle133"; DATE="2026-11-24"
IDS=["moche-sealion-pup","teotihuacan-mural-fragment","zapotec-seated-figure","aztec-seated-deity"]
ET,ST,PG=464,591,501
DECIS="""## D136 — Cycle133 美洲 4 条（460 → 464）
**查重发现**：候选 2005.6 即既有 `moche-bat-vessel`，遂改取**海狮幼崽瓶**(2014.375)。
新增：`moche-sealion-pup`（莫切海狮瓶，**核心**；胃石药性＋载亡者传说）、`teotihuacan-mural-fragment`（特奥蒂瓦坎壁画，500—550，**核心**；口卷＋奠酒＋龙舌兰刺＝献祭语义）、`zapotec-seated-figure`（萨波特克陪俑，**核心**；**历日象形13水/13燧刀**、身份之争）、`aztec-seated-deity`（阿兹特克坐神 Macuilxochitl?，**核心**；享乐神、**平民邻里小庙**）。
art-americas 36→40。写前查重（含同名对象）有效拦截一次重复。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）。
"""
REPORT=("- 美洲 4 条（460 → 464，CMA）：莫切海狮幼崽瓶（胃石药性＋载亡者传说）、特奥蒂瓦坎壁画残块（口卷＋奠酒＋**龙舌兰刺＝血与 pulque**）、"
 "萨波特克陪俑（**历日象形「13水/13燧刀」**、身份之争）、阿兹特克坐神 Macuilxochitl?（享乐神＋**平民邻里小庙**）。art-americas 36→40。"
 "**查重拦截**：候选 2005.6 即既有 moche-bat-vessel，改取海狮瓶 2014.375。站点 497 → 501 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["美洲（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"dup_caught":"2005.6=moche-bat-vessel，改取2014.375",
 "new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["美洲"],"gaps_found":{"entries":4},"network":"CMA","verdict":"art-americas 36→40（总464）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle132":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle132":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **460**（L2 456 / L3 4 / L1 0） |","| 条目 | **464**（L2 460 / L3 4 / L1 0） |"),("| 来源 | **587**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **591**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **497**，站内断链 **0** |","| 页面 | **501**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **460** | L2 456 / L3 4 / **L1 0** |","| 条目总数 | **464** | L2 460 / L3 4 / **L1 0** |"),("| 来源库 | **587**（另 11 条预备来源未计入） |","| 来源库 | **591**（另 11 条预备来源未计入） |"),("| 站点页面 | **497** |","| 站点页面 | **501** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **460**（L2 456 / L3 4，**无 L1**） |","| 条目 | **464**（L2 460 / L3 4，**无 L1**） |"),("| 来源 | **587**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **591**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **497** |","| 站点页面 | **501** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)