# -*- coding: utf-8 -*-
"""Cycle21c：对 6 个作品档案条目取其 Wikidata 尺寸(P2048高/P2049宽)、藏品编号(P217)、材质(P186)、
并输出对照表；有值者可作为【已复核·Wikidata】写入待核实（不改正文断言）。"""
import json,os,subprocess
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
def vals(q,pid):
    out=[]
    for c in q.get("claims",{}).get(pid,[]):
        v=c.get("mainsnak",{}).get("datavalue",{}).get("value")
        if isinstance(v,dict):
            if "amount" in v: out.append(v["amount"])
            elif "id" in v: out.append(v["id"])
            elif "text" in v: out.append(v["text"])
            elif "time" in v: out.append(v["time"])
        else: out.append(v)
    return out
def lab(qid):
    e=ent(qid) or {}
    L=e.get("labels",{})
    return ((L.get("zh") or L.get("en") or {}) or {}).get("value") or qid
W={"mona-lisa":"Q12418","starry-night":"Q45585","birth-of-venus-work":"Q151047",
   "sistine-ceiling-work":"Q844675","guernica-work":"Q175036","rite-of-spring-work":"Q206015"}
out={}
for eid,qid in W.items():
    q=ent(qid) or {}
    rec={"qid":qid,"height_P2048":vals(q,"P2048"),"width_P2049":vals(q,"P2049"),
         "inventory_P217":vals(q,"P217"),"material_P186":[lab(x) for x in vals(q,"P186") if str(x).startswith("Q")][:3],
         "genre_P136":[lab(x) for x in vals(q,"P136") if str(x).startswith("Q")][:3]}
    out[eid]=rec
    print(eid,qid,"H:",rec["height_P2048"],"W:",rec["width_P2049"],"inv:",rec["inventory_P217"][:2],"material:",rec["material_P186"])
json.dump(out,open(os.path.join(ROOT,"reports","work_dims_c21.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)