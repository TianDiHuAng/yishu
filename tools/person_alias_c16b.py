# -*- coding: utf-8 -*-
"""Cycle16b：①把 polymath/universal genius 等加入类型词，补解 leonardo；②登记 6 条 wd-* 来源并挂到对应人物条目。"""
import io,os,json,re,subprocess,urllib.parse
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")
UA="YishuBot/1.0 (educational; local)"
def curl_json(url,tries=5):
    import time
    for i in range(tries):
        p=subprocess.run(["curl","-sS","-m","20","-A",UA,url],capture_output=True,text=True,encoding="utf-8",errors="replace")
        if p.returncode==0 and p.stdout.strip().startswith("{"):
            try: return json.loads(p.stdout)
            except Exception: pass
        time.sleep(0.6*(i+1))
    return None
def search(name,limit=6):
    d=curl_json("https://www.wikidata.org/w/api.php?action=wbsearchentities&search=%s&language=en&format=json&limit=%d"%(urllib.parse.quote(name),limit)) or {}
    return [(x["id"],x.get("label",""),x.get("description","")) for x in d.get("search",[])]
def ent(q): return (curl_json("https://www.wikidata.org/wiki/Special:EntityData/%s.json"%q) or {}).get("entities",{}).get(q)
def times(q,pid):
    out=[]
    for c in q.get("claims",{}).get(pid,[]):
        v=c.get("mainsnak",{}).get("datavalue",{}).get("value")
        if isinstance(v,dict) and "time" in v: out.append(v["time"])
    return out
def yr(t):
    m=re.match(r"([+-])(\d{4})",t or "")
    return (-int(m.group(2)) if m.group(1)=="-" else int(m.group(2))) if m else None
TYPE={"painter","sculptor","composer","artist","architect","musician","calligrapher","polymath","pianist","humanist"}
es={e["id"]:e for e in json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]}
TARGET={"leonardo":"Leonardo da Vinci","donatello":"Donatello","vermeer":"Johannes Vermeer",
        "delacroix":"Eugene Delacroix","monet":"Claude Monet","monteverdi":"Claudio Monteverdi"}
found={}
for eid,en in TARGET.items():
    e=es[eid]; wy=[int(x) for x in re.findall(r"\d{3,4}",e["when"])]
    for qid,lbl,desc in search(en,6):
        q=ent(qid)
        if not q: continue
        if not any(k in (desc or "").lower() for k in TYPE): continue
        b=times(q,"P569"); by=yr(b[0]) if b else None
        if by is None or not wy or abs(by-wy[0])>2: continue
        found[eid]={"qid":qid,"birth":by,"death":yr(times(q,"P570")[0]) if times(q,"P570") else None,
                    "labels":{k:v["value"] for k,v in q.get("labels",{}).items() if k in ("zh","en")},"desc":desc[:70]}
        break
print("resolved:",{k:(v["qid"],v["birth"]) for k,v in found.items()})
# 登记来源并挂到条目
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for eid,info in found.items():
    sid="wd-%s"%eid
    if sid not in have:
        sd["sources"].append({"id":sid,"title":"Wikidata: %s (Q%s)"%(info["labels"].get("en",eid),info["qid"]),
            "author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026",
            "url":"https://www.wikidata.org/wiki/Q%s"%info["qid"],"type":"权威结构化数据","verified":True,
            "verified_note":"Cycle16 curl 读取 EntityData 成功；类型词+生年±2 双闸消歧"})
        have.add(sid)
    p=os.path.join(LD,eid+".json")
    o=json.load(open(p,encoding="utf-8")) if os.path.exists(p) else {"id":eid}
    srcs=list(dict.fromkeys((o.get("sources") or es[eid].get("sources",[]))+[sid]))
    o["sources"]=srcs
    note="【已复核·Wikidata】生卒：第二来源 %s（https://www.wikidata.org/wiki/Q%s），据其结构化数据：生年 %s，卒年 %s。"%(
        sid,info["qid"],info["birth"],info["death"])
    pend=o.get("sections",{}).get("待核实","")
    if "【已复核·Wikidata】生卒" not in pend:
        o.setdefault("sections",{})["待核实"]=(pend+" "+note).strip()
    json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
json.dump(found,open(os.path.join(ROOT,"reports","person_alias_c16.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("sources total",len(sd["sources"]),"verified",sum(1 for s in sd["sources"] if s["verified"]))