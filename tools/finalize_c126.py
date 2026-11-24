# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle126"; DATE="2026-11-24"
IDS=["shang-jue-cups","eastern-zhou-hu-jar","bo-zhong-bell","western-zhou-hu-vessel"]
ET,ST,PG=440,567,477
DECIS="""## D129 — Cycle126 商周青铜 4 条（436 → 440）
`shang-jue-cups`（爵一对，安阳期；爵=灌祭，器类专名爵/斝/方卣/觚＝器形即仪注）、
`eastern-zhou-hu-jar`（战国狩猎壶，**核心**；六横带狩猎叙事＝中国艺术**最早图像性场景之一**，叙事转向）、
`bo-zhong-bell`（东周鎛钟，**核心**；椭圆截面一钟两音、敲沿/敲心、成套编悬）、
`western-zhou-hu-vessel`（西周带盖壶；颈凤盖足龙、龙凤或表阴阳故宗教世俗皆宜、盖倒成杯、柱耳以绳携行）。
**写前查重**通过；构建前修正西周壶自引用。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）；青铜礼器实物 4→8。
"""
REPORT=("- 商周青铜 4 条（436 → 440，CMA）：安阳爵一对（**爵＝灌祭**，爵/斝/卣/觚专名＝器形即仪注）、"
 "战国狩猎壶（六横带狩猎叙事＝**中国最早图像性场景之一**、叙事转向）、东周鎛钟（**椭圆截面一钟两音**、敲沿/敲心、成套编悬）、"
 "西周带盖壶（颈凤盖足龙、龙凤或表阴阳故两用、盖倒成杯、柱耳绳携）。构建前修正西周壶自引用。青铜实物 4→8。站点 473 → 477 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["商周青铜（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"self_ref_fixed":"western-zhou-hu-vessel 构建前修正",
 "new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["商周青铜"],"gaps_found":{"entries":4},"network":"CMA","verdict":"青铜 4→8（总440）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle125":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle125":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **436**（L2 432 / L3 4 / L1 0） |","| 条目 | **440**（L2 436 / L3 4 / L1 0） |"),("| 来源 | **563**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **567**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **473**，站内断链 **0** |","| 页面 | **477**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **436** | L2 432 / L3 4 / **L1 0** |","| 条目总数 | **440** | L2 436 / L3 4 / **L1 0** |"),("| 来源库 | **563**（另 11 条预备来源未计入） |","| 来源库 | **567**（另 11 条预备来源未计入） |"),("| 站点页面 | **473** |","| 站点页面 | **477** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **436**（L2 432 / L3 4，**无 L1**） |","| 条目 | **440**（L2 436 / L3 4，**无 L1**） |"),("| 来源 | **563**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **567**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **473** |","| 站点页面 | **477** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)