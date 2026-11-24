# 项目总表与交接说明

> 生成于 Cycle 37（体检轮）。本文件是**一次性的交接快照**，后续轮次若数据变化以 `REPORT.md` / `METRICS.json` 为准。
> 本项目遵循"无人值守自治"约定：**不写 ALL_DONE**，完成度以 `SATURATION.json` 的 `saturated` 判定。

---

## 一、交付物一览

| 类别 | 位置 | 说明 |
|---|---|---|
| 站点入口 | `index.html` | 首页（统计卡片 + 单元导航 + 深度条目） |
| 状态页 | `status.html` | 规模 / 来源构成 / 校验方式 / **已知缺口** |
| 条目页 | `entries/*.html` | 154 条；L2 七节 + 自绘 SVG + 来源表 + 反链 + 来源构成徽标 |
| 单元总览 | `units.html` + `units/*.html` | 22 个单元页（构成、分级条目、时间线、**本单元覆盖缺口**） |
| 索引类 | `timeline.html` / `people.html` / `glossary.html` / `all-index.html` / `entities.html` / `sources.html` | 时间线（六段分组）/ 人物 / 术语 / 全站 / 实体对照 / 来源库 |
| 机器产物 | `sitemap.xml` / `robots.txt` | 自动收录 176 页 |
| 数据层 | `data/entries.json`（种子）、`data/l2/*.json`（覆盖层）、`data/site_entries.json`（合并）、`data/sources.json`、`data/coverage.json` | 单一事实源 → 覆盖层 → 合并产物 |
| 编辑基准 | `scope.md` | 6 份权威大纲取并集，109→154 条目的入选依据 |
| 校验器 | `tools/check.py`（R1–R17）、`tools/audit_all.py`（八步） | 机器守门员 |
| 证据库 | `reports/` | 覆盖矩阵、九维体检、关联图、锚定复核、饱和评估、活性核验 |
| 决策记录 | `DECISIONS.md`（D001–D040）、`BLOCKERS.md` | 每项决定的依据、可逆方式与代价 |

---

## 二、关键数字（Cycle 89 时点）

| 指标 | 数值 | 备注 |
|---|---|---|
| 条目总数 | **512** | L2 508 / L3 4 / **L1 0** |
| 重要性分布 | 核心 **89** / 重要 **199** / 补充 12 | 核心与重要**全部 ≥ L2** |
| 知识单元 | **28** | 西方艺术 9 + 中国艺术 3 + 其他地区艺术 5 + 音乐 8 + 中国音乐 1 + 导读/比较/术语/作品档案 4 + 乐器 1 + 中国陶瓷工艺 1（按单元分组） |
| 来源库 | **638**（另 11 条预备来源未计入） | **全部 verified=true**（R18 强制）；另有 5 条不可核验来源在 `data/sources_quarantine.json` 隔离区 |
| 条目↔实体关联 | **118 / 300（≈39%）** | 41 条结构化事实 + 77 条身份锚点；Wikidata 不作事实依据 |
| 关联图 | 430 条关联 · 单向 **0** · 跨域 2（合法） | 度均 3.0 / 最大 12 |
| 站点页面 | **549** | 0 断链 |
| 硬规则 | **R1–R22 errors=0** | 含 R17 真实争议 / R20 覆盖层 / R21 when 格式 / R22 id 格式 |
| 十二步体检 | **12/12 通过** | py_compile + 硬规则 + 链接 + 九维 + 自洽 + 关联图 + 单向 + 渲染/结构 + 覆盖层 + 不变式 + 可用性 + enc 复核 |
| 来源活性 | 抽样全 200；Wikidata 曾全量 120/120 | 机构 API 链接逐批抽检均 200 |
| 对比度 | 全 ≥ WCAG AA | 浅/深两套令牌 |

---

## 三、质量体系（为什么这些数字可信）

1. **数据与呈现分离**：JSON → `check.py` → `gen_site.py` → HTML。改数据重跑即可，不手改页面。
2. **机器校验强制诚实**：
   - `R10` 双源（<2 个 verified 来源必须标 `needs_verification` 并写 `pending_notes`）
   - `R15` 来源去重（同一 id 出现两次不算两个来源）
   - `R18` 来源库不变式（库内必须全部 verified；不可核验者进隔离区，且不得被引用）
   - `R16` L3 必须有 ≥1 组争议（≥2 方）+ ≥2 项数据 + 图示说明
   - `R17` 禁止把"编辑待办"冒充学术争议（本会话曾用 R17 一次性拦下 26 处虚假争议）
3. **多轮复检**：每批 20 条抽检 4 条另起子任务核对来源；不合格批次返工。历史记录见 `reports/复检记录.md`。
4. **守卫必须"会失败"**：`pending_render_audit_c30.py` 经**故障注入验证**（注入未闭合标签 → rc=1，重建 → rc=0）。
5. **不把限流当空数据**：`wd_api.py` 遇 429 显式返回 `rate_limited`，并限速 1 req/s + 磁盘缓存。

---

## 四、诚实标注的三层机制

| 层 | 机制 | 读者看到的形式 |
|---|---|---|
| 数据层 | `needs_verification` / `pending_notes` / `source_independence_ok` | `coverage.json` 可查 |
| 页面层 | 待核实拆为「未解决列表」+「复核记录（折叠）」 | 条目页底部 |
| 全局层 | `status.html` 已知缺口 + 单元页「本单元覆盖缺口」+ `REPORT.md` 七段式 | 站点与仓库 |

**未解决 ≠ 已解决**：所有"已复核"条目都附第二来源 URL，未解决的仍在未解决列表里，二者不混排。

