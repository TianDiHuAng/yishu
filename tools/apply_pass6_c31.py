# -*- coding: utf-8 -*-
"""Cycle31：采纳 14 条人工确认的锚点；明确拒绝 5 条（口径不同或描述为空）。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")
ADOPT={
 "prehistoric-art":"Q1842924","cave-art":"Q214334","egyptian-art":"Q318394",
 "greek-art":"Q1747618","roman-art":"Q3354732","romanesque":"Q46805",
 "renaissance":"Q1133779","romanticism-art":"Q27273707","gregorian-chant":"Q26473",
 "opera":"Q1344","tonality":"Q192822","20th-century-classical":"Q1338153",
 "minimalism-music":"Q572901","zen-painting":"Q8069073",
}
REJECT={
 "realism-art":"检索仅得两篇论文，无『现实主义艺术运动』实体",
 "symphony":"无合适实体（此前命中的是 Sarah Brightman 专辑）",
 "paleolithic-sculpture":"Q755548『art of the Paleolithic』比条目（旧石器雕塑）宽；Q5839483 描述为空",
 "buddhist-art-india":"Q1001041『Buddhist art』是泛佛教艺术，比条目（印度佛教艺术）宽",
 "khmer-art":"Q109016942『Khmer art』描述为空无法辨别；Q4203993『Cambodian art』口径略异",
}
cand=json.load(open(os.path.join(ROOT,"reports","entity_pass6_c31.json"),encoding="utf-8"))
lookup={}
for eid,cs in cand.items():
    for c in cs:
        if c.get("qid"): lookup[(eid,c["qid"])]=c
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
rows=[]
for eid,qid in ADOPT.items():
    c=lookup.get((eid,qid),{})
    label=c.get("label") or eid; desc=(c.get("desc") or "")[:60]
    sid="wd-anchor-%s"%eid
    if sid not in have:
        sd["sources"].append({"id":sid,"title":"Wikidata 实体（身份锚点）：%s（%s）"%(label,qid),
            "author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026",
            "url":"https://www.wikidata.org/wiki/%s"%qid,"type":"权威结构化数据（身份锚点）","verified":True,
            "verified_note":"Cycle31 人工指定检索词 + 逐条核对口径后采纳；仅作身份锚点，不作事实依据"})
        have.add(sid)
    p=os.path.join(LD,eid+".json")
    o=json.load(open(p,encoding="utf-8")) if os.path.exists(p) else {"id":eid}
    o["sources"]=list(dict.fromkeys((o.get("sources") or es[eid].get("sources",[]))+[sid]))
    json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    rows.append("| %s | %s | %s | %s |"%(eid,label,qid,desc))
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
md=["# Cycle31 人工指定 QID 后采纳的锚点","","采纳 %d 条（口径已逐条核对）："%len(ADOPT),"",
    "| 条目 id | 实体标签 | QID | 描述 |","|---|---|---|---|"]+rows+["","## 已拒绝（%d）"%len(REJECT),""]
for k,v in REJECT.items(): md.append("- **%s**：%s"%(k,v))
open(os.path.join(ROOT,"reports","entity_pass6_vetted.md"),"w",encoding="utf-8").write("\n".join(md))
print("adopted",len(ADOPT),"rejected",len(REJECT),"sources",len(sd["sources"]))