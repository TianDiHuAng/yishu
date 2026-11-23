# -*- coding: utf-8 -*-
"""Cycle47 收尾：D050 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D050 — Cycle47 同法排查：又补 3 个整块遗漏（非洲 / 美洲原住民 / 太平洋），新增 3 单元 6 条目（171 → 177，单元 23 → 26）
- **排查方法**（承接 D049）：拿 AP Art History（O3）的十个内容区块逐一对 `catalog` 的 region/unit 取值，发现**三个区块零覆盖**：非洲（撒哈拉以南）、美洲原住民与前哥伦布、太平洋（大洋洲）。它们与伊斯兰艺术同属「从未被种下」——矩阵里也没有对应行，因此自我掩盖。
- **决定**：新增单元 `art-africa` / `art-americas` / `art-oceania`，并各建 2 条器物条目：
  - 非洲：`benin-plaque`（贝宁宫庭铜牌，1500—1600s，45.7×38.1）、`benin-ancestral-head`（祖灵纪念头像）；
  - 美洲：`maya-el-peru-stela`（埃尔佩鲁石碑，692年，274.4×182.3）、`aztec-feathered-serpent`（羽蛇，真伪未定）；
  - 大洋洲：`maori-hei-tiki`（毛利软玉吊坠）、`asmat-war-shield`（阿斯马特战盾，c.1940）。
- **三处必须写进正文的「不舒服内容」**（不写成脚注、不淡化）：
  1. **贝宁铜牌**：牌面左下编号即不列颠博物馆旧藏号；1898年入该馆，**前一年英军自王宫库房取走**。返还争议不代任何一方结论。
  2. **贝宁头像**：该馆自陈「与当下在美国博物馆的公开展示形成对照」——从祭坛的私人宗教器物到展柜陈列的语境转换，照录不删。
  3. **阿兹特克羽蛇**：该馆明确「无法断定是伪作」，表面分析「迄今没有帮助」，且躯体盘绕呈人形隆起、口部面具不合惯例。本条目**不作真伪定性**，把悬置状态本身写成内容。
- **可逆方式**：删 6 条 overlay 与 catalog 元组、移除 3 个单元与 6 条来源；`build_scope.py` 重跑。
- **代价**：6 条均单机构（`needs_verification`）；单元 23 → 26，`units.html`/sitemap/矩阵随之变化（已重生成并校验）。
- **遗留**：三个新单元暂无**导览条目**（伊斯兰艺术有），已在 BACKLOG 记为下一轮候选。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle47","date":"2026-11-23","status":"completed",
 "gap_methods":["按 AP 内容区块系统排查遗漏"],"network":"partial: museum APIs ok",
 "new_entries":6,"new_entry_ids":["benin-plaque","benin-ancestral-head","maya-el-peru-stela","aztec-feathered-serpent","maori-hei-tiki","asmat-war-shield"],
 "new_units":["art-africa","art-americas","art-oceania"],"units_total":26,
 "finding":"除伊斯兰艺术外，非洲/美洲原住民/太平洋三区块同样从未种下（矩阵自我掩盖）",
 "must_state_issues":["贝宁铜牌1897年被英军取走、1898入BM","贝宁头像祭坛→展柜语境转换","阿兹特克羽蛇真伪未定"],
 "new_sources":6,"sources_total":322,"entries_total":177,"pages":212,
 "check_result":"errors=0","check_links_result":"broken=0(212页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle47","date":"2026-11-23","methods_used":["AP区块排查"],
 "gaps_found":{"entries":6,"units":3,"note":"非洲/美洲/大洋洲整块遗漏"},"network":"partial (museum APIs)",
 "verdict":"补 3 整块（177/26单元）；殖民来源与真伪争议写入正文；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle47"' not in t:
    block=('if cyc=="cycle47":\n'
           '    L.append("- 承接上轮的漏项发现，**用同一方法系统排查**：拿 AP Art History 的十个内容区块逐一比对 catalog 的 region/unit，'
           '又发现**三个整块零覆盖**——非洲（撒哈拉以南）、美洲原住民与前哥伦布、太平洋。新增 3 单元 + 6 条目（171 → **177**，单元 23 → **26**）：'
           '贝宁铜牌与祖灵头像、埃尔佩鲁玛雅石碑、阿兹特克羽蛇、毛利软玉吊坠、阿斯马特战盾。'
           '三处「不舒服的内容」写进正文而非脚注：贝宁铜牌牌面左下编号即 BM 旧藏号（1898入藏，前一年英军自王宫库房取走）；'
           '贝宁头像该馆自陈「与当下在美国博物馆的公开展示形成对照」；**阿兹特克羽蛇真伪未定**——该馆明言无法断伪、表面分析无帮助，'
           '本条目不作定性，把悬置状态本身当成内容。站点 203 → 212 页，体检 8/8。")\n')
    anchor='if cyc=="cycle46":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 171（L2 165 / L3 6 / L1 0） |","| 条目 | 177（L2 171 / L3 6 / L1 0） |"),
    ("| 来源 | 316（全部 verified；隔离区 5 条不可核验） |","| 来源 | 322（全部 verified；隔离区 5 条不可核验） |"),
    ("| 页面 | 203，站内断链 **0** |","| 页面 | 212，站内断链 **0** |"),
    ("| 单元 | 23（新增伊斯兰艺术） |","| 单元 | 26（新增伊斯兰/非洲/美洲/太平洋） |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **171** | L2 165 / L3 6 / **L1 0** |","| 条目总数 | **177** | L2 171 / L3 6 / **L1 0** |"),
    ("| 来源库 | **316** |","| 来源库 | **322** |"),
    ("| 站点页面 | **203** |","| 站点页面 | **212** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])