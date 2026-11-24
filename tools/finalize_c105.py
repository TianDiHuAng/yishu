# -*- coding: utf-8 -*-
"""Cycle105 收尾：D108 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D108 — Cycle105 大洋洲再补 4 条（356 → 360；大洋洲 11）
音乐两单元虽最薄，但其内容为「百科型」概念条目，新增需**新的可核验音乐来源**；在确认可核来源前不轻动，改继续收窄 `art-oceania`（原 7 条），用可核验 CMA 补 4 件：
`sepik-ancestral-figure`（塞皮克祖像，1800s，**核心**）、`sepik-hook-figure`（塞皮克钩形像·阿拉姆巴克，约1920—30，**核心**）、
`cook-ceremonial-adze`（曼加伊亚礼斧，1800s）、`ambrym-grade-figure`（安布里姆等级社会祖像，约1930，**核心**）。
四处要点：①塞皮克村落以**男子会所**为仪式中心，最神圣器物**避妇女儿童**，祖像藏其中；
②阿拉姆巴克「钩形像」表**战神/猎神**，出征前以特制物**擦拭以求神灵附体**，钩=羽、中央=心（新月形肋）、下=小腿；
③礼斧见**铁器与纪念品市场**带来的变局，木柄刻 **K 纹**、石刃以**椰绳编缚**，传说编绳纹样**由神授**；
④安布里姆以**蕨木干雕**巨像尊祖，配合**晋升等级庆典**，**巨头象征 mana**，原覆泥灰上彩。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；大洋洲 7 → 11 条，但**密克罗尼西亚与澳洲原住民**仍缺。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle105","date":"2026-11-24","status":"completed",
 "gap_methods":["大洋洲续深"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["sepik-ancestral-figure","sepik-hook-figure","cook-ceremonial-adze","ambrym-grade-figure"],
 "oceania_objects":11,"new_sources":4,"sources_total":489,"entries_total":360,"pages":397,
 "check_result":"errors=0","check_links_result":"broken=0(397页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle105","date":"2026-11-24","methods_used":["大洋洲续深"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"大洋洲 7→11（总360）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle105"' not in t:
    block=('if cyc=="cycle105":\n'
           '    L.append("- 大洋洲（`art-oceania` 7条）续补 4 件（356 → 360）：塞皮克祖像、塞皮克钩形像（阿拉姆巴克）、库克礼斧、安布里姆等级祖像。'
           '①塞皮克以**男子会所**为仪式中心、圣物**避妇孺**；②「钩形像」表**战神/猎神**，出征前**擦拭求附体**，钩=羽、中央=心、下=小腿；'
           '③礼斧见**铁器与纪念品市场**变局，木柄 **K 纹**、石刃**椰绳编缚**、传说**神授纹样**；④安布里姆**蕨木干雕**巨像、配合**晋升等级庆典**、**巨头=mana**。'
           '音乐两单元最薄但需**新的可核验音乐来源**，故本轮不动，改收窄大洋洲。站点 393 → 397 页，体检 12/12。")\n')
    anchor='if cyc=="cycle104":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **356**（L2 352 / L3 4 / L1 0） |","| 条目 | **360**（L2 356 / L3 4 / L1 0） |"),
    ("| 来源 | **485**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **489**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **393**，站内断链 **0** |","| 页面 | **397**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **356** | L2 352 / L3 4 / **L1 0** |","| 条目总数 | **360** | L2 356 / L3 4 / **L1 0** |"),
    ("| 来源库 | **485**（另 11 条预备来源未计入） |","| 来源库 | **489**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **393** |","| 站点页面 | **397** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **356**（L2 352 / L3 4，**无 L1**） |","| 条目 | **360**（L2 356 / L3 4，**无 L1**） |"),
    ("| 来源 | **485**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **489**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **393** |","| 站点页面 | **397** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])