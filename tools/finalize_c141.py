# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle141"; DATE="2026-11-24"
IDS=["attic-bf-amphora-dionysus","sisyphos-bell-krater","attic-amphora-wedgwood","attic-stamnos-dionysus"]
ET,ST,PG=492,618,529
DECIS="""## D144 — Cycle141 希腊陶器 4 条（488 → 492）
`attic-bf-amphora-dionysus`（雅典黑绘双耳瓶，**核心**；黑绘刻线＋狄俄尼索斯/西勒诺斯/迈那得）、
`sisyphos-bell-krater`（西西弗斯画师钟形杯，约前440，**核心**；红绘＋双管舞者＋阿提卡画师在意）、
`attic-amphora-wedgwood`（雅典双耳瓶，约前450—440；**18世纪英国收藏**＋**韦奇伍德仿制**＝古典的二次生命）、
`attic-stamnos-dionysus`（雅典红绘斯塔姆诺斯；酒神与随从）。
**如实记录**：O340722/O340727/O340729 **记录无 summary**，三条目**不补写历史**（只据 desc 字段陈述并标注）。
art-ancient 34→38。写前查重通过。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（V&A）。
"""
REPORT=("- 希腊陶器 4 条（488 → 492，V&A）：雅典黑绘双耳瓶（黑绘刻线＋狄俄尼索斯/西勒诺斯）、西西弗斯画师钟形杯（红绘＋双管舞者）、"
 "雅典双耳瓶（**18世纪英国收藏＋韦奇伍德仿制＝古典的二次生命**）、雅典红绘斯塔姆诺斯（酒神题材）。"
 "O340722/727/729 **记录无 summary**，三条目不补写历史。art-ancient 34→38。站点 525 → 529 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["希腊陶器（V&A）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["希腊陶器"],"gaps_found":{"entries":4},"network":"V&A","verdict":"art-ancient 34→38（总492）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle140":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle140":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **488**（L2 484 / L3 4 / L1 0） |","| 条目 | **492**（L2 488 / L3 4 / L1 0） |"),("| 来源 | **614**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **618**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **525**，站内断链 **0** |","| 页面 | **529**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **488** | L2 484 / L3 4 / **L1 0** |","| 条目总数 | **492** | L2 488 / L3 4 / **L1 0** |"),("| 来源库 | **614**（另 11 条预备来源未计入） |","| 来源库 | **618**（另 11 条预备来源未计入） |"),("| 站点页面 | **525** |","| 站点页面 | **529** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **488**（L2 484 / L3 4，**无 L1**） |","| 条目 | **492**（L2 488 / L3 4，**无 L1**） |"),("| 来源 | **614**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **618**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **525** |","| 站点页面 | **529** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)