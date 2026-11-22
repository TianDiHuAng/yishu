# PROGRESS.md — 进度游标

> 每次启动先读本文件，从"当前阶段/下一轮起点"续作。全部完成后写入 `ALL_DONE`。

- 状态：进行中
- 当前阶段：阶段4（分批写作，L1先行，按 核心→重要→补充 升级）
- 累计已处理条目数：109 L1 + 82 L2（2样板 + 40 + 40）
- 本轮（第2批）已处理：40 条（4核心 + 36重要）→ L2
- 下一轮起点：剩余全部27条（23重要 + 4补充），清单见下方
- 最近更新：2026-11-22

## 阶段清单
- [x] 阶段0 范围：scope.md、coverage.json、覆盖矩阵（109条目/17单元/6大纲并集）
- [x] 阶段1 来源库：sources.json（95条，90 verified ≥80）
- [x] 阶段2 校验器：tools/check.py（R1-R15，当前 errors=0）
- [x] 阶段3 样板：impressionism、baroque-music 到 L2，通过检查
- [ ] 阶段4 分批写作：第1、2批共80条完成；剩余27条（23重要+4补充）待升级 —— 下一轮可全部完成
- [ ] 阶段5 总览页/索引/时间线/导航/REPORT.md（骨架已生成，随条目增加需刷新）
- [x] 站点生成：gen_site.py → index.html（113页，0断链）
- [x] 批次复检：两批共抽16条；两批均完成返工与复核（见 reports/复检记录.md）

## 续跑日志
- 2026-11-22 14:57 初始化项目，读 TASK_art.md（63行）与 WORKFLOW.md（384行），工作区原为空，git init 完成。
- 2026-11-22 15:10 阶段0：联网对照6份权威大纲目录取并集，生成 scope.md（109条目/17单元）、coverage.json、覆盖矩阵.md、entries.json(L1种子)。
- 2026-11-22 15:15 阶段1：build_sources.py+reverify_sources.py 联网核对，sources.json 91条/86 verified。
- 2026-11-22 15:20 阶段2：check.py 实现 R1-R14，修正R2公元前年份逻辑后 errors=0；commit 0ac5ce6。
- 2026-11-22 15:30 阶段3+站点：两条样板到L2；gen_site.py 渲染113页；修正条目页 breadcrumb 的 ../ 层级错配，check_links broken=0。
- 2026-11-22 15:45 阶段4第1批：10代理分两波写作40核心条目→L2；check errors=0。
- 2026-11-22 15:50 批次复检1：抽8条，6 PASS/2 REWORK（gothic、greek-art），已返工并同步；commit 9bcede5 + 返工同步commit。
- 2026-11-22 15:52 生成本轮覆盖报告 REPORT.md；记录下一轮起点。
- 2026-11-22 16:05 阶段4第2批：40条（4核心+36重要）→L2，共82 L2；合成后 check errors=0 / broken=0。
- 2026-11-22 16:10 来源完整性修复：发现8条 sources 重复 id，加固 check.py R15（唯一id计数+禁重复），新增4条已核验来源+source_fixes.json 修复；修复 check.py R2 接受朝代纪年（汉代/汉—唐）。
- 2026-11-22 16:12 批次复检2：抽8条，2 PASS/6 REWORK（年代区间与技法术语无来源逐字支撑），触发整批返工；6条改概括+移入待核实+全批40条补诚实声明；recheck2b 复核又发现3条残留，二轮清理完成；程序化审计确认正文无裸断言。全链校验 errors=0/broken=0。
- 2026-11-22 16:20 REPORT.md 改为读取 reports/复检记录.md，避免生成器覆盖手填结论。

## 下一轮操作清单（供续跑）
1. 重读本文件、REPORT.md、DECISIONS.md、reports/复检记录.md。
2. 剩余27条一次写完（不超过40配额）。用 make_batch2.py 同法生成输入（改为 batch3），排除已有 L2 覆盖层。
3. workflow 写作（7个chunk）→ render_l2_svg.py → merge_l2.py → check.py → gen_site.py → check_links.py → build_report.py。
4. 27条→抽4条复检（或按20抽4再补）；有问题返工。
5. 全部109条到 L2 后：阶段5 刷新 REPORT.md，若有余力为核心条目做 L3；最终全链校验通过，写入 ALL_DONE，并 update_goal complete。

## 下一轮27条清单
mannerism,mona-lisa,northern-renaissance,raphael,venetian-school,fugue,monteverdi,sonata,guzheng,pipa,yayue,haydn,sonata-form,organum,debussy,impressionism-music,minimalism-music,serialism,madrigal,palestrina,lied,schubert,symphonic-poem,cave-art,paleolithic-sculpture,gongbi,early-christian-art

ALL_DONE 标记：（尚未写入 — 阶段4尚有27条L1待升级）
