# -*- coding: utf-8 -*-
"""Cycle107 收尾：D110 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D110 — Cycle107 用 V&A 再补 4 条（364 → 368；跨韩/埃/伊朗/日）
继续用 V&A（唯一可达的开放 API）拓展薄区，新增：
`tiger-magpie-hochakdo`（韩国民画《虎鹊图》，1850—1910，**核心**）、`mamluk-mosque-lamp`（马穆鲁克清真寺灯，1342—45，**核心**）、
`minai-bowl-kashan`（卡尚米纳伊碗，1180—1220，**核心**）、`japanese-inro`（日本印笼，18世纪）。
四处要点：①虎为**最强辟邪兽**、鹊**报喜**，新年**悬于家门**；②清真寺灯上的**司库徽记**把宗教用器变成**马穆鲁克行政阶层的身份标记**；
③mina'i 为**釉上彩＋描金**，碗心**双骑手分居金树**、内壁**四对坐者若交谈**；④印笼源于**和服无口袋**，以**丝绳＋根付**悬于腰带。
**如实保留两处资料截断**：《虎鹊图》「不仅是……」与《印笼》「盛印章与……」的记录均在句中**截断**，本条目**不补写**，仅按常例标注「盛药」**存疑**。
**资料处理**：V&A 尺寸为 Height/Width/Depth 多值，本条目按「装裱/画心」「高/宽」分别写明确切数值（111/57.5/73.7/43.3 等）。
**QC**：全量 **223 条、161 尺寸项、0 问题**。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条 V&A 来源。
代价：均单一机构（V&A）；韩国绘画/日本漆器/伊斯兰玻璃釉陶由此起步，仍属点状。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle107","date":"2026-11-24","status":"completed",
 "gap_methods":["V&A 拓展薄区（韩/埃及/伊朗/日）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":["tiger-magpie-hochakdo","mamluk-mosque-lamp","minai-bowl-kashan","japanese-inro"],
 "qc":{"entries_checked":223,"dim_checks":161,"issues":0},
 "new_sources":4,"sources_total":497,"entries_total":368,"pages":405,
 "check_result":"errors=0","check_links_result":"broken=0(405页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle107","date":"2026-11-24","methods_used":["V&A 拓展薄区"],
 "gaps_found":{"entries":4},"network":"V&A 200","verdict":"总368；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle107"' not in t:
    block=('if cyc=="cycle107":\n'
           '    L.append("- 继续用 V&A（唯一可达开放 API）补 4 条（364 → 368），跨韩国/埃及/伊朗/日本：韩国民画《虎鹊图》、马穆鲁克清真寺灯、'
           '卡尚米纳伊碗、日本印笼。①虎为**最强辟邪兽**、鹊**报喜**、新年悬门；②清真寺灯上的**司库徽记**使宗教用器成**行政阶层身份标记**；'
           '③mina\'i 为**釉上彩＋描金**，碗心**双骑手分居金树**；④印笼源于**和服无口袋**、以**丝绳＋根付**悬佩。'
           '**如实保留两处资料截断**（虎鹊「不仅是…」、印笼「盛印章与…」）不补写，「盛药」存疑。QC 全量 **223条/161尺寸/0问题**。'
           '站点 401 → 405 页，体检 12/12。")\n')
    anchor='if cyc=="cycle106":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **364**（L2 360 / L3 4 / L1 0） |","| 条目 | **368**（L2 364 / L3 4 / L1 0） |"),
    ("| 来源 | **493**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **497**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **401**，站内断链 **0** |","| 页面 | **405**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **364** | L2 360 / L3 4 / **L1 0** |","| 条目总数 | **368** | L2 364 / L3 4 / **L1 0** |"),
    ("| 来源库 | **493**（另 11 条预备来源未计入） |","| 来源库 | **497**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **401** |","| 站点页面 | **405** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **364**（L2 360 / L3 4，**无 L1**） |","| 条目 | **368**（L2 364 / L3 4，**无 L1**） |"),
    ("| 来源 | **493**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **497**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **401** |","| 站点页面 | **405** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])