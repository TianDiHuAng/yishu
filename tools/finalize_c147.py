# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle147"; DATE="2026-11-24"
IDS=["mamluk-glass-bottle-1350","mamluk-glass-beaker","mamluk-glass-bottle-1347","mamluk-lamp-1320"]
ET,ST,PG=516,642,553
DECIS="""## D150 — Cycle147 伊斯兰玻璃 4 条（512 → 516）
`mamluk-glass-bottle-1350`（约1350；**铭文即主纹**蓝彩大字、凤凰纹章、匿名苏丹献辞）、
`mamluk-glass-beaker`（1250—1350；**红狮白章＋苏丹颂铭**＋鱼叶轻描）、
`mamluk-glass-bottle-1347`（1347—70；金描圆章/开光、Jurji 颂铭、**「稀疏亦精」**；无尺寸）、
`mamluk-lamp-1320`（1320—30；Qijlis 剑徽＋「安拉之寺」经文、**供灯＝虔诚**的仪式经济）。
art-islamic 45→49。写前查重通过。**自查**：初稿一处 ASCII 双引号（"两点两纹"）会断字符串，构建前改「」。
**如实**：多处 summary 截断、O624 无尺寸，均未补写/不提供。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（V&A）。
"""
REPORT=("- 伊斯兰玻璃 4 条（512 → 516，V&A）：约1350马穆鲁克描金瓶（**铭文即主纹**、凤凰纹章、匿名苏丹献辞）、狮纹杯（**红狮白章＋苏丹颂铭**）、"
 "1347—70描金瓶（金描圆章、Jurji 颂铭、**稀疏亦精**；无尺寸）、Qijlis 清真寺灯（剑徽＋「安拉之寺」经文、**供灯＝虔诚**）。"
 "初稿一处 ASCII 双引号构建前已改「」。art-islamic 45→49。站点 549 → 553 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["伊斯兰玻璃（V&A）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["伊斯兰玻璃"],"gaps_found":{"entries":4},"network":"V&A","verdict":"art-islamic 45→49（总516）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle146":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle146":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **512**（L2 508 / L3 4 / L1 0） |","| 条目 | **516**（L2 512 / L3 4 / L1 0） |"),("| 来源 | **638**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **642**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **549**，站内断链 **0** |","| 页面 | **553**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **512** | L2 508 / L3 4 / **L1 0** |","| 条目总数 | **516** | L2 512 / L3 4 / **L1 0** |"),("| 来源库 | **638**（另 11 条预备来源未计入） |","| 来源库 | **642**（另 11 条预备来源未计入） |"),("| 站点页面 | **549** |","| 站点页面 | **553** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **512**（L2 508 / L3 4，**无 L1**） |","| 条目 | **516**（L2 512 / L3 4，**无 L1**） |"),("| 来源 | **638**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **642**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **549** |","| 站点页面 | **553** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)