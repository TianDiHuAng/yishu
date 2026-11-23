# -*- coding: utf-8 -*-
"""Cycle50 收尾：D053 + METRICS/SATURATION/REPORT/PROGRESS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D053 — Cycle50 catalog 不再是真值：14 处「覆盖层静默改写」已归并，并加 R20 守卫
- **事实**：巡检 `data/l2/*.json` 是否携带基础字段（title/kind/unit/era/region/medium/tier/def/when/overview），发现 **14 处覆盖层与 catalog 取值不同**：6 处 `when`、8 处 `overview`。由于 `merge_l2` 用 `update(ov)`，**全站显示的其实是覆盖层的值**——`check.py` 校验的是合并结果，**catalog 的原值从未被校验**。也就是说 `README`/`DECISIONS` 里「catalog.py 是单一事实源」这句话，此前**不成立**。
- **决定**：
  1. 把覆盖层的值**并入 catalog**（唯一字符串替换，两种引号都试，count==1 才改），再从覆盖层**删除该字段**；14 处全部完成、0 失败。
  2. 新增 **`tools/overlay_guard.py`（R20）**：覆盖层**不得**携带基础字段，违规即返回码 1；已接入 `audit_all`（成为第 9 步）。
- **为何采用覆盖层的值而非 catalog 的**：这些覆盖层值出现在后续轮次，措辞更**谨慎**（例如 `realism-art`：catalog「约公元1840—1870年」→「19世纪中叶」；`romanesque`：「约公元1000—1150年」→「约11—12世纪（中世纪盛期）」；`clerical-script`：「约公元前2世纪—公元3世纪」→「汉代」）。这几条精确年代**从未取得第二来源**，此前一直挂在待核实里；采用较谨慎的表述，与本项目「宁少勿编」的立场一致。
- **验证**：合并后 `overlay_field_audit` **不一致归零**；`overlay_guard` 做**注入测试**（往 `gothic.json` 塞一个 `when` → 报 `('gothic.json', ['when'])` 且 rc=1；还原 → rc=0 且 0 违规）；`audit_all` 现为 **9 步全通过**。
- **附带清理**：`roman-art` 最后一个 `overview` 载者（值本已相同）一并删除，覆盖层从此只承载深度字段（level/sections/svg/needs_verification/pending_notes/sources/related）。
- **可逆方式**：还原 catalog 对应字符串、把字段写回覆盖层、移除 guard。
- **代价**：6 个 `when` 变得更**宽泛**（如「汉代」「汉—唐」）；这是刻意取舍——宽泛但站得住，优于精确但无来源。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle50","date":"2026-11-23","status":"completed",
 "gap_methods":["全字段覆盖巡检（不止 related）"],"network":"partial",
 "new_entries":0,"fixes":15,
 "root_cause":"覆盖层携带基础字段，merge_l2 的 update() 使其成为全站真值，catalog 原值未被校验",
 "synced_fields":{"when":6,"overview":8},"overlays_cleaned":"14 字段 + roman-art overview",
 "new_guard":"tools/overlay_guard.py（R20）接入 audit_all，注入测试 rc=1→0",
 "audit_steps":9,"entries_total":180,"pages":215,
 "check_result":"errors=0","check_links_result":"broken=0(215页)","audit_all":"9/9 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle50","date":"2026-11-23","methods_used":["全字段巡检"],
 "gaps_found":{"field_drift":14},"network":"partial",
 "verdict":"14 处字段漂移归并 + R20 守卫；catalog 恢复为唯一真值；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle50"' not in t:
    block=('if cyc=="cycle50":\n'
           '    L.append("- 顺着上轮「字段被 update() 覆盖」的线索做**全字段巡检**，发现更严重的问题：'
           '**14 处覆盖层与 catalog 取值不同**（6 个 when、8 个 overview），而 `merge_l2` 的 update 让**覆盖层的值成为全站真值**，'
           '`check.py` 却只校验合并结果——也就是说「catalog.py 是单一事实源」这句话此前**并不成立**。'
           '处置：把覆盖层值**并入 catalog**、从覆盖层删除该字段（14/14 成功），并新增 **R20 守卫 overlay_guard**'
           '（覆盖层不得携带基础字段，违规 rc=1，已接入 audit_all 成为第 9 步），注入测试 rc=1→0。'
           '采用覆盖层值的理由：这些表述更谨慎（realism 1840—1870 → 19世纪中叶；romanesque 1000—1150 → 约11—12世纪），'
           '而那几条精确年代从未取得第二来源。代价是 6 个 when 变宽泛——**宽泛但站得住，优于精确但无来源**。")\n')
    anchor='if cyc=="cycle49":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])