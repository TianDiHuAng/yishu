# -*- coding: utf-8 -*-
"""Cycle23：人工确认 pass2 的 15 个候选中，仅采纳 12 个语义相符的；
拒绝 3 个（并写明原因）：
  romanesque → Q46261 是"建筑"实体，而条目是艺术风格（跨媒介），锚定会以偏概全
  renaissance → Q23731823 是法国政党，与文艺复兴无关（纯字符串巧合）
  baroque-music → Q3328590 是"法国巴洛克音乐"，比条目（巴洛克音乐通论）窄
采纳项登记为身份锚点来源并生成 reports/entity_pass2_vetted.md。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")
REJECT={
 "romanesque":"Q46261 为『建筑』实体，条目是跨媒介的艺术风格，锚定会以偏概全",
 "renaissance":"Q23731823 为法国政党，纯字符串巧合",
 "baroque-music":"Q3328590 为『法国巴洛克音乐』，比条目（巴洛克音乐通论）更窄",
}
cand=json.load(open(os.path.join(ROOT,"reports","entity_pass2_c23.json"),encoding="utf-8"))
keep=[c for c in cand if c["id"] not in REJECT]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
rows=[]
for it in keep:
    sid="wd-anchor-%s"%it["id"]
    if sid not in have:
        sd["sources"].append({"id":sid,
            "title":"Wikidata 实体（身份锚点）：%s（%s）"%(it["label"],it["qid"]),
            "author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026",
            "url":"https://www.wikidata.org/wiki/%s"%it["qid"],
            "type":"权威结构化数据（身份锚点）","verified":True,
            "verified_note":"Cycle23 英文标签与条目 id 比对命中（人工确认语义相符）；仅作身份锚点，不作事实依据"})
        have.add(sid)
    p=os.path.join(LD,it["id"]+".json")
    o=json.load(open(p,encoding="utf-8")) if os.path.exists(p) else {"id":it["id"]}
    o["sources"]=list(dict.fromkeys((o.get("sources") or es[it["id"]].get("sources",[]))+[sid]))
    json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append("| %s | %s | %s | %s |"%(it["id"],it["title"],it["qid"],it["label"]))
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
md=["# Cycle23 实体锚点 pass2（人工确认后）","",
    "采纳 %d 条（英文标签与条目 id 比对命中且语义相符）："%len(keep),"",
    "| 条目 id | 标题 | QID | 实体标签 |","|---|---|---|---|"]+rows+["",
    "## 已拒绝（%d 条，写明原因）"%len(REJECT),""]
for k,v in REJECT.items(): md.append("- **%s**：%s"%(k,v))
open(os.path.join(ROOT,"reports","entity_pass2_vetted.md"),"w",encoding="utf-8").write("\n".join(md))
print("adopted",len(keep),"| rejected",len(REJECT),"| sources total",len(sd["sources"]))