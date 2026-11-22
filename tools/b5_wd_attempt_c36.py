# -*- coding: utf-8 -*-
"""Cycle36：尝试用 Wikidata 的时间声明（P571 起始 / P582 终止 / P580 开始）解决 B5 剩余项。
目标：
 1) realism-art 的『约1840—1870』→ 查 Realism (art movement) 的起止
 2) romanesque 的『终点1150』→ 查 Romanesque art 的终止时间
 3) donatello『解剖准确性』→ 非时间事实，跳过
 4) cursive-script 张旭作品 / 草书年代 → 查 Zhang Xu / cursive script 时间声明
只输出证据，不做判定。"""
import json,os,re,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from wd_api import search, api_get
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def claims(qid,pids):
    d,err=api_get({"action":"wbgetentities","ids":qid,"props":"claims|labels","languages":"zh|en","format":"json"})
    if err or not d: return {"error":err}
    e=(d.get("entities",{}) or {}).get(qid) or {}
    out={"qid":qid,"labels":{k:v["value"] for k,v in e.get("labels",{}).items() if k in ("zh","en")}}
    for p in pids:
        vals=[]
        for c in e.get("claims",{}).get(p,[]):
            v=c.get("mainsnak",{}).get("datavalue",{}).get("value")
            if isinstance(v,dict) and "time" in v: vals.append(v["time"])
            elif isinstance(v,dict) and "id" in v: vals.append(v["id"])
        if vals: out[p]=vals
    return out
# 1) realism 运动实体
res={}
s1,err=search("Realism art movement","en",5)
print("realism 候选:",s1)
res["realism_candidates"]=s1
for q,lbl,desc in s1:
    if "art" in (desc or "").lower() or "realis" in (lbl or "").lower():
        res["realism_entity"]=claims(q,["P571","P580","P582"])
        break
# 2) Romanesque art
res["romanesque_entity"]=claims("Q46805",["P571","P580","P582"])
# 3) 张旭 / 草书
s2,_=search("Zhang Xu","zh",5)
print("张旭 候选:",s2)
res["zhangxu_candidates"]=s2
for q,lbl,desc in s2:
    if "calligraph" in (desc or "").lower() or "书法" in (desc or ""):
        res["zhangxu_entity"]=claims(q,["P569","P570","P800","P170"])
        break
res["cursive_entity"]=claims("Q607543",["P571","P580","P582"])
print("romanesque:",res["romanesque_entity"])
print("cursive:",res["cursive_entity"])
print("realism:",res.get("realism_entity"))
print("zhangxu:",res.get("zhangxu_entity"))
json.dump(res,open(os.path.join(ROOT,"reports","b5_wd_attempt_c36.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)