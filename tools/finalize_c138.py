# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle138"; DATE="2026-11-24"
IDS=["ming-jingdezhen-bowl-1450","doucai-stemcup-1465","kangxi-jar-lid-qing","armorial-porcelain-cup"]
ET,ST,PG=480,606,517
DECIS="""## D141 — Cycle138 中国瓷器 4 条（476 → 480）
`ming-jingdezhen-bowl-1450`（明青花婴戏碗，**核心**；婴戏＝多子寓意、据御窑瓷片断代）、
`doucai-stemcup-1465`（斗彩高足杯，**核心**；青花勾轮廓＋釉上填彩＋二次烧成）、
`kangxi-jar-lid-qing`（康熙青花盖罐；「ginger jar」流通命名 vs 本土容器/陈设）、
`armorial-porcelain-cup`（纹章瓷杯；盾徽＋「Le Grand」；**记录无 summary**，不补写历史）。
art-ceramics 12→16。写前查重通过。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（V&A）。
"""
REPORT=("- 中国瓷器 4 条（476 → 480，V&A）：明青花婴戏碗（**婴戏＝多子寓意**、据御窑瓷片断代）、斗彩高足杯（**青花勾轮廓＋釉上填彩＋二次烧成**）、"
 "康熙青花盖罐（**ginger jar** 流通命名 vs 本土容器/陈设）、纹章瓷杯（盾徽＋「Le Grand」；**记录无 summary，不补写**）。art-ceramics 12→16。"
 "站点 513 → 517 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["中国瓷器（V&A）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["中国瓷器"],"gaps_found":{"entries":4},"network":"V&A","verdict":"art-ceramics 12→16（总480）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle137":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle137":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **476**（L2 472 / L3 4 / L1 0） |","| 条目 | **480**（L2 476 / L3 4 / L1 0） |"),("| 来源 | **602**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **606**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **513**，站内断链 **0** |","| 页面 | **517**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **476** | L2 472 / L3 4 / **L1 0** |","| 条目总数 | **480** | L2 476 / L3 4 / **L1 0** |"),("| 来源库 | **602**（另 11 条预备来源未计入） |","| 来源库 | **606**（另 11 条预备来源未计入） |"),("| 站点页面 | **513** |","| 站点页面 | **517** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **476**（L2 472 / L3 4，**无 L1**） |","| 条目 | **480**（L2 476 / L3 4，**无 L1**） |"),("| 来源 | **602**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **606**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **513** |","| 站点页面 | **517** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)