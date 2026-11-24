# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle117"; DATE="2026-11-24"
IDS=["kente-cloth-va1900","kente-cloth-va1950","mano-mask-liberia","gelede-mask-yoruba"]
ET,ST,PG=404,533,441
DECIS="""## D120 — Cycle117 非洲织物+面具 4 条（400 → 404）
`kente-cloth-va1900`/`kente-cloth-va1950`（V&A 肯特布×2，条织/错位排布/谚语命名/裁后对花）、`mano-mask-liberia`（马诺面具，11类型=社会管理工具，Harley 收集）、`gelede-mask-yoruba`（Gelede 面具，男演女敬 Ìyá Nlá、少女+鳄鱼、活动尾机械）。
**如实保留截断**：肯特布区分 Asante/Ewe 的句、Duga 声誉句均**未补写**。非洲 28→32 条；织物门类跨非/伊斯兰/大洋洲三洲。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构。
"""
REPORT=("- 非洲织物+面具 4 条（400 → 404）：V&A 肯特布×2（条织错位/谚语命名/裁后对花）、CMA 马诺面具（11类型＝社会管理工具）、"
 "Gelede 面具（男演女敬 **Ìyá Nlá**、少女+鳄鱼并置、活动尾机械、多层重漆）。肯特布区分 Asante/Ewe 的句与 Duga 声誉句**截断未补写**。"
 "非洲 28 → 32 条。站点 437 → 441 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["非洲织物+面具"],"network":"CMA/V&A",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["非洲织物/面具"],"gaps_found":{"entries":4},"network":"CMA/V&A","verdict":"非洲 28→32（总404）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle116":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle116":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **400**（L2 396 / L3 4 / L1 0） |","| 条目 | **404**（L2 400 / L3 4 / L1 0） |"),("| 来源 | **529**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **533**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **437**，站内断链 **0** |","| 页面 | **441**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **400** | L2 396 / L3 4 / **L1 0** |","| 条目总数 | **404** | L2 400 / L3 4 / **L1 0** |"),("| 来源库 | **529**（另 11 条预备来源未计入） |","| 来源库 | **533**（另 11 条预备来源未计入） |"),("| 站点页面 | **437** |","| 站点页面 | **441** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **400**（L2 396 / L3 4，**无 L1**） |","| 条目 | **404**（L2 400 / L3 4，**无 L1**） |"),("| 来源 | **529**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **533**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **437** |","| 站点页面 | **441** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)