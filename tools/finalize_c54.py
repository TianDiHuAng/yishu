# -*- coding: utf-8 -*-
"""Cycle54 收尾：修状态页 R 编号 + D057 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py"); s=io.open(P,encoding="utf-8").read()
if "硬规则（R1–R18）" in s:
    s=s.replace("硬规则（R1–R18）","硬规则（R1–R19）"); io.open(P,"w",encoding="utf-8").write(s); print("status R label fixed")

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D057 — Cycle54 不变式全面盘点：3 项处置 + 盘点脚本常驻（体检第 10 步）
- **背景**：内容连做三轮（+25 条）后，自 Cycle50 起未再做过全量不变式复核，本轮补做。
- **盘点结果与处置**：
  1. **11 条「死重来源」**（在库但无任何条目引用：`enc-night-watch`、`enc-pearl-earring`、`enc-the-scream`、`enc-longshan`、`wd-japanese-architecture`、`wd-indian-architecture` 等）→ 移入 **`data/sources_reserve.json`（预备来源）**，并在 `status.html` 公开其数量与性质。理由：`sources.json` 应只存**被引用**者，否则"来源总数"虚增。
  2. **L3 门禁复核（6 → 4）**：`rembrandt`（69 字，仅"学界主要讨论分期"）与 `monet`（原文即写明"概述未提及争议性观点"）**无两方具名立场**，按 R16 **降级为 L2**，并在各自待核实中写明降级理由；`gothic` 原写"学界存在讨论"过于笼统，改写为**具名两方**——以 **1140 年**（圣但尼唱诗班重建）为起点 vs 以**12 世纪后期—16 世纪**为框架，两说均有来源支撑，并列不裁定，**保留 L3**。现存 L3：`greek-art`、`gothic`、`impressionism`、`baroque-music`。
  3. **新增 `tools/invariants_c54.py`**（9 项检查：计数一致、死重来源、层级/重要性分布、L3 判读、孤儿、重复、related 悬空/单向、needs_verification 一致性、单元页条目数），**接入 `audit_all` 成为第 10 步**；只有**硬性问题**才使构建失败，L3 两方判读降级为**人工复核清单**（自动关键词检测不可靠，本轮就误报了 `impressionism` 与 `baroque-music` —— 二者实际分别有"批评者/支持者""保守派/新音乐"两方）。
- **当前盘点状态**：硬性问题 **0**、人工复核 2（均为误报，已人工确认）。
- **可逆方式**：把 reserve 移回 sources.json、把两条 level 改回 L3、移除 audit 第 10 步。
- **代价**：来源总数由 337 **降为 326**（并公开 11 条预备来源）；L3 由 6 降为 4 —— 数字变小，但数字变真。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle54","date":"2026-11-23","status":"completed",
 "gap_methods":["不变式全面盘点（9项）"],"network":"partial",
 "new_entries":0,"fixes":12,
 "findings":{"dead_sources":11,"l3_weak":2,"l3_improved":1},
 "actions":["11 条死重来源移入 sources_reserve.json（status 页公开）",
   "rembrandt/monet 降级 L2（无两方立场）","gothic 改写为具名两方并保留 L3",
   "新增 invariants_c54.py 并接入 audit_all 第 10 步（仅硬性问题失败）"],
 "l3_after":4,"sources_total":326,"sources_reserve":11,"entries_total":195,"pages":230,
 "audit_steps":10,"false_positive_note":"关键词判读误报 impressionism / baroque-music",
 "check_result":"errors=0","check_links_result":"broken=0(230页)","audit_all":"10/10 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s2p=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s2p,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle54","date":"2026-11-23","methods_used":["不变式盘点"],
 "gaps_found":{"dead_sources":11,"l3_weak":2},"network":"partial",
 "verdict":"盘点处置到位：来源去虚、L3 去弱留强；新增第 10 步体检；未饱和"})
json.dump(sd,open(s2p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

R=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(R,encoding="utf-8").read()
if 'cyc=="cycle54"' not in t:
    block=('if cyc=="cycle54":\n'
           '    L.append("- **不变式全面盘点（Cycle50 以来首次）**，三项处置：①**11 条「死重来源」**（在库但零引用，'
           '如《夜巡》《珍珠耳环的少女》《呐喊》的来源）移入 `data/sources_reserve.json` 并在状态页公开——'
           '**来源总数 337 → 326**，数字变小但变真；②**L3 门禁复核 6 → 4**：`rembrandt` 与 `monet` 无两方具名立场，'
           '按 R16 **降为 L2**（`monet` 原文即写"概述未提及争议"），`gothic` 把"学界存在讨论"改写为**具名两方**'
           '（1140 年起点 vs 12世纪后期—16世纪框架）后**保留 L3**；③新增 **invariants_c54.py（9 项检查）为体检第 10 步**，'
           '仅硬性问题失败，L3 判读降为人工复核（本轮关键词法误报了 impressionism 与 baroque-music，二者实际各有两方）。'
           '现存 L3：希腊艺术、哥特式、印象派、巴洛克音乐；盘点硬性**问题 0**。")\n')
    anchor='if cyc=="cycle53":'
    assert anchor in t
    io.open(R,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 来源 | 337（全部 verified；隔离区 5 条不可核验） |","| 来源 | 326（全部 verified；隔离区 5 条 + 预备 11 条） |"),
    ("| 条目 | 195（L2 189 / L3 6 / L1 0） |","| 条目 | 195（L2 191 / L3 4 / L1 0） |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 来源库 | **337** |","| 来源库 | **326**（另 11 条预备来源未计入） |"),
    ("| 条目总数 | **195** | L2 189 / L3 6 / **L1 0** |","| 条目总数 | **195** | L2 191 / L3 4 / **L1 0** |")])]:
    s3=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s3: s3=s3.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s3)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])