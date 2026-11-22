# -*- coding: utf-8 -*-
"""Cycle37 收尾：D041 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D041 — Cycle37 来源库隔离与 R18 不变式 + 项目总表
- **事实**：体检核对数字时发现 `sources.json` 里有 **5 条 `verified=false`**（2 条 Wikipedia 页面 404、1 条 Met 时间线 429、1 条 Khan 为反爬壳页、1 条 NGA 403）。经查**没有任何条目引用它们**。
- **决定**：
  1. 把这 5 条移入 `data/sources_quarantine.json`（保留原因，备来源恢复后重核），使 `sources.json` 变为 **279 条且全部 verified**；
  2. 新增 `check.py R18`：来源库内出现未核验来源 → 报错；被引用的来源必须在库内。
  3. 并做**故障注入验证** R18：临时插入一条 `verified=false` → 报 `[R18] 来源库含未核验来源` 且 rc=1；还原后 rc=0。
  4. 新增 `PROJECT_STATUS.md`（项目总表与交接说明），并在撰写时**自查发现两处数字错误**（来源写成"284 全部 verified"实为 279、建筑条目写成 3 实为 4），已更正。
- **理由**：一个"来源库"里混着不可用条目，等于给后续引用留了隐患；把"库内必全 verified"变成机器不变式，比靠人记更可靠。写下总表时自查出的两处错误，也说明**交接文档必须对着数据核**，不能凭记忆。
- **可逆方式**：把隔离区条目搬回并移除 R18 即可。
- **代价**：来源库数字从 284 调整为 279；隔离区需在来源恢复后人工重核。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle37","date":"2026-11-22","status":"completed",
 "gap_methods":["F体检(第八次)","来源库不变式","交接文档"],"network":"partial: wikidata ok",
 "new_entries":0,"upgrades":0,"reviews":0,"fixes":5,
 "healthcheck":{"audit":"8/8","dead":0,"duplicates":0,"contradictions":0,"orphans":0,"bad_anchors":0,
   "sitemap":"0/0","contrast":"AA","oneway":0,"render_mismatch":0,"html_struct":0},
 "liveness":{"wd_sources":120,"http_200":120,"failed":0},
 "sources_quarantined":5,"sources_total":279,"r18_added":True,
 "doc":"PROJECT_STATUS.md 新增（含数字自查与更正）",
 "check_result":"errors=0","check_links_result":"broken=0(176页)","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle37","date":"2026-11-22","methods_used":["F体检","来源库不变式","交接文档"],
 "gaps_found":{"unverified_sources":5},"network":"partial",
 "verdict":"5 条不可核验来源隔离 + R18（经注入验证）；新增项目总表；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle37"' not in t:
    block=('if cyc=="cycle37":\n'
           '    L.append("- 本轮为**体检轮 + 来源库治理**。八步体检全通过、120/120 来源活性 200。'
           '核对数字时发现 sources.json 里有 **5 条 verified=false**（2 个页面 404、Met 429、Khan 反爬壳页、NGA 403），'
           '且**没有任何条目引用**——已移入 data/sources_quarantine.json（留原因），'
           '并新增 **check.py R18** 不变式：「来源库内必须全部 verified，被引用者必须在库内」，'
           '且做了**注入验证**（临时塞入一条未核验来源 → 报 R18 且 rc=1，还原 → rc=0）。'
           '另新增 PROJECT_STATUS.md（项目总表与交接），撰写时**自查发现并更正了两处数字错误**'
           '（来源 284→279、建筑条目 3→4）。来源库现 **279 条全部 verified**。")\n')
    anchor='if cyc=="cycle36":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 36 已完成** → 下轮 **Cycle 37（体检轮）**",
              "- 当前轮次：**Cycle 37（体检轮）已完成** → 下轮 **Cycle 38**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")