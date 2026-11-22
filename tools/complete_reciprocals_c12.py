# -*- coding: utf-8 -*-
"""Cycle12：把 47 条单向关联补成双向（均为 same_unit 或 same_domain，无跨域），
写入各条目的 L2 覆盖层 related 字段；不新增任何语义断言，仅为导航一致性。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")
aud=json.load(open(os.path.join(ROOT,"reports","oneway_audit.json"),encoding="utf-8"))
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
added=0
for row in aud["rows"]:
    if row["class"] not in ("same_unit","same_domain"): continue
    tgt=row["to"]; src=row["from"]
    p=os.path.join(LD,tgt+".json")
    if os.path.exists(p):
        o=json.load(open(p,encoding="utf-8"))
        rel=list(dict.fromkeys(o.get("related", es[tgt].get("related",[]))+[src]))
    else:
        o={"id":tgt,"level":es[tgt].get("level","L2"),"related":list(dict.fromkeys(es[tgt].get("related",[])+[src]))}
    o["related"]=rel
    json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    added+=1
print("reciprocal links written:",added)