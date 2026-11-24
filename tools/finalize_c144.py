# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle144"; DATE="2026-11-24"
IDS=["utamaro-plum-blind","kunisada-dressing-room","hiroshige-sumida-snow","hokusai-36views"]
ET,ST,PG=504,630,541
DECIS="""## D147 — Cycle144 浮世绘 4 条（500 → 504）
`utamaro-plum-blind`（歌麿摺物，1790s末，**核心**；私人订制＋女性心理、琴后神情；无尺寸）、
`kunisada-dressing-room`（国贞后台三联右幅，1820s初，**核心**；道顿堀剧场、全男班、跨城巡演、两层建筑）、
`hiroshige-sumida-snow`（广重隅田雪团扇绘，1843—47，**核心**；atozuri 后印的印次质量）、
`hokusai-36views`（北斋富岳三十六景·巨浪，约1831，**核心**；蓝摺绘、**首个纯大判风景系列**）。
art-asia 内浮世绘群扩充。**如实**：O71806 无尺寸/desc 截断；多处 summary 截断均未补写。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（V&A）。
"""
REPORT=("- 浮世绘 4 条（500 → 504，V&A）：歌麿摺物（**私人订制＋女性心理**、琴后神情；无尺寸）、国贞后台三联右幅（道顿堀剧场、**全男班**、跨城巡演、两层建筑）、"
 "广重隅田雪团扇绘（**atozuri 后印的印次质量**）、北斋富岳三十六景·巨浪（蓝摺绘、**首个纯大判风景系列**）。多处截断未补写。"
 "站点 537 → 541 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["浮世绘（V&A）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["浮世绘"],"gaps_found":{"entries":4},"network":"V&A","verdict":"总504；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle143":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle143":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **500**（L2 496 / L3 4 / L1 0） |","| 条目 | **504**（L2 500 / L3 4 / L1 0） |"),("| 来源 | **626**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **630**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **537**，站内断链 **0** |","| 页面 | **541**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **500** | L2 496 / L3 4 / **L1 0** |","| 条目总数 | **504** | L2 500 / L3 4 / **L1 0** |"),("| 来源库 | **626**（另 11 条预备来源未计入） |","| 来源库 | **630**（另 11 条预备来源未计入） |"),("| 站点页面 | **537** |","| 站点页面 | **541** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **500**（L2 496 / L3 4，**无 L1**） |","| 条目 | **504**（L2 500 / L3 4，**无 L1**） |"),("| 来源 | **626**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **630**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **537** |","| 站点页面 | **541** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)