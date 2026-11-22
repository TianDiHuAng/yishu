# PROGRESS.md — 进度游标（自治模式）

> 每次启动先读本文件与 BACKLOG/METRICS/SATURATION/REPORT，从"下轮起点"续作。
> 按 AUTONOMOUS.md：不写 ALL_DONE；饱和以 SATURATION.json 为准。

- 当前轮次：**Cycle 25 已完成** → 下轮 **Cycle 26**
- 状态：正常（未饱和）；来源通道：Wikidata 可用（curl）
- 最近更新：2026-11-22

## 上轮（Cycle 17）做了什么
- 按 `reports/matrix_targets_c7.md` 的 A 类清单**开工建筑缺口**（最大缺口）：
  - 新建 **哥特式建筑**（Q176483）与 **罗马式建筑**（Q46261）两条，medium=建筑，归入 art-medieval
  - 每条挂 2–3 来源：Wikipedia 专页（已核验）+ Wikidata 实体 + 关联风格页
  - 手工撰写 L2 七节（不经代理，规避批量写作的失真风险）
- **诚实处理关键点**：实测这两个 Wikidata 实体**无 P571（起始年代）声明** → Wikidata 只确认"实体身份/正式名称"，**不承担年代**；已在每条"待核实"写入**来源分工说明**，并把年代类断言全部留在待核实
- **中国建筑未建**：目前只有 Wikidata 一条可核验来源，按"≥2 来源"规则**不建**，记入 BACKLOG
- 质量闸：两条 wd 来源 URL 200、标签与 QID 一致；新建条目正文年份均已在待核实列明（issues 0）；内容自洽性审计 0 问题
- 结果：条目 142 → **144**（L2 138 + L3 6）；站点 171 → **173** 页；来源 **204**；`check errors=0`、`links broken=0`

## 下轮起点（Cycle 18）
1. 读状态；`python tools/audit_all.py`（应 6/6）。
2. 继续 A 类建筑缺口，但**只在能凑够第二来源时**建：
   - 中国建筑：现有仅 Wikidata → 先找可用第三通道（如 Commons 分类页 `commons.wikimedia.org` 可提供"该建筑传统存在"的佐证，但**不构成事实来源**，需谨慎）；若仍凑不齐则维持不建
   - 南亚/东南亚建筑：`enc-khmer-art`、`enc-angkor` 已核验且确实论述吴哥建筑 → 可考虑"高棉建筑"（2 来源）
3. 作品类条目继续扩核（P571/P195 → 待核实留痕）。
4. 质量闸抽检 ≥3；更新状态；commit+push。

## 长期待办（BACKLOG P4）
- A 类 58 项（建筑为主，受"第二来源"制约）；L3 仅 6 条（需两方立场）；B5 剩 5 项；B4 导览类。

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
- Cycle 14：Wikidata 通道（5 作品）+ 修 sources 并集 bug。
- Cycle 15：32 人物核验（26 一致/0 矛盾）。
- Cycle 16：人物 32/32 挂 Wikidata 来源；来源 202。
- **Cycle 17：建筑缺口开工（哥特/罗马式 2 条），中国建筑因单源未建；144 条目/173 页。**

ALL_DONE：按 AUTONOMOUS.md 不写。
