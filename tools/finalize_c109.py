# -*- coding: utf-8 -*-
"""Cycle109 收尾：D112 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D112 — Cycle109 伊斯兰织物 4 条（372 → 376；门类首次覆盖织物）
`art-islamic` 此前无**织物**类，本轮以 V&A 补 4 件：
`ardabil-carpet`（阿尔达比勒地毯，1539—40，**核心**）、`ushak-carpet`（乌沙克地毯，约1500，**核心**）、
`ottoman-silk-lampas`（奥斯曼灯芯缎丝织，16世纪）、`ottoman-silk-velvet`（布尔萨丝绒，17世纪初，**核心**）。
四处要点：①阿尔达比勒毯由**沙阿·塔赫玛斯普**作**一对之一**献先祖神祠，为现存最大最精伊斯兰毯之一，**羊毛栽绒丝绸地、10色、非对称结**；
②乌沙克毯的**中央团花母题源于伊朗**，15世纪末被**土耳其织工采用**（母题传播史）；
③奥斯曼宫廷丝织**刻意去人物纹**以维系**逊尼派多数**支持；④布尔萨丝绒以**kemha/seraser** 复合织物为最贵，夹银或银鎏金线，是社会**等级**标识。
**如实保留资料截断**：奥斯曼灯芯缎 summary 在「抽象…」处截断，未补写具体纹样名。
**尺寸**按 V&A 多值口径写「宽530—535.5、长1031—1044」等区间，不伪造单一数。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条 V&A 来源。
代价：均单一机构（V&A）；伊斯兰织物由此起步，仍缺埃及/印度织物与更多地毯类型。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle109","date":"2026-11-24","status":"completed",
 "gap_methods":["V&A 伊斯兰织物（首次覆盖织物门类）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":["ardabil-carpet","ushak-carpet","ottoman-silk-lampas","ottoman-silk-velvet"],
 "new_sources":4,"sources_total":505,"entries_total":376,"pages":413,
 "check_result":"errors=0","check_links_result":"broken=0(413页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle109","date":"2026-11-24","methods_used":["V&A 伊斯兰织物"],
 "gaps_found":{"entries":4},"network":"V&A 200","verdict":"总376；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle109"' not in t:
    block=('if cyc=="cycle109":\n'
           '    L.append("- `art-islamic` 首次覆盖**织物门类**，补 4 条（372 → 376）：阿尔达比勒地毯、乌沙克地毯、奥斯曼灯芯缎丝织、布尔萨丝绒。'
           '①阿尔达比勒毯为沙阿·塔赫玛斯普**一对之一**献先祖神祠、现存最大最精伊斯兰毯之一（羊毛栽绒丝绸地/10色/非对称结）；'
           '②乌沙克毯**中央团花母题源于伊朗**、15世纪末被土耳其织工采用；③奥斯曼宫廷丝织**刻意去人物纹**以维系**逊尼派多数**；'
           '④布尔萨丝绒以 **kemha/seraser** 为最贵、夹银线、是社会**等级**标识。'
           '如实保留奥斯曼灯芯缎 summary 的**截断处**不补写；尺寸按 V&A 多值写**区间**（宽530—535.5、长1031—1044）。站点 409 → 413 页，体检 12/12。")\n')
    anchor='if cyc=="cycle108":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **372**（L2 368 / L3 4 / L1 0） |","| 条目 | **376**（L2 372 / L3 4 / L1 0） |"),
    ("| 来源 | **501**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **505**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **409**，站内断链 **0** |","| 页面 | **413**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **372** | L2 368 / L3 4 / **L1 0** |","| 条目总数 | **376** | L2 372 / L3 4 / **L1 0** |"),
    ("| 来源库 | **501**（另 11 条预备来源未计入） |","| 来源库 | **505**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **409** |","| 站点页面 | **413** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **372**（L2 368 / L3 4，**无 L1**） |","| 条目 | **376**（L2 372 / L3 4，**无 L1**） |"),
    ("| 来源 | **501**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **505**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **409** |","| 站点页面 | **413** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])