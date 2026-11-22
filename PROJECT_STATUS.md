# 项目总表与交接说明

> 生成于 Cycle 37（体检轮）。本文件是**一次性的交接快照**，后续轮次若数据变化以 `REPORT.md` / `METRICS.json` 为准。
> 本项目遵循"无人值守自治"约定：**不写 ALL_DONE**，完成度以 `SATURATION.json` 的 `saturated` 判定。

---

## 一、交付物一览

| 类别 | 位置 | 说明 |
|---|---|---|
| 站点入口 | `index.html` | 首页（统计卡片 + 单元导航 + 深度条目） |
| 状态页 | `status.html` | 规模 / 来源构成 / 校验方式 / **已知缺口** |
| 条目页 | `entries/*.html` | 145 条；L2 七节 + 自绘 SVG + 来源表 + 反链 + 来源构成徽标 |
| 单元总览 | `units.html` + `units/*.html` | 22 个单元页（构成、分级条目、时间线、**本单元覆盖缺口**） |
| 索引类 | `timeline.html` / `people.html` / `glossary.html` / `all-index.html` / `entities.html` / `sources.html` | 时间线（六段分组）/ 人物 / 术语 / 全站 / 实体对照 / 来源库 |
| 机器产物 | `sitemap.xml` / `robots.txt` | 自动收录 176 页 |
| 数据层 | `data/entries.json`（种子）、`data/l2/*.json`（覆盖层）、`data/site_entries.json`（合并）、`data/sources.json`、`data/coverage.json` | 单一事实源 → 覆盖层 → 合并产物 |
| 编辑基准 | `scope.md` | 6 份权威大纲取并集，109→145 条目的入选依据 |
| 校验器 | `tools/check.py`（R1–R17）、`tools/audit_all.py`（八步） | 机器守门员 |
| 证据库 | `reports/` | 覆盖矩阵、九维体检、关联图、锚定复核、饱和评估、活性核验 |
| 决策记录 | `DECISIONS.md`（D001–D040）、`BLOCKERS.md` | 每项决定的依据、可逆方式与代价 |

---

## 二、关键数字（Cycle 37 时点）

| 指标 | 数值 | 备注 |
|---|---|---|
| 条目总数 | **145** | L2 139 / L3 6 / **L1 0** |
| 重要性分布 | 核心 48 / 重要 85 / 补充 12 | 核心与重要**全部 ≥ L2** |
| 知识单元 | 22 | 艺术 8 + 中国艺术 2 + 亚洲艺术 1 + 音乐 7 + 中国音乐 1 + 导读/比较/术语/作品档案 4 |
| 来源库 | **279** | **全部 verified=true**（R18 强制）；另有 5 条不可核验来源在 `data/sources_quarantine.json` 隔离区 |
| 条目↔实体关联 | **118 / 145（81%）** | 41 条结构化事实 + 77 条身份锚点 |
| 关联图 | 430 条关联 · 单向 **0** · 跨域 2（合法） | 度均 3.0 / 最大 12 |
| 站点页面 | **176** | 0 断链 |
| 硬规则 | R1–R17 **errors=0** | 含 R17「争议必须真实」 |
| 八步体检 | **8/8 通过** | py_compile(150 工具) + 硬规则 + 链接 + 九维 + 自洽 + 关联图 + 单向 + 渲染/结构 |
| 来源活性 | **120 / 120 HTTP 200** | 逐个 curl 实测 |
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

**这是一个"结构完成、来源受限"的知识库**：schema、校验器、生成器、审计工具、诚实标注体系全部就位并经反复验证（八步体检 8/8、来源活性 120/120、渲染与结构 0 异常）；内容覆盖面停在 145 条，不是写不动，而是**当前环境拿不到可核验的内容来源**。来源一旦可用，A 类 58 项与 B2 22 项可按既有流程直接补写，无需返工架构。