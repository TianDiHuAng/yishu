# -*- coding: utf-8 -*-
"""Cycle21：为 A 类剩余建筑缺口（日本建筑、印度建筑）解析 Wikidata 实体并用三重消歧确认。"""
import json,os,subprocess,urllib.parse,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
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
def search(q,lang="en",limit=5):
    d=curl_json("https://www.wikidata.org/w/api.php?action=wbsearchentities&search=%s&language=%s&format=json&limit=%d"%(urllib.parse.quote(q),lang,limit)) or {}
    return [(x["id"],x.get("label",""),x.get("description","")) for x in d.get("search",[])]
def ent(q): return (curl_json("https://www.wikidata.org/wiki/Special:EntityData/%s.json"%q) or {}).get("entities",{}).get(q)
res={}
for key,q in [("japanese-architecture","Japanese architecture"),("indian-architecture","Architecture of India")]:
    cands=search(q)
    print("==",key)
    for cid,lbl,desc in cands[:4]: print("   ",cid,lbl,"|",desc[:60])
    picked=None
    for cid,lbl,desc in cands:
        e=ent(cid)
        if not e: continue
        labels={k:v["value"] for k,v in e.get("labels",{}).items() if k in ("zh","en")}
        d=(desc or "").lower()
        if ("architecture" in d or "architectural" in d) and any("architect" in v.lower() or "建筑" in v for v in labels.values()):
            picked={"qid":cid,"labels":labels,"desc":desc}; break
    res[key]=picked
    print("   picked:",picked)
json.dump(res,open(os.path.join(ROOT,"reports","arch_c21.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)