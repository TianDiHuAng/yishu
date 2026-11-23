# -*- coding: utf-8 -*-
"""Cycle71 收尾：D075 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D075 — Cycle71 伊斯兰单元加深（232 → 236；伊斯兰 5 → 9）
- **决定**：新增 `iznik-mosque-lamp`（清真寺灯，1585—95，28.4×19.5cm）、`minai-beaker`（米纳伊人物杯，1180—1220，13.3×12.3cm）、`luster-dish-prince`（卡尚光泽彩盘，1170—1220，7.5×39cm）、`iznik-tile-spandrel`（伊兹尼克拱肩砖，约1570—75，76×29.9×2.5cm）。
- **四处「名义功能 vs 实际功能」或「技术史」要点**：
  1. **清真寺灯可能不照明**：因本件**不透光**，该馆判断其主要功能**很可能不是照明**，而是**悬于寺内/陵墓增添美感**；并另提一个**声学猜想**（减弱大厅回响）——条目**并列三说，不替馆方择一**。
  2. **米纳伊＝首次真多彩**：名称出自波斯语「珐琅」；**釉上彩**使红与黑得以实现（釉下做不到），故为「真正的多彩陶瓷」；图样**承接写本插图**（列坐宫廷、登座统治者、王子狩猎）。
  3. **光泽彩盘的稀有做法**：**光泽地为底、蓝釉为纹**；卡尚与**巴士拉、福斯塔特**并为中心，说明这是跨区域奢侈品而非孤例。
  4. **拱肩砖只是「一半」**：与**已失的右半**原构成龛/窗/门上方的装饰拱；**浓烈红色靠浓稠铁质化妆土**实现，是该时期的技术成就。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构；伊斯兰 9 条集中于伊兹尼克与卡尚两地（奥斯曼陶与塞尔柱陶），**伊斯兰建筑本体与手抄本插图仍缺**。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle71","date":"2026-11-23","status":"completed",
 "gap_methods":["伊斯兰单元加深"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["iznik-mosque-lamp","minai-beaker","luster-dish-prince","iznik-tile-spandrel"],
 "islamic_total":9,
 "must_state":["清真寺灯主功能非照明（三说并列）","米纳伊＝首次真多彩（釉上彩）","光泽彩蓝釉于光泽地","拱肩砖仅存一半"],
 "new_sources":4,"sources_total":367,"entries_total":236,"pages":272,
 "check_result":"errors=0","check_links_result":"broken=0(272页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle71","date":"2026-11-23","methods_used":["伊斯兰加深"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"伊斯兰 5→9（总 236）；功能与技术的三说并列；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle71"' not in t:
    block=('if cyc=="cycle71":\n'
           '    L.append("- 伊斯兰单元加深 **5 → 9 条（总 232 → 236）**：伊兹尼克清真寺灯、卡尚米纳伊人物杯、卡尚光泽彩盘、'
           '伊兹尼克拱肩砖。四处「名义 vs 实际」或技术史要点：①**清真寺灯因不透光，主功能很可能不是照明**，'
           '而是悬于寺内添美，该馆另提**声学猜想**（减弱回响）——条目**三说并列不择一**；'
           '②**米纳伊＝首次真正多彩陶瓷**：釉上彩方能出红与黑，图样承接**写本插图**（列坐宫廷、狩猎）；'
           '③光泽彩盘以**光泽地为底、蓝釉为纹**见称，卡尚与**巴士拉、福斯塔特**并为中心；'
           '④拱肩砖**只是「一半」**（右半已失），原本构成门上装饰拱，浓烈红色靠**铁质化妆土**实现。站点 268 → 272 页，体检 12/12。")\n')
    anchor='if cyc=="cycle70":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 232（L2 228 / L3 4 / L1 0） |","| 条目 | 236（L2 232 / L3 4 / L1 0） |"),
    ("| 来源 | 363（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 367（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 268，站内断链 **0** |","| 页面 | 272，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **232** | L2 228 / L3 4 / **L1 0** |","| 条目总数 | **236** | L2 232 / L3 4 / **L1 0** |"),
    ("| 来源库 | **363**（另 11 条预备来源未计入） |","| 来源库 | **367**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **268** |","| 站点页面 | **272** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])