# -*- coding: utf-8 -*-
"""Cycle70 收尾：D074 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D074 — Cycle70 乐器再补 4 条（228 → 232）；`check.py` 连抓两处缺陷
- **决定**：`music-instruments` 单元再补 4 条：`pipa-instrument`（琵琶·清代实物，95.4×27.4×8cm）、`koto-instrument`（江户筝，117.8cm）、`hitoyogiri-flute`（一節切，33.5×2.6cm）、`mangbetu-harp`（曼贝图五弦竖琴，柄36.9cm）。
- **`check.py` 抓到的两处真实缺陷（均已修）**：
  1. **R4/R18：来源 id 用了点号**——我在元组里写成 `cma-1921.914`，而来源库登记为 `cma-1921-914`（连字符）。校验器直接报「来源id未定义」+「引用不在来源库」。修法：统一改连字符。
  2. **R5：标题重复**——新条目 `pipa-instrument` 的标题 `琵琶` 与**已存在的 `pipa` 条目**重名。修法不是删除，而是改名 **「琵琶（清代实物）」** 并在 `related` 中指向既有 `pipa` 条目——**通用条目 + 实物条目**并存，互为补充。
- **四处内容要点**：
  1. **琵琶的名实与路线**：「pi 向前弹／pa 向后挑」是**右手动作**的名称来源；该馆以**壁画等历史图像**说明其沿**丝绸之路**自西亚中亚传入；19世纪中国琉特类常见**蝙蝠琴首**（谐「福」）。
  2. **江户筝是「观赏对象」**：装饰极繁（菊、芒草、柴垣、双蝶；彩漆＋蒔绘），该馆据此认为它**更可能被欣赏而非演奏**。
  3. **一節切的「小竹」身份**：被视为尺八一类，较普化更小、音量更弱，19世纪短暂复兴时称 kotake；**竹节位置在四正孔之间与背面拇指孔之间**是形制标志。
  4. **曼贝图竖琴的采集史**：细长头骨为曼贝图特征，常为男女歌者伴奏；该馆写明由克利夫兰艺术家 **Paul Travis 于 1928 年**在中非旅行时获得。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源；标题与关联可还原。
- **代价**：4 条均单机构；乐器单元 8 条，仍以东亚与非洲为主，**南亚除西塔外、东南亚、伊斯兰乐器仍缺**。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle70","date":"2026-11-23","status":"completed",
 "gap_methods":["乐器路线续推"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["pipa-instrument","koto-instrument","hitoyogiri-flute","mangbetu-harp"],
 "validator_catches":["R4/R18 来源id点号（cma-1921.914）","R5 标题重复（琵琶 vs 既有 pipa）"],
 "fixes":2,"instruments_total":8,
 "new_sources":4,"sources_total":363,"entries_total":232,"pages":268,
 "check_result":"errors=0","check_links_result":"broken=0(268页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle70","date":"2026-11-23","methods_used":["乐器续推"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"乐器 4→8 条（总 232）；校验器抓 2 缺陷并修；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle70"' not in t:
    block=('if cyc=="cycle70":\n'
           '    L.append("- 乐器单元再补 **4 条（228 → 232，乐器 4 → 8）**：琵琶（清代实物）、江户筝、一節切笛、曼贝图五弦竖琴。'
           '**`check.py` 连抓两处真实缺陷**：①**R4/R18** —— 来源 id 我写成带点号的 `cma-1921.914`，而库内是连字符，'
           '校验器立刻报「来源id未定义」「引用不在来源库」；②**R5** —— 新条目标题 `琵琶` 与**既有 `pipa` 条目重名**，'
           '修法是改名「**琵琶（清代实物）**」并关联既有条目，让**通用条目与实物条目并存**。'
           '四处要点：琵琶的名实（pi 前弹／pa 后挑）与丝路传入、蝙蝠琴首取「福」；江户筝装饰极繁故此馆认为**更可能被欣赏而非演奏**；'
           '一節切较普化更小更弱，19世纪复兴时称「小竹」，**竹节位置**是形制标志；曼贝图竖琴细长头骨为族属特征，'
           '且该馆写明由克利夫兰艺术家 **Paul Travis 1928 年**在中非获得。站点 264 → 268 页，体检 12/12。")\n')
    anchor='if cyc=="cycle69":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 228（L2 224 / L3 4 / L1 0） |","| 条目 | 232（L2 228 / L3 4 / L1 0） |"),
    ("| 来源 | 359（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 363（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 264，站内断链 **0** |","| 页面 | 268，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **228** | L2 224 / L3 4 / **L1 0** |","| 条目总数 | **232** | L2 228 / L3 4 / **L1 0** |"),
    ("| 来源库 | **359**（另 11 条预备来源未计入） |","| 来源库 | **363**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **264** |","| 站点页面 | **268** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])