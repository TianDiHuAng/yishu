# -*- coding: utf-8 -*-
"""Cycle88 收尾：D091 + METRICS/REPORT/PROGRESS/PROJECT_STATUS（300 条目里程碑）。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D091 — Cycle88 达到 300 条目（296 → 300）；补 4 件巴洛克雕塑/绘画
新增 `puget-sauli-study`（皮热小稿，1663—68）、`parodi-sleeping-christ`（帕罗迪《睡着的基督圣婴》，约1675，**核心**）、
`doccia-spring-relief`（多西亚瓷厂《春》浮雕，18世纪中期）、`liss-cupid`（利斯《丘比特》，约1630，**核心**）。
四处要点：①小稿中**摊开的书**指改革事业、**扭转身体**指个人异象；②帕罗迪以**不同抛光度**区分肌肤与稻草，
睡眠作为死亡隐喻引导冥想；③多西亚瓷厂1743年购索尔达尼后裔手中的1708年四季模型，将雕塑转译为瓷；
④利斯融合**威尼斯色彩**与**卡拉瓦乔明暗**，该馆对威尼斯前辈未定（提香/丁托列托/委罗内塞）。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；达到 300 条目，但**覆盖仍不均衡**（欧洲与中国仍占多数，非西方地区虽已起步仍薄）。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle88","date":"2026-11-23","status":"completed",
 "gap_methods":["巴洛克作品填补"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["puget-sauli-study","parodi-sleeping-christ","doccia-spring-relief","liss-cupid"],
 "milestone":"300 entries","new_sources":4,"sources_total":431,"entries_total":300,"pages":337,
 "check_result":"errors=0","check_links_result":"broken=0(337页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle88","date":"2026-11-23","methods_used":["巴洛克作品"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"达到 300 条目；未饱和（覆盖不均衡）"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle88"' not in t:
    block=('if cyc=="cycle88":\n'
           '    L.append("- **达到 300 条目**（296 → 300）：皮热《圣阿莱桑德罗·绍利》小稿、帕罗迪《睡着的基督圣婴》、'
           '多西亚瓷厂《春》浮雕、利斯《丘比特》。①小稿中**摊开的书**指改革事业、**扭身**指个人异象；'
           '②帕罗迪用**不同抛光度**区分肌肤与稻草，睡眠作为死亡隐喻引导冥想；'
           '③多西亚瓷厂1743年购索尔达尼后裔手中的1708年四季模型，把雕塑转译为瓷；'
           '④利斯融合**威尼斯色彩**与**卡拉瓦乔明暗**，馆方对威尼斯前辈未定（提香/丁托列托/委罗内塞）。'
           '站点 333 → 337 页，体检 12/12。**300 是数量里程碑，不等于覆盖均衡**。")\n')
    anchor='if cyc=="cycle87":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 296（L2 292 / L3 4 / L1 0） |","| 条目 | **300**（L2 296 / L3 4 / L1 0） |"),
    ("| 来源 | 427（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 431（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 333，站内断链 **0** |","| 页面 | 337，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **296** | L2 292 / L3 4 / **L1 0** |","| 条目总数 | **300** | L2 296 / L3 4 / **L1 0** |"),
    ("| 来源库 | **427**（另 11 条预备来源未计入） |","| 来源库 | **431**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **333** |","| 站点页面 | **337** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])