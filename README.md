# 艺术史与音乐史导读

一个**数据驱动、机器校验、诚实标注**的静态知识库：零 JavaScript、可离线阅读、可直接部署到 GitHub Pages。

> 首页：[index.html](index.html) · 状态页：[status.html](status.html) · 覆盖报告：[REPORT.md](REPORT.md)

## 它是什么

- **145 个条目**，覆盖西方艺术史（古代→当代）、中国绘画与书法、西方音乐史（中世纪→当代）、中国音乐史，以及导读/比较/术语/作品档案等辅助单元。
- 每个条目都是一条结构化 JSON，经**机器校验**后由确定性生成器渲染为 HTML；所有图示为**内联 SVG 自绘**，不含任何作品图片、乐谱或歌词。
- **不编造**：查不到的年份、尺寸、收藏地一律写入该条目的"待核实"，绝不进正文凑数。

## 规模与当前状态

| 指标 | 数值 |
|---|---|
| 条目 | **304**（L2 300 / L3 4，**无 L1**） |
| 知识单元 | **28** |
| 来源 | **435**（全部 verified；另有 11 预备 / 5 隔离） |
| 条目↔Wikidata 关联 | **118 / 300 ≈ 39%**（另有大量机构藏品记录） |
| 站点页面 | **341** |
| 硬规则校验 | `check.py` **R1–R22**，errors = 0 |
| 十二步体检 | 全通过（py_compile / 渲染一致性 / HTML 结构 / 不变式 / 可用性 / enc 复核） |

## 目录结构

| 路径 | 职责 |
|---|---|
| `index.html` / `status.html` | 首页 / 站点状态（规模、来源构成、校验方式、已知缺口） |
| `entries/*.html` | 条目页：L2 七节 + 自绘 SVG；待核实拆为"未解决列表 + 复核记录" |
| `units.html` / `units/<unit>.html` | 单元总览索引 / 每单元页（构成、分级条目、时间线、待核实） |
| `timeline.html` | 时间线（六段时期分组、带锚点） |
| `people.html` / `glossary.html` | 人物索引（按起始年代）/ 术语表（按标题序） |
| `entities.html` | 条目 ↔ Wikidata 实体对照（身份锚点，**非事实依据**） |
| `all-index.html` / `sources.html` | 全站索引 / 来源库（含核验状态） |
| `sitemap.xml` / `robots.txt` | 自动收录根目录全部页面 |
| `assets/style.css` | 设计系统：CSS 变量、深色模式、`focus-visible`、打印样式、SVG 类 |
| `scope.md` | 入选清单（6 份权威大纲取并集，编辑基准线） |
| `data/entries.json` | L1 种子（由 `build_scope.py` 从 `tools/catalog.py` 生成） |
| `data/l2/*.json` | 覆盖层：每条目的七节、SVG、来源、L3 争议块 |
| `data/site_entries.json` | 合并后的站点数据（`merge_l2.py` 产出） |
| `data/sources.json` | 全局来源库（含 verified / verified_note / 类型） |
| `data/coverage.json` | 覆盖状态（层级、来源数、待核实、独立性） |
| `reports/` | 覆盖矩阵、体检报告、锚定与饱和评估等审计证据 |
| `REPORT.md` | 每轮覆盖报告（七段式，供快速验收） |
| `DECISIONS.md` / `PROGRESS.md` / `BLOCKERS.md` | 决策记录 / 进度游标 / 阻塞记录 |

## 管线（每轮循环）

```bash
python tools/merge_l2.py           # L1 种子 ∪ L2 覆盖层（来源取并集）→ site_entries.json
python tools/check.py              # 硬规则 R1–R17（须 errors=0）
python tools/gen_site.py           # 确定性渲染 → index.html / entries/ / units/ / sitemap.xml
python tools/check_links.py        # 站内链接（须 broken=0）
python tools/audit_all.py          # 八步体检：py_compile→check→links→九维→自洽→关联图→单向→渲染/结构
python tools/build_report_autonomous.py   # 刷新 REPORT.md
```

辅助工具：

