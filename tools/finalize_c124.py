# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle124"; DATE="2026-11-24"
IDS=["maya-battle-vessel-nebaj","maya-palace-cylinder","chama-deities-cylinder","ulua-ring-vessel"]
ET,ST,PG=432,559,469
DECIS="""## D127 — Cycle124 玛雅陶器/大理石器 4 条（428 → 432）
`maya-battle-vessel-nebaj`（战事献俘瓶，**核心**；图像+口沿铭文+可可饮器三者锁定＝政治事件的可饮记录）、
`maya-palace-cylinder`（宫宴筒瓶；王之大事？饮器/赠礼/随葬三重生命）、
`chama-deities-cylinder`（Chamá 筒瓶，God K；**风格＝城邦身份**，Chamá 风格仅短暂生产）、
`ulua-ring-vessel`（乌卢阿**大理石**圈足瓶；蝙蝠首柄、涡卷锐利；玛雅腹地为彩陶、乌卢阿为整雕＝区域分工）。
**写前查重**通过。美洲 32→36 条（陶器＋首次大理石器）。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）。
"""
REPORT=("- 玛雅陶器/大理石器 4 条（428 → 432，CMA）：Nebaj 战事献俘瓶（**图像+口沿铭文+可可饮器**三者锁定＝政治事件的可饮记录）、"
 "宫宴筒瓶（御座阶梯、饮器/赠礼/随葬**三重生命**）、Chamá 神祇筒瓶（God K；**风格＝城邦身份**、仅短暂生产）、"
 "乌卢阿**大理石**圈足瓶（蝙蝠首柄、涡卷锐利；玛雅腹地为彩陶、乌卢阿整雕＝区域分工）。美洲 32 → 36。站点 465 → 469 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["玛雅陶器/大理石器（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["玛雅陶器/大理石"],"gaps_found":{"entries":4},"network":"CMA","verdict":"美洲 32→36（总432）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle123":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle123":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **428**（L2 424 / L3 4 / L1 0） |","| 条目 | **432**（L2 428 / L3 4 / L1 0） |"),("| 来源 | **555**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **559**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **465**，站内断链 **0** |","| 页面 | **469**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **428** | L2 424 / L3 4 / **L1 0** |","| 条目总数 | **432** | L2 428 / L3 4 / **L1 0** |"),("| 来源库 | **555**（另 11 条预备来源未计入） |","| 来源库 | **559**（另 11 条预备来源未计入） |"),("| 站点页面 | **465** |","| 站点页面 | **469** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **428**（L2 424 / L3 4，**无 L1**） |","| 条目 | **432**（L2 428 / L3 4，**无 L1**） |"),("| 来源 | **555**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **559**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **465** |","| 站点页面 | **469** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)