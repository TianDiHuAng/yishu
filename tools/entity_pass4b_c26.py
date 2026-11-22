# -*- coding: utf-8 -*-
"""Cycle26 pass4b：用限速+缓存的 wd_api 重跑中文标签锚定（不再静默失败）。
规则：zh 检索 → 取实体 zh/en 标签与 en 描述 → norm(zh标签)==norm(条目标题) 且描述含类型词。"""
import json,os,re,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from wd_api import search, api_get
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
def norm(t): return re.sub(r"[《》〈〉（）()\[\]【】·、，,\.\s\"'：:]","",t or "")
TW={"人物":["painter","sculptor","composer","artist","architect","musician","polymath","calligrapher"],
 "作品":["painting","fresco","sculpture","musical work","ballet","composition","mural","opera","artwork"],
 "风格":["style","movement","school","genre","tradition","tendency"],
 "时期":["period","era","civilization","age","century","dynasty","art"],
 "术语":["term","technique","concept","notation","instrument","mode","system","theory","principle","genre"]}
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
todo=[e for e in es if not any(s.startswith("wd-") for s in e["sources"])]
print("未锚定:",len(todo))
cand={}; errs=[]
for i,e in enumerate(todo,1):
    cs,err=search(e["title"],"zh",6)
    if err: errs.append((e["id"],err))
    cand[e["id"]]=cs
    if i%20==0: print("  search",i,"/",len(todo),"errs",len(errs))
ids=sorted({q for cs in cand.values() for q,_,_ in cs})
info={}
for k in range(0,len(ids),40):
    ch=ids[k:k+40]
    d,err=api_get({"action":"wbgetentities","ids":"|".join(ch),"props":"labels|descriptions","languages":"zh|en","format":"json"})
    if err: errs.append(("batch%d"%k,err)); continue
    for qid,e in (d.get("entities",{}) or {}).items():
        info[qid]={"labels":{a:b["value"] for a,b in e.get("labels",{}).items() if a in ("zh","en")},
                   "desc":((e.get("descriptions",{}).get("en") or {}).get("value") or "")}
print("实体信息:",len(info),"/",len(ids),"| 错误:",len(errs))
hits=[]; near=[]
for e in todo:
    t=norm(e["title"]); tw=TW.get(e["kind"],[])
    for qid,lbl,dd in cand[e["id"]]:
        it=info.get(qid)
        if not it: continue
        zh=norm(it["labels"].get("zh",""))
        if zh==t and any(w in (it["desc"] or "").lower() for w in tw):
            hits.append({"id":e["id"],"kind":e["kind"],"title":e["title"],"qid":qid,
                         "label":it["labels"].get("zh"),"desc":(it["desc"] or dd)[:60]}); break
        if zh==t: near.append({"id":e["id"],"qid":qid,"label":it["labels"].get("zh"),"desc":(it["desc"] or dd)[:40]})
print("精确命中:",len(hits),"| 近似:",len(near))
for h in hits: print("  OK",h["id"],h["qid"],h["label"],"|",h["desc"][:45])
json.dump({"hits":hits,"near":near,"errors":errs},open(os.path.join(ROOT,"reports","entity_pass4_c26.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)