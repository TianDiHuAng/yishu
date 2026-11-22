# PROGRESS.md — 进度游标（自治模式）

> 每次启动先读本文件与 BACKLOG/METRICS/SATURATION/REPORT，从"下轮起点"续作。
> 按 AUTONOMOUS.md：不写 ALL_DONE；饱和以 SATURATION.json 为准。

- 当前轮次：**Cycle 4 已完成** → 下轮 **Cycle 5（体检轮 F）**
- 状态：正常（未饱和）
- 最近更新：2026-11-22

## 上轮（Cycle 4）做了什么
- 缺口发现 4 种（B1 History of painting 权威大纲 / B4 作品档案 / B5 剩余6项 / B6 回溯5条来源）
- B1 发现南亚/东南亚/东亚艺术零覆盖 → 核验9条来源 → 新增 art-asia 单元8条（印度艺术/佛教艺术/阿旃陀/高棉/吴哥/日本艺术/浮世绘/禅画，D014 记录）
- 实现 L3 深度层：check.py R16 校验（争议≥2方+数据≥2项+图示说明，禁虚构学者）+ gen_site.py 渲染争议并列表/数据表/深度徽章；4个核心条目升级 L3（greek-art/gothic/impressionism/baroque-music），争议均为真实分歧、holder 用泛称
- B5 剩余6项：仅1项（romanesque 地区差异）可核验解决，5项诚实保留待核实
- B6 回溯5条：4条仍不可达/SSL失败，1条可达但日期异常未采纳
- QC 抽检4条：4 PASS（含2条L3的争议/数据逐项获来源支撑）
- 结果：**137 条目**（L2 133 + L3 4）；check errors=0 / check_links broken=0（141页）；来源154（149 verified）；orphan=0
- 提交：cycle4批1（8亚洲条目）、cycle4批2（L3实现+4升级+B5剩余1项）

## 下轮起点（Cycle 5 — 体检轮 F，替代一半配额）
1. 读所有状态文件；check.py（应 errors=0）。
2. **体检 F（必做）**：死链（check_links）、过期数据（现状类>12个月未核对的重新核对）、重复条目、全站数据矛盾、孤儿页（应=0）、与来源文本重合度（抽查）。
3. 缺口发现 ≥2 种（轮换 B4/B6/B7）；B6 的5条动态继续回溯（若仍不可达，按 §6 记 BLOCKERS 并跳过）。
4. 执行 BACKLOG P4：L3 再升级4-6个核心条目（有真实争议者）；覆盖矩阵150空格补盲（需权威依据）；B5 剩余5项。
5. 质量闸抽检10%；异常监控；更新状态文件；commit+push。

## 长期待办（BACKLOG P4）
- 核心条目 L3 深度升级（44个核心仍 L2）；覆盖矩阵150空格补盲；B5 剩余5项；B4 作品档案缺口（需来源）；B6 5条动态（4不可达）。

## 历史日志
- pre-autonomous：109条目、42→82 L2。
- Cycle 1：114条目全L2、新增5中国艺术史。
- Cycle 2：125条目全L2、新增11导读比较。
- Cycle 3：129条目全L2、B5复核38项+孤儿清零+新增4条。
- Cycle 4：137条目（L3启动，4条L3）、新增8亚洲艺术、B5剩余1项、抽检4全PASS。

ALL_DONE：按 AUTONOMOUS.md 不写。
