# PROGRESS.md — 进度游标（自治模式）

> 每次启动先读本文件与 BACKLOG/METRICS/SATURATION/REPORT，从"下轮起点"续作。
> 按 AUTONOMOUS.md：不写 ALL_DONE；饱和以 SATURATION.json 为准。

- 当前轮次：**Cycle 1 已完成** → 下轮 **Cycle 2**
- 状态：正常（未饱和）
- 最近更新：2026-11-22

## 上轮（Cycle 1）做了什么
- 缺口发现 5 种方法（B1 权威大纲对照 / B2 覆盖矩阵 / B3 悬空引用 / B5 待核实 / B7 深度缺口）
- B1 用新大纲发现中国史前—先秦—魏晋—隋唐 5 处缺口 → 联网核验 10 条新来源 → 新增 5 条目（D011 记录依据）
- 27 条重要/补充 tier L1→L2；本轮共 32 任务，分 4 批执行，每批 check+commit
- 质量闸抽检 4 条：3 PASS / 1 REWORK（early-christian-art 已返工）
- 结果：**114 条目全部 L2**（L1=0）；check errors=0 / check_links broken=0；来源 105（100 verified）
- 4 次 cycle1 提交：`d43aea6`、`dae8e50`、`873b300`、`63e398c`（返工在第4批后）

## 下轮起点（Cycle 2）
1. 读 PROGRESS / BACKLOG / METRICS / SATURATION / REPORT / DECISIONS / BLOCKERS；运行 check.py（当前应 errors=0）。
2. 缺口发现要做 ≥3 种，**本轮必须轮换到尚未用的 B4（读者问题清单）与 B6（近期动态）**，再从 B1/B2/B3/B5/B7 中选 1 种。
   - B4：为初学者/学生/爱好者/从业者各列20个问题，检查站内能否直接找到答案。
   - B6：联网搜近12个月艺术史/音乐史新研究、新发现、新事件，补充或更新相关条目（标日期+来源）。
3. 排序入 BACKLOG.md；执行 ≤40 任务；每10个 check+commit。
4. 质量闸：抽检 10%（≥3）另起子任务核对来源；异常监控（待核实占比、相似度）。
5. 更新 coverage.json / METRICS.json / SATURATION.json / PROGRESS.md / REPORT.md；git commit。
6. Cycle 5 时做体检 F（死链/过期数据/重复/矛盾/孤儿/重合度），替代当轮一半配额。

## 长期待办（BACKLOG P4）
- 32 条孤儿页补入链；82 条待核实逐项复核；核心条目 L3 深度升级；覆盖矩阵稀疏格补盲。

## 历史日志
- pre-autonomous（阶段0-5）：109 条目、91→95 来源、42→82 L2、两批复检返工。
- Cycle 1（2026-11-22）：114 条目全部 L2、105 来源（100 verified）、抽检返工1条。

ALL_DONE：按 AUTONOMOUS.md 不写。
