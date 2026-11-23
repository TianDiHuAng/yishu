# -*- coding: utf-8 -*-
"""Cycle90 收尾：D093 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D093 — Cycle90 中国青铜礼器实物 4 条（300 → 304）
新增 `shang-jia-vessel`（商代铜爵，约前1250—前1046）、`shang-ding-small`（商代小鼎，前1200—前1100）、
`zhou-ding-large`（西周大鼎，前1000年代，**核心**）、`lai-zhong-bell`（逨钟，约前800—前700，**核心**）。
四处要点：①爵的三足可架火加热，关联商代祖先祭与祈丰收/战功；②鼎在宋代以来即成为**青铜著录、铭文与类型学**的研究对象，
早于现代考古学；③西周大鼎的**饕餮凝视**意在激起敬畏，鼎又同时是**政治权力与合法性**象征；
④逨钟是八件成组编钟之一，**118字铭文**记世职与孝行，也被该馆视为**中国书法早期实例**（抽象线条与字形结构）。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；青铜礼器实物由 0 增至 4，仍缺兵器、车马器与战国晚期精致器物。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle90","date":"2026-11-23","status":"completed",
 "gap_methods":["中国青铜礼器实物"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["shang-jia-vessel","shang-ding-small","zhou-ding-large","lai-zhong-bell"],
 "bronze_objects":4,"new_sources":4,"sources_total":435,"entries_total":304,"pages":341,
 "check_result":"errors=0","check_links_result":"broken=0(341页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle90","date":"2026-11-23","methods_used":["中国青铜礼器"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"青铜实物 0→4（总 304）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle90"' not in t:
    block=('if cyc=="cycle90":\n'
           '    L.append("- 中国青铜礼器此前只有概念条目，本轮补 4 件实物（300 → 304）：商代铜爵、商代小鼎、西周大鼎、逨钟。'
           '①爵的三足可架火，关联**祖先祭祀**与祈丰收/战功；②鼎在**宋代以来**即成青铜著录、铭文与类型学研究对象，'
           '早于现代考古学；③西周大鼎的**饕餮凝视**激起敬畏，鼎兼具**政治权力与合法性**象征；'
           '④逨钟为**八件成组编钟**之二，**118字铭文**记世职与孝行，也被视为中国书法早期实例。'
           '站点 337 → 341 页，体检 12/12。")\n')
    anchor='if cyc=="cycle89":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **300**（L2 296 / L3 4 / L1 0） |","| 条目 | **304**（L2 300 / L3 4 / L1 0） |"),
    ("| 来源 | **431**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **435**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **337**，站内断链 **0** |","| 页面 | **341**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **300** | L2 296 / L3 4 / **L1 0** |","| 条目总数 | **304** | L2 300 / L3 4 / **L1 0** |"),
    ("| 来源库 | **431**（另 11 条预备来源未计入） |","| 来源库 | **435**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **337** |","| 站点页面 | **341** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **300**（L2 296 / L3 4，**无 L1**） |","| 条目 | **304**（L2 300 / L3 4，**无 L1**） |"),
    ("| 来源 | **431**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **435**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **337** |","| 站点页面 | **341** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])