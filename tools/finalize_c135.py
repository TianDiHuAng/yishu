# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle135"; DATE="2026-11-24"
IDS=["minai-beaker-princes","safavid-poppy-textile","safavid-khamsa-khusrau","sasanian-horse-vessel"]
ET,ST,PG=468,594,505
DECIS="""## D138 — Cycle135 伊斯兰 4 条（464 → 468）
`minai-beaker-princes`（米纳伊坐王子高足杯，**核心**；珐琅釉上彩=首次真正多色瓷，人物场景「借用书籍插图」）、
`safavid-poppy-textile`（萨法维罂粟纹金地织物，**核心**；断纬成花、印伊两地共享趣味）、
`safavid-khamsa-khusrau`（《五宝》霍斯鲁与希琳，**核心**；银点星夜景＋奉果（丰产）＋tanbur 乐人；诗/色/声合奏）、
`sasanian-horse-vessel`（萨珊马形饮器，**核心**；尼萨马血统、无权杖环王像=王权与疆域）。
**命名修正**：1947.500.b 实为**尼扎米《五宝》**插图（非「列王纪」），id 用 `safavid-khamsa-khusrau` 以免误导。
art-islamic 33→37。写前查重通过。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）。
"""
REPORT=("- 伊斯兰 4 条（464 → 468，CMA）：米纳伊坐王子高足杯（**珐琅釉上彩＝首次真正多色瓷**、人物场景「借用手抄本插图」）、"
 "萨法维罂粟纹织物（**断纬成花**、印伊共享趣味）、《五宝》霍斯鲁与希琳（**银点星夜景＋奉果＋tanbur**，诗/色/声合奏）、萨珊马形饮器（**尼萨马血统＋权杖环王像**）。"
 "命名修正：该页为**尼扎米《五宝》**（非列王纪），id 用 khamsa。art-islamic 33→37。站点 501 → 505 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["伊斯兰（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"naming_fix":"1947.500.b=尼扎米《五宝》，id 用 khamsa",
 "new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["伊斯兰"],"gaps_found":{"entries":4},"network":"CMA","verdict":"art-islamic 33→37（总468）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle134":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle134":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **464**（L2 460 / L3 4 / L1 0） |","| 条目 | **468**（L2 464 / L3 4 / L1 0） |"),("| 来源 | **591**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **594**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **501**，站内断链 **0** |","| 页面 | **505**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **464** | L2 460 / L3 4 / **L1 0** |","| 条目总数 | **468** | L2 464 / L3 4 / **L1 0** |"),("| 来源库 | **591**（另 11 条预备来源未计入） |","| 来源库 | **594**（另 11 条预备来源未计入） |"),("| 站点页面 | **501** |","| 站点页面 | **505** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **464**（L2 460 / L3 4，**无 L1**） |","| 条目 | **468**（L2 464 / L3 4，**无 L1**） |"),("| 来源 | **591**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **594**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **501** |","| 站点页面 | **505** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)