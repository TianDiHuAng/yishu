# -*- coding: utf-8 -*-
"""Cycle29 收尾：D032 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D032 — Cycle29 待核实节的呈现重构（结构不变，文字零改动）
- **决定**：条目页的「待核实」由一整段文字改为三层呈现：
  ① 开头「状态说明：…」独立为提示句（.note）；
  ② **待核实（未解决）** 用有序列表，按 （N） 编号切分，无编号则按句号/分号切句；
  ③ **复核记录** 用 `<details>` 折叠，逐条列出【已复核…】片段与第二来源 URL。
  字符串内容**一字未改**，只改渲染。
- **理由**：145 页的待核实经多轮复核已堆到 3–10 项，混排版导致"未解决"与"已解决"糊在一起，读者难以判断哪些还没落实。这与项目"诚实标注"的目标相冲突——**诚实不仅要不隐瞒，还要让人一眼看出哪条还没解决**。
- **过程中的两个坑（已修）**：
  1. 首次补丁脚本写入后内容未生效（git diff 只显示 1 行），改为**单脚本原子完成全部替换并在末尾自检**（打印 has render_pending / L2 calls / L1 calls / css），避免"以为改了其实没改"。
  2. 首版按【已复核】切分时，把开头"状态说明…以【已复核】为准"里的**行内提及**也当成记录标记，导致正文被切碎。改为先整句摘出状态说明，再按"【已复核…】+正文至下一个【"匹配。
- **可逆方式**：恢复为单段 `<div class='pending'>…</div>` 渲染即可。
- **代价**：复核记录默认折叠，读者需点开（但每条都有摘要计数提示）。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle29","date":"2026-11-22","status":"completed",
 "gap_methods":["呈现层重构（无内容变更）"],"network":"partial",
 "new_entries":0,"upgrades":0,"reviews":145,"fixes":3,
 "ui_change":"待核实 → 提示句 + 未解决列表 + 复核记录折叠（145 页）",
 "fix_detail":"首次补丁未落盘→改单脚本自检；首版切分误伤状态说明→先摘句再切分",
 "check_result":"errors=0","check_links_result":"broken=0(176页)","audit_all":"7/7 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle29","date":"2026-11-22","methods_used":["呈现重构"],
 "gaps_found":{},"network":"partial",
 "verdict":"待核实呈现重构（145页）；文字未改；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle29"' not in t:
    block=('if cyc=="cycle29":\n'
           '    L.append("- 本轮做**呈现层重构**（文字零改动）：145 页的「待核实」原本混作一大段，'
           '多轮复核后堆到 3–10 项，「未解决」与「已解决」糊在一起。改为三层：'
           '①状态说明独立成提示句；②**待核实（未解决）**用有序列表（按（N）编号或句号切分）；'
           '③**复核记录**用 details 折叠并逐条附第二来源 URL。'
           '理由是诚实标注不仅要不隐瞒，还要让人一眼看出哪条仍未落实。'
           '过程中修了两个自造坑：补丁未落盘（改单脚本+末尾自检）、切分误伤状态说明中的行内提及。")\n')
    anchor='if cyc=="cycle28":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 28（体检轮）已完成** → 下轮 **Cycle 29**",
              "- 当前轮次：**Cycle 29 已完成** → 下轮 **Cycle 30**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")