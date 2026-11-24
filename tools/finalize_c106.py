# -*- coding: utf-8 -*-
"""Cycle106 收尾：D109（V&A 来源首次启用 + 韩国/伊斯兰 4 条 + BLOCKER 记音乐来源不可达）。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D109 — Cycle106 启用 V&A API 来源，补韩国/伊斯兰 4 条（360 → 364）；音乐史来源不可达记 BLOCKER
- **来源可达性实测**：Wikipedia(000)、IMSLP(000)、Met(000)、Britannica(403)、Oxford Music Online(302 付费墙)；**仅 V&A API 200**。
  → **结论**：music-medieval / music-renaissance 等音乐文本单元，**新增条目缺乏可核验来源**，本轮不动，记入 BLOCKERS（见下）。
- **首次启用 V&A 来源**（此前 0 条），其详情 API 字段丰富（physicalDescription / materialsAndTechniques / dimensions / summaryDescription），足以支撑 L2 正文。
  新增 `korean-celadon-bottle`（高丽青瓷镶嵌铜红长颈瓶，1200—1250，**核心**）、`korean-celadon-bowl-lotus`（高丽青瓷莲童碗，1200—1250，**核心**）、
  `korean-white-flask-longevity`（朝鲜白瓷寿纹扁壶，1750—1800）、`kashan-salting-mihrab`（卡尚米哈拉布釉砖，约1300，**核心**）。
- **四处要点**：①高丽青瓷以**黑白镶嵌**成图绘性，并试点**釉下铜红**；②莲童碗留**三支烧痕**＝装烧方式的物证；
  ③朝鲜白瓷史：**918—1392 高丽朝已产白瓷**，至19世纪白瓷主导；壶上**堆白蝙蝠环「壽」**，足底**谚文款录文存疑**（不补正）；
  ④卡尚米哈拉布原为**墓葬标志**，其拱形为**清真寺朝向龛（米哈拉布）的缩微**；记录在「亡者身份」句处**截断，未补写**。
- **工程事件（R22 再次立功）**：V&A systemNumber 含大写 **O**（如 `O22419`），被 R22「id 只许小写字母/数字/连字符」拦下；统一改为 `vam-o22419` 后通过。
  另修两处自查：overlay 节名误作「与前后风格的不同与争议」→ 改回 R7 要求的「与前后风格的关系和争论」；QC 的 V&A 尺寸分支兼容 dict/list。
- **QC**：全量 **219 条、157 尺寸项、0 问题**。
- 可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条 V&A 来源。
- 代价：4 条均单一机构（V&A）；韩国瓷器由此起步，但**韩国绘画/佛教雕塑**仍缺。
""")
# BLOCKERS
bp=os.path.join(ROOT,"BLOCKERS.md"); bs=io.open(bp,encoding="utf-8").read() if os.path.exists(bp) else ""
add="""
## B-music-src（Cycle106 记录）— 音乐史文本来源当前不可达
- 实测 2026-11-24：en.wikipedia=000、imslp.org=000、metmuseum.org=000、britannica.com=403、oxfordmusiconline.com=302（付费墙）；仅 api.vam.ac.uk=200。
- 影响：`music-medieval`(4)、`music-renaissance`(3) 等音乐文本单元，**新增条目无法取得可核验来源**，故暂停新增，不做无源凑数。
- 现有音乐条目所用 `enc-*` 来源为早前已核验；本轮不追加同类新来源。
- 解除条件：出现可达且权威的音乐史数据库/在线词典（如某机构开放 API 或镜像），可重开。
"""
if "B-music-src" not in bs:
    io.open(bp,"a",encoding="utf-8").write(add); print("blocker added")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle106","date":"2026-11-24","status":"completed",
 "gap_methods":["启用 V&A 来源；补韩国/伊斯兰；音乐来源实测"],"network":"V&A 200；wiki/imslp/met 000；britannica 403；oxford 302",
 "new_entries":4,"new_entry_ids":["korean-celadon-bottle","korean-celadon-bowl-lotus","korean-white-flask-longevity","kashan-salting-mihrab"],
 "new_source_type":"V&A 开放数据 API（首次）","blockers":["B-music-src 音乐史文本来源不可达"],
 "qc":{"entries_checked":219,"dim_checks":157,"issues":0},
 "new_sources":4,"sources_total":493,"entries_total":364,"pages":401,
 "check_result":"errors=0","check_links_result":"broken=0(401页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle106","date":"2026-11-24","methods_used":["V&A 来源","韩国/伊斯兰"],
 "gaps_found":{"entries":4},"network":"V&A 200 only","verdict":"总364；音乐文本单元记 BLOCKER；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle106"' not in t:
    block=('if cyc=="cycle106":\n'
           '    L.append("- **首次启用 V&A 开放数据 API**（此前 0 条），补 4 条（360 → 364）：高丽青瓷镶嵌铜红长颈瓶、高丽青瓷莲童碗、'
           '朝鲜白瓷寿纹扁壶、卡尚米哈拉布釉砖。①高丽青瓷以**黑白镶嵌**成图绘性并试点**釉下铜红**；②莲童碗留**三支烧痕**＝装烧物证；'
           '③朝鲜白瓷**高丽朝已产**、19世纪主导，壶上**堆白蝙蝠环「壽」**、足底**谚文款录文存疑**；④卡尚米哈拉布原为**墓葬标志**、'
           '拱形为**清真寺朝向龛的缩微**，记录在「亡者身份」句**截断未补写**。'
           '**来源实测**：wiki/imslp/met=000、britannica=403、oxford=302，仅 **V&A=200**；故音乐文本单元记 **BLOCKER（B-music-src）**，不无源凑数。'
           '**R22 再立功**：V&A systemNumber 含大写 O 被拦，统一 `vam-o…` 小写后通过。QC 全量 **219条/157尺寸/0问题**。站点 397 → 401 页，体检 12/12。")\n')
    anchor='if cyc=="cycle105":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **360**（L2 356 / L3 4 / L1 0） |","| 条目 | **364**（L2 360 / L3 4 / L1 0） |"),
    ("| 来源 | **489**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **493**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **397**，站内断链 **0** |","| 页面 | **401**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **360** | L2 356 / L3 4 / **L1 0** |","| 条目总数 | **364** | L2 360 / L3 4 / **L1 0** |"),
    ("| 来源库 | **489**（另 11 条预备来源未计入） |","| 来源库 | **493**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **397** |","| 站点页面 | **401** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **360**（L2 356 / L3 4，**无 L1**） |","| 条目 | **364**（L2 360 / L3 4，**无 L1**） |"),
    ("| 来源 | **489**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **493**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **397** |","| 站点页面 | **401** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])