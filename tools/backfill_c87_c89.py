# -*- coding: utf-8 -*-
"""补记 cycle87（希腊罗马 4 条）与 cycle89（文档对齐）的 METRICS/SATURATION/DECISIONS。
之前 cycle87 的条目随 cycle88 一并提交，但漏写轮次记录，导致 REPORT 无 cycle87 块。
"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MP=os.path.join(ROOT,"METRICS.json"); met=json.load(open(MP,encoding="utf-8"))
rounds=met["rounds"]
idx88=next((i for i,r in enumerate(rounds) if r["cycle"]=="cycle88"), None)
assert idx88 is not None
cycle87={"cycle":"cycle87","date":"2026-11-23","status":"completed",
 "gap_methods":["希腊罗马实物填补"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["kouros-torso","herakles-bronze","roman-athlete-statue","vespasian-recut-head"],
 "greco_roman_objects":4,"new_sources":4,"sources_total":427,"entries_total":296,"pages":333,
 "checker_catch":"R2 抓到公元前区间写法歧义（已双写公元前）",
 "check_result":"errors=0","check_links_result":"broken=0(333页)","audit_all":"12/12 ok","commits":1}
if not any(r["cycle"]=="cycle87" for r in rounds):
    rounds.insert(idx88,cycle87); print("cycle87 metrics inserted")
cycle89={"cycle":"cycle89","date":"2026-11-23","status":"completed",
 "gap_methods":["交付前文档一致性收束"],"network":"partial",
 "new_entries":0,"fixes":1,
 "fix_detail":"README/PROGRESS/PROJECT_STATUS 数字对齐为 300/431/337/R1-R22/12步；补齐 cycle87 报告块",
 "entries_total":300,"sources_total":431,"pages":337,
 "check_result":"errors=0","check_links_result":"broken=0(337页)","audit_all":"12/12 ok","commits":1}
if not any(r["cycle"]=="cycle89" for r in rounds):
    rounds.append(cycle89); print("cycle89 metrics appended")
json.dump(met,open(MP,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
SP=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(SP,encoding="utf-8"))
for c in sd["cycles"]:
    pass
if not any(c["cycle"]=="cycle87" for c in sd["cycles"]):
    sd["cycles"].append({"cycle":"cycle87","date":"2026-11-23","methods_used":["希腊罗马实物"],
      "gaps_found":{"entries":4},"network":"partial (museum APIs)",
      "verdict":"希腊罗马 0→4（总 296）；未饱和"})
if not any(c["cycle"]=="cycle89" for c in sd["cycles"]):
    sd["cycles"].append({"cycle":"cycle89","date":"2026-11-23","methods_used":["文档对齐"],
      "gaps_found":{},"network":"partial",
      "verdict":"文档数字对齐 300/431/337；未饱和"})
json.dump(sd,open(SP,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D092 — Cycle89 补记 cycle87 轮次 + 文档数字对齐
- 发现 cycle87（希腊罗马 4 条，292→296）的条目随 cycle88 一并提交，但 **METRICS / DECISIONS / REPORT 均未记录**，
  导致 REPORT 生成器虽已补 cycle87 块却永远不会被执行。
- 处置：在 METRICS 的 cycle86 与 cycle88 之间**插入 cycle87 记录**（entries_total=296, sources_total=427, pages=333）；
  SATURATION 同步补记；DECISIONS 本条即补记。另在 METRICS 末尾追加 cycle89（文档对齐）记录，使 REPORT 指向最新轮次。
- 同时对齐 README / PROGRESS / PROJECT_STATUS 的汇总数字为 **300 条 / 431 来源 / 28 单元 / 337 页 / R1–R22 / 12 步**；
  这些此前散落在旧数字（145/279/176/R17 等），属"交接文档滞后"，不影响数据与站点本身。
- 强调：**300 是数量里程碑，不等于覆盖均衡**；未写 ALL_DONE，饱和以 `SATURATION.json` 为准（当前未饱和）。
- 可逆方式：删除 cycle87/cycle89 记录并把文档数字回滚（不建议）。
- 代价：METRICS 中 cycle87 为事后补记（日期同为 2026-11-23），但条目与 commit 均在仓库中可核。
""")
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:60],(r.stderr or "").strip()[-100:])