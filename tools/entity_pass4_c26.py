# -*- coding: utf-8 -*-
"""Cycle26 pass4：中文标签锚定（针对 pass3 系统性漏掉的中系条目）。
规则：zh 检索 → 批量取 zh/en 标签与 en 描述 → 要求 norm(zh 标签) **完全等于** norm(条目中文标题)
且 en 描述含该类条目类型词。只输出候选，人工确认后再写库。"""
import json,os,re,subprocess,urllib.parse
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
UA="YishuBot/1.0 (educational; local)"
def curl_json(u,tries=3,timeout=20):
    import time
    for i in range(tries):
        p=subprocess.run(["curl","-sS","-m",str(timeout),"-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
        if p.returncode==0 and p.stdout.strip().startswith("{"):
            try: return json.loads(p.stdout)
            except Exception: pass
        time.sleep(0.4*(i+1))
    return None
def search(q,lang,limit=6):
    d=curl_json("https://www.wikidata.org/w/api.php?action=wbsearchentities&search=%s&language=%s&format=json&limit=%d"%(urllib.parse.quote(q),lang,limit))
    return [(x["id"],x.get("label",""),x.get("description","")) for x in (d or {}).get("search",[])]
def norm(t): return re.sub(r"[《》〈〉（）()\[\]【】·、，,\.\s\"'：:]","",t or "")
TW={"人物":["painter","sculptor","composer","artist","architect","musician","polymath","calligrapher"],
 "作品":["painting","fresco","sculpture","musical work","ballet","composition","mural","opera","artwork"],
 "风格":["style","movement","school","genre","tradition","tendency"],
 "时期":["period","era","civilization","age","century","dynasty","art"],
 "术语":["term","technique","concept","notation","instrument","mode","system","theory","principle","genre"]}
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
todo=[e for e in es if not any(s.startswith("wd-") for s in e["sources"])]
print("未锚定:",len(todo))
cand={}
for e in todo:
    cand[e["id"]]=search(e["title"],"zh",6)
ids=sorted({q for cs in cand.values() for q,_,_ in cs})
info={}
for i in range(0,len(ids),50):
    ch=ids[i:i+50]
    r=curl_json("https://www.wikidata.org/w/api.php?action=wbgetentities&ids=%s&props=labels|descriptions&languages=zh|en&format=json"%("%7C".join(ch)))
    for qid,e in ((r or {}).get("entities",{}) or {}).items():
        info[qid]={"labels":{k:v["value"] for k,v in e.get("labels",{}).items() if k in ("zh","en")},
                   "desc":((e.get("descriptions",{}).get("en") or {}).get("value") or "")}
    print("  batch",i//50+1,"cached",len(info),"/",len(ids))
hits=[]; near=[]
for e in todo:
    t=norm(e["title"]); tw=TW.get(e["kind"],[]); pick=None
    for qid,lbl,dd in cand[e["id"]]:
        it=info.get(qid,{"labels":{},"desc":dd or ""})
        zh=norm(it["labels"].get("zh",""))
        if zh and zh==t and any(w in (it["desc"] or "").lower() for w in tw):
            pick={"id":e["id"],"kind":e["kind"],"title":e["title"],"qid":qid,
                  "label":it["labels"].get("zh"),"desc":(it["desc"] or dd)[:60]}
            break
        if zh and zh==t: near.append({"id":e["id"],"title":e["title"],"qid":qid,"label":it["labels"].get("zh"),"desc":(it["desc"] or dd)[:40],"why":"标签相同但描述无类型词"})
    if pick: hits.append(pick)
print("精确命中:",len(hits),"| 近似(标签同但描述不含类型词):",len(near))
for h in hits: print("  OK",h["id"],h["qid"],h["label"],"|",h["desc"][:45])
for n in near[:8]: print("  NEAR",n["id"],n["qid"],n["label"],"|",n["desc"][:40])
json.dump({"hits":hits,"near":near},open(os.path.join(ROOT,"reports","entity_pass4_c26.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)