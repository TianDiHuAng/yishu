# PROGRESS.md — 进度游标

> 每次启动先读本文件，从"当前阶段/下一轮起点"续作。全部完成后写入 `ALL_DONE`。

- 状态：进行中
- 当前阶段：阶段3（样板条目）
- 下一轮起点：写2个核心条目到L2并生成合规SVG，通过 check.py
- 累计已处理条目数：109（L1种子，阶段0生成）
- 最近更新：2026-11-22

## 阶段清单
- [x] 阶段0 范围：scope.md、coverage.json、覆盖矩阵（109条目/17单元/6大纲并集）
- [x] 阶段1 来源库：sources.json（91条，86 verified ≥80）
- [x] 阶段2 校验器：tools/check.py（R1-R14，当前 errors=0）
- [ ] 阶段3 样板：2个条目到L2并通过检查
- [ ] 阶段4 分批写作（L1先行，每轮≤40条）
- [ ] 阶段5 总览页/索引/时间线/导航/REPORT.md
- [ ] 站点生成：gen_site.py → index.html

## 续跑日志
- 2026-11-22 14:57 初始化项目，读 TASK_art.md（63行）与 WORKFLOW.md（384行），工作区原为空，git init 完成。
- 2026-11-22 15:10 阶段0：联网对照6份权威大纲目录取并集，生成 scope.md（109条目/17单元）、coverage.json、覆盖矩阵.md、entries.json(L1种子)。
- 2026-11-22 15:15 阶段1：build_sources.py+reverify_sources.py 联网核对，sources.json 91条/86 verified。
- 2026-11-22 15:20 阶段2：check.py 实现 R1-R14，修正R2公元前年份逻辑后 errors=0；commit 0ac5ce6。

ALL_DONE 标记：（尚未写入）
