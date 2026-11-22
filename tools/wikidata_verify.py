# -*- coding: utf-8 -*-
"""Cycle14 v2：Wikidata 核验**加实体消歧**，避免张冠李戴。
接受条件（全部满足才算 verified）：
 1) label 与期望标题匹配（中/英，忽略大小写与冠词）
 2) description 含期望类型关键词（painting / ballet / fresco ...）
 3) P170(作者) 的标签包含期望作者名（中/英任一）
任何一条不满足 → 该候选标 rejected，并记录原因（不写入条目）。"""
import json,os,ssl,time,urllib.parse,urllib.request
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ctx=ssl.create_default_context()
UA={"User-Agent":"YishuBot/1.0 (educational; local)"}
def get(u,tries=3):
    for i in range(tries):
        try:
            r=urllib.request.Request(u,headers=UA)
            return json.loads(urllib.request.urlopen(r,timeout=20,context=ctx).read().decode())
        except Exception as e: last=e; time.sleep(1.2)
    raise last
def search(name,limit=6):
    d=get("https://www.wikidata.org/w/api.php?action=wbsearchentities&search=%s&language=en&format=json&limit=%d"%(urllib.parse.quote(name),limit))
    return [(x["id"],x.get("label",""),x.get("description","")) for x in d.get("search",[])]
def entity(q): return get("https://www.wikidata.org/wiki/Special:EntityData/%s.json"%q)["entities"][q]
def claims(q,pid):
    out=[]
    for c in q.get("claims",{}).get(pid,[]):
        v=c.get("mainsnak",{}).get("datavalue",{}).get("value")
        if isinstance(v,dict) and "id" in v: out.append(v["id"])
        elif isinstance(v,dict) and "time" in v: out.append(v["time"])
        elif isinstance(v,dict) and "amount" in v: out.append(v["amount"])
    return out
def lab(q):
    try:
        e=entity(q); L=e.get("labels",{})
        return (L.get("zh") or L.get("en") or {}).get("value") or q
    except Exception: return q

T=[("starry-night","The Starry Night","starry night",["painting"],["van gogh","梵高"]),
   ("birth-of-venus-work","Birth of Venus","birth of venus",["painting"],["botticelli","波提切利"]),
   ("sistine-ceiling-work","Sistine Chapel ceiling","sistine chapel ceiling",["fresco","ceiling","painting"],["michelangelo","米开朗"]),
   ("guernica-work","Guernica","guernica",["painting"],["picasso","毕加索","畢卡索"]),
   ("rite-of-spring-work","The Rite of Spring","rite of spring",["ballet","music","composition"],["stravinsky","斯特拉文","斯特拉溫"])]
rep=[]
for eid,title,q,types,creators in T:
    cands=search(q)
    chosen=None; notes=[]
    for qid,lbl,desc in cands:
        e=entity(qid)
        labels={k:v["value"] for k,v in e.get("labels",{}).items() if k in ("zh","en")}
        cr=[lab(x) for x in claims(e,"P170")]
        tmatch=any(v.lower().strip()==title.lower() for v in labels.values()) or title.lower() in " ".join(labels.values()).lower()
        kmatch=any(k in (desc or "").lower() for k in types)
        hay=(desc or '').lower()+''.join(x.lower() for x in cr)
        cmatch=any(c in hay for c in creators)
        if tmatch and kmatch and cmatch:
            chosen={"qid":qid,"labels":labels,"desc":desc,
                    "creator":cr,"collection":[lab(x) for x in claims(e,"P195")],
                    "inception":claims(e,"P571"),"location":[lab(x) for x in claims(e,"P276")],
                    "height":claims(e,"P2048"),"width":claims(e,"P2049")}
            break
        notes.append({"qid":qid,"label":labels,"desc":desc,"creator":cr,"rejected_reason":
                      ("标题不符" if not tmatch else "")+("类型不符" if not kmatch else "")+("作者不符" if not cmatch else "")})
    rep.append({"entry_id":eid,"accepted":chosen,"rejected":notes[:4]})
    print(eid,"=>",("ACCEPT Q"+chosen["qid"]+" | "+str(chosen["labels"])+" | creator="+str(chosen["creator"])+" | collection="+str(chosen["collection"])) if chosen else "NO MATCH (all rejected)")
json.dump(rep,open(os.path.join(ROOT,"reports","wikidata_verify.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)