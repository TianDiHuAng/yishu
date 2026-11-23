# -*- coding: utf-8 -*-
"""Cycle43 收尾：D046 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D046 — Cycle43 以「馆藏作品」填补长期受阻的覆盖缺口（157 → 161）
- **背景**：A 类/B2 类缺口此前一直记为「需可核验内容来源」，而 Wikipedia/Met/Tate 不可达。本轮改走**馆藏记录**路线，用 Cleveland 的策展说明直接建作品条目，**在不降低标准的前提下**填掉了四个实缺口。
- **新增 4 条（均为单机构 → needs_verification）**：
  1. `indian-standing-buddha-kashmir` 克什米尔立佛（约900年，黄铜嵌银铜，98.1 cm）→ 补**印度佛教艺术**（此前因无来源被列为拒建）；
  2. `mathura-railing-pillar` 马图拉栏楯柱（100年代，红砂岩）→ 补**南亚雕塑**；
  3. `chen-hongshou-album` 陈洪绶《仿古册》（1598—1652）→ 补**明代绘画**作品实例；
  4. `zhao-mengfu-river-village` 赵孟頫《河村渔乐》（约1302—03）→ 补**元代绘画**作品实例。
- **亦真亦谨的处理**：
  - 克什米尔立佛：该馆说明中「造像约900年」与「座上题记人物活动约998—1026年」存在时间差，本条目**不调和**，而是把它当作两件事实分别陈述并列入待核实；
  - 马图拉柱：基座第二场景该馆用 possibly/probably 措辞，条目**保留推测语气**；
  - 陈洪绶、赵孟頫：该馆评价性用语（archaistic/quirky、南人仕元）**标注为「该馆称」**，不作通说。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均带 `needs_verification`，因为确无第二机构；但这比"因噎废食不建"更符合"诚实标注"——条目存在、事实有出处、独立性缺口公开。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle43","date":"2026-11-23","status":"completed",
 "gap_methods":["馆藏记录填补 A/B 类缺口","变音折叠配对（无新配对）"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["indian-standing-buddha-kashmir","mathura-railing-pillar","chen-hongshou-album","zhao-mengfu-river-village"],
 "gaps_closed":["印度佛教艺术作品实例","南亚雕塑（马图拉）","明代绘画作品实例","元代绘画作品实例"],
 "single_institution_flagged":4,"new_sources":4,"sources_total":301,"entries_total":161,"pages":192,
 "pair_detection":"变音折叠后仅 4 例同名，全部年代不符（同名异作），无新增双机构配对",
 "check_result":"errors=0","check_links_result":"broken=0(192页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle43","date":"2026-11-23","methods_used":["馆藏记录补缺口"],
 "gaps_found":{"entries":4,"closed":["印度佛教","南亚雕塑","明代","元代"]},"network":"partial (museum APIs)",
 "verdict":"4 条馆藏作品填补实缺口（161）；均单机构已标记；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle43"' not in t:
    block=('if cyc=="cycle43":\n'
           '    L.append("- 用**馆藏作品**填补长期受阻的覆盖缺口（157 → 161）：克什米尔立佛（约900）、马图拉栏楯柱（100年代）、'
           '陈洪绶《仿古册》、赵孟頫《河村渔乐》——分别补上**印度佛教艺术 / 南亚雕塑 / 明代 / 元代**的具体作品实例。'
           '这些缺口此前一直记为「需可核验内容来源」而搁置，本轮证明：**馆藏策展记录本身就是可核验来源**。'
           '亦真亦谨的处理：立佛的年代与座上题记人物活动年代的时间差**不调和**而是并列进待核实；'
           '马图拉柱基座第二场景保留该馆的推测措辞；陈洪绶、赵孟頫的评价性用语标注为「该馆称」。'
           '另做变音折叠配对复核：仅 4 例同名且全部年代不符（同名异作），无新增双机构配对。站点 188 → 192 页，体检 8/8。")\n')
    anchor='if cyc=="cycle42":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 157（L2 151 / L3 6 / L1 0） |","| 条目 | 161（L2 155 / L3 6 / L1 0） |"),
    ("| 来源 | 297（全部 verified；隔离区 5 条不可核验） |","| 来源 | 301（全部 verified；隔离区 5 条不可核验） |"),
    ("| 页面 | 188，站内断链 **0** |","| 页面 | 192，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **157** | L2 151 / L3 6 / **L1 0** |","| 条目总数 | **161** | L2 155 / L3 6 / **L1 0** |"),
    ("| 来源库 | **297** |","| 来源库 | **301** |"),
    ("| 站点页面 | **188** |","| 站点页面 | **192** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-150:])