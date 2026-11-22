# PROGRESS.md — 进度游标（自治模式）

> 每次启动先读本文件与 BACKLOG/METRICS/SATURATION/REPORT，从"下轮起点"续作。
> 按 AUTONOMOUS.md：不写 ALL_DONE；饱和以 SATURATION.json 为准。

- 当前轮次：**Cycle 16 已完成** → 下轮 **Cycle 17**
- 状态：正常（未饱和）；来源通道：**Wikidata 可用（curl）**
- 最近更新：2026-11-22

## 上轮（Cycle 16）做了什么
- **补齐 Cycle15 遗留的 6 条未匹配人物**：加英文别名检索 + 补人物类型词（如 polymath 让 leonardo 命中）
  → donatello Q37562(1386)、leonardo Q762(1452)、vermeer Q41264(1632)、delacroix Q33477(1798)、monet Q296(1840)、monteverdi Q53068(1567) 全部与条目 `when` 一致
- **人物 Wikidata 覆盖率 6 → 32/32**：批量 `wbgetentities` 一次取标签，为全部 32 个人物条目挂 `wd-*` 来源并写入【已复核·Wikidata】生卒留痕；**mismatch 仍为 0**
- **作品事实核验**：monet（1840—1926）、mona-lisa（1503 创作 / 卢浮宫绘画部 / 达·芬奇）与条目一致，已留痕
- **修正 5 处「QQ」重复 QID**（title 与 url 同步），抽样 Q762 返回 HTTP 200
- 结果：来源 174 → **202（verified 197）**；全库平均 **2.46 来源/条**；`check errors=0`、`links broken=0`、`audit_all 6/6`

## 下轮起点（Cycle 17）
1. 读状态；`python tools/audit_all.py`（应 6/6）。
2. **作品类条目扩核**（继续用 Wikidata）：对 `mona-lisa` 之外的作品条目（如 `birth-of-venus-work` 已完成、`starry-night` 已完成）逐条核验 P571/P195；对仍缺"创作年份/收藏地"的条目补【已复核·Wikidata】留痕（不改正文断言）。
3. **A 类建筑缺口（谨慎）**：`wbsearchentities` 找实体（如 Chinese architecture Q957904）；**必须凑够第二来源**——优先用已核验且确论述该建筑传统的既有来源：
   - 哥特建筑 ← `enc-gothic-architecture` + `wd-gothic-architecture`
   - 罗马式建筑 ← `enc-romanesque` + `wd-romanesque-architecture`
   - 高棉/吴哥建筑 ← `enc-khmer-art`/`enc-angkor` + `wd-angkor-wat`
   凑不齐（如中国建筑目前只有 Wikidata）→ **不建**，记 BACKLOG 待来源。
4. 质量闸抽检 ≥3（含新增来源真实性抽样）；更新状态；commit+push。

## 长期待办（BACKLOG P4）
- A 类矩阵补盲 58 项（建筑为主，受"第二来源"制约）；L3 仅 6 条（需两方立场，Wikidata 同源不适用）；B5 剩 5 项；B4 导览类。

## 历史日志
- pre-autonomous：109 条目、42→82 L2。
- Cycle 1–3：114→129 全 L2；B5 复核 38 项；孤儿清零。
- Cycle 4：137、8 亚洲艺术、L3 启动。
- Cycle 5（体检）：六维通过、L3 至 16。
- Cycle 6：142、5 作品档案、L3 返工 28→6（R17）。
- Cycle 7–9（本地）：单元总览×21、人物/术语索引、a11y+sitemap。
- Cycle 10（体检）：九维通过 + 关联图审计。
- Cycle 11（本地）：内容自洽性审计（0 问题）。
- Cycle 12（本地）：关联对称化（单向 47→0）+ 前后条目导航。
- Cycle 13：网络定位 + audit_all。
- Cycle 14：Wikidata 通道打通（5 作品）+ 修 sources 并集 bug。
- Cycle 15：32 人物核验（26 一致 / 0 矛盾 / 6 消歧未过）。
- **Cycle 16：6 条补齐 → 人物 32/32 全核验并挂 Wikidata 来源；来源 202（197 verified）。**

ALL_DONE：按 AUTONOMOUS.md 不写。