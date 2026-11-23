# -*- coding: utf-8 -*-
"""Cycle89：文档数字一次性对齐（README/PROGRESS/PROJECT_STATUS）。
以仓库实际数据为准；只替换当前状态的汇总数字，不动历史叙述段落。
"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# README
p=os.path.join(ROOT,"README.md"); s=io.open(p,encoding="utf-8").read()
fixes=[
 ("| 条目 | 145（L2 139 / L3 6，**无 L1**） |","| 条目 | **300**（L2 296 / L3 4，**无 L1**） |"),
 ("| 知识单元 | 22 |","| 知识单元 | **28** |"),
 ("| 来源 | 284（其中 Wikidata 结构化 120 条；全部 verified） |","| 来源 | **431**（全部 verified；另有 11 预备 / 5 隔离） |"),
 ("| 条目↔Wikidata 关联 | 118 / 145 = 81% |","| 条目↔Wikidata 关联 | **118 / 300 ≈ 39%**（另有大量机构藏品记录） |"),
 ("| 站点页面 | 176 |","| 站点页面 | **337** |"),
 ("| 硬规则校验 | `check.py` R1–R17，errors = 0 |","| 硬规则校验 | `check.py` **R1–R22**，errors = 0 |"),
 ("| 八步体检 | 全通过（含 py_compile / 渲染一致性 / HTML 结构） |","| 十二步体检 | 全通过（py_compile / 渲染一致性 / HTML 结构 / 不变式 / 可用性 / enc 复核） |"),
]
for a,b in fixes:
    if a in s: s=s.replace(a,b); print("README:",a[:26])
io.open(p,"w",encoding="utf-8").write(s)
# PROGRESS
p=os.path.join(ROOT,"PROGRESS.md"); s=io.open(p,encoding="utf-8").read()
fixes=[
 ("`data/sources.json` **279 条全部 verified**（另 5 条不可核验者在 `sources_quarantine.json`）",
  "`data/sources.json` **431 条全部 verified**（另 11 预备 / 5 隔离）"),
 ("校验器 | 必填/日期/来源/重复/链接/SVG/一致性 | ✅ | `tools/check.py` R1–R18，errors=0",
  "校验器 | 必填/日期/来源/重复/链接/SVG/一致性 | ✅ | `tools/check.py` R1–R22，errors=0"),
 ("全部 145 条：L2 139 / L3 6 / **L1 = 0**","全部 **300** 条：L2 296 / L3 4 / **L1 = 0**"),
 ("index / units×22 / timeline","index / units×28 / timeline"),
 ("176 页，`check_links` 0 断链","337 页，`check_links` 0 断链"),
 ("## 二、最终数字（Cycle 39 验证）","## 二、最终数字（Cycle 89 验证）"),
 ("| 条目 | 292（L2 288 / L3 4 / L1 0） |","| 条目 | **300**（L2 296 / L3 4 / L1 0） |"),
 ("| 重要性 | 核心 48 · 重要 85 · 补充 12（核心与重要全部 ≥L2） |",
  "| 重要性 | 核心 **89** · 重要 **199** · 补充 12（核心与重要全部 ≥L2） |"),
 ("| 单元 | **28**（新增陶瓷工艺） |","| 单元 | **28**（新增陶瓷工艺 / 乐器 / 中国陶瓷工艺） |"),
 ("| 来源 | 423（全部被引用且 verified；隔离区 5 + 预备 11） |",
  "| 来源 | **431**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
 ("| 条目↔实体 | 118 / 145 = **81%** |","| 条目↔实体 | 118 / 300 ≈ **39%**（Wikidata 仅为身份锚点/结构化事实） |"),
 ("| 页面 | 329，站内断链 **0** |","| 页面 | **337**，站内断链 **0** |"),
]
for a,b in fixes:
    if a in s: s=s.replace(a,b); print("PROGRESS:",a[:28])
io.open(p,"w",encoding="utf-8").write(s)
# PROJECT_STATUS
p=os.path.join(ROOT,"PROJECT_STATUS.md"); s=io.open(p,encoding="utf-8").read()
fixes=[
 ("## 二、关键数字（Cycle 37 时点）","## 二、关键数字（Cycle 89 时点）"),
 ("| 条目总数 | **292** | L2 288 / L3 4 / **L1 0** |","| 条目总数 | **300** | L2 296 / L3 4 / **L1 0** |"),
 ("| 重要性分布 | 核心 48 / 重要 85 / 补充 12 |","| 重要性分布 | 核心 **89** / 重要 **199** / 补充 12 |"),
 ("| 知识单元 | 22 | 艺术 8 + 中国艺术 2 + 亚洲艺术 1 + 音乐 7 + 中国音乐 1 + 导读/比较/术语/作品档案 4 |",
  "| 知识单元 | **28** | 西方艺术 9 + 中国艺术 3 + 其他地区艺术 5 + 音乐 8 + 中国音乐 1 + 导读/比较/术语/作品档案 4 + 乐器 1 + 中国陶瓷工艺 1（按单元分组） |"),
 ("| 来源库 | **423**（另 11 条预备来源未计入） |","| 来源库 | **431**（另 11 条预备来源未计入） |"),
 ("| 条目↔实体关联 | **118 / 145（81%）** | 41 条结构化事实 + 77 条身份锚点 |",
  "| 条目↔实体关联 | **118 / 300（≈39%）** | 41 条结构化事实 + 77 条身份锚点；Wikidata 不作事实依据 |"),
 ("| 站点页面 | **329** | 0 断链 |","| 站点页面 | **337** | 0 断链 |"),
 ("| 硬规则 | R1–R17 **errors=0** | 含 R17「争议必须真实」 |","| 硬规则 | **R1–R22 errors=0** | 含 R17 真实争议 / R20 覆盖层 / R21 when 格式 / R22 id 格式 |"),
 ("| 八步体检 | **8/8 通过** | py_compile(150 工具) + 硬规则 + 链接 + 九维 + 自洽 + 关联图 + 单向 + 渲染/结构 |",
  "| 十二步体检 | **12/12 通过** | py_compile + 硬规则 + 链接 + 九维 + 自洽 + 关联图 + 单向 + 渲染/结构 + 覆盖层 + 不变式 + 可用性 + enc 复核 |"),
 ("| 来源活性 | **120 / 120 HTTP 200** | 逐个 curl 实测 |","| 来源活性 | 抽样全 200；Wikidata 曾全量 120/120 | 机构 API 链接逐批抽检均 200 |"),
]
for a,b in fixes:
    if a in s: s=s.replace(a,b); print("STATUS:",a[:28])
io.open(p,"w",encoding="utf-8").write(s)
print("docs synced")