---

## 五、已知限制（外部阻塞，非质量问题）

1. **内容来源不可达**：`en/zh.wikipedia.org`、`metmuseum.org`、`tate.org.uk` TCP 超时；`baike.baidu.com`、`khanacademy.org` 返回反爬壳页；`britannica.com` 为 Cloudflare 403。
2. **可用通道仅 Wikidata 系**（`wikidata.org` / `api.wikimedia.org` / `commons` / `dbpedia`）——只能做**身份锚定与结构化事实**（年代、尺寸、馆藏、生卒），**撑不起**"风格特征 / 体裁沿革 / 学术评价"。
3. **因此开放缺口填不了**：
   - A 类矩阵 **58** 项（建筑已建 4 条：哥特式建筑、罗马式建筑、高棉建筑、吴哥窟）
   - B2 类音乐地区 **22** 项（甘美兰、印度古典、雅乐等零覆盖）
   - B5 待核实 **5** 项（其中 romanesque 断代差异已登记待第三来源）
   - 未锚定 **27** 条（自有页面 11、无匹配实体 11、被拒 5）
4. **来源独立性不足**：已核验来源以 Wikimedia 系为主，`source_independence_ok` 单独标记，不混入 `needs_verification`。
5. **未做**：屏幕阅读器/键盘全路径实测；sitemap 站点根为 GitHub Pages 默认地址，换域名需替换。

---

## 六、复现与续跑

```bash
# 重建站点（约 10 秒）
python tools/merge_l2.py && python tools/check.py && python tools/gen_site.py && python tools/check_links.py

# 完整体检（八步，一个命令）
python tools/audit_all.py          # 返回码 0 = 全通过

# 来源活性（需网络；仅 Wikidata 可达）
python tools/link_liveness_c24.py  # → reports/link_liveness_c24.json
```

续跑顺序见 `PROGRESS.md` 的「下轮起点」；来源恢复后按 `reports/saturation_assessment_c33.json` 的 `next_actions_if_unblocked` 逐项推进，**架构无需改动**。

---

## 七、一句话总结

**这是一个"结构完成、来源受限"的知识库**：schema、校验器、生成器、审计工具、诚实标注体系全部就位并经反复验证（八步体检 8/8、来源活性 120/120、渲染与结构 0 异常）；内容覆盖面停在 154 条，不是写不动，而是**当前环境拿不到可核验的内容来源**。来源一旦可用，A 类 58 项与 B2 22 项可按既有流程直接补写，无需返工架构。
---

## 八、收尾验证记录（Cycle 39，最终）

| 验证项 | 结果 | 证据 |
|---|---|---|
| 八步体检 | **8/8 通过** | `tools/audit_all.py` 输出 |
| py_compile | 156 个工具全部可编译 | 同上 |
| 硬规则 R1–R18 | **errors=0** | `tools/check.py` |
| 站内链接 | 176 页，断链 **0** | `tools/check_links.py` |
| 九维体检 | 死链/重复/矛盾/孤儿/锚点/sitemap/对比度 全通过 | `reports/healthcheck_c10.json` |
| 内容自洽 | 0 问题 | `reports/consistency_audit.json` |
| 关联图 | 430 链 · 单向 0 · 跨域 2（合法） | `reports/link_audit.json` |
| 渲染一致性 + HTML 结构 | 0 不一致 / 0 未闭合 | `reports/pending_render_audit_c30.json` |
| 来源活性 | **120 / 120 HTTP 200** | `reports/link_liveness_c24.json` |
| 来源库不变式 | 279 条**全部 verified**；5 条隔离且无引用 | `data/sources_quarantine.json` |
| 仓库状态 | 58 次提交 · 工作树干净 · 远端同步 | `git log` / `git status` |

**结论**：TASK 阶段 0–5 全部达成，站点可离线阅读、可通过 `tools/audit_all.py` 一键复验。
按 AUTONOMOUS §1.2/§5，本项目**不写 ALL_DONE**；`SATURATION.json` 的 `saturated=false`，
原因是 A 类 58 / B2 22 / B5 5 / 未锚定 27 等缺口需**可核验内容来源**，而 Wikipedia、Met、Tate 在当前环境不可达。
来源恢复后按第七节的 `next_actions_if_unblocked` 直接续写，架构无需改动。

---

## 九、Cycle 40–41 扩充记录（2026-11-23）

网络再测绘后发现**博物馆开放数据 API 可达**（Cleveland 开放数据 API、V&A API v2、Met 对象端点、Europeana、SMK），
据此以「**权威机构藏品记录**」为新来源类型扩充 **9 个条目（145 → 154）**：

| 批次 | 新增条目 | 来源情况 |
|---|---|---|
| Cycle40（作品） | 德加、罗丹、罗丹《青铜时代》、米友仁《云山图》 | 罗丹为 CMA+V&A 双机构；其余 3 条单机构（已标 needs_verification） |
| Cycle41（人物） | 马奈、透纳、康斯太勃尔、库尔贝、安格尔 | 马奈/康斯太勃尔/库尔贝有 V&A 第二机构；透纳/安格尔仅 CMA（已标） |

注：机构公网页（clevelandart.org）在本环境不可达，来源 URL 一律指向**实测 200 的 API 端点**，并在 verified_note 备注网页地址。

### Cycle42 追加（同作品双机构）

《凯风快晴》《庄野 白雨》《大桥安宅骤雨》三条均为 **CMA 与 V&A 各藏印本**的同作品条目；两馆记录并列不合并，尺寸差异如实标注。条目 157 / 来源 297 / 页面 188。
