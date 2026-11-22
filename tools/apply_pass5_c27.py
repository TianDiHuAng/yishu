# -*- coding: utf-8 -*-
"""Cycle27：采纳 pass5 中人工确认的 5 条锚点，拒绝 3 条（写明原因）。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")
ADOPT={"mannerism":"Q131808","minimalism":"Q173436","conceptual-art":"Q203209",
       "regular-script":"Q1196029","polyphony":"Q1917591"}
REJECT={
 "renaissance":"Q23731823 再次是法国『复兴党』，同名陷阱；文艺复兴的通用实体需人工指定 QID",
 "china-music-history":"Q119086285 与 Q119086337 描述均为空，无法区分专著/学科条目",
 "pipa":"Q18874076 描述为空，无法确定是乐器还是同名诗作",
}
cand={x["id"]:x for x in json.load(open(os.path.join(ROOT,"reports","entity_pass5_c27.json"),encoding="utf-8"))}
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
rows=[]
for eid,qid in ADOPT.items():
    c=cand.get(eid,{})
    label=c.get("zh") or c.get("en") or eid; desc=(c.get("desc") or "")[:60]
    sid="wd-anchor-%s"%eid
    if sid not in have:
        sd["sources"].append({"id":sid,"title":"Wikidata 实体（身份锚点）：%s（%s）"%(label,qid),
            "author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026",
            "url":"https://www.wikidata.org/wiki/%s"%qid,"type":"权威结构化数据（身份锚点）","verified":True,
            "verified_note":"Cycle27 英文/中文精确匹配 + 人工确认语义相符；仅作身份锚点，不作事实依据"})
        have.add(sid)
    p=os.path.join(LD,eid+".json")
    o=json.load(open(p,encoding="utf-8")) if os.path.exists(p) else {"id":eid}
    o["sources"]=list(dict.fromkeys((o.get("sources") or es[eid].get("sources",[]))+[sid]))
    json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append("| %s | %s | %s | %s |"%(eid,label,qid,desc))
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
md=["# Cycle27 锚点（pass5，人工确认）","","采纳 %d 条："%len(ADOPT),"",
    "| 条目 id | 实体标签 | QID | 描述 |","|---|---|---|---|"]+rows+["","## 已拒绝（%d）"%len(REJECT),""]
for k,v in REJECT.items(): md.append("- **%s**：%s"%(k,v))
open(os.path.join(ROOT,"reports","entity_pass5_vetted.md"),"w",encoding="utf-8").write("\n".join(md))
print("adopted",len(ADOPT),"rejected",len(REJECT),"sources",len(sd["sources"]))