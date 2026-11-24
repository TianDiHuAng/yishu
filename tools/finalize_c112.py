# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle112"; DATE="2026-11-24"
IDS=["malinke-helmet-mask","gambanda-female-mask","nkishi-power-figure","bwa-buffalo-mask"]
ET,ST,PG=388,517,425
NOTE="非洲面具/灵力像 4 条（CMA）"
DECIS="""## D115 — Cycle112 非洲再补 4 条（384 → 388）
以 CMA（描述更实）补 `art-africa`：`malinke-helmet-mask`（马林凯 suruku 盔面具，1800s中后，**核心**）、`gambanda-female-mask`（彭德 gambanda 女面具，1900s初，**核心**）、`nkishi-power-figure`（卢巴 mankishi 灵力像，19—20世纪，**核心**）、`bwa-buffalo-mask`（布瓦水牛面具，20世纪，**核心**）。
要点：①suruku 属 **Korè 会社**（源自巴姆巴拉），用于**割礼/成人礼**，或为会社等级标识；②gambanda 为**酋长之妻**，依彭德面相观表**理想女子**，发式为**数百小辫**，雕刻家**世袭、村外作业**；③nkishi 的**布覆颅腔藏物**示其为 **mankishi 灵力物**，多由**仪式专家**雕刻、用于治疗/护佑/占卜/裁断；④布瓦水牛面具表**护佑灌木精灵**，旱季用于成人礼/长老葬礼/集市/丰收/年度更新。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）；非洲 24→28 条。
"""
REPORT=("- 非洲再补 4 条（384 → 388，CMA）：马林凯 suruku 盔面具、彭德 gambanda 女面具、卢巴 nkishi 灵力像、布瓦水牛面具。"
 "①suruku 属 **Korè 会社**、用于**割礼/成人礼**；②gambanda 表**酋长之妻·理想女子**、**数百小辫**、雕刻家**世袭村外作业**；"
 "③nkishi **布覆颅腔藏物**示为 **mankishi 灵力物**、多由**仪式专家**雕、用于治疗/占卜/裁断；④布瓦水牛表**护佑灌木精灵**、旱季仪式起舞。"
 "站点 421 → 425 页，体检 12/12。")
# docs
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["非洲面具/灵力像（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["非洲（CMA）"],"gaps_found":{"entries":4},"network":"CMA","verdict":"非洲 24→28（总388）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    block=('if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT))
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle111":', block+'if cyc=="cycle111":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **384**（L2 380 / L3 4 / L1 0） |","| 条目 | **388**（L2 384 / L3 4 / L1 0） |"),("| 来源 | **513**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **517**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **421**，站内断链 **0** |","| 页面 | **425**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **384** | L2 380 / L3 4 / **L1 0** |","| 条目总数 | **388** | L2 384 / L3 4 / **L1 0** |"),("| 来源库 | **513**（另 11 条预备来源未计入） |","| 来源库 | **517**（另 11 条预备来源未计入） |"),("| 站点页面 | **421** |","| 站点页面 | **425** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **384**（L2 380 / L3 4，**无 L1**） |","| 条目 | **388**（L2 384 / L3 4，**无 L1**） |"),("| 来源 | **513**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **517**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **421** |","| 站点页面 | **425** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)