# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle123"; DATE="2026-11-24"
IDS=["rai-singh-bikaner","rajasthan-head-drawing","nyankhnesut-relief","djedbastetiufankh-block-statue"]
ET,ST,PG=428,555,465
DECIS="""## D126 — Cycle123 印度2+埃及2（424 → 428）
`rai-singh-bikaner`（比卡内尔王公像，约1610；侍阿克巴、女嫁贾汉吉尔——肖像＝联盟索引；或依 Nur Muhammad 底稿）、
`rajasthan-head-drawing`（基什加尔头像稿，约1780；重勾眉眼须/柔色塑面＝过程证据）、
`nyankhnesut-relief`（萨卡拉第6王朝浮雕，**核心**；题材＝食物生产供墓；15馆分散＋2000年才定位墓址）、
`djedbastetiufankh-block-statue`（块像，25—26王朝；蹲坐抱膝立方形「几不可碎」；柜述含 Ankh-Hor 托龛行进像与波斯期袍）。
**纪律**：write_c123 中「"sow…」的 ASCII 引号触发语法错，改弯引号后通过；「"sow…"标注文字**截断未补写**。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）；印度绘画 10→12、埃及 10→12。
"""
REPORT=("- 印度2+埃及2（424 → 428，CMA）：比卡内尔王公莱·辛格像（侍阿克巴、女嫁贾汉吉尔＝联盟索引）、基什加尔头像稿"
 "（重勾/柔染分工、备后用）、萨卡拉尼安赫涅苏特浮雕（食物生产供墓；**15馆分散、2000年才定位墓址**——一座墓的现代命运本身即材料）、"
 "杰德巴斯特提乌凡赫块像（蹲坐抱膝立方「几不可碎」；同柜 Ankh-Hor 托龛行进像与波斯期袍）。"
 "「\"sow…」标注截断未补写；脚本 ASCII 引号已改弯引号。站点 461 → 465 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["印度绘画+埃及雕塑（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["印度/埃及"],"gaps_found":{"entries":4},"network":"CMA","verdict":"总428；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle122":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle122":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **424**（L2 420 / L3 4 / L1 0） |","| 条目 | **428**（L2 424 / L3 4 / L1 0） |"),("| 来源 | **551**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **555**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **461**，站内断链 **0** |","| 页面 | **465**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **424** | L2 420 / L3 4 / **L1 0** |","| 条目总数 | **428** | L2 424 / L3 4 / **L1 0** |"),("| 来源库 | **551**（另 11 条预备来源未计入） |","| 来源库 | **555**（另 11 条预备来源未计入） |"),("| 站点页面 | **461** |","| 站点页面 | **465** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **424**（L2 420 / L3 4，**无 L1**） |","| 条目 | **428**（L2 424 / L3 4，**无 L1**） |"),("| 来源 | **551**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **555**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **461** |","| 站点页面 | **465** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)