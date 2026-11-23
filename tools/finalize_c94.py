# -*- coding: utf-8 -*-
"""Cycle94 收尾：D097 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D097 — Cycle94 现代名作 4 条（316 → 320）
新增 `picasso-la-vie`（毕加索《人生》，1903，**核心**）、`braque-estaque-port`（布拉克《埃斯塔克港》，1906，**核心**）、
`monet-water-lilies-agapanthus`（莫奈《睡莲·百子莲》，约1915—26，**核心**）、`picasso-bottle-glass-fork`（毕加索《瓶、杯、叉》，1911—12，**核心**）。
四处要点：①《人生》缘起 Casagemas 自杀后的蓝色时期，冷色统摄；该馆对内容给出「写实/生命循环」两解，条目并列不裁定；
②布拉克野兽派海景以「色彩解放」与互补色短笔触表现兴奋，是其后立体主义的前史；
③莫奈《睡莲》以**删去地平与岸线**加巨幅横幅制造「无限感」；
④《瓶、杯、叉》是分析立体主义范例，字母「fe 20」「EAN」的含义该馆**明言只有艺术家知道**，条目照录不可解。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；现代艺术单元由少量人物条目扩展出**可核查的实物**，但抽象表现主义、超现实主义实物仍少。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle94","date":"2026-11-23","status":"completed",
 "gap_methods":["现代名作实物填补"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["picasso-la-vie","braque-estaque-port","monet-water-lilies-agapanthus","picasso-bottle-glass-fork"],
 "modern_masterworks":4,"new_sources":4,"sources_total":451,"entries_total":320,"pages":357,
 "check_result":"errors=0","check_links_result":"broken=0(357页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle94","date":"2026-11-23","methods_used":["现代名作"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"现代名作 0→4（总 320）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle94"' not in t:
    block=('if cyc=="cycle94":\n'
           '    L.append("- 现代艺术单元由人物条目扩展出**可核查实物**，本轮补 4 件（316 → 320）：毕加索《人生》、布拉克《埃斯塔克港》、'
           '莫奈《睡莲·百子莲》、毕加索《瓶、杯、叉》。①《人生》缘起 Casagemas 自杀后的蓝色时期，冷色统摄，'
           '该馆对内容给出「写实/生命循环」**两解并列**；②布拉克野兽派海景以**色彩解放**与互补色短笔触写兴奋，是其立体主义前史；'
           '③莫奈以**删去地平与岸线**＋巨幅横幅制造无限感；④《瓶、杯、叉》为分析立体主义范例，'
           '字母「fe 20」「EAN」含义该馆**明言只有艺术家知道**。站点 353 → 357 页，体检 12/12。")\n')
    anchor='if cyc=="cycle93":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **316**（L2 312 / L3 4 / L1 0） |","| 条目 | **320**（L2 316 / L3 4 / L1 0） |"),
    ("| 来源 | **447**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **451**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **353**，站内断链 **0** |","| 页面 | **357**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **316** | L2 312 / L3 4 / **L1 0** |","| 条目总数 | **320** | L2 316 / L3 4 / **L1 0** |"),
    ("| 来源库 | **447**（另 11 条预备来源未计入） |","| 来源库 | **451**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **353** |","| 站点页面 | **357** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **316**（L2 312 / L3 4，**无 L1**） |","| 条目 | **320**（L2 316 / L3 4，**无 L1**） |"),
    ("| 来源 | **447**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **451**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **353** |","| 站点页面 | **357** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])