# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle139"; DATE="2026-11-24"
IDS=["japanese-armour-1800","japanese-armour-1859","kabuto-helmet-1700","japanese-sword-1300"]
ET,ST,PG=484,610,521
DECIS="""## D142 — Cycle139 日本武具 4 条（480 → 484；新增「武具」类别）
`japanese-armour-1800`（土井家胴丸，**核心**；胴丸约1400年始、护腿缩肩、车轮槌家徽）、
`japanese-armour-1859`（妙心宗春 1859 甲胄，**核心**；妙心家16世纪起、**摹镰仓＋江户加饰**的双重性）、
`kabuto-helmet-1700`（桃形兜；四板、纵向脊、日野式颈甲）、
`japanese-sword-1300`（正宗铭太刀刀身，**核心**；**金象嵌铭＝归属而非真伪确证**；记录无尺寸不列）。
art-asia 内新增「日本武具」子群。写前查重通过。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（V&A）。
"""
REPORT=("- 日本武具 4 条（480 → 484，V&A）：土井家胴丸（**胴丸约1400年始**、护腿缩肩、车轮槌家徽）、妙心宗春 1859 甲胄（妙心家16世纪起、"
 "**摹镰仓＋江户加饰**的双重性）、桃形兜（四板、纵向脊、日野式颈甲）、正宗铭太刀刀身（**金象嵌铭＝归属而非真伪确证**；无尺寸不列）。"
 "art-asia 新增「武具」子群。站点 517 → 521 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["日本武具（V&A）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["日本武具"],"gaps_found":{"entries":4},"network":"V&A","verdict":"总484；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle138":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle138":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **480**（L2 476 / L3 4 / L1 0） |","| 条目 | **484**（L2 480 / L3 4 / L1 0） |"),("| 来源 | **606**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **610**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **517**，站内断链 **0** |","| 页面 | **521**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **480** | L2 476 / L3 4 / **L1 0** |","| 条目总数 | **484** | L2 480 / L3 4 / **L1 0** |"),("| 来源库 | **606**（另 11 条预备来源未计入） |","| 来源库 | **610**（另 11 条预备来源未计入） |"),("| 站点页面 | **517** |","| 站点页面 | **521** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **480**（L2 476 / L3 4，**无 L1**） |","| 条目 | **484**（L2 480 / L3 4，**无 L1**） |"),("| 来源 | **606**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **610**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **517** |","| 站点页面 | **521** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)