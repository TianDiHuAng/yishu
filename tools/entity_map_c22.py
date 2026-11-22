# -*- coding: utf-8 -*-
"""Cycle22 v3：两阶段实体映射（避免逐条抓取导致超时）。
阶段1：逐条目检索候选 QID（zh，失败回退 en）；
阶段2：把所有候选 QID 分块（50/块）一次性 wbgetentities 取 zh/en 标签与 en 描述；
阶段3：本地匹配——标签规范化后与标题相等（或互为子串）+ 描述含该类条目的类型词。
输出 reports/entity_map_c22.json。"""
import json,os,re,subprocess,urllib.parse,time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
UA="YishuBot/1.0 (educational; local)"
def curl_json(u,tries=4,timeout=25):
    for i in range(tries):
        p=subprocess.run(["curl","-sS","-m",str(timeout),"-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
        if p.returncode==0 and p.stdout.strip().startswith("{"):
            try: return json.loads(p.stdout)
            except Exception: pass
        time.sleep(0.4*(i+1))
    return None
def search(q,lang,limit=5):
    d=curl_json("https://www.wikidata.org/w/api.php?action=wbsearchentities&search=%s&language=%s&format=json&limit=%d"%(urllib.parse.quote(q),lang,limit))
    return [(x["id"],x.get("label",""),x.get("description","")) for x in (d or {}).get("search",[])]
def norm(t): return re.sub(r"[《》〈〉（）()\[\]【】·、，,\.\s\"']","",t or "")
TYPE_WORDS={"人物":["painter","sculptor","composer","artist","architect","musician","polymath","calligrapher","pianist","violinist","conductor","singer"],
 "作品":["painting","fresco","sculpture","musical work","ballet","composition","mural","opera","artwork","symphony"],
 "风格":["style","movement","school","genre","tradition","tendency","period"],
 "时期":["period","era","civilization","age","century","dynasty","art"],
 "术语":["term","technique","concept","notation","instrument","mode","temperament","system","theory","principle","practice"]}
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
have={e["id"] for e in es if any(s.startswith("wd-") for s in e.get("sources",[]))}
todo=[e for e in es if e["id"] not in have]
print("待映射:",len(todo))
cand={}
for e in todo:
    c=search(e["title"],"zh",5)
    if not c: c=search(e["title"],"en",5)
    cand[e["id"]]=c
# 批量取实体
ids=sorted({q for cs in cand.values() for q,_,_ in cs})
cache={}
for i in range(0,len(ids),50):
    chunk=ids[i:i+50]
    d=curl_json("https://www.wikidata.org/w/api.php?action=wbgetentities&ids=%s&props=labels|descriptions&languages=zh|en&format=json"%("|".join(chunk).replace("|","%7C")))
    for qid,e in ((d or {}).get("entities",{}) or {}).items():
        cache[qid]={"labels":{k:v["value"] for k,v in e.get("labels",{}).items() if k in ("zh","en")},
                    "desc":((e.get("descriptions",{}).get("en") or {}).get("value") or "")}
    print("  batch",i//50+1,"cached",len(cache),"/",len(ids))
res={"matched":[],"ambiguous":[],"none":[]}
for e in todo:
    t=norm(e["title"]); words=TYPE_WORDS.get(e["kind"],[])
    pick=None; alts=[]
    for qid,lbl,desc in cand[e["id"]]:
        info=cache.get(qid,{"labels":{},"desc":desc or ""})
        labels=list(info["labels"].values())+[lbl]
        d=(info["desc"] or desc or "").lower()
        same=any(norm(v)==t or (t and (t in norm(v) or norm(v) in t)) for v in labels if v)
        typ=any(w in d for w in words)
        if same and typ:
            pick={"qid":qid,"label":(info["labels"].get("zh") or info["labels"].get("en") or lbl),"desc":(info["desc"] or desc)[:60]}
            break
        alts.append({"qid":qid,"label":lbl,"desc":(desc or "")[:45],"same":bool(same),"typ":bool(typ)})
    if pick: res["matched"].append({"id":e["id"],"kind":e["kind"],"title":e["title"],**pick})
    elif alts: res["ambiguous"].append({"id":e["id"],"kind":e["kind"],"title":e["title"],"candidates":alts[:3]})
    else: res["none"].append({"id":e["id"],"kind":e["kind"],"title":e["title"]})
json.dump(res,open(os.path.join(ROOT,"reports","entity_map_c22.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("matched %d / ambiguous %d / none %d"%(len(res["matched"]),len(res["ambiguous"]),len(res["none"])))
for m in res["matched"][:10]: print("  OK",m["id"],m["qid"],m["label"],"|",m["desc"][:45])