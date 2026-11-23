# -*- coding: utf-8 -*-
"""Cycle51 收尾：D054 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D054 — Cycle51 深度推进 5 条（180 → 185）；并如实说明「想补约鲁巴，结果得到 Nok」
- **决定**：按上轮评估的薄弱区块推进，新增 5 条：莫切蝙蝠形陶瓶、印加束腰外衣、**Nok 陶塑头像**、高丽青瓷镶嵌菊纹瓶、缅甸 Kammavacha 戒律文书。
- **必须说明的一处偏差**：我原本要补 **约鲁巴**，检索也是以 yoruba 为关键词；但筛出的可写件（说明 >250 字符且质量最高者）实际是 **Nok 文化**（尼日利亚中部，公元前1千纪—公元后数世纪）的赤陶头像——**Nok ≠ 约鲁巴**，二者文化与年代都不同。因此本轮**约鲁巴仍为零覆盖**，不得算作已补。条目按实际对象命名为 `nok-terracotta-head`，不冒充约鲁巴。
- **三处「博物馆自身多说并存」的处理**：
  1. **Nok 年代三说**：该馆文化栏写「500 BCE–200 CE **或** 1500–1 BCE」，本件热释光测年为 **20–620 CE**。三者**不调和**，并列写入待核实，正文分别陈述。
  2. **女性制作者**：该馆把作者记为「unknown female ceramicist」，论据是「这些作品所含成型与烧造技术只有女性使用」；条目照录该论据，并注明**具体技术细目未取得**。
  3. **高丽青瓷的金继修补**：该馆把日本 kintsugi（15世纪起）写进说明；条目据此指出「一件高丽青瓷在近代被以日本方法修复，说明它已被视为极受珍视的藏品」——器物价值跨越原产文化。
- **两处技术性修正**：`inca-tunic` 的 unit 我误写成 `art-asia`，已改为 `art-americas`；导入时 `related` 由构建自动对称化（新增 187 条、悬空 0），无需手工补反向。
- **可逆方式**：删 5 条 overlay 与 catalog 元组、移除 5 条来源，重跑 `build_scope.py`。
- **代价**：5 条均单机构（`needs_verification`）；**约鲁巴、安第斯其他文化（纳斯卡/奇穆）、朝鲜以外东亚陶瓷仍未覆盖**。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle51","date":"2026-11-23","status":"completed",
 "gap_methods":["按区块深度推进"],"network":"partial: museum APIs ok",
 "new_entries":5,"new_entry_ids":["moche-bat-vessel","inca-tunic","nok-terracotta-head","goryeo-celadon-bottle","kammavacha-manuscript"],
 "intent_vs_result":"拟补约鲁巴，实际得到 Nok 文化（不同文化），约鲁巴仍零覆盖",
 "multi_source_discrepancies":["Nok 年代三说（文化栏两说 + 热释光 20–620 CE）","Nok 女性制作者论据细目未取得","高丽青瓷金继修补的跨文化价值"],
 "new_sources":5,"sources_total":327,"entries_total":185,"pages":220,
 "check_result":"errors=0","check_links_result":"broken=0(220页)","audit_all":"9/9 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle51","date":"2026-11-23","methods_used":["按区块深度推进"],
 "gaps_found":{"entries":5,"note":"约鲁巴未被覆盖（所得为 Nok）"},"network":"partial (museum APIs)",
 "verdict":"新增 5 条（185）；约鲁巴仍零覆盖已如实记录；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle51"' not in t:
    block=('if cyc=="cycle51":\n'
           '    L.append("- 按区块深度推进，新增 **5 条（180 → 185）**：莫切蝙蝠形陶瓶、印加束腰外衣、Nok 陶塑头像、'
           '高丽青瓷镶嵌菊纹瓶、缅甸 Kammavacha 戒律文书。'
           '**一处偏差如实记录**：我本拟补**约鲁巴**（检索也用 yoruba），但筛出的可写件实际是 **Nok 文化**（尼日利亚中部，年代与文化皆不同），'
           '故条目按实际对象命名，**约鲁巴仍为零覆盖**，不得算作已补。'
           '三处「馆方多说并存」照录不调和：Nok 年代有文化栏两说与热释光 20–620 CE 三说；'
           '「女性制作者」的论据（成型与烧造技术仅女性使用）细目未取得；高丽青瓷的日本 kintsugi 近代修补提示其价值已跨文化。'
           '技术上修正 `inca-tunic` 误置于 art-asia，并确认 related 由构建自动对称化（187 条、悬空 0）。站点 215 → 220 页，体检 9/9。")\n')
    anchor='if cyc=="cycle50":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 180（L2 174 / L3 6 / L1 0） |","| 条目 | 185（L2 179 / L3 6 / L1 0） |"),
    ("| 来源 | 322（全部 verified；隔离区 5 条不可核验） |","| 来源 | 327（全部 verified；隔离区 5 条不可核验） |"),
    ("| 页面 | 215，站内断链 **0** |","| 页面 | 220，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **180** | L2 174 / L3 6 / **L1 0** |","| 条目总数 | **185** | L2 179 / L3 6 / **L1 0** |"),
    ("| 来源库 | **322** |","| 来源库 | **327** |"),
    ("| 站点页面 | **215** |","| 站点页面 | **220** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])