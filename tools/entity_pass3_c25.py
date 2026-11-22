# -*- coding: utf-8 -*-
"""Cycle25 pass3（最高精度）：对未锚定条目，用 id 的英文形式检索，
要求 norm(实体英文标签) **完全等于** norm(id)，且描述含该类条目类型词。
只输出候选报告，不写库。"""
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
def search(q,limit=6):
    d=curl_json("https://www.wikidata.org/w/api.php?action=wbsearchentities&search=%s&language=en&format=json&limit=%d"%(urllib.parse.quote(q),limit))
    return [(x["id"],x.get("label",""),x.get("description","")) for x in (d or {}).get("search",[])]
def norm(t): return re.sub(r"[^a-z0-9]","",(t or "").lower())
TW={"人物":["painter","sculptor","composer","artist","architect","musician","polymath","calligrapher"],
 "作品":["painting","fresco","sculpture","musical work","ballet","composition","mural","opera","artwork"],
 "风格":["style","movement","school","genre","tradition","tendency"],
 "时期":["period","era","civilization","age","century","dynasty","art"],
 "术语":["term","technique","concept","notation","instrument","mode","system","theory","principle","genre"]}
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
todo=[e for e in es if not any(s.startswith("wd-") for s in e["sources"])]
hits=[]
for e in todo:
    q=e["id"].replace("-"," "); nid=norm(e["id"]); tw=TW.get(e["kind"],[])
    for qid,lbl,desc in search(q):
        if norm(lbl)!=nid: continue
        if any(t in (desc or "").lower() for t in tw):
            hits.append({"id":e["id"],"kind":e["kind"],"title":e["title"],"qid":qid,"label":lbl,"desc":desc[:60]})
            break
print("pass3 精确命中:",len(hits),"（未锚定共 %d）"%len(todo))
for h in hits: print("  ",h["id"],h["qid"],h["label"],"|",h["desc"][:45])
json.dump(hits,open(os.path.join(ROOT,"reports","entity_pass3_c25.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)