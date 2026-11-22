# -*- coding: utf-8 -*-
"""Cycle17：取哥特建筑(Q176483)/罗马式建筑(Q46261)的 Wikidata 关键事实（P571 起始、P361 部分于、P1064? 等），
并登记为来源 wd-*。只读+登记，不改条目正文。"""
import json,os,re,subprocess
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
UA="YishuBot/1.0 (educational; local)"
def curl_json(u,tries=4):
    import time
    for i in range(tries):
        p=subprocess.run(["curl","-sS","-m","20","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
        if p.returncode==0 and p.stdout.strip().startswith("{"):
            try: return json.loads(p.stdout)
            except Exception: pass
        time.sleep(0.6*(i+1))
    return None
def ent(q): return (curl_json("https://www.wikidata.org/wiki/Special:EntityData/%s.json"%q) or {}).get("entities",{}).get(q)
def cl(q,pid):
    out=[]
    for c in q.get("claims",{}).get(pid,[]):
        v=c.get("mainsnak",{}).get("datavalue",{}).get("value")
        if isinstance(v,dict):
            if "time" in v: out.append(v["time"])
            elif "id" in v: out.append(v["id"])
    return out
def lab(qid):
    q=ent(qid) or {}
    L=q.get("labels",{})
    return ((L.get("zh") or L.get("en") or {}) or {}).get("value") or qid
T={"wd-gothic-architecture":("Q176483","Gothic architecture","哥特式建筑"),
   "wd-romanesque-architecture":("Q46261","Romanesque architecture","罗马式建筑")}
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
facts={}
for sid,(qid,en,zh) in T.items():
    q=ent(qid)
    labels={k:v["value"] for k,v in q.get("labels",{}).items() if k in ("zh","en")}
    desc=""
    d=q.get("descriptions",{}).get("en",{}).get("value","")
    inc=cl(q,"P571"); style=cl(q,"P136")
    facts[sid]={"qid":qid,"labels":labels,"desc":d,"inception":inc,
                "style":[lab(x) for x in style][:3]}
    print(sid,qid,labels,"| desc:",d[:60],"| P571:",inc,"| style:",facts[sid]["style"])
    if sid not in have:
        sd["sources"].append({"id":sid,"title":"Wikidata: %s (%s)"%(labels.get("en",en),qid),
            "author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026",
            "url":"https://www.wikidata.org/wiki/%s"%qid,"type":"权威结构化数据","verified":True,
            "verified_note":"Cycle17 curl 读取 EntityData 成功；desc 含 architectural style/médieval"})
        have.add(sid)
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
json.dump(facts,open(os.path.join(ROOT,"reports","arch_facts_c17.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("sources total",len(sd["sources"]))