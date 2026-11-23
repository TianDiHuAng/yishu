# -*- coding: utf-8 -*-
"""Cycle82 收尾：D086 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D086 — Cycle82 中国绘画续补 4 条（272 → 276）
新增 `wang-hui-bamboo`（王翚仿王蒙，1694，**核心**）、`dong-qichang-qingbian`（董其昌《青弁图》，1617，**核心**）、
`lan-ying-pure-conversation`（蓝瑛《支许清谈》，1643）、`qiu-ying-garden`（仇英《独乐园》，1515—52，**核心**）。
四处要点：①王翚「摹古」是**主动构图行为**——把高士自亭中移到溪畔、连题识并摹、追踪文同→王蒙→王翚双层师承；
②董其昌把山水化为**抽象结构**，让**气/势**贯穿画面，笔墨取得**独立于物象**的生命；
③蓝瑛赠禅僧无云，以支遁与许询类比友谊，时值**明亡前一年**，并被该馆称为**浙派最后代表**；
④仇英《独乐园》据**11世纪原型**再绘，反成**苏州作坊摹本模板**。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；中国绘画作品 11 条，仍缺壁画与长卷的更多实例。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle82","date":"2026-11-23","status":"completed",
 "gap_methods":["中国绘画续深"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["wang-hui-bamboo","dong-qichang-qingbian","lan-ying-pure-conversation","qiu-ying-garden"],
 "chinese_painting_works":11,"new_sources":4,"sources_total":407,"entries_total":276,"pages":313,
 "check_result":"errors=0","check_links_result":"broken=0(313页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle82","date":"2026-11-23","methods_used":["中国绘画续深"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"中国绘画作品 7→11（总 276）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle82"' not in t:
    block=('if cyc=="cycle82":\n'
           '    L.append("- 中国绘画续补 **4 条（272 → 276）**：王翚仿王蒙、董其昌《青弁图》、蓝瑛《支许清谈》、仇英《独乐园》。'
           '①王翚「摹古」是**主动构图行为**（高士移出亭、并摹题识、文同→王蒙→王翚双层师承）；'
           '②董其昌把山水化为**抽象结构**，**气/势**贯穿画面，笔墨**独立于物象**；'
           '③蓝瑛赠僧无云，以六朝高士类比友谊，时值**明亡前一年**，该馆称其为**浙派最后代表**；'
           '④仇英《独乐园》据**11世纪原型**再绘，反成**苏州作坊摹本模板**。站点 309 → 313 页，体检 12/12。")\n')
    anchor='if cyc=="cycle81":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 272（L2 268 / L3 4 / L1 0） |","| 条目 | 276（L2 272 / L3 4 / L1 0） |"),
    ("| 来源 | 403（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 407（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 309，站内断链 **0** |","| 页面 | 313，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **272** | L2 268 / L3 4 / **L1 0** |","| 条目总数 | **276** | L2 272 / L3 4 / **L1 0** |"),
    ("| 来源库 | **403**（另 11 条预备来源未计入） |","| 来源库 | **407**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **309** |","| 站点页面 | **313** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])