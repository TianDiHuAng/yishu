# -*- coding: utf-8 -*-
"""Cycle85 收尾：D089 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D089 — Cycle85 西方乐器/演奏图像 4 条（284 → 288）
新增 `braque-violin-collage`（布拉克《小提琴》拼贴，1914，**核心**）、`dumont-harpsichord-miniature`（羽管键琴前女子细密画，约1788）、
`lancret-cello-drawing`（朗克雷大提琴手稿，约1725—30）、`dusart-violin-tavern`（杜萨特酒馆小提琴手，1685）。
四处要点：①布拉克1912年发明拼贴纸，本作以报纸、木纹纸、花纹纸和炭笔构成小提琴与玻璃杯，制造**交错平面**；
②18世纪弹琴被视为贵族女性**必备修养**，画中人身份不明、索菲·阿尔努说仅来自被归于他人的副本；
③朗克雷的大提琴手后来进入户外音乐会油画，本稿特写**运弓手的紧握**；
④荷兰酒馆版画以音乐/酒/西勒诺斯联想与拉丁诗句构成**社会对照与纵酒警示**。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；其中 3 件为演奏图像而非乐器实物，`music-instruments` 单元边界较宽。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle85","date":"2026-11-23","status":"completed",
 "gap_methods":["西方乐器/演奏图像"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["braque-violin-collage","dumont-harpsichord-miniature","lancret-cello-drawing","dusart-violin-tavern"],
 "music_images":4,"new_sources":4,"sources_total":419,"entries_total":288,"pages":325,
 "check_result":"errors=0","check_links_result":"broken=0(325页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle85","date":"2026-11-23","methods_used":["西方演奏图像"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"西方乐器/演奏图像 0→4（总 288）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle85"' not in t:
    block=('if cyc=="cycle85":\n'
           '    L.append("- 西方乐器此前只有古琴/琵琶等非西方实物，本轮补 4 件演奏图像与一件拼贴（284 → 288）：'
           '布拉克1914年拼贴《小提琴》、杜蒙羽管键琴细密画、朗克雷大提琴手稿、杜萨特酒馆小提琴手。'
           '①布拉克1912年发明的拼贴纸把报纸、木纹纸、花纹纸与炭笔叠成小提琴与玻璃杯，制造**交错平面**；'
           '②18世纪弹琴被视为贵族女性**必备修养**，细密画中人身份不明，索菲·阿尔努说仅来自被归于他人的副本；'
           '③大提琴手稿后来进入户外音乐会油画，特写**运弓之手**；④荷兰酒馆版画以音乐、酒、西勒诺斯联想与拉丁诗句构成**纵酒警示**。'
           '站点 321 → 325 页，体检 12/12。")\n')
    anchor='if cyc=="cycle84":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 284（L2 280 / L3 4 / L1 0） |","| 条目 | 288（L2 284 / L3 4 / L1 0） |"),
    ("| 来源 | 415（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 419（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 321，站内断链 **0** |","| 页面 | 325，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **284** | L2 280 / L3 4 / **L1 0** |","| 条目总数 | **288** | L2 284 / L3 4 / **L1 0** |"),
    ("| 来源库 | **415**（另 11 条预备来源未计入） |","| 来源库 | **419**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **321** |","| 站点页面 | **325** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])