# -*- coding: utf-8 -*-
"""Cycle14 收尾：记录 D020（Wikidata 来源类型与消歧规则 + 来源并集 bug），更新状态。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEC=os.path.join(ROOT,"DECISIONS.md")
block="""
## D020 — Cycle14：启用 Wikidata 作为「权威结构化数据」来源（并修来源并集 bug）
- **决定**：
  1. 新增来源类型「权威结构化数据」，来源为 Wikidata EntityData（`https://www.wikidata.org/wiki/Qxxx`），本轮登记 5 条（wd-starry-night / wd-birth-of-venus / wd-sistine-ceiling / wd-guernica / wd-rite-of-spring）。
  2. 采用**三重消歧**才接受实体：标题匹配 + 描述含类型关键词（painting / fresco / ballet…）+ 作者名出现在描述或 P170 中；否则记为 rejected 并写明原因。
  3. 修正 `merge_l2.py` 的 `sources` 语义为**并集（只增不删）**。
- **理由**：Wikipedia/Met/Tate 不可达且百度/Khan 只返回反爬壳页（Cycle13 结论），但本轮实测 **Wikidata / Wikimedia API / Commons / DBpedia 可达且返回可用 JSON**。TASK 对本项目最易错的信息恰是"作品年份、收藏地"，而 Wikidata 正是这类事实的结构化来源，可作为第二/第三来源。消歧规则源自本轮一次真实险情：`The Rite of Spring` 首次命中的实体作者标签为「西德尼·諾蘭」，若不加校验就会张冠李戴。
- **可逆方式**：从 sources.json 删除 5 条 wd-* 并从对应 `data/l2/*.json` 的 sources 中移除即可；merge 的并集逻辑可改回覆盖。
- **代价/风险**：Wikidata 为社区维护（与 Wikipedia 同源），**独立性仍不足**；`Q206015`（春之祭）的 P170 字段实为异常值（标签为西德尼·諾蘭），本条已在条目"待核实"中标注**不采信该字段**。因此本轮只把"作者/收藏地"记为【已复核·Wikidata】，不改动正文断言，也不据此升级任何条目层级。

## D021 — 来源并集 bug（本轮发现）
- **决定**：`merge_l2.py` 合并覆盖层时，`sources` 由"覆盖层替换基础层"改为"基础层 ∪ 覆盖层"（保持顺序去重）。
- **理由**：本轮把 wikidata 来源写进 5 个作品档案覆盖层时，这些覆盖层原本没有 `sources` 键，写入后变成"仅 wikidata 一条"，merge 时把基础层的 2 条 Wikipedia 来源整段覆盖掉 → `check.py R10` 报"仅1个verified来源"。这是真实的数据丢失，不是误报。
- **可逆方式**：改回 `merged[eid].update(ov)` 即恢复旧行为（不建议）。
- **代价**：以后若确实需要"删除某来源"，必须在 sources 之外用显式删除列表表达，不能靠覆盖层省略。
"""
io.open(DEC,"a",encoding="utf-8").write(block)

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle14","date":"2026-11-22","status":"completed",
 "gap_methods":["网络能力再探测(Wikidata)","B5待核实复核"],
 "network":"partial: Wikidata/Wikimedia API/Commons/DBpedia reachable (JSON ok); Wikipedia/Met/Tate blocked; Baidu/Khan anti-bot shells",
 "new_entries":0,"upgrades":0,"reviews":5,"fixes":6,
 "new_sources":5,"verified_works":5,
 "fix_detail":"5条作品档案登记Wikidata来源并记录【已复核·Wikidata】；修复merge_l2来源覆盖bug（改为并集）",
 "check_result":"errors=0","check_links_result":"broken=0(171页)","audit_all":"6/6 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

sat=os.path.join(ROOT,"SATURATION.json"); s2=json.load(open(sat,encoding="utf-8"))
s2["cycles"].append({"cycle":"cycle14","date":"2026-11-22","methods_used":["网络再探测","B5复核"],
 "gaps_found":{"可核验事实":5},"network":"partial(Wikidata ok)",
 "verdict":"突破：Wikidata 可核验作品作者/收藏地；修来源并集bug；未饱和"})
json.dump(s2,open(sat,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("decisions+state updated")