| 工具 | 用途 |
|---|---|
| `tools/wd_api.py` | Wikidata 客户端：正确 UA、**限速 1 req/s**、指数退避、磁盘缓存、返回 `(data, err)`（**不把限流当空数据**） |
| `tools/person_dates_c15.py` | 人物生卒交叉核验（P569/P570） |
| `tools/wikidata_verify.py` | 作品事实核验（创作年/收藏/作者），三重消歧 |
| `tools/entity_pass*.py` | 条目↔实体锚定的多轮匹配（id/英文标签/中文别名） |
| `tools/consistency_audit.py` | 内容自洽：正文是否与"待核实"矛盾、复核留痕是否误入正文 |
| `tools/link_audit.py` / `oneway_audit.py` | 关联图审计（跨域/单向/入链分布） |
| `tools/pending_render_audit_c30.py` | 渲染一致性 + HTML 结构（**有错时返回码 1**） |
| `tools/saturation_assess_c33.py` | 饱和评估（§5 两条件） |

## 关键约定

1. **双层分级**：条目重要性（核心/重要/补充）与写作深度（L1 骨架 / L2 七节 / L3 深度）是两回事。**L1 未全完成前不深写**；L3 只给核心条目且必须有**两方真实立场**。
2. **双源规则**：关键事实需 ≥2 个 verified 来源；不足则 `needs_verification=true` 且 `pending_notes` 非空。
3. **口径一致**：把条目锚到 Wikidata 实体时，实体口径必须与条目**严格一致**——偏宽（Buddhist art vs 印度佛教艺术）、偏窄（法国巴洛克音乐 vs 巴洛克音乐）、或描述为空，一律拒绝。
4. **身份锚点 ≠ 事实依据**：`wd-anchor-*` 只证明"条目讲的是哪个实体"，不支撑任何风格/年代断言，页面上亦如此声明。
5. **来源并集**：覆盖层只增不删来源（`merge_l2.py` 并集），避免"漏写导致基础来源被丢弃"。
6. **诚实标注的呈现**：待核实拆成"未解决列表"与"复核记录"两块，读者一眼能看出哪条还没落实。
7. **SVG**：由 `render_l2_svg.py` 从结构化 diagram 确定性渲染，保证不出界、无脚本、浅深两色可读。
8. **校验器即护栏**：`R17` 禁止把"编辑待办"包装成学术争议；`py_compile` 与渲染一致性检查让工具/页面损坏无法被提交。

## 已知限制（诚实披露）

- **内容来源不可达**：Wikipedia / Met / Tate 在本构建环境 TCP 超时；百度百科、Khan Academy 只返回反爬壳页；Britannica 为 Cloudflare 403。可用的仅有 **Wikidata / Wikimedia API / Commons / DBpedia**（结构化数据）。
- **因此**：新增条目（A 类矩阵 58 项，建筑已建 3 条）、B2 类音乐地区缺口（22 项，如甘美兰/印度古典/雅乐）、B5 待核实 5 项，**均无法在当前环境填补**——不是缺口不存在，而是来源进不来。
- **来源独立性不足**：已核验来源以 Wikipedia 与 Wikidata 为主（同属 Wikimedia），`coverage.json` 的 `source_independence_ok` 单独标记，未混入 `needs_verification` 以免比例失真。
- **未锚定 27 条**：自有页面 11 条（本无对应实体）、中国专题 11 条（无匹配实体）、早前被拒 5 条。
- 未做屏幕阅读器/键盘全路径实测；sitemap 中的站点根为 GitHub Pages 默认地址（`https://tiandihuang.github.io/yishu/`），换域名需替换。

## 如何续跑

按 `PROGRESS.md` 的"下轮起点"执行：

1. 读 `PROGRESS.md` / `BACKLOG.md` / `SATURATION.json` / `REPORT.md`；
2. 跑 `python tools/audit_all.py`（应为 8/8）；
3. 做**网络探针**：若 Wikipedia 等可读，按 `reports/saturation_assessment_c33.json` 的 `next_actions_if_unblocked` 推进；若仍只有壳页，则只做本地可验证的工作（锚定、文档、体检），**绝不降标准写内容**；
4. 每完成一批 `commit`；每 5 轮做一次完整体检；饱和以 `SATURATION.json` 为准。

> 本项目遵循"无人值守自治"约定：**不写 ALL_DONE**，以 `SATURATION.json` 的 `saturated` 作为完成度判据；当前 **saturated = false**（原因见上）。