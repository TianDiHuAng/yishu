# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle142"; DATE="2026-11-24"
IDS=["polonaise-carpet","salting-carpet","chelsea-carpet","cairo-court-carpet"]
ET,ST,PG=496,622,533
DECIS="""## D145 — Cycle142 伊斯兰地毯 4 条（492 → 496）
`polonaise-carpet`（『波兰式』毯，1600—25，**核心**；实为伊朗制、误名＝流通史化石、近纳杰夫神祠毯）、
`salting-carpet`（萨尔廷毯，1560—80，**核心**；团花云带＋哈菲兹边诗＋夜莺＝诗入毯）、
`chelsea-carpet`（切尔西毯，1500—50，**核心**；无铭断代、与书籍艺术类比）、
`cairo-court-carpet`（开罗奥斯曼宫廷毯，1525—50，**核心**；六片缝合的完整性假象＋21相关碎片散藏）。
art-islamic 37→41。**自查**：polonaise 曾误写「克利夫兰藏」，构建前改为 V&A。
**如实保留截断**：polonaise「Many were found…」、chelsea「medallion…」未补写。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（V&A）。
"""
REPORT=("- 伊斯兰地毯 4 条（492 → 496，V&A）：『波兰式』毯（**实为伊朗制、误名＝流通化石**、近纳杰夫神祠毯）、萨尔廷毯（团花云带＋**哈菲兹边诗**＋夜莺＝**诗入毯**）、"
 "切尔西毯（**无铭断代**、与书籍艺术类比）、开罗宫廷毯（**六片缝合的完整性假象**＋**21相关碎片散藏**）。"
 "构建前修正 polonaise 藏地误写。art-islamic 37→41。站点 529 → 533 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["伊斯兰地毯（V&A）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["伊斯兰地毯"],"gaps_found":{"entries":4},"network":"V&A","verdict":"art-islamic 37→41（总496）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle141":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle141":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **492**（L2 488 / L3 4 / L1 0） |","| 条目 | **496**（L2 492 / L3 4 / L1 0） |"),("| 来源 | **618**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **622**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **529**，站内断链 **0** |","| 页面 | **533**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **492** | L2 488 / L3 4 / **L1 0** |","| 条目总数 | **496** | L2 492 / L3 4 / **L1 0** |"),("| 来源库 | **618**（另 11 条预备来源未计入） |","| 来源库 | **622**（另 11 条预备来源未计入） |"),("| 站点页面 | **529** |","| 站点页面 | **533** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **492**（L2 488 / L3 4，**无 L1**） |","| 条目 | **496**（L2 492 / L3 4，**无 L1**） |"),("| 来源 | **618**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **622**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **529** |","| 站点页面 | **533** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)