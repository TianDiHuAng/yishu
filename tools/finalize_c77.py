# -*- coding: utf-8 -*-
"""Cycle77 收尾：D081 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D081 — Cycle77 伊斯兰写本与细密画 4 条（256 → 260）：补上「写本插图」这一缺门
- **背景**：伊斯兰单元此前 13 条全为器物（陶/金属），**写本与细密画为零**；D075 记过这一缺口。本轮检索得 36 件可写件，取 4 件。
- **决定**：新增 `great-mongol-shahnama-folio`（《大蒙古列王纪》屠龙叶，1330—35，45.8×34.4cm，**核心**）、`shiraz-frontispiece`（设拉子《列王纪》对页左半，1444）、`quran-folio-seljuq`（塞尔柱《古兰经》叶，1100s）、`panj-ganj-page`（贾米《五宝》复合册页，**核心**）。
- **四处要点**：
  1. **「借用的中国元素参与构成动势」**：屠龙叶中的**山石、树干与龙**取法中国样式；该馆的评语是「翻涌的山水与扭动的龙**以同等力度**表现，画面获得非凡的统一」——即外来母题非拼贴，而是参与形式统一。
  2. **卷首图画的是读者自己**：设拉子对页「**并不图解叙事**」，而很可能表现**该写本为其娱乐而作的宫廷观众**；且此叶**已从写本拆离**，**对页另一半在同馆（1945.169）**。
  3. **书的「物」也会被切分**：以两例并置（拆散的对页、以及下条的复合册页），把「写本作为整体物」的收藏史问题显性化。
  4. **复合册页的三重物证**：贾米《五宝》页——**文本1500—1520 赫拉特**（Sultan-Ali Mashhadi 为 Badi al-Zaman Mirza 抄）、**绘画与边饰1603—07 德干**（Mushfiq 为莫卧儿大臣 Abd al-Rahim 补）、收藏者为阿克巴与贾汉吉尔两朝重臣。**该记录无尺寸字段，本条目不列尺寸。**
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构；写本类 4 条，**奥斯曼与马穆鲁克写本、伊斯兰建筑（除砖与钢板外）仍缺**。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle77","date":"2026-11-23","status":"completed",
 "gap_methods":["伊斯兰写本/细密画填补"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["great-mongol-shahnama-folio","shiraz-frontispiece","quran-folio-seljuq","panj-ganj-page"],
 "islamic_total":17,"manuscripts":4,
 "must_state":["屠龙叶的中国式元素参与形式统一","卷首图画的是宫廷观众且已拆离（另一半在同馆）","古兰经叶两面 23+23 行出处","《五宝》页两段工序（赫拉特抄/德干绘）与收藏者；无尺寸"],
 "new_sources":4,"sources_total":391,"entries_total":260,"pages":297,
 "check_result":"errors=0","check_links_result":"broken=0(297页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle77","date":"2026-11-23","methods_used":["伊斯兰写本"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"伊斯兰写本 0→4（伊斯兰共 17，总 260）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle77"' not in t:
    block=('if cyc=="cycle77":\n'
           '    L.append("- **补上「写本与细密画」缺门**（伊斯兰单元原 13 条全为器物）：新增 4 条（总 256 → 260）——'
           '《大蒙古列王纪》屠龙叶、设拉子《列王纪》对页左半、塞尔柱《古兰经》叶、贾米《五宝》复合册页。'
           '四处要点：①屠龙叶的**山石、树干与龙取法中国**，该馆称「翻涌山水与扭动之龙**以同等力度**表现」'
           '——外来母题**参与形式统一**而非拼贴；②卷首图**并不图解叙事**，很可能画的是**宫廷观众自身**，'
           '且此叶**已从写本拆离**、**对页另一半在同馆（1945.169）**；③古兰经叶两面各 23 行、出处分别标为 56:1—26 与 55:73—78；'
           '④《五宝》页是**复合工序**：文本 1500—1520 赫拉特抄成、绘画与边饰 1603—07 在德干补作，收藏者为莫卧儿重臣 Abd al-Rahim；'
           '**该记录无尺寸字段，故本条目不列尺寸**。站点 293 → 297 页，体检 12/12。")\n')
    anchor='if cyc=="cycle76":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 256（L2 252 / L3 4 / L1 0） |","| 条目 | 260（L2 256 / L3 4 / L1 0） |"),
    ("| 来源 | 387（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 391（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 293，站内断链 **0** |","| 页面 | 297，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **256** | L2 252 / L3 4 / **L1 0** |","| 条目总数 | **260** | L2 256 / L3 4 / **L1 0** |"),
    ("| 来源库 | **387**（另 11 条预备来源未计入） |","| 来源库 | **391**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **293** |","| 站点页面 | **297** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])