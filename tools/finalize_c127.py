# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle127"; DATE="2026-11-24"
IDS=["korean-orchids-rocks","korean-snowscape-figures","japan-eight-views-xiaoxiang","japan-miraculous-origins"]
ET,ST,PG=444,571,481
DECIS="""## D130 — Cycle127 日朝绘画 4 条（440 → 444）
`korean-orchids-rocks`（李昰应兰石八曲屏，1897—98，**核心**；摄政1866—73＋文人画复兴、兰为四君子、单色墨垂兰）、
`korean-snowscape-figures`（金禔雪景，标1584，**核心**；父金安老失势后隐居，雪景＝「心景」；**记录生卒自相矛盾（1524—1593 vs 1481—1537），照录存疑**）、
`japan-eight-views-xiaoxiang`（渡边始兴潇湘八景六曲屏，1700s；狩野派单色墨、中国题材、取景宏阔喻中国之大）、
`japan-miraculous-origins`（优陀念佛缘起绘卷卷二，1300s初，**核心**；良忍「一切互相联」＋念佛互益，长卷时间性阅读）。
**如实保留截断**：兰石屏 summary「associated with th…」未补写。日朝绘画＋4。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）。
"""
REPORT=("- 日朝绘画 4 条（440 → 444，CMA）：李昰应兰石八曲屏（**摄政＋文人画复兴**、兰为四君子、单色墨垂兰）、"
 "金禔雪景人物（父失势后隐居，**雪景＝心景**；**记录生卒自相矛盾照录存疑**）、渡边始兴潇湘八景屏（狩野派单色墨、中国题材、宏阔喻中国之大）、"
 "优陀念佛缘起绘卷卷二（良忍「一切互相关联」＋念佛互益、长卷时间性阅读）。站点 477 → 481 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["日朝绘画（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"date_suspect":"金禔雪景生卒记载自相矛盾照录",
 "new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["日朝绘画"],"gaps_found":{"entries":4},"network":"CMA","verdict":"总444；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle126":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle126":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **440**（L2 436 / L3 4 / L1 0） |","| 条目 | **444**（L2 440 / L3 4 / L1 0） |"),("| 来源 | **567**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **571**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **477**，站内断链 **0** |","| 页面 | **481**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **440** | L2 436 / L3 4 / **L1 0** |","| 条目总数 | **444** | L2 440 / L3 4 / **L1 0** |"),("| 来源库 | **567**（另 11 条预备来源未计入） |","| 来源库 | **571**（另 11 条预备来源未计入） |"),("| 站点页面 | **477** |","| 站点页面 | **481** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **440**（L2 436 / L3 4，**无 L1**） |","| 条目 | **444**（L2 440 / L3 4，**无 L1**） |"),("| 来源 | **567**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **571**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **477** |","| 站点页面 | **481** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)