# -*- coding: utf-8 -*-
"""Cycle104 收尾：D107 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D107 — Cycle104 印象/后印象 4 条（352 → 356）
按单元计数（`art-impression` 8 条）定向补 4 件，刻意选**梵高三种不同媒介**以显其范围，另加毕沙罗：
`van-gogh-plane-trees`（梵高《大悬铃木·圣雷米修路工》，1889，油画，**核心**）、`van-gogh-dr-gachet`（《加歇医生》，1890，蚀刻，**核心**）、
`pissarro-lock-pontoise`（毕沙罗《蓬图瓦兹水闸》，1872，油画，**核心**）、`van-gogh-drenthe-wheelbarrow`（梵高《德伦特风景》，1883，水彩）。
四处要点：①圣雷米疗养期**医生准其户外写生**以缓解抑郁，**致提奥书信**直接描述画中巨木与修路；
②《加歇医生》是梵高**唯一蚀刻**，经**毕沙罗推荐**、加歇**赠铜版并助其手压印制**；
③毕沙罗以**纯色碎笔触、不打草稿**的户外快速写生捕捉**瞬间光气**；
④德伦特荒原以**钢绿/冷蓝/淡紫**的**有限色盘**写出「没入无限的广袤平原」。注：`Landscape with Wheelbarrow` 实为梵高（非塞尚），已按 creator 字段更正。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构，梵高占 3；印象由 8 → 12 条，但**雷诺阿、西斯莱、塞尚**等仍缺。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle104","date":"2026-11-24","status":"completed",
 "gap_methods":["印象/后印象（定向最薄单元）"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["van-gogh-plane-trees","van-gogh-dr-gachet","pissarro-lock-pontoise","van-gogh-drenthe-wheelbarrow"],
 "impression_objects":4,"note":"Landscape with Wheelbarrow 实为梵高，已按 creator 更正",
 "new_sources":4,"sources_total":485,"entries_total":356,"pages":393,
 "check_result":"errors=0","check_links_result":"broken=0(393页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle104","date":"2026-11-24","methods_used":["印象/后印象"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"印象 8→12（总356）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle104"' not in t:
    block=('if cyc=="cycle104":\n'
           '    L.append("- 印象/后印象（`art-impression` 8条）补 4 件（352 → 356），刻意选**梵高三种媒介**＋毕沙罗：梵高《大悬铃木》（油画）、'
           '《加歇医生》（蚀刻）、毕沙罗《蓬图瓦兹水闸》、梵高《德伦特风景》（水彩）。①圣雷米疗养期**医生准其户外写生**，致提奥书信直述画中巨木修路；'
           '②《加歇医生》为梵高**唯一蚀刻**，经**毕沙罗推荐**、加歇**赠铜版助印**；③毕沙罗以**碎笔触不打草稿**捕捉**瞬间光气**；'
           '④德伦特荒原以**钢绿/冷蓝/淡紫**的**有限色盘**写「没入无限」。注：Landscape with Wheelbarrow 实为梵高（非塞尚），已按 creator 更正。'
           '站点 389 → 393 页，体检 12/12。")\n')
    anchor='if cyc=="cycle103":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **352**（L2 348 / L3 4 / L1 0） |","| 条目 | **356**（L2 352 / L3 4 / L1 0） |"),
    ("| 来源 | **481**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **485**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **389**，站内断链 **0** |","| 页面 | **393**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **352** | L2 348 / L3 4 / **L1 0** |","| 条目总数 | **356** | L2 352 / L3 4 / **L1 0** |"),
    ("| 来源库 | **481**（另 11 条预备来源未计入） |","| 来源库 | **485**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **389** |","| 站点页面 | **393** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **352**（L2 348 / L3 4，**无 L1**） |","| 条目 | **356**（L2 352 / L3 4，**无 L1**） |"),
    ("| 来源 | **481**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **485**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **389** |","| 站点页面 | **393** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])