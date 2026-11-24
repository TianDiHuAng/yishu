# -*- coding: utf-8 -*-
"""Cycle110 收尾：D113 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D113 — Cycle110 中世纪再补 4 条（376 → 380；象牙/珐琅/雪花石）
继续以 V&A 补 `art-medieval`（异材质）：`ivory-crucified-christ`（象牙基督受难像，1290—1310，**核心**）、
`ivory-virgin-child-paris`（巴黎象牙圣母子，约1240，**核心**）、`limoges-gospel-cover`（利摩日福音书封，约1200，**核心**）、
`alabaster-pieta`（尼德兰雪花石《哀悼基督》，约1430，**核心**）。
四处要点：①象牙基督像以**濒死面容（闭目/头偏/左颊伤）**在**可手持尺度**表现私人虔敬，并可联到**皮萨诺1298象牙圣母**线索；
②巴黎象牙圣母子是**最早法国立姿象牙之一**，衣褶与**主教座堂门廊石雕**相类（缩微）；
③利摩日錾胎珐琅书封以**基督庄严＋Α/Ω＋四福音象征**为图，且**远销全欧至冰岛**；
④雪花石《哀悼基督》以**新旧风格融合（传统＋绘画般写实）**为价值核心，属虔敬像。
**如实保留资料截断**：象牙基督（「Although it is…」）、巴黎象牙（「the so…」石门圣母教堂名）、雪花石（「realism…」）三处 V&A 说明**截断，均未补写**；尺寸按 mm/cm 双写（400×315mm＝40×31.5cm）。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条 V&A 来源。
代价：均单一机构（V&A）；中世纪 10 → 14 条，象牙/珐琅/雪花石齐备，但**彩绘写本**仍缺。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle110","date":"2026-11-24","status":"completed",
 "gap_methods":["V&A 中世纪异材质"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":["ivory-crucified-christ","ivory-virgin-child-paris","limoges-gospel-cover","alabaster-pieta"],
 "new_sources":4,"sources_total":509,"entries_total":380,"pages":417,
 "check_result":"errors=0","check_links_result":"broken=0(417页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle110","date":"2026-11-24","methods_used":["V&A 中世纪异材质"],
 "gaps_found":{"entries":4},"network":"V&A 200","verdict":"中世纪 10→14（总380）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle110"' not in t:
    block=('if cyc=="cycle110":\n'
           '    L.append("- 中世纪再补 4 条（376 → 380）：象牙基督受难像、巴黎象牙圣母子、利摩日福音书封、雪花石《哀悼基督》。'
           '①象牙基督以**濒死面容**在**可手持尺度**表现私人虔敬，并可联到**皮萨诺1298象牙圣母**线索；'
           '②巴黎象牙圣母子为**最早法国立姿象牙之一**、衣褶同于**门廊石雕**（缩微）；③利摩日錾胎珐琅书封以**基督庄严＋Α/Ω＋四福音象征**、**远销全欧至冰岛**；'
           '④雪花石《哀悼基督》以**新旧风格融合（传统＋绘画般写实）**为价值核心。'
           '如实保留象牙基督、巴黎象牙、雪花石三处 summary 的**截断**不补写。站点 413 → 417 页，体检 12/12。")\n')
    anchor='if cyc=="cycle109":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **376**（L2 372 / L3 4 / L1 0） |","| 条目 | **380**（L2 376 / L3 4 / L1 0） |"),
    ("| 来源 | **505**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **509**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **413**，站内断链 **0** |","| 页面 | **417**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **376** | L2 372 / L3 4 / **L1 0** |","| 条目总数 | **380** | L2 376 / L3 4 / **L1 0** |"),
    ("| 来源库 | **505**（另 11 条预备来源未计入） |","| 来源库 | **509**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **413** |","| 站点页面 | **417** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **376**（L2 372 / L3 4，**无 L1**） |","| 条目 | **380**（L2 376 / L3 4，**无 L1**） |"),
    ("| 来源 | **505**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **509**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **413** |","| 站点页面 | **417** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])