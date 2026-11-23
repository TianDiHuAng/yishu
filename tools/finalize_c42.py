# -*- coding: utf-8 -*-
"""Cycle42 收尾：D045 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D045 — Cycle42 首批「同作品·双机构」条目：浮世绘三例（154 → 157）
- **决定**：不再只找「同一艺术家、不同作品」的弱双源，改为**先比对同作品**：用 CMA 的亚洲/工艺类候选（58 件，策展说明均 >200 字符）逐条到 V&A 检索同题同年代藏品，得到**三组真正的同作品双机构**，并各建一条：
  1. **《凯风快晴》（赤富士）**：CMA 1930.189（early 1830s）+ V&A O129067《晴日南风（Gaifū kaisei）》，纸本 25.2×37.4 cm；
  2. **《庄野 白雨》**：CMA 1948.306（1833）+ V&A O410702，纸本 22.9×34.9 cm；
  3. **《大桥安宅骤雨》**：CMA 1921.318（1857）+ V&A O420904，纸本 14.13×9.04 cm。
- **方法论收获**：自动标题比对因**变音符**（Ōhashi/Shōno）漏判——规范化应保留重音折叠；实际命中靠**系列名与日文罗马字并查**人工确认。已记入本条，供后续复用。
- **写作纪律**：两馆记录**并列而不合并**——尺寸只在有记录的一侧给，绝不把一侧的尺寸写成作品的尺寸；《大桥》两馆尺寸差异（14.13×9.04 对大判）**如实写出并列入待核实**，不推断版次。
- **可逆方式**：删 3 条 overlay 与 catalog 元组、移除 6 条来源，重跑 `build_scope.py`。
- **代价**：浮世绘条目归入 `art-asia` 且 medium 沿用「绘画」（与该单元既有 `ukiyo-e` 条目一致），实际材质在正文写为木版画。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle42","date":"2026-11-23","status":"completed",
 "gap_methods":["同作品跨机构比对（CMA↔V&A）"],"network":"partial: museum APIs ok",
 "new_entries":3,"new_entry_ids":["hokusai-red-fuji","hiroshige-shono","hiroshige-ohashi-atake"],
 "dual_institution_all":True,"new_sources":6,"sources_total":297,"entries_total":157,"pages":188,
 "finding":"自动标题比对因变音符漏判，需按系列名/罗马字并查；人工确认后得 3 组同作品双机构",
 "check_result":"errors=0","check_links_result":"broken=0(188页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle42","date":"2026-11-23","methods_used":["同作品比对"],
 "gaps_found":{"entries":3},"network":"partial (museum APIs)",
 "verdict":"3 条浮世绘「同作品双机构」条目（157）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle42"' not in t:
    block=('if cyc=="cycle42":\n'
           '    L.append("- 本轮把扩充方式**升级为「同作品跨机构比对」**：用 CMA 的 58 件亚洲/工艺候选逐条到 V&A 查同题同年代藏品，'
           '得到**三组真正的同作品双机构**并各建一条——**《凯风快晴》**（CMA 1930.189 + V&A O129067）、'
           '**《庄野 白雨》**（CMA 1948.306 + V&A O410702）、**《大桥安宅骤雨》**（CMA 1921.318 + V&A O420904），条目 154 → **157**。'
           '方法论收获：自动标题比对因**变音符**（Ōhashi / Shōno）漏判，须按系列名与罗马字并查后人工确认。'
           '写作纪律：两馆记录**并列不合并**，尺寸只在有记录一侧给；《大桥》两馆尺寸差异（14.13×9.04 对常见大判）如实写出并列入待核实。'
           '站点 185 → 188 页，八步体检 8/8。")\n')
    anchor='if cyc=="cycle41":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PP=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PP,encoding="utf-8").read()
for a,b in [("| 条目 | 154（L2 148 / L3 6 / L1 0） |","| 条目 | 157（L2 151 / L3 6 / L1 0） |"),
            ("| 来源 | 291（全部 verified；隔离区 5 条不可核验） |","| 来源 | 297（全部 verified；隔离区 5 条不可核验） |"),
            ("| 页面 | 185，站内断链 **0** |","| 页面 | 188，站内断链 **0** |")]:
    if a in s2: s2=s2.replace(a,b)
io.open(PP,"w",encoding="utf-8").write(s2)

PS=os.path.join(ROOT,"PROJECT_STATUS.md"); s3=io.open(PS,encoding="utf-8").read()
for a,b in [("| 条目总数 | **154** | L2 148 / L3 6 / **L1 0** |","| 条目总数 | **157** | L2 151 / L3 6 / **L1 0** |"),
            ("| 来源库 | **291** |","| 来源库 | **297** |"),
            ("| 站点页面 | **185** |","| 站点页面 | **188** |")]:
    if a in s3: s3=s3.replace(a,b)
s3=s3.rstrip()+"\n\n### Cycle42 追加（同作品双机构）\n\n《凯风快晴》《庄野 白雨》《大桥安宅骤雨》三条均为 **CMA 与 V&A 各藏印本**的同作品条目；两馆记录并列不合并，尺寸差异如实标注。条目 157 / 来源 297 / 页面 188。\n"
io.open(PS,"w",encoding="utf-8").write(s3)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-150:])