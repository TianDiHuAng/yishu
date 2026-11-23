# -*- coding: utf-8 -*-
"""Cycle98 收尾：D101 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D101 — Cycle98 中国玉器 4 条（332 → 336）
新增 `liangzhu-bi-disc`（良渚玉璧，约前3300—2200，**核心**）、`shang-cong-tube`（商代玉琮，约前1600—1056，**核心**）、
`shang-jade-ge`（商代玉戈·饕餮纹，约前1600—1050）、`qijia-jade-dao`（齐家三孔玉刀，约前2000—1700，**核心**）。
四处要点：①璧与琮为良渚**高等级墓必备礼器配对**，大璧置于墓主胸前；②琮的**《周礼》祭地**记载与**史前功能未明**并列，不以前者强解后者；
③玉极硬，以**石英砂等磨料**研磨；戈形**源自青铜兵器**，刃自饕餮口部生出，与同期青铜器共用纹样；
④齐家玉刀**仅厚2毫米**，同类出土时**刃立、平行排列**于祭祀场地。四件皆置于 `art-ancient`（该单元容纳古代与古典，含中国先秦）。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；中国玉器由概念条目扩展为实物 4 件，仍缺汉玉与明清玉。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle98","date":"2026-11-23","status":"completed",
 "gap_methods":["中国玉器实物"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["liangzhu-bi-disc","shang-cong-tube","shang-jade-ge","qijia-jade-dao"],
 "jade_objects":4,"new_sources":4,"sources_total":466,"entries_total":336,"pages":373,
 "check_result":"errors=0","check_links_result":"broken=0(373页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle98","date":"2026-11-23","methods_used":["中国玉器实物"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"中国玉器 0→4（总336）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle98"' not in t:
    block=('if cyc=="cycle98":\n'
           '    L.append("- 中国玉器由概念条目扩展为 4 件实物（332 → 336）：良渚玉璧、商代玉琮、商代玉戈（饕餮纹）、齐家三孔玉刀。'
           '①璧与琮为良渚**高等级墓必备礼器配对**，大璧置于墓主胸前；②琮的**《周礼》祭地**与**史前功能未明**并列，不以前者强解后者；'
           '③玉极硬、以**石英砂等磨料**研磨，戈形**源自青铜兵器**、与青铜器共用饕餮纹；④齐家玉刀**仅厚2毫米**、同类出土时**刃立平行排列**。'
           '站点 369 → 373 页，体检 12/12。")\n')
    anchor='if cyc=="cycle97":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **332**（L2 328 / L3 4 / L1 0） |","| 条目 | **336**（L2 332 / L3 4 / L1 0） |"),
    ("| 来源 | **462**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **466**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **369**，站内断链 **0** |","| 页面 | **373**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **332** | L2 328 / L3 4 / **L1 0** |","| 条目总数 | **336** | L2 332 / L3 4 / **L1 0** |"),
    ("| 来源库 | **462**（另 11 条预备来源未计入） |","| 来源库 | **466**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **369** |","| 站点页面 | **373** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **332**（L2 328 / L3 4，**无 L1**） |","| 条目 | **336**（L2 332 / L3 4，**无 L1**） |"),
    ("| 来源 | **462**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **466**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **369** |","| 站点页面 | **373** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])