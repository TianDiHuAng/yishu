# -*- coding: utf-8 -*-
"""Cycle91 收尾：D094 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D094 — Cycle91 日本佛教雕塑 4 条（304 → 308）
新增 `miroku-asuka`（飞鸟弥勒，7世纪末，**核心**）、`nikko-bodhisattva`（平安日光菩萨，约800）、
`kofukuji-seated-buddha`（平安兴福寺周边坐佛，12世纪，**核心**）、`amida-shitennoji`（1269四天王寺阿弥陀像，**核心**）。
四处要点：①佛教6世纪传入日本，未来佛救赎对贵族尤有共鸣，小型礼拜像流行；
②日光菩萨衣纹与曲姿取法中国，但单块粗榧木的木纹与雕刻互动是日本创新，原与月光菩萨夹护药师；
③坐佛右手施无畏印，左手为替换件导致身份不明（药师或释迦），保留两说；
④阿弥陀像呈迎接姿态，像内文书含《阿弥陀经》、结缘名簿与「33日造成于四天王寺」记录。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；日本佛教雕塑由 0 增至 4，仍缺奈良大佛、镰仓大佛等巨构。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle91","date":"2026-11-23","status":"completed",
 "gap_methods":["日本佛教雕塑"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["miroku-asuka","nikko-bodhisattva","kofukuji-seated-buddha","amida-shitennoji"],
 "japanese_buddhist_sculpture":4,"new_sources":4,"sources_total":439,"entries_total":308,"pages":345,
 "check_result":"errors=0","check_links_result":"broken=0(345页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle91","date":"2026-11-23","methods_used":["日本佛教雕塑"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"日本佛教雕塑 0→4（总 308）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle91"' not in t:
    block=('if cyc=="cycle91":\n'
           '    L.append("- 日本佛教雕塑此前近乎为零，本轮补 4 条（304 → 308）：飞鸟弥勒、日光菩萨、兴福寺周边坐佛、四天王寺阿弥陀像。'
           '①佛教6世纪传入、未来佛救赎对贵族有共鸣，小型礼拜像流行；②日光菩萨衣纹/曲姿取法中国，但**单块粗榧木的木纹与雕刻互动**为日本创新；'
           '③坐佛**左手为替换件**导致身份不明（药师或释迦），条目保留两说；④阿弥陀像像内文书含《阿弥陀经》、**结缘名簿**与「33日造成于四天王寺」记录。'
           '站点 341 → 345 页，体检 12/12。")\n')
    anchor='if cyc=="cycle90":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **304**（L2 300 / L3 4 / L1 0） |","| 条目 | **308**（L2 304 / L3 4 / L1 0） |"),
    ("| 来源 | **435**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **439**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **341**，站内断链 **0** |","| 页面 | **345**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **304** | L2 300 / L3 4 / **L1 0** |","| 条目总数 | **308** | L2 304 / L3 4 / **L1 0** |"),
    ("| 来源库 | **435**（另 11 条预备来源未计入） |","| 来源库 | **439**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **341** |","| 站点页面 | **345** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **304**（L2 300 / L3 4，**无 L1**） |","| 条目 | **308**（L2 304 / L3 4，**无 L1**） |"),
    ("| 来源 | **435**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **439**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **341** |","| 站点页面 | **345** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])