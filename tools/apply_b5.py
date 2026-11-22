# -*- coding: utf-8 -*-
"""应用 B5 复核结果（仅 _verified 且 _facts_ok 的项）：
1) 把新来源加入 sources.json（去重）；
2) 把来源 id 加入对应条目的 sources 数组；
3) 在 L2 覆盖层的"待核实"节，为已解决项追加"【已复核】第二来源..."记录，保留原文本不删除（诚实留痕）。
"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")
items=[x for x in json.load(open(os.path.join(ROOT,"reports","b5_research_verified.json"),encoding="utf-8"))
       if x.get("_verified") and x.get("_facts_ok")]
# 1) 来源库
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); exist={s["id"] for s in sd["sources"]}
added=[]
for x in items:
 s=x["source"]
 if s["id"] in exist: continue
 sd["sources"].append({k:s[k] for k in ("id","title","author","year","url","type") if k in s}|
                      {"verified":True,"verified_note":s.get("verified_note","B5复核HTTP200")})
 exist.add(s["id"]); added.append(s["id"])
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
# 2)+3) 按条目聚合
from collections import defaultdict
byentry=defaultdict(list)
for x in items: byentry[x["entry_id"]].append(x)
n=0
for eid,xs in byentry.items():
 p=os.path.join(LD,eid+".json")
 if not os.path.exists(p): print("no overlay",eid); continue
 o=json.load(open(p,encoding="utf-8"))
 srcs=list(o.get("sources",[])) if "sources" in o else []
 # L2覆盖层可能没有sources字段，从seed读取后写回
 if "sources" not in o:
  seed=[e for e in json.load(open(os.path.join(D,"entries.json"),encoding="utf-8"))["entries"] if e["id"]==eid]
  srcs=list(seed[0]["sources"]) if seed else []
 for x in xs:
  sid=x["source"]["id"]
  if sid not in srcs: srcs.append(sid)
 o["sources"]=srcs
 pend=o["sections"].get("待核实","")
 notes=[]
 for x in xs:
  line="【已复核】%s：第二来源 %s（%s），据该来源：%s"%(x["pending_item"][:34],x["source"]["id"],x["source"]["url"][:48],x.get("body_rewrite","见来源页。")[:110])
  if x["source"]["id"] not in pend: notes.append(line)
 if notes:
  o["sections"]["待核实"]=pend+" "+" ".join(notes)
 json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
 n+=1
print("sources added=%d, entries updated=%d"%(len(added),n))
