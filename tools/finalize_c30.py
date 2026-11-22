# -*- coding: utf-8 -*-
"""Cycle30（体检轮）收尾：D033 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D033 — Cycle30 体检新增常驻检查「渲染一致性 + HTML 结构」，并对其做了故障注入验证
- **决定**：把 Cycle29 的呈现改动纳入常规体检，新增 `tools/pending_render_audit_c30.py` 并作为 `audit_all` 第 8 步常驻：
  ① **渲染一致性**：独立重算每条目的「未解决项数 / 复核记录数」，与页面实际渲染的 `<li>` 数与 details 摘要数字比对；
  ② **HTML 结构**：用 `html.parser` 逐页解析，捕获未闭合标签、多余闭合等结构错误；
  ③ 有不一致或结构错误时**返回码 1**，使 audit_all 整体失败。
- **并且做了故障注入测试**：人为往 `entries/gothic.html` 尾部注入 `<div><ol><li>fake`，检查如预期报出 3 处未闭合（div/ol/li）且 rc=1；随后重新生成站点，rc 回到 0。**验证守卫真的会失败，而不是永远显示 ok**。
- **理由**：Cycle29 大改了 145 页的渲染逻辑，仅靠 `check_links`（只查链接存在）无法发现"列表切分错位"或"标签未闭合"。守卫若从不失败，就等于没有守卫——所以必须注入故障验证一次。
- **可逆方式**：从 STEPS 移除该步即可。
- **代价**：体检多约 1–2 秒；解析 145 页。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle30","date":"2026-11-22","status":"completed",
 "gap_methods":["F体检(第六次)+新型结构校验"],"network":"partial",
 "new_entries":0,"upgrades":0,"reviews":145,"fixes":1,
 "healthcheck":{"audit_steps":"8/8","dead":0,"duplicates":0,"contradictions":0,"orphans":0,
   "bad_anchors":0,"sitemap":"176/176 一致","contrast":"AA","oneway":0,
   "render_mismatch":0,"html_struct_errors":0},
 "guard_test":"注入故障→报3处未闭合且 rc=1；重建后 rc=0（证明守卫有效）",
 "liveness_sample":"8/8 HTTP 200（最新锚点）",
 "check_result":"errors=0","check_links_result":"broken=0(176页)","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle30","date":"2026-11-22","methods_used":["F体检","渲染/结构校验","故障注入"],
 "gaps_found":{"structural":0},"network":"partial",
 "verdict":"八步体检全通过；渲染一致性0/结构错误0；守卫经注入验证有效；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle30"' not in t:
    block=('if cyc=="cycle30":\n'
           '    L.append("- 本轮为**体检轮 F**（第六次）：audit_all 增到 **8 步并全通过**。'
           '针对 Cycle29 的大改，新增两项常驻检查：**渲染一致性**（独立重算未解决项/复核记录数并与页面比对，0 不一致）'
           '与 **HTML 结构**（html.parser 逐页解析，0 未闭合）。'
           '并做了**故障注入测试**：人为往一页尾部注入 <div><ol><li>，检查如预期报 3 处未闭合且 rc=1，重建后 rc=0 ——'
           '证明守卫真的会失败，而不是永远显示 ok。'
           '活性抽样：最新 8 个锚点全部 HTTP 200。")\n')
    anchor='if cyc=="cycle29":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 29 已完成** → 下轮 **Cycle 30**",
              "- 当前轮次：**Cycle 30（体检轮）已完成** → 下轮 **Cycle 31**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")