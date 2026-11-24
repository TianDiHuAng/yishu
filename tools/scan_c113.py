# -*- coding: utf-8 -*-
"""Cycle113：V&A 检索乐器实物。"""
import json,os,subprocess,urllib.parse
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","20","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try:return json.loads(p.stdout)
    except Exception:return None
Q=["violin","harpsichord","sitar","koto","djembe","didgeridoo","bagpipe","natural trumpet","lute"]
rows=[]
for q in Q:
    d=get("https://api.vam.ac.uk/v2/objects/search?q=%s&page_size=6"%urllib.parse.quote(q))
    for r in (d or {}).get("records",[]):
        t=str(r.get("objectType") or "")
        if not any(k in t.lower() for k in ["violin","harp","sitar","koto","drum","didg","bagpipe","trumpet","lute","flute","zither","lyre","shawm","oboe","guitar"]): continue
        rows.append({"sys":r.get("systemNumber"),"title":r.get("_primaryTitle"),"date":r.get("_primaryDate"),
                     "type":t,"place":r.get("_primaryPlace"),"q":q})
seen=set();uniq=[]
for r in rows:
    if r["sys"] in seen: continue
    seen.add(r["sys"]);uniq.append(r)
print("候选",len(uniq))
for r in uniq[:30]:
    print("%-8s %-40s %-16s %-18s %s"%(r["sys"],str(r["title"])[:40],str(r["date"])[:16],str(r["type"])[:18],r["q"]))
json.dump(uniq,open(os.path.join(ROOT,"reports","vam_c113.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)