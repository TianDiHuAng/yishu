# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle137"; DATE="2026-11-24"
IDS=["matisse-interior-etruscan","degas-frieze-dancers","rouault-end-autumn","cannon-memorial-woodcut"]
ET,ST,PG=476,602,513
DECIS="""## D140 — Cycle137 现代/当代 4 条（472 → 476）
`matisse-interior-etruscan`（马蒂斯《有伊特鲁里亚瓶的室内》，1940，**核心**；二战爆发后半年、尼斯Régina，「艺术作平衡」＝心理防御）、
`degas-frieze-dancers`（德加《舞者饰带》，约1895，**核心**；四视角＋流淌笔触＋或受迈布里奇启发）、
`rouault-end-autumn`（鲁奥《秋末·第4号》，1952，**核心**；信仰为核、逃往埃及联想、彩窗式色框）、
`cannon-memorial-woodcut`（坎农纪念木刻组画，约1978，**核心**；Kiowa-Caddo、波普色盘、油画→木刻转译；**记录无尺寸，不列尺寸**）。
**命名修正**：1952.153 作者是**马蒂斯**（原拟 Bonnard），id 用 matisse。
art-contemporary 9→13。写前查重通过。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）。
"""
REPORT=("- 现代/当代 4 条（472 → 476，CMA）：马蒂斯《有伊特鲁里亚瓶的室内》（二战初、**艺术作平衡＝心理防御**）、"
 "德加《舞者饰带》（**四视角**＋流淌笔触＋**迈布里奇**启发）、鲁奥《秋末·第4号》（信仰为核、**彩窗式色框**）、"
 "坎农纪念木刻组画（Kiowa-Caddo、**波普色盘**、油画→木刻转译；**记录无尺寸不列**）。命名修正：1952.153 实为马蒂斯。art-contemporary 9→13。"
 "站点 509 → 513 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["现代/当代（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"naming_fix":"1952.153=马蒂斯（非Bonnard）",
 "new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["现代/当代"],"gaps_found":{"entries":4},"network":"CMA","verdict":"art-contemporary 9→13（总476）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle136":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle136":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **472**（L2 468 / L3 4 / L1 0） |","| 条目 | **476**（L2 472 / L3 4 / L1 0） |"),("| 来源 | **598**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **602**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **509**，站内断链 **0** |","| 页面 | **513**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **472** | L2 468 / L3 4 / **L1 0** |","| 条目总数 | **476** | L2 472 / L3 4 / **L1 0** |"),("| 来源库 | **598**（另 11 条预备来源未计入） |","| 来源库 | **602**（另 11 条预备来源未计入） |"),("| 站点页面 | **509** |","| 站点页面 | **513** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **472**（L2 468 / L3 4，**无 L1**） |","| 条目 | **476**（L2 472 / L3 4，**无 L1**） |"),("| 来源 | **598**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **602**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **509** |","| 站点页面 | **513** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)