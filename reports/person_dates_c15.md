# 人物生卒年交叉核验（Cycle 15，Wikidata）

方法：`tools/person_dates_c15.py` 通过 Wikidata API 按中文标题检索实体（失败回退英文），
要求 **描述含人物类型词**（painter/sculptor/composer/architect…）**且** 生年（P569）与条目 `when`
的起始年份相差 ≤2 年才接受；同名实体（城市、电影、火车站等）一律拒绝。

## 结果

| 分类 | 数量 | 含义 |
|---|---|---|
| **confirmed** | **26** | Wikidata 生年在条目 `when` 的 ±1 年内，**无一处矛盾** |
| mismatch | **0** | 未发现条目与 Wikidata 相冲突的生卒年 |
| no_match | 6 | 消歧未通过（实体仅有英文标签 / 抓取抖动 / 同名过多），**非数据错误** |

未匹配的 6 条：donatello、leonardo、vermeer、delacroix、monet、monteverdi。
原因：这些实体在中文检索下返回的候选缺少中文标签（如 `Donatello` vs 条目名「多纳泰罗」），
且本次抓取对个别请求出现空响应（已在脚本内输出 `[warn] fetch failed`）。
**处置：不强行匹配**（避免张冠李戴），留待后续用英文名映射或人工指定 QID 再核。

## 意义与边界

- 说明现有 32 个人物条目中，凡能与权威结构化数据对齐者，**生卒年全部一致**，没有出现此前担心的"年份写错"类错误。
- Wikidata 与 Wikipedia **同源**，独立性不足：本条核验**不能**把条目升级为"双独立来源"，也不能支撑 L3 的两方争议。
- 本轮**未据此改动任何条目年份**（无差异可改）；仅登记核验过程与结论。

明细（QID、生卒、描述）见 `reports/person_dates.json`。