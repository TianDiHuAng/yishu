# -*- coding: utf-8 -*-
"""Cycle17 收尾：①两条建筑条目补"来源分工"诚实说明；②D022；③状态与 REPORT。
说明要点：Wikidata 仅确认实体身份与名称（desc=style of architecture），**不提供年代**；
年代与结构特征依据已核验的 Wikipedia 专页；两者同源，独立性不足。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LD=os.path.join(ROOT,"data","l2")
DISC=("【来源分工说明】本条的结构特征与时代描述依据已核验的 Wikipedia 专页；"
      "Wikidata（wd-*）仅用于确认实体身份与正式名称（其描述为 architectural style），**不提供年代数据**；"
      "两者同属 Wikimedia 体系，独立性不足，故年代类断言一律留在本待核实节。")
for eid in ["gothic-architecture","romanesque-architecture"]:
    p=os.path.join(LD,eid+".json"); o=json.load(open(p,encoding="utf-8"))
    if "来源分工说明" not in o["sections"]["待核实"]:
        o["sections"]["待核实"]+=" "+DISC
        json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
        print("disclosure added:",eid)
# D022
DEC=os.path.join(ROOT,"DECISIONS.md")
block="""
## D022 — Cycle17 新增 2 条建筑条目（A 类缺口的第一步，附来源分工说明）
- **决定**：新建 `gothic-architecture`（哥特式建筑）、`romanesque-architecture`（罗马式建筑），归入 `art-medieval`，medium=建筑；每条挂 2–3 个来源（Wikipedia 专页 + Wikidata 实体 + 关联风格页），并在"待核实"写**来源分工说明**。
- **理由**：`reports/matrix_targets_c7.md` 的 A 类 58 项中，"建筑"是最大缺口（中国 19、欧洲 11、法国 10、美国 5、南亚 4 条现有条目却无建筑专条）。但按 §4 与 TASK 的双源要求，**只有能凑够两个来源的传统才可建条**：哥特/罗马式有已核验的 Wikipedia 专页（Cycle1/Cycle4 核验）+ Wikidata 实体；而**中国建筑目前只有 Wikidata 一条可核验来源，故不建**，记入 BACKLOG。
- **诚实边界**：实测这两个 Wikidata 实体**没有 P571（起始年代）与 P136（风格）声明**，因此 Wikidata 在本轮只承担"实体身份/正式名称"的确认职责，**不承担年代**；这已在每条"待核实"里明确写出，避免读者误以为年代有双源支撑。
- **可逆方式**：从 catalog.py 删除这两行、从 sources.json 删除两条 wd-* 与 l2 覆盖层即可。
- **代价**：新条目与既有 `gothic` / `romanesque`（艺术风格页）存在主题邻近，已在 `related` 中互链区分（一个是风格整体，一个是建筑门类）。
"""
io.open(DEC,"a",encoding="utf-8").write(block)
# METRICS / SATURATION
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle17","date":"2026-11-22","status":"completed",
 "gap_methods":["B2矩阵A类(建筑)","B5/Wikidata实体核验"],"network":"partial: wikidata ok",
 "new_entries":2,"upgrades":0,"reviews":2,"fixes":0,
 "new_sources":2,"sources_total":204,"verified":204 if False else None,
 "qc_result":"2 新建 wd 来源均 200 且标签一致；正文年份全部在待核实列明（issues 0）",
 "check_result":"errors=0","check_links_result":"broken=0(173页)","audit_all":"6/6 ok","commits":1})
d["rounds"][-1].pop("verified",None)
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle17","date":"2026-11-22","methods_used":["B2补盲","Wikidata核验"],
 "gaps_found":{"建筑缺口开工":2},"network":"partial","verdict":"A类建筑缺口开工（哥特/罗马式）；中国建筑待第二来源；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("done")