# 艺术史与音乐史导读

数据驱动、机器校验、诚实标注的静态知识库。零 JavaScript，可离线阅读，可部署到 GitHub Pages。

## 目录结构

| 路径 | 职责 |
|---|---|
| `index.html` | 站点首页（由 gen_site.py 生成） |
| `entries/*.html` | 条目详情页（L1 骨架 / L2 七节 + 自绘 SVG） |
| `timeline.html` / `all-index.html` / `sources.html` | 时间线 / 全站索引 / 来源库 |
| `units.html` / `units/<unit>.html` | 单元总览索引 / 每个知识单元的总览页（构成、分级条目、时间线片段、待核实） |
| `people.html` / `glossary.html` | 人物索引（按起始年代）/ 术语表（按标题序） |
| `assets/style.css` | 设计系统（CSS 变量、深色模式、SVG 类） |
| `scope.md` | 入选清单（6 份权威大纲取并集，编辑基准线） |
| `data/entries.json` | L1 种子数据（单一事实源，由 build_scope.py 生成） |
| `data/l2_generated/` | 写作代理原始产出 + 输入分块（暂存） |
| `data/l2/*.json` | L2/L3 覆盖层（每条目的七节 + SVG） |
| `data/site_entries.json` | 合并后的站点数据（merge_l2.py 产出） |
| `data/sources.json` | 全局来源库（91 条，86 已联网核验） |
| `data/coverage.json` | 覆盖状态（层级/来源数/待核实/独立性） |
| `tools/` | 构建与校验脚本 |
| `reports/覆盖矩阵.md` | 时期 × 地区 × 媒介 覆盖矩阵 |
| `REPORT.md` | 覆盖报告与复检结论 |
| `DECISIONS.md` / `PROGRESS.md` / `BLOCKERS.md` | 决策 / 进度游标 / 阻塞记录 |

## 重新生成

```bash
python tools/merge_l2.py       # 合并 L1 + L2 覆盖层
python tools/check.py          # 质量守门员（须 errors=0）
python tools/gen_site.py       # 渲染静态站点
python tools/check_links.py    # 站内链接核验（须 broken=0）
python tools/build_report.py   # 刷新 REPORT.md
python tools/link_audit.py         # 关联图审计（跨域/单向/入链分布）→ reports/link_audit.json
python tools/consistency_audit.py  # 内容自洽性审计（正文与"待核实"是否矛盾等）→ reports/consistency_audit.json
python tools/healthcheck_c10.py    # 九维站体检（死链/重复/矛盾/孤儿/锚点/sitemap/对比度等）
python tools/audit_all.py          # 一键体检：串行跑上述校验，汇总成一张表（返回码0=全通过）
```

来源核验（联网）：`python tools/build_sources.py` 然后 `python tools/reverify_sources.py`。

## 关键约定

- **层级**：条目重要性分核心/重要/补充；写作深度分 L1（骨架）/L2（七节）/L3（深度）。L1 全完成后才升 L2，核心→重要→补充顺序。
- **双源规则**：关键事实需 ≥2 个 verified 来源 id；查不到的年份/收藏地一律进"待核实"，不写入正文。
- **诚实标注**：coverage.json 的 `source_independence_ok` 单独标记来源是否真独立（不同作者且不同域名），不混入 needs_verification，避免比例失真。
- **SVG**：所有图示自绘，由 render_l2_svg.py 从结构化 diagram 确定性渲染，保证不出界、无脚本、浅深两色可读；不使用任何作品图片。
- **无人值守**：每轮最多 40 条，读 PROGRESS.md 续作，完成后写 ALL_DONE。
