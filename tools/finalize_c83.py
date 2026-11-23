# -*- coding: utf-8 -*-
"""Cycle83 收尾：D087 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D087 — Cycle83 中国书法作品 4 条（276 → 280）
新增 `yueshan-daizong-calligraphy`（越山道宗行草，约1660—1709）、`lizong-wangwei-album`（宋理宗书王维诗册页，1256，**核心**）、
`lanting-lacquer-panel`（兰亭雅集朱漆雕板，1400—1500s）、`chen-jiru-four-poems`（陈继儒行书四诗，1500—1600s，**核心**）。
四处要点：①越山自福建赴日、任黄檗宗万福寺第七代住持，其圆转连笔成为该宗修行者的典型书风；
②宋理宗书王维诗、马麟画作原合装一扇，是皇室—宫廷画家合作，并牵出杭州宫廷/文官/寺院间的禅美学；
③兰亭题材由353年的事件经绘画转入漆、玉、瓷，王羲之观鹅上移表明工艺表面不遵循手卷叙事；
④陈继儒书风近董其昌却焚儒服、拒征召——风格相近而人生选择相反。
并记录：馆方英文标题写 cursive script 但括注 xingshu（行书），本条依括注定体，留待核原作。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；书法作品从术语条目扩展到 4 件实物，仍缺王羲之、颜真卿等早期大家的可靠实物。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle83","date":"2026-11-23","status":"completed",
 "gap_methods":["中国书法作品填补"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["yueshan-daizong-calligraphy","lizong-wangwei-album","lanting-lacquer-panel","chen-jiru-four-poems"],
 "calligraphy_works":4,"new_sources":4,"sources_total":411,"entries_total":280,"pages":317,
 "check_result":"errors=0","check_links_result":"broken=0(317页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle83","date":"2026-11-23","methods_used":["中国书法作品"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"书法作品 0→4（总 280）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle83"' not in t:
    block=('if cyc=="cycle83":\n'
           '    L.append("- **中国书法此前只有术语条目**，本轮补 4 件作品（276 → 280）：越山道宗行草、宋理宗书王维诗册页、'
           '兰亭雅集朱漆雕板、陈继儒行书四诗。①越山自福建赴日、任黄檗宗万福寺第七代住持，圆转连笔成该宗典型书风；'
           '②帝书与马麟画原合装一扇，牵出杭州宫廷/文官/寺院间的禅美学；③兰亭题材由353年事件转入漆玉瓷，'
           '「观鹅」上移说明工艺表面不遵循手卷叙事；④陈继儒书风近董其昌却**焚儒服、拒征召**——风格相近而人生选择相反。'
           '馆方英文标题写 cursive script 却括注 xingshu（行书），条目依括注定体并留待核原作。站点 313 → 317 页，体检 12/12。")\n')
    anchor='if cyc=="cycle82":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 276（L2 272 / L3 4 / L1 0） |","| 条目 | 280（L2 276 / L3 4 / L1 0） |"),
    ("| 来源 | 407（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 411（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 313，站内断链 **0** |","| 页面 | 317，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **276** | L2 272 / L3 4 / **L1 0** |","| 条目总数 | **280** | L2 276 / L3 4 / **L1 0** |"),
    ("| 来源库 | **407**（另 11 条预备来源未计入） |","| 来源库 | **411**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **313** |","| 站点页面 | **317** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])