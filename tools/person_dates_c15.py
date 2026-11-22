# -*- coding: utf-8 -*-
"""Cycle15 v3：人物生卒核验，改用 curl 获取（urllib 在本环境 DNS 不稳定，curl 稳定 200）。
消歧：中文/英文检索 → label 含条目名 → description 含人物类型词 → 生年与条目 when 相差≤5。
输出 reports/person_dates.json：confirmed / mismatch / no_match。只读，不改知识库。"""
import json,os,re,subprocess,urllib.parse
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
UA="YishuBot/1.0 (educational; local)"
def curl_json(url,tries=5):
    import time
    last=None
    for i in range(tries):
        p=subprocess.run(["curl","-sS","-m","20","-A",UA,url],capture_output=True,text=True,encoding="utf-8",errors="replace")
        if p.returncode==0 and p.stdout.strip().startswith("{"):
            try: return json.loads(p.stdout)
            except Exception as e: last=e
        else:
            last=p.stderr[:60] if p.stderr else "rc=%d"%p.returncode
        time.sleep(0.8*(i+1))
    print("   [warn] fetch failed:",url[:70],last)
    return None
def search(name,lang="zh",limit=8):
    u="https://www.wikidata.org/w/api.php?action=wbsearchentities&search=%s&language=%s&format=json&limit=%d"%(urllib.parse.quote(name),lang,limit)
    d=curl_json(u) or {}
    return [(x["id"],x.get("label",""),x.get("description","")) for x in d.get("search",[])]
def ent(q):
    return curl_json("https://www.wikidata.org/wiki/Special:EntityData/%s.json"%q)
def times(q,pid):
    out=[]
    for c in q.get("claims",{}).get(pid,[]):
        v=c.get("mainsnak",{}).get("datavalue",{}).get("value")
        if isinstance(v,dict) and "time" in v: out.append(v["time"])
    return out
def year(t):
    m=re.match(r"([+-])(\d{4})",t or "")
    if not m: return None
    y=int(m.group(2)); return -y if m.group(1)=="-" else y
def lab(qid):
    e=ent(qid) or {}
    L=(e.get("entities",{}).get(qid) or {}).get("labels",{})
    return ((L.get("zh") or L.get("en") or {}) or {}).get("value") or qid
TYPE={"painter","sculptor","composer","artist","architect","musician","conductor","pianist","violinist","calligrapher"}
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
persons=[e for e in es if e["kind"]=="人物"]
rep={"confirmed":[],"mismatch":[],"no_match":[]}
for e in persons:
    cands=search(e["title"],"zh",6)
    used_lang="zh"
    if not cands:
        cands=search(e["title"],"en",6); used_lang="en"
    wy=[int(x) for x in re.findall(r"\d{3,4}",e["when"])]
    chosen=None
    for qid,lbl,desc in cands:
        payload=ent(qid) or {}
        q=(payload.get("entities") or {}).get(qid)
        if not q: continue
        labels={k:v["value"] for k,v in q.get("labels",{}).items() if k in ("zh","en")}
        d=(desc or "").lower()
        tmatch=any(v and (v in e["title"] or e["title"] in v) for v in labels.values()) or (lbl and (lbl in e["title"] or e["title"] in lbl))
        kmatch=any(k in d for k in TYPE)
        b=times(q,"P569"); dd=times(q,"P570")
        by=year(b[0]) if b else None
        near=(not wy) or (by is not None and any(abs(by-w)<=5 for w in wy))
        rank=cands.index((qid,lbl,desc))
        strict_ok = tmatch and kmatch and near
        loose_ok = (used_lang=="zh") and rank<3 and kmatch and (by is not None and wy and abs(by-wy[0])<=2)
        if strict_ok or loose_ok:
            chosen={"qid":qid,"labels":labels,"desc":desc,"birth":by,
                    "death":year(dd[0]) if dd else None}
            break
    if not chosen:
        rep["no_match"].append({"id":e["id"],"title":e["title"],"when":e["when"],
                                "candidates":[(c[0],c[1],c[2][:40]) for c in cands[:3]]})
        continue
    rec={"id":e["id"],"title":e["title"],"when":e["when"],"qid":chosen["qid"],
         "wd_birth":chosen["birth"],"wd_death":chosen["death"],"desc":chosen["desc"][:70]}
    if wy and chosen["birth"] is not None and abs(chosen["birth"]-wy[0])<=1: rep["confirmed"].append(rec)
    else:
        rec["entry_first_year"]=wy[0] if wy else None
        rec["delta"]=(chosen["birth"]-wy[0]) if (wy and chosen["birth"] is not None) else None
        rep["mismatch"].append(rec)
json.dump(rep,open(os.path.join(ROOT,"reports","person_dates.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("人物 %d：confirmed %d / mismatch %d / no_match %d"%(len(persons),len(rep["confirmed"]),len(rep["mismatch"]),len(rep["no_match"])))
for m in rep["mismatch"][:10]: print("  MISMATCH",m["id"],m["when"],"WD",m["wd_birth"],m["wd_death"],"delta",m.get("delta"),m["desc"][:40])
for m in rep["no_match"][:8]: print("  NO_MATCH",m["id"],[c[1] for c in m["candidates"][:2]])