# -*- coding: utf-8 -*-
"""Cycle84 收尾：D088 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D088 — Cycle84 欧洲巴洛克 4 件（280 → 284）
新增 `pedro-de-mena-peter`（德·梅纳彩绘木雕，约1663—70，**核心**）、`soldani-apollo-daphne`（索尔达尼陶土稿，约1700）、
`caravaggio-andrew`（卡拉瓦乔《圣安德烈受难》，1606—07，**核心**）、`la-tour-peter`（拉图尔《悔悟的圣彼得》，1645，**核心**）。
四处要点：①西班牙彩绘木雕是**团队协作**（主雕刻师/塑底/上色/嵌玻璃眼），肌肤与粗布用不同笔触制造真实感；
②索尔达尼据贝尼尼大理石稿，把「**正在变形的那一瞬**」作为巴洛克关切（新构图/瞬间/变形）；
③卡拉瓦乔把受难呈现为**亲密私密**事件而非公开酷刑，强烈明暗暗示神在场；该馆称其为画家**在美洲唯一祭坛画**；
④拉图尔与卡拉瓦乔的关系该馆明言「**仍不清楚**」，条目只并列明暗语言与题材相似，不写师承。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；欧洲巴洛克作品 4 件，仍缺建筑与更多版画。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle84","date":"2026-11-23","status":"completed",
 "gap_methods":["欧洲巴洛克作品填补"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["pedro-de-mena-peter","soldani-apollo-daphne","caravaggio-andrew","la-tour-peter"],
 "baroque_works":4,"new_sources":4,"sources_total":415,"entries_total":284,"pages":321,
 "check_result":"errors=0","check_links_result":"broken=0(321页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle84","date":"2026-11-23","methods_used":["欧洲巴洛克作品"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"欧洲巴洛克 0→4（总 284）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle84"' not in t:
    block=('if cyc=="cycle84":\n'
           '    L.append("- 欧洲巴洛克作品此前仅靠人物与流派条目支撑，本轮补 4 件（280 → 284）：德·梅纳彩绘木雕、'
           '索尔达尼《阿波罗与达芙妮》陶土稿、卡拉瓦乔《圣安德烈受难》、拉图尔《悔悟的圣彼得》。'
           '①西班牙彩绘木雕揭示**团队协作**（雕刻/塑底/上色/玻璃眼）与不同表面笔触；'
           '②索尔达尼据贝尼尼原作，把「**正在变形的一瞬**」做成形式主题；'
           '③卡拉瓦乔将受难改为**亲密私密**事件，强烈明暗暗示神在场，该馆称为其**在美洲唯一祭坛画**；'
           '④拉图尔与卡拉瓦乔的关系该馆明言**仍不清楚**，条目只并列形式相似、不写师承。站点 317 → 321 页，体检 12/12。")\n')
    anchor='if cyc=="cycle83":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 280（L2 276 / L3 4 / L1 0） |","| 条目 | 284（L2 280 / L3 4 / L1 0） |"),
    ("| 来源 | 411（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 415（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 317，站内断链 **0** |","| 页面 | 321，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **280** | L2 276 / L3 4 / **L1 0** |","| 条目总数 | **284** | L2 280 / L3 4 / **L1 0** |"),
    ("| 来源库 | **411**（另 11 条预备来源未计入） |","| 来源库 | **415**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **317** |","| 站点页面 | **321** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])