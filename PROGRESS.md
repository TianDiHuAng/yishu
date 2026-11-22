# PROGRESS.md — 进度游标

> 每次启动先读本文件，从"当前阶段/下一轮起点"续作。全部完成后写入 `ALL_DONE`。

- 状态：进行中
- 当前阶段：阶段0（范围界定）
- 下一轮起点：scope.md / coverage.json / 覆盖矩阵 生成中
- 本轮已处理条目数：0 / 40
- 最近更新：2026-11-22

## 阶段清单
- [ ] 阶段0 范围：scope.md、coverage.json、覆盖矩阵
- [ ] 阶段1 来源库：sources.json（≥80条，核对后 verified）
- [ ] 阶段2 校验器：tools/check.py
- [ ] 阶段3 样板：2个条目到L2并通过检查
- [ ] 阶段4 分批写作（L1先行，每轮≤40条）
- [ ] 阶段5 总览/索引/时间线/导航/REPORT.md
- [ ] 站点生成：gen_site.py → index.html

## 续跑日志
- 2026-11-22 14:57 初始化项目，读 TASK_art.md（63行）与 WORKFLOW.md（384行），工作区原为空，git init 完成。

ALL_DONE 标记：（尚未写入）
