# -*- coding: utf-8 -*-
"""Cycle22 应用：把 21 条匹配结果登记为"身份锚点"来源并挂到条目；
生成 reports/entity_anchors.md；不据此改动任何正文断言。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")
m=json.load(open(os.path.join(ROOT,"reports","entity_map_c22.json"),encoding="utf-8"))["matched"]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
n=0; rows=[]
for it in m:
    sid="wd-anchor-%s"%it["id"]
    if sid not in have:
        sd["sources"].append({"id":sid,
            "title":"Wikidata 实体（身份锚点）：%s（%s）"%(it["label"],it["qid"]),
            "author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026",
            "url":"https://www.wikidata.org/wiki/%s"%it["qid"],
            "type":"权威结构化数据（身份锚点）","verified":True,
            "verified_note":"Cycle22 批量 wbgetentities 成功；标签与条目标题匹配、描述类型词匹配；仅作身份锚点，不作事实依据"})
        have.add(sid)
    p=os.path.join(LD,it["id"]+".json")
    o=json.load(open(p,encoding="utf-8")) if os.path.exists(p) else {"id":it["id"]}
    o["sources"]=list(dict.fromkeys((o.get("sources") or es[it["id"]].get("sources",[]))+[sid]))
    json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    n+=1; rows.append("| %s | %s | [%s](https://www.wikidata.org/wiki/%s) | %s |"%(it["id"],it["title"],it["qid"],it["qid"],it["desc"][:50]))
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
md=["# 条目 ↔ Wikidata 实体锚点（Cycle 22）","",
    "说明：以下映射**仅用于身份锚定**（确认条目所指对象在 Wikidata 中有同一实体），",
    "**不作为事实依据**——条目的年代、风格、评价等断言仍以各条目标注的来源为准。","",
    "| 条目 id | 标题 | Wikidata | 实体描述 |","|---|---|---|---|"]+rows
open(os.path.join(ROOT,"reports","entity_anchors.md"),"w",encoding="utf-8").write("\n".join(md))
print("anchors applied:",n,"| sources total",len(sd["sources"]))