# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle122"; DATE="2026-11-24"
IDS=["yuan-lion-jar","jiajing-carved-lacquer-jar","yongle-meiping-cloud","ten-bamboo-album"]
ET,ST,PG=424,551,461
DECIS="""## D125 — Cycle122 中国陶瓷/版印 4 条（420 → 424）
`yuan-lion-jar`（元青花狮首罐，**核心**；伊朗钴料（或卡尚）＋云肩纹与伊尔汗语汇共享＋内外销并行）、
`jiajing-carved-lacquer-jar`（嘉靖剔彩龙凤罐，**核心**；多层漆雕、龙凤宫廷徽记、配色似同期五彩）、
`yongle-meiping-cloud`（永乐甜白暗花梅瓶，**核心**；anhua 需光可读、甜白如融雪、用于宫廷祭献）、
`ten-bamboo-album`（十竹斋书画谱初版 1633，**核心**；「画一般的印刷」＋饾版对位＋影响日韩）。
**写前查重**通过；related 自查后修正两处（art-ceramics/chinese-ceramics-history 不存在 → chenghua-doucai-cup / china-calligraphy-history）。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）；编者胡正言该馆未记，未补写。
"""
REPORT=("- 中国陶瓷/版印 4 条（420 → 424，CMA）：元青花狮首罐（**伊朗钴料**或自卡尚、云肩纹与伊尔汗语汇共享、内外销并行）、"
 "嘉靖剔彩龙凤罐（多层漆雕、龙凤宫廷徽记、配色似同期五彩）、永乐甜白暗花梅瓶（**anhua 需光可读**、甜白如融雪、宫廷祭献）、"
 "十竹斋书画谱初版（1633，「**画一般的印刷**」＋饾版对位＋影响日韩）。"
 "写前查重通过；related 自查修正 2 处。站点 457 → 461 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["中国陶瓷/版印（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"related_fixed":2,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["中国陶瓷/版印"],"gaps_found":{"entries":4},"network":"CMA","verdict":"总424；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle121":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle121":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **420**（L2 416 / L3 4 / L1 0） |","| 条目 | **424**（L2 420 / L3 4 / L1 0） |"),("| 来源 | **548**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **551**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **457**，站内断链 **0** |","| 页面 | **461**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **420** | L2 416 / L3 4 / **L1 0** |","| 条目总数 | **424** | L2 420 / L3 4 / **L1 0** |"),("| 来源库 | **548**（另 11 条预备来源未计入） |","| 来源库 | **551**（另 11 条预备来源未计入） |"),("| 站点页面 | **457** |","| 站点页面 | **461** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **420**（L2 416 / L3 4，**无 L1**） |","| 条目 | **424**（L2 420 / L3 4，**无 L1**） |"),("| 来源 | **548**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **551**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **457** |","| 站点页面 | **461** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)