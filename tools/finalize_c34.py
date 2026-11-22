# -*- coding: utf-8 -*-
"""Cycle34 收尾：D037 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D037 — Cycle34 文档定稿 + 单元页公开「本单元覆盖缺口」
- **决定**：
  1. **重写 README**：此前的版本还写着"来源 91 条/86 verified"与"完成后写 ALL_DONE"（与自治约定冲突）。新版按现状重写：规模数字、22 个目录职责、完整管线（含 `audit_all` 八步）、9 条关键约定、**已知限制专章**（来源不可达的具体清单）、以及"如何续跑"。
  2. **单元页新增「本单元覆盖缺口」**：从 `reports/matrix_targets_c7.json`（A 类）与 `matrix_b_review_c19.json`（B2）按该单元涉及的地区×媒介筛选，页面直接展示，并标注"补写需先取得可核验来源，未取得前不写作"。
- **理由**：站点已有 `status.html` 展示全局缺口，但读者是按单元浏览的——在单元页就地看到"这一块还缺什么"，比翻到状态页更有用；同时把"为什么不补"的规则写在旁边的做法，本身就是诚实标注。
- **可逆方式**：删除 `load_gap_targets` 与对应区块，README 可回退到旧版（不推荐）。
- **代价**：单元页依赖 `reports/` 下两个 JSON（缺失时静默跳过，不报错）。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle34","date":"2026-11-22","status":"completed",
 "gap_methods":["文档定稿","站点信息架构补全"],"network":"partial",
 "new_entries":0,"upgrades":0,"reviews":0,"fixes":0,
 "ui_change":"单元页新增『本单元覆盖缺口』（A/B2 按地区×媒介筛选）",
 "doc":"README 全面重写（规模/管线/9条约定/已知限制/续跑指引）",
 "check_result":"errors=0","check_links_result":"broken=0(176页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle34","date":"2026-11-22","methods_used":["文档定稿","信息架构"],
 "gaps_found":{},"network":"partial",
 "verdict":"README 重写 + 单元页缺口可视化；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle34"' not in t:
    block=('if cyc=="cycle34":\n'
           '    L.append("- 本轮是**文档与信息架构轮**。①**重写 README**：旧版仍写着「来源 91 条/86 verified」与「完成后写 ALL_DONE」'
           '（与自治约定冲突），新版改为现状数字、完整管线（audit_all 八步）、9 条关键约定、**已知限制专章**'
           '（Wikipedia/Met/Tate 不可达、百度与 Khan 仅壳页、来源独立性不足、27 条未锚定）与续跑指引。'
           '②**单元页新增「本单元覆盖缺口」**：从矩阵 A/B2 清单按地区×媒介筛选后就地展示，并注明'
           '「补写需先取得可核验来源，未取得前不写作」——把「为什么这里空着」直接写在读者眼前。")\n')
    anchor='if cyc=="cycle33":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 33（体检轮+饱和评估）已完成** → 下轮 **Cycle 34**",
              "- 当前轮次：**Cycle 34 已完成** → 下轮 **Cycle 35**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")