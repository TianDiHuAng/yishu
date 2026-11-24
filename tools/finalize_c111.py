# -*- coding: utf-8 -*-
"""Cycle111 收尾：D114 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D114 — Cycle111 大洋洲（含澳洲原住民）+ 乐器 4 条（380 → 384）
用 V&A 补 `art-oceania` 并首次纳入**澳洲原住民**，另以**实物**扩充 `music-instruments`（不受音乐文本 BLOCKER 影响，因这是器物）：新增
`tapa-cloth-samoa`（萨摩亚树皮布，1800s，**核心**）、`aboriginal-tapestry-pike`（平克原住民挂毯，1989，**核心**）、
`maori-flax-cloak`（毛利亚麻斗篷，1800s）、`ottoman-nay-flute`（奥斯曼 nay 笛，1860—67，**核心**，music-instruments）。
四处要点：①tapa 以**构树皮**经**浸—捶—拼—晒**的妇女劳动成布，象征与实用兼用；
②平克属**瓦尔马贾里人**、生于**大沙沙漠**边缘，作品以**俯视抽象**写沙漠记忆，本件是 1976 年**维多利亚挂毯工坊**的**限量小挂毯**；
③毛利亚麻斗篷为**搓捻（twining）**成布、缀**黑缨/流苏**（记录极简，不补写纹样织法）；
④nay 为**边棱吹管**，**三节旋木嵌金属、十二指孔、三倍音域**，土耳其版用于 **Mevlevi 旋转舞乐**。
**如实保留资料截断**：tapa summary 在「装饰因…」处**截断，未补写**；毛利斗篷记录**极简**，只作材料—形制陈述。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条 V&A 来源。
代价：均单一机构（V&A）；大洋洲 11 → 14 条（**澳洲原住民破零**），乐器 12 → 13。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle111","date":"2026-11-24","status":"completed",
 "gap_methods":["V&A 大洋洲+澳洲原住民；乐器实物"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":["tapa-cloth-samoa","aboriginal-tapestry-pike","maori-flax-cloak","ottoman-nay-flute"],
 "new_sources":4,"sources_total":513,"entries_total":384,"pages":421,
 "check_result":"errors=0","check_links_result":"broken=0(421页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle111","date":"2026-11-24","methods_used":["V&A 大洋洲/原住民/乐器"],
 "gaps_found":{"entries":4},"network":"V&A 200","verdict":"大洋洲 11→14、乐器 12→13（总384）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle111"' not in t:
    block=('if cyc=="cycle111":\n'
           '    L.append("- V&A 补大洋洲并**首次纳入澳洲原住民**，另以**实物**扩充乐器（380 → 384）：萨摩亚树皮布、平克原住民挂毯（1989）、'
           '毛利亚麻斗篷、奥斯曼 nay 笛。①tapa 以**构树皮**经**浸—捶—拼—晒**的妇女劳动成布；②平克属**瓦尔马贾里人**、生于**大沙沙漠**，'
           '以**俯视抽象**写沙漠记忆，本件为 1976 **维多利亚挂毯工坊**限量小挂毯；③毛利斗篷**搓捻成布**、缀黑缨流苏（记录极简，不补纹样）；'
           '④nay 为**边棱吹管**、三节旋木嵌金属、十二指孔、三倍音域，土耳其版用于 **Mevlevi 旋转舞乐**。'
           '如实保留 tapa summary 的「装饰因…」**截断**不补写。站点 417 → 421 页，体检 12/12。")\n')
    anchor='if cyc=="cycle110":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **380**（L2 376 / L3 4 / L1 0） |","| 条目 | **384**（L2 380 / L3 4 / L1 0） |"),
    ("| 来源 | **509**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **513**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **417**，站内断链 **0** |","| 页面 | **421**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **380** | L2 376 / L3 4 / **L1 0** |","| 条目总数 | **384** | L2 380 / L3 4 / **L1 0** |"),
    ("| 来源库 | **509**（另 11 条预备来源未计入） |","| 来源库 | **513**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **417** |","| 站点页面 | **421** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **380**（L2 376 / L3 4，**无 L1**） |","| 条目 | **384**（L2 380 / L3 4，**无 L1**） |"),
    ("| 来源 | **509**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **513**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **417** |","| 站点页面 | **421** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])