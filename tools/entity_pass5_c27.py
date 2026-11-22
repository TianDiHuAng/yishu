# -*- coding: utf-8 -*-
"""Cycle27 pass5（限速客户端）：对仍未锚定的条目并行尝试两条路：
 A) 英文：用 id 的英文形式检索，norm(英语标签)==norm(id) 且描述含类型词；
 B) 中文：用标题检索，norm(中文标签)==norm(标题) 且（描述含类型词 或 描述为空）。
输出带描述的候选，供人工确认。"""
import json,os,re,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from wd_api import search, api_get
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
def norm(t): return re.sub(r"[《》〈〉（）()\[\]【】·、，,\.\s\"'：:]","",t or "")
def norm_en(t): return re.sub(r"[^a-z0-9]","",(t or "").lower())
TW={"人物":["painter","sculptor","composer","artist","architect","musician","polymath","calligrapher"],
 "作品":["painting","fresco","sculpture","musical work","ballet","composition","mural","opera","artwork"],
 "风格":["style","movement","school","genre","tradition","tendency"],
 "时期":["period","era","civilization","age","century","dynasty","art"],
 "术语":["term","technique","concept","notation","instrument","mode","system","theory","principle","genre"]}
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
todo=[e for e in es if not any(s.startswith("wd-") for s in e["sources"])]
print("未锚定:",len(todo))
ids=set()
for e in todo:
    for q,_,_ in search(e["id"].replace("-"," "),"en",6)[0]: ids.add(q)
    for q,_,_ in search(e["title"],"zh",6)[0]: ids.add(q)
print("候选实体数:",len(ids))
info={}
idlist=sorted(ids)
for k in range(0,len(idlist),40):
    d,err=api_get({"action":"wbgetentities","ids":"|".join(idlist[k:k+40]),
                   "props":"labels|descriptions","languages":"zh|en","format":"json"})
    if err: print("  batch err",err); continue
    for qid,e in (d.get("entities",{}) or {}).items():
        info[qid]={"labels":{a:b["value"] for a,b in e.get("labels",{}).items() if a in ("zh","en")},
                   "desc":((e.get("descriptions",{}).get("en") or {}).get("value") or "")}
print("实体信息:",len(info),"err-free")
res=[]
for e in todo:
    tz=norm(e["title"]); te=norm_en(e["id"]); tw=TW.get(e["kind"],[])
    cands=[]
    for q,lbl,dd in search(e["id"].replace("-"," "),"en",6)[0]: cands.append((q,"A",lbl,dd))
    for q,lbl,dd in search(e["title"],"zh",6)[0]: cands.append((q,"B",lbl,dd))
    best=None
    for q,branch,lbl,dd in cands:
        it=info.get(q); 
        if not it: continue
        zh=norm(it["labels"].get("zh","")); en=norm_en(it["labels"].get("en") or lbl)
        desc=(it["desc"] or dd or "").lower()
        typ=any(w in desc for w in tw)
        if branch=="A" and en==te and typ:
            best={"how":"A(英文精确)","qid":q,"zh":it["labels"].get("zh"),"en":it["labels"].get("en"),"desc":(it["desc"] or dd)[:60]}; break
        if branch=="B" and zh==tz and (typ or not desc):
            best={"how":"B(中文精确)","qid":q,"zh":it["labels"].get("zh"),"en":it["labels"].get("en"),"desc":(it["desc"] or dd)[:60]}; break
    if best: res.append({"id":e["id"],"kind":e["kind"],"title":e["title"],**best})
print("候选命中:",len(res))
for r in res: print("  ",r["id"],r["qid"],r["how"],r["zh"],"|",r["desc"][:45])
json.dump(res,open(os.path.join(ROOT,"reports","entity_pass5_c27.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)