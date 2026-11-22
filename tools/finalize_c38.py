# -*- coding: utf-8 -*-
"""Cycle38 收尾：D042 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D042 — Cycle38 状态页数字改为动态生成（并修掉两处口径错误）
- **决定**：
  1. `sources.html` 顶部新增**隔离来源说明**（5 条：404/反爬壳页/限流/403），并注明"禁止被任何条目引用（R18 强制）"。
  2. `status.html` 的「已知缺口」中「建筑已开工 N 条」改为**从数据动态统计**；硬规则范围更新为 R1–R18；并补充一句 R18 不变式说明。
- **过程中修的两处错误（我造成的）**：
  - 首次补丁把 Python 字符串从中间换行截断 → 生成器 SyntaxError（被 py_compile 当场拦下）。改为整块重写并用 `py_compile` 自检。
  - 第一版统计把「medium 含"建筑"」当建筑条目 → 显示 **10 条**（把"建筑,雕塑""绘画,建筑"等综合条目也算进去了）。改为 `medium == "建筑"` 的**专用建筑条目** → 正确显示 **4 条**（哥特式建筑 / 罗马式建筑 / 高棉建筑 / 吴哥窟）。
- **理由**：状态页是给读者看的"承诺页"，数字必须与数据一致且口径正确。**口径错了比数字错了更危险**——10 条会让读者以为建筑覆盖已相当可观，实际只有 4 条专条。
- **可逆方式**：回退到硬编码（不推荐）。
- **代价**：状态页每次生成多一次统计；`_arch` 口径写死为"专条"，若将来新增"建筑"前缀媒介需同步。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle38","date":"2026-11-22","status":"completed",
 "gap_methods":["站点收尾打磨"],"network":"partial",
 "new_entries":0,"upgrades":0,"reviews":0,"fixes":3,
 "ui_change":"sources.html 隔离来源说明；status.html 数字动态化 + R18 说明",
 "self_fixed":["字符串换行截断（py_compile 拦下）","建筑计数口径错误 10→4"],
 "check_result":"errors=0","check_links_result":"broken=0(176页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle38","date":"2026-11-22","methods_used":["站点打磨"],
 "gaps_found":{},"network":"partial",
 "verdict":"状态/来源页透明化；修两处自造错误；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle38"' not in t:
    block=('if cyc=="cycle38":\n'
           '    L.append("- 本轮为**站点收尾打磨**：①sources.html 增加**隔离来源说明**'
           '（5 条：404 / 反爬壳页 / 限流 / 403，明示禁止被引用，R18 强制）；'
           '②status.html 数字改为**动态生成**，硬规则范围更新为 R1–R18 并补不变式说明。'
           '过程中修掉两处自己造成的错误：补丁把字符串从中间换行截断（被 py_compile 当场拦下）；'
           '建筑计数误用「medium 含建筑」→ 显示 10 条，改为「medium == 建筑」的专条 → 正确 4 条。'
           '口径错比数字错更危险：10 条会让读者以为建筑覆盖可观，实际只有 4 条专条。")\n')
    anchor='if cyc=="cycle37":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 37（体检轮）已完成** → 下轮 **Cycle 38**",
              "- 当前轮次：**Cycle 38 已完成** → 下轮 **Cycle 39（体检轮）**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")