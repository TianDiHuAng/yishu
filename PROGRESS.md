# PROGRESS.md — 进度游标

> 每次启动先读本文件，从"当前阶段/下一轮起点"续作。全部完成后写入 `ALL_DONE`。

- 状态：进行中
- 当前阶段：阶段4（分批写作，L1先行，按 核心→重要→补充 升级）
- 累计已处理条目数：109 L1 + 42 L2（2样板 + 40本轮核心）
- 本轮（第1批）已处理：40 条核心 → L2
- 下一轮起点：剩余4个核心（stravinsky, schoenberg, china-music-history, jingju）+ 重要 tier 前36个
- 最近更新：2026-11-22

## 阶段清单
- [x] 阶段0 范围：scope.md、coverage.json、覆盖矩阵（109条目/17单元/6大纲并集）
- [x] 阶段1 来源库：sources.json（91条，86 verified ≥80）
- [x] 阶段2 校验器：tools/check.py（R1-R14，当前 errors=0）
- [x] 阶段3 样板：impressionism、baroque-music 到 L2，通过检查
- [ ] 阶段4 分批写作：第1批40核心完成；剩余4核心 + 59重要 + 4补充 待升级
- [ ] 阶段5 总览页/索引/时间线/导航/REPORT.md（骨架已生成，随条目增加需刷新）
- [x] 站点生成：gen_site.py → index.html（113页，0断链）
- [x] 批次复检：抽8条，6 PASS/2 REWORK，2条已返工并同步

## 续跑日志
- 2026-11-22 14:57 初始化项目，读 TASK_art.md（63行）与 WORKFLOW.md（384行），工作区原为空，git init 完成。
- 2026-11-22 15:10 阶段0：联网对照6份权威大纲目录取并集，生成 scope.md（109条目/17单元）、coverage.json、覆盖矩阵.md、entries.json(L1种子)。
- 2026-11-22 15:15 阶段1：build_sources.py+reverify_sources.py 联网核对，sources.json 91条/86 verified。
- 2026-11-22 15:20 阶段2：check.py 实现 R1-R14，修正R2公元前年份逻辑后 errors=0；commit 0ac5ce6。
- 2026-11-22 15:30 阶段3+站点：两条样板到L2；gen_site.py 渲染113页；修正条目页 breadcrumb 的 ../ 层级错配，check_links broken=0。
- 2026-11-22 15:45 阶段4第1批：10代理分两波写作40核心条目→L2，SVG由render_l2_svg.py确定性渲染；check errors=0。
- 2026-11-22 15:50 批次复检：recheck子任务抽8条核对来源，6 PASS/2 REWORK（gothic、greek-art），已返工并重跑全链校验 errors=0/broken=0；commit 9bcede5 + 返工同步commit。
- 2026-11-22 15:52 生成本轮覆盖报告 REPORT.md；记录下一轮起点。

## 下一轮操作清单（供续跑）
1. 重读本文件、REPORT.md、DECISIONS.md。
2. 用 tools/make_batch1.py 同法生成下一批输入（剩余4核心 + 重要前36，共40条），注意排除已有 L2 覆盖层的 id。
3. workflow 写作 → render_l2_svg.py → merge_l2.py → check.py → gen_site.py → check_links.py → build_report.py。
4. 每满20条抽4条复检；更新 coverage/progress/commit。
5. 剩余条目写完后，阶段5 刷新 REPORT.md 统计，全链校验通过，写入 ALL_DONE。

ALL_DONE 标记：（尚未写入 — 阶段4尚有67条L1待升级）
