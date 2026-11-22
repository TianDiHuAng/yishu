# -*- coding: utf-8 -*-
"""Cycle16：为 6 条未匹配人物加英文名别名，重跑核验并输出差异。
别名只用于**检索**（不写入条目正文），仍受"类型词 + 生年±2"双闸约束。"""
import io,os,json,re,subprocess,urllib.parse
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="YishuBot/1.0 (educational; local)"
ALIAS={"donatello":"Donatello","leonardo":"Leonardo da Vinci","vermeer":"Johannes Vermeer",
       "delacroix":"Eugene Delacroix","monet":"Claude Monet","monteverdi":"Claudio Monteverdi"}
def curl_json(url,tries=5):
    import time
    for i in range(tries):
        p=subprocess.run(["curl","-sS","-m","20","-A",UA,url],capture_output=True,text=True,encoding="utf-8",errors="replace")
        if p.returncode==0 and p.stdout.strip().startswith("{"):
            try: return json.loads(p.stdout)
            except Exception: pass
        time.sleep(0.6*(i+1))
    return None
def search(name,lang="en",limit=6):
    u="https://www.wikidata.org/w/api.php?action=wbsearchentities&search=%s&language=%s&format=json&limit=%d"%(urllib.parse.quote(name),lang,limit)
    d=curl_json(u) or {}
    return [(x["id"],x.get("label",""),x.get("description","")) for x in d.get("search",[])]
def ent(q): return curl_json("https://www.wikidata.org/wiki/Special:EntityData/%s.json"%q)
def times(q,pid):
    out=[]
    for c in q.get("claims",{}).get(pid,[]):
        v=c.get("mainsnak",{}).get("datavalue",{}).get("value")
        if isinstance(v,dict) and "time" in v: out.append(v["time"])
    return out
def yr(t):
    m=re.match(r"([+-])(\d{4})",t or "")
    return (-int(m.group(2)) if m.group(1)=="-" else int(m.group(2))) if m else None
TYPE={"painter","sculptor","composer","artist","architect","musician","calligrapher","pianist"}
es={e["id"]:e for e in json.load(open(os.path.join(ROOT,"data","site_entries.json"),encoding="utf-8"))["entries"]}
out={}
for eid,en in ALIAS.items():
    e=es[eid]; wy=[int(x) for x in re.findall(r"\d{3,4}",e["when"])]
    best=None
    for qid,lbl,desc in search(en,"en",6):
        p=ent(qid) or {}
        q=(p.get("entities") or {}).get(qid)
        if not q: continue
        d=(desc or "").lower()
        if not any(k in d for k in TYPE): continue
        b=times(q,"P569"); dd=times(q,"P570")
        by=yr(b[0]) if b else None; dy=yr(dd[0]) if dd else None
        if by is None or not wy or abs(by-wy[0])>2: continue
        best={"qid":qid,"desc":desc[:70],"birth":by,"death":dy,
              "labels":{k:v["value"] for k,v in q.get("labels",{}).items() if k in ("zh","en")}}
        break
    out[eid]={"entry_when":e["when"],"search_en":en,"result":best}
    print(eid,"=>",("Q"+best["qid"] if best else "NO MATCH"), best["labels"] if best else "", best["birth"] if best else "")
json.dump(out,open(os.path.join(ROOT,"reports","person_alias_c16.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)