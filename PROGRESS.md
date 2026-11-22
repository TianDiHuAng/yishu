# PROGRESS.md — 进度游标（自治模式）

> 每次启动先读本文件与 BACKLOG/METRICS/SATURATION/REPORT，从"下轮起点"续作。
> 按 AUTONOMOUS.md：不写 ALL_DONE；饱和以 SATURATION.json 为准。

- 当前轮次：**Cycle 15 已完成** → 下轮 **Cycle 16**
- 状态：正常（未饱和）；来源通道：**Wikidata 可用（经 curl）**
- 最近更新：2026-11-22

## 上轮（Cycle 15）做了什么
- **人物生卒年交叉核验**（`tools/person_dates_c15.py`，改用 curl 抓取——本环境 urllib 的 DNS 不稳定而 curl 稳定 200）
  - 消歧规则：中文检索 → 描述含人物类型词 + 生年与条目 `when` 相差 ≤2；同名实体（城市/电影/车站）一律拒绝
  - 结果：32 人物中 **confirmed 26 / mismatch 0 / no_match 6**
  - **关键结论**：凡能与 Wikidata 对齐的人物条目，生卒年**全部一致，无一处矛盾** —— 此前担心的"年份写错"未出现
  - 6 条未匹配（donatello/leonardo/vermeer/delacroix/monet/monteverdi）为**消歧未过**（实体缺中文标签或抓取抖动），已**拒绝强行匹配**，不猜测
  - 因**无差异可改**，本轮未修改任何条目年份；结论与明细写入 `reports/person_dates_c15.md` / `.json`
- 工具鲁棒性：curl 重试 5 次 + 失败显式告警（避免把网络抖动误判为"无此实体"）
- `audit_all 6/6`、`check.py errors=0`、`check_links broken=0`

## 下轮起点（Cycle 16）
1. 读状态；`python tools/audit_all.py`（应 6/6）。
2. **补全 6 条未匹配人物**：为 donatello/leonardo/vermeer/delacroix/monet/monteverdi 提供英文名映射（可用条目 `def`/`overview` 中的英文名或既有 source 标题推导），重新核验；仍不通过则记录并放弃（不猜测）。
3. **作品事实扩核**：对 5 个作品档案之外的**作品类条目**（如 mona-lisa）核验 P571/P195；对已有"待核实"中"缺创作年份/收藏地"的条目，若 Wikidata 可确认，则写入【已复核·Wikidata】留痕（不改正文断言）。
4. **A 类建筑缺口（谨慎起步）**：用 `wbsearchentities` 找实体；**必须凑够 2 个来源**才建条目——Wikidata 只能作其一，另一来源须为已核验且确实论述该建筑传统的既有来源（如 enc-khmer-art 论吴哥建筑、enc-gothic-architecture 论哥特建筑、enc-romanesque 论罗马式建筑）。凑不齐就不建，避免单源条目。
5. 质量闸抽检 ≥3；更新状态；commit+push。

## 长期待办（BACKLOG P4）
- A 类矩阵补盲 58 项（建筑为主，受"第二来源"制约）；L3 仅 6 条（需两方真实立场，Wikidata 同源不适用）；B5 剩 5 项；B4 导览类。

## 历史日志
- pre-autonomous：109条目、42→82 L2。
- Cycle 1–3：114→129 全 L2；B5 复核 38 项；孤儿清零。
- Cycle 4：137、8 亚洲艺术、L3 启动。
- Cycle 5（体检）：六维通过、L3 至 16。
- Cycle 6：142、5 作品档案、L3 返工 28→6（R17）。
- Cycle 7–9（本地）：单元总览×21、人物/术语索引、a11y+sitemap。
- Cycle 10（体检）：九维通过 + 关联图审计。
- Cycle 11（本地）：内容自洽性审计（0 问题）。
- Cycle 12（本地）：关联对称化（单向 47→0）+ 前后条目导航。
- Cycle 13：网络定位（可达站点多仅壳页）+ audit_all（6/6）。
- Cycle 14：**Wikidata 通道打通** → 5 作品核验 + 修 sources 并集 bug。
- Cycle 15：**32 人物生卒核验**（26 一致 / 0 矛盾 / 6 消歧未过）。

ALL_DONE：按 AUTONOMOUS.md 不写。