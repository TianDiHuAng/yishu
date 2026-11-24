# PROGRESS.md — 进度游标（自治模式）

> 每次启动先读本文件；从「下轮起点」续作。按 AUTONOMOUS.md：**不写 ALL_DONE**，完成度以 `SATURATION.json` 为准。

- 当前轮次：**Cycle 40 已完成（新增 4 条目：145 → 149）**
- 状态：**未饱和**（saturated=false），受外部来源阻塞
- 最近更新：2026-11-22

## 一、任务书（TASK）阶段完成度

| 阶段 | 要求 | 状态 | 证据 |
|---|---|---|---|
| 阶段0 范围 | scope.md + coverage.json + 覆盖矩阵 | ✅ | `scope.md`（6 份权威大纲并集）、`data/coverage.json`、`reports/覆盖矩阵.md` |
| 阶段1 来源库 | ≥80 条，逐页核对后 verified | ✅ | `data/sources.json` **431 条全部 verified**（另 11 预备 / 5 隔离） |
| 阶段2 校验器 | 必填/日期/来源/重复/链接/SVG/一致性 | ✅ | `tools/check.py` R1–R22，errors=0 |
| 阶段3 样板 | 2 条到 L2 通过检查 | ✅ | impressionism / baroque-music（后续均已扩展） |
| 阶段4 分批写作 | L1 先行，每轮 ≤40 条，逐步升 L2/L3 | ✅ | 全部 **300** 条：L2 296 / L3 4 / **L1 = 0** |
| 阶段5 总览 | 总览/索引/时间线/导航/REPORT | ✅ | index / units×28 / timeline / people / glossary / all-index / sources / entities / status + `REPORT.md` |
| 站点生成 | `gen_site.py` 产出以 `index.html` 为首页 | ✅ | 337 页，`check_links` 0 断链 |
| 批次复检 | 每 20 条抽检 4 条 | ✅ | `reports/复检记录.md`（含返工与复核记录） |

## 二、最终数字（Cycle 89 验证）

| 指标 | 数值 |
|---|---|
| 条目 | **436**（L2 432 / L3 4 / L1 0） |
| 重要性 | 核心 **89** · 重要 **199** · 补充 12（核心与重要全部 ≥L2） |
| 单元 | **28**（新增陶瓷工艺 / 乐器 / 中国陶瓷工艺） |
| 来源 | **563**（全部被引用且 verified；隔离区 5 + 预备 11） |
| Wikidata 来源 | 120（43 结构化事实 + 77 身份锚点） |
| 条目↔实体 | 118 / 300 ≈ **39%**（Wikidata 仅为身份锚点/结构化事实） |
| 页面 | **473**，站内断链 **0** |
| 硬规则 | R1–R18 **errors=0** |
| 八步体检 | **8/8 通过**（py_compile 156 工具 / 硬规则 / 链接 / 九维 / 自洽 / 关联图 / 单向 / 渲染+HTML结构） |
| 来源活性 | **120 / 120 HTTP 200** |
| 提交 | 58 次，远端同步 |

## 三、为什么不写 ALL_DONE（AUTONOMOUS 优先于 TASK）

- AUTONOMOUS §1.2 明确："这个项目没有'做完'，只有'饱和'。**不要写 ALL_DONE**。"
- 本项目 `saturated = false`，理由见 `reports/saturation_assessment_c33.json`：
  - 条件②（核心与重要全达 L2）**已成立**；
  - 条件①（连续 3 轮无新缺口）**未成立**——最近仍在发现新缺口（Cycle31 锚定 14、Cycle32 锚定 4）。
- 开放缺口（**外部阻塞，非质量问题**）：A 类矩阵 58、B2 音乐地区 22、B5 待核实 5、未锚定 27。

## 四、外部阻塞（唯一未完成原因）

| 来源 | 可达性 |
|---|---|
| Wikidata / Wikimedia API / Commons / DBpedia | ✅ 200（仅结构化数据） |
| en/zh.wikipedia.org、metmuseum.org、tate.org.uk | ❌ TCP 超时 |
| baike.baidu.com、khanacademy.org | ⚠️ 200 但仅返回反爬壳页 |
| britannica.com | ⚠️ 403 Cloudflare |

Wikidata 只能做**身份锚定与结构化事实**（年代/尺寸/馆藏/生卒），**撑不起**风格特征、体裁沿革、学术评价类陈述。

## 五、下轮起点（来源恢复后按序执行）

1. 跑 `python tools/audit_all.py`（应 8/8）。
2. 跑网络探针：`curl -m 10 https://en.wikipedia.org/wiki/Gothic_architecture`；**出现可读正文**才继续第 3 步。
3. 按 `reports/saturation_assessment_c33.json` 的 `next_actions_if_unblocked`：
   - A 类建筑剩余（南亚/日本/伊斯兰等，≥2 来源/条，≤14 条/轮）
   - B2 音乐地区空白（甘美兰/印度古典/雅乐等）
   - B5 剩余 5 项（含 romanesque 断代 1150 vs 1200 的第三来源判定）
4. 每 5 轮做一次完整体检；发现新缺口即维持 `saturated=false`。

## 六、历史日志（轮次 → 关键动作）

- pre-autonomous：109 条目、42→82 L2、91→95 来源。
- C1 114 全 L2 · 新增 5 中国艺术史 ｜ C2 125 · 新增 11 导读比较 ｜ C3 129 · B5 复核 38 项 + 孤儿清零
- C4 137 · 8 亚洲艺术 · L3 启动 ｜ C5 体检 ｜ C6 142 · 5 作品档案 · **L3 返工 28→6（新增 R17）**
- C7–9 本地：单元总览×21 / 人物·术语索引 / a11y+sitemap ｜ C10 体检 ｜ C11 内容自洽审计（0 问题）
- C12 关联对称化（单向 47→0）｜ C13 网络精确定位 + audit_all ｜ C14 **Wikidata 通道**（5 作品）+ 修 sources 并集 bug
- C15 32 人物生卒核验（0 矛盾）｜ C16 人物 32/32 挂来源 ｜ C17–18 建筑缺口（哥特/罗马式/高棉）
- C19 B 类复核（发现 B2 22 项）｜ C20 体检 ｜ C21 作品尺寸入档 ｜ C22–23 实体锚定（59 条，拒误配 3 类）
- C24 体检（120/120 活性）｜ C25 pass3 + status.html ｜ C26 **发现静默限流 → wd_api**（锚定 34→54）
- C27 锚定收官（77，69%→）｜ C28 体检（修 sitemap 漏收）｜ C29 待核实三层呈现 ｜ C30 体检（渲染/结构守卫 + 故障注入）
- C31 人工 QID（79%）｜ C32 中国别名（81%）｜ C33 体检 + 饱和评估 ｜ C34 README 重写 + 单元缺口
- C35 来源构成徽标 ｜ C36 B5 收尾（romanesque 断代差异）｜ C37 来源隔离 + R18 ｜ C38 状态页动态化 ｜ C39 收尾验证

> ALL_DONE：**按 AUTONOMOUS.md 不写**；结构完成、饱和未达、来源恢复后可直接续写。