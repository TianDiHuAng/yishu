# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle125"; DATE="2026-11-24"
IDS=["luristan-ibex-standard","luristan-axel-cup","greco-roman-votive-relief","amida-descent-painting"]
ET,ST,PG=436,563,473
DECIS="""## D128 — Cycle125 混合 4 条（432 → 436）
`luristan-ibex-standard`（羱羊标顶，**核心**；双羊前腿成环＝承杆结构，或为军事徽记）、
`luristan-axel-cup`（轴杯，**核心**；卢里斯坦「几乎无文字，所知皆由器物反推」，养马供亚述）、
`greco-roman-votive-relief`（托勒密双面习作浮雕；石灰岩片/ostraca，一面野犬首一面侧面人，「供临摹」；votive 之名与习作性质的关系**存疑照录**）、
`amida-descent-painting`（阿弥陀二十五菩萨来迎图，南北朝，**核心**；来迎图＝死亡的视觉脚本，观音持莲台供亡者乘归）。
写前查重通过。古代 30→33、西亚 3→5、日本相关＋1。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）。
"""
REPORT=("- 混合 4 条（432 → 436，CMA）：卢里斯坦羱羊标顶（双羊前腿成环＝承杆、或为军事徽记）、卢里斯坦轴杯"
 "（**无文字社会，所知皆由器物反推**；养马供亚述马匹与硬件）、托勒密双面习作浮雕（石灰岩片/ostraca，野犬首/侧面人，供临摹；"
 "votive 之名存疑照录）、阿弥陀二十五菩萨来迎图（来迎＝**死亡的视觉脚本**、观音持莲台）。古代 30→33。站点 469 → 473 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["卢里斯坦/埃及习作/日本来迎"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["卢里斯坦/埃及/日本"],"gaps_found":{"entries":4},"network":"CMA","verdict":"总436；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle124":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle124":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **432**（L2 428 / L3 4 / L1 0） |","| 条目 | **436**（L2 432 / L3 4 / L1 0） |"),("| 来源 | **559**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **563**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **469**，站内断链 **0** |","| 页面 | **473**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **432** | L2 428 / L3 4 / **L1 0** |","| 条目总数 | **436** | L2 432 / L3 4 / **L1 0** |"),("| 来源库 | **559**（另 11 条预备来源未计入） |","| 来源库 | **563**（另 11 条预备来源未计入） |"),("| 站点页面 | **469** |","| 站点页面 | **473** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **432**（L2 428 / L3 4，**无 L1**） |","| 条目 | **436**（L2 432 / L3 4，**无 L1**） |"),("| 来源 | **559**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **563**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **469** |","| 站点页面 | **473** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)