# -*- coding: utf-8 -*-
"""Cycle210 探测：为人物条目查 GND（德国国家图书馆规范档，经 lobid.org）。
匹配规则：只接受 GND 记录的 sameAs 里含有本条目 Wikidata QID 的命中（按编号匹配，不按人名猜）。
只写 tmp/gnd_c232.json，不改数据。"""
import json,os,re,subprocess,sys,time,urllib.parse
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
UA="YishuBot/1.0 (educational art-history knowledge base)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
E=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
SM={s["id"]:s for s in json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))["sources"]}
out={}
todo=[]
for e in E:
    if e.get("kind")!="人物": continue
    if any(s.startswith("gnd-") for s in e.get("sources",[])): continue
    qid=None
    for s in e.get("sources",[]):
        u=SM.get(s,{}).get("url","")
        m=re.search(r"wikidata\.org/wiki/(Q\d+)",u)
        if m: qid=m.group(1);break
    if not qid: continue
    m=re.search(r"（([^）]+)）",e["title"])
    name=m.group(1) if m else None
    todo.append((e["id"],qid,name,e["title"]))
print("candidates",len(todo)); sys.stdout.flush()
for eid,qid,name,title in todo:
    hit=None
    # 1) 直接按 sameAs 查 QID
    q='sameAs.id:"http://www.wikidata.org/entity/%s"'%qid
    d=get("https://lobid.org/gnd/search?q=%s&format=json&size=3"%urllib.parse.quote(q))
    for mbr in (d or {}).get("member",[]):
        same=[x.get("id","") if isinstance(x,dict) else x for x in mbr.get("sameAs",[])]
        if any(x.endswith("/"+qid) for x in same): hit=mbr;break
    if hit:
        rec={"gnd":hit.get("gndIdentifier"),"name":hit.get("preferredName"),
             "birth":(hit.get("dateOfBirth") or [None])[0],"death":(hit.get("dateOfDeath") or [None])[0],
             "prof":[p.get("label") for p in hit.get("professionOrOccupation",[]) if isinstance(p,dict)][:4],"qid":qid}
        out[eid]=rec
        print("HIT ",eid,qid,rec["gnd"],rec["name"],rec["birth"],rec["death"],rec["prof"])
    else:
        print("miss",eid,qid,name)
    sys.stdout.flush(); time.sleep(0.3)
json.dump(out,open(os.path.join(ROOT,"tmp","gnd_c232.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("hits",len(out),"of",len(todo))
