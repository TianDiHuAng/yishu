# -*- coding: utf-8 -*-
"""修复被误写成控制字符的来源 id：把 'cma-1972-\\x01' 与引用改为 'cma-1972-9'。"""
import json,os,glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BAD="cma-1972-\x01"; GOOD="cma-1972-9"
p=os.path.join(ROOT,"data","sources.json"); sd=json.load(open(p,encoding="utf-8"))
for s in sd["sources"]:
    if s["id"]==BAD:
        s["id"]=GOOD; print("lib fixed ->",s["id"])
json.dump(sd,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
for q in glob.glob(os.path.join(ROOT,"data","l2","*.json")):
    o=json.load(open(q,encoding="utf-8")); src=o.get("sources") or []
    if BAD in src:
        o["sources"]=[GOOD if x==BAD else x for x in src]
        json.dump(o,open(q,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
        print("overlay fixed:",o["id"])
# 校验
sd2=json.load(open(p,encoding="utf-8"))
print("lib has GOOD:", any(s["id"]==GOOD for s in sd2["sources"]), "| lib has BAD:", any(s["id"]==BAD for s in sd2["sources"]))