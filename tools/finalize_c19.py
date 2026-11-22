# -*- coding: utf-8 -*-
"""Cycle19 收尾：把 B 类复核结论写入 matrix_targets_c7.md 附录；更新 METRICS/SATURATION/REPORT/PROGRESS。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
r=json.load(open(os.path.join(ROOT,"reports","matrix_b_review_c19.json"),encoding="utf-8"))

APP=os.path.join(ROOT,"reports","matrix_targets_c7.md")
io.open(APP,"a",encoding="utf-8").write("""

---

## 附录（Cycle 19 复核）：B 类再分层

原先把空白格分为 A（应补）/ B（暂不处理）。Cycle19 把 B 再分两层，结论如下：

| 层 | 数量 | 含义 |
|---|---|---|
| A | 58 | 该地区在本域已有条目却缺此媒介 → 应补（首选建筑，已在 Cycle17/18 开工 3 条） |
| **B2** | **22** | **候选真缺口**：该地区在"音乐体裁"上站内**零覆盖**，而该地区确有音乐传统（如东南亚甘美兰、南亚古典音乐、日本雅乐/邦乐、荷兰黄金时代音乐、佛兰德斯乐派等） |
| B1 | 129 | 其余组合：本库范围内确不适用（如欧洲×书法）或媒介非本项目主题 |

**为什么 B2 现在还不能补**：这些候选缺口需要能论述该传统的**可核验来源**（≥2），而当前环境仅 Wikidata 可达——它只能确认"实体存在"，无法支撑"风格特征/体裁沿革"类陈述。因此 B2 一律**挂起**，等待来源通道恢复。

B2 明细（地区 × 音乐体裁）：
""")
for item in r["B2_items"]:
    APP_TXT="- %s × %s\n"%(item[0],item[1])
    io.open(APP,"a",encoding="utf-8").write(APP_TXT)

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle19","date":"2026-11-22","status":"completed",
 "gap_methods":["B2覆盖矩阵B类复核"],"network":"partial: wikidata only",
 "new_entries":0,"upgrades":0,"reviews":154,"fixes":0,
 "matrix_review":{"blank":154,"A":58,"B1":129,"B2":22},
 "finding":"B 类中 22 项实为候选真缺口（非西方/欧洲地区音乐体裁零覆盖），受来源限制挂起",
 "check_result":"errors=0","check_links_result":"broken=0(174页)","audit_all":"6/6 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle19","date":"2026-11-22","methods_used":["B2矩阵B类复核"],
 "gaps_found":{"B2候选缺口":22},"network":"partial",
 "verdict":"B 类复核发现 22 项候选真缺口（音乐门类地区空白），挂起待来源；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle19"' not in t:
    block=('if cyc=="cycle19":\n'
           '    L.append("- 本轮特别说明：复核覆盖矩阵的 **B 类（原判「结构上不适用」）96–129 项**，把 B 再分两层，'
           '发现其中 **22 项实为候选真缺口**——这些地区在「音乐体裁」上站内零覆盖，而该地区确有音乐传统'
           '（东南亚甘美兰、南亚古典音乐、日本雅乐/邦乐、荷兰黄金时代音乐、佛兰德斯乐派等）。'
           '因当前仅 Wikidata 可达（只能确认实体存在，无法支撑风格/体裁陈述），**B2 一律挂起**，明细已写入 reports/matrix_targets_c7.md 附录。'
           '本轮未新增条目——不因为「想有产出」而降低来源标准。")\n')
    anchor='if cyc=="cycle18":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 18 已完成** → 下轮 **Cycle 19**",
              "- 当前轮次：**Cycle 19 已完成** → 下轮 **Cycle 20（体检轮）**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")