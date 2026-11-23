# -*- coding: utf-8 -*-
"""Cycle97 收尾：D100 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D100 — Cycle97 古代美洲 4 条（328 → 332）
新增 `maya-deer-vessel`（玛雅鹿形黑陶瓶，250—600，**核心**）、`wari-tunic`（瓦里束腰衣，700—1100，**核心**）、
`inca-tunic-1957`（印加束腰衣，1400—1540，**核心**）、`aztec-xochipilli-maize`（阿兹特克持玉米坐像，1325—1521）。
四处要点：①玛雅黑陶以**还原气氛**烧成，鹿纹并置**死亡**（金星/海螺）与**丰产**（蛙蟾报雨）；
②瓦里束腰衣**经线横向**（异于常态）且**似影响印加**构造；③印加细密挂毯为**贵族特权**，由 Aclla 选女等织造、**国家再分配**作赏赐，纹样「印加之钥」；
④阿兹特克坐像或为 Macuilxochitl/Xochipilli，持花锥、背玉米，串起「花=美/丰产/性/创造力」。
**纪律改进**：本轮先用脚本**查重 id**，发现 `inca-tunic` 已存在，遂改用 **`inca-tunic-1957`**；又发现既有 `aztec-feathered-serpent`，遂弃用同题的「真伪存疑羽蛇」改取**持玉米坐像**作第 4 件——避免重演 Cycle96 重名事故。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；美洲 21 → 25 条，前哥伦布仍以陶/织物为主，石雕与建筑少数。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle97","date":"2026-11-23","status":"completed",
 "gap_methods":["古代美洲"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["maya-deer-vessel","wari-tunic","inca-tunic-1957","aztec-xochipilli-maize"],
 "americas_objects":4,"discipline":"写前查重 id（inca-tunic→inca-tunic-1957；避开 aztec-feathered-serpent 同题）",
 "new_sources":4,"sources_total":462,"entries_total":332,"pages":369,
 "check_result":"errors=0","check_links_result":"broken=0(369页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle97","date":"2026-11-23","methods_used":["古代美洲"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"美洲 21→25（总332）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle97"' not in t:
    block=('if cyc=="cycle97":\n'
           '    L.append("- 古代美洲补 4 条（328 → 332）：玛雅鹿形黑陶瓶、瓦里束腰衣、印加束腰衣、阿兹特克持玉米坐像。'
           '①玛雅黑陶**还原烧成**，鹿纹并置**死亡**（金星/海螺）与**丰产**（蛙蟾报雨）；②瓦里束腰衣**经线横向**且**似影响印加**；'
           '③印加细密挂毯为**贵族特权**，Aclla 选女织造、**国家再分配**作赏赐（「印加之钥」）；④阿兹特克坐像持花锥、背玉米，'
           '串起「花=美/丰产/性/创造力」。**纪律**：本轮写前查重 id，避开既有 `inca-tunic` 与 `aztec-feathered-serpent` 同题。'
           '站点 365 → 369 页，体检 12/12。")\n')
    anchor='if cyc=="cycle96":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **328**（L2 324 / L3 4 / L1 0） |","| 条目 | **332**（L2 328 / L3 4 / L1 0） |"),
    ("| 来源 | **459**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **462**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **365**，站内断链 **0** |","| 页面 | **369**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **328** | L2 324 / L3 4 / **L1 0** |","| 条目总数 | **332** | L2 328 / L3 4 / **L1 0** |"),
    ("| 来源库 | **459**（另 11 条预备来源未计入） |","| 来源库 | **462**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **365** |","| 站点页面 | **369** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **328**（L2 324 / L3 4，**无 L1**） |","| 条目 | **332**（L2 328 / L3 4，**无 L1**） |"),
    ("| 来源 | **459**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **462**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **365** |","| 站点页面 | **369** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])