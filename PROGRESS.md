# PROGRESS.md — 进度游标（自治模式）

> 每次启动先读本文件与 BACKLOG/METRICS/SATURATION/REPORT，从"下轮起点"续作。
> 按 AUTONOMOUS.md：不写 ALL_DONE；饱和以 SATURATION.json 为准。

- 当前轮次：**Cycle 14 已完成（突破：可用来源通道找到）** → 下轮 **Cycle 15**
- 状态：正常（未饱和）；**网络部分可用**：Wikidata / Wikimedia API / Commons / DBpedia 可达
- 最近更新：2026-11-22

## 上轮（Cycle 14）关键突破
- **找到可用来源通道**：Cycle13 的结论要修正为——Wikipedia/Met/Tate 不可达、百度/Khan 只给反爬壳页，但
  **`www.wikidata.org`（含 `w/api.php` 与 `Special:EntityData/*.json`）、`api.wikimedia.org`、`commons.wikimedia.org`、`dbpedia.org` 均可达且返回可用 JSON**（301→200）。
- **新建 `tools/wikidata_verify.py`**（三重消歧：标题 + 描述类型词 + 作者名），核验 5 个作品档案：
  - 星夜 Q45585（作者 梵高｜收藏 现代艺术博物馆）✓ 与条目一致
  - 维纳斯的诞生 Q151047（波提切利｜乌菲兹）✓
  - 西斯廷天顶画 Q844675（米开朗琪罗｜梵蒂冈博物馆）✓
  - 格尔尼卡 Q175036（畢卡索｜索菲亚王后国家艺术中心）✓
  - 春之祭 Q206015（描述为 Igor Stravinsky 的芭蕾音乐；**P170 字段异常=西德尼·諾蘭，已标注不采信**）
- 5 条作品档案登记 `wd-*` 来源并写入【已复核·Wikidata】留痕（**不改正文断言**，D020）
- **修复真实数据丢失 bug（D021）**：`merge_l2` 的 `sources` 由"覆盖层替换"改为**并集**；此前写 wikidata 来源时把基础层 2 条 Wikipedia 来源整段覆盖，导致 R10 报"仅1个verified来源"。
- 结果：来源 164→**169（verified 164）**；`check.py errors=0`、`check_links broken=0`、`audit_all 6/6`。

## 下轮起点（Cycle 15）——优先用 Wikidata 恢复内容建设
1. 读状态；`python tools/audit_all.py`（应 6/6）。
2. **扩用 Wikidata 核验**（本轮已验证通道可用）：
   - 对 20+ 个**人物条目**核验生卒年（P569/P570）与国籍/领域，记录差异（不自动改，先出报告）；
   - 对已有作品类条目核验 **P571 创作年**、P195 收藏、P2048/2049 尺寸；把可确认项写入"待核实"留痕；
   - A 类建筑缺口：用 `wbsearchentities` 找"Chinese architecture (Q957904)"等实体，若描述与类型匹配，可据 Wikidata 建立**建筑类条目**（≤14 条/轮，每条 ≥2 来源：Wikidata + 既有/新增可达来源）。
3. 注意：Wikidata 与 Wikipedia **同源（独立性不足）**，因此只用于"事实定位/交叉印证"，**不据此升级 L3**（L3 仍需两方真实立场）。
4. 若 Wikidata 也不可用：回到本地改进（导读↔正文互通 / status.html）。
5. 质量闸抽检 ≥3；更新状态；commit+push。

## 长期待办（BACKLOG P4）
- A 类矩阵补盲 58 项（首选建筑，现在具备用 Wikidata 起步的条件）；L3 仅 6 条；B5 剩 5 项；B4 导览类。

## 历史日志
- pre-autonomous：109条目、42→82 L2。
- Cycle 1–3：114→129 条全 L2；B5 复核 38 项；孤儿清零。
- Cycle 4：137、8 亚洲艺术、L3 启动。
- Cycle 5（体检）：六维通过、L3 至 16。
- Cycle 6：142、5 作品档案、L3 返工 28→6（R17）。
- Cycle 7–9（本地）：单元总览×21、人物/术语索引、a11y+sitemap。
- Cycle 10（体检）：九维通过 + 关联图审计。
- Cycle 11（本地）：内容自洽性审计（0 问题）。
- Cycle 12（本地）：关联对称化（单向 47→0）+ 向前后导航。
- Cycle 13：网络精确定位（可达站点仅壳页）+ audit_all（6/6）。
- **Cycle 14：发现 Wikidata 可用 → 5 作品核验通过 + 修 sources 并集 bug。**

ALL_DONE：按 AUTONOMOUS.md 不写。