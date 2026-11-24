# -*- coding: utf-8 -*-
"""Cycle109：V&A 检索伊斯兰织物/地毯/丝织。"""
import json,os,subprocess,urllib.parse
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","20","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try:return json.loads(p.stdout)
    except Exception:return None
Q=["ottoman carpet","safavid silk textile","islamic textile","persian carpet","ottoman silk","mamluk textile"]
rows=[]
for q in Q:
    d=get("https://api.vam.ac.uk/v2/objects/search?q=%s&page_size=6"%urllib.parse.quote(q))
    for r in (d or {}).get("records",[]):
        rows.append({"sys":r.get("systemNumber"),"title":r.get("_primaryTitle"),"date":r.get("_primaryDate"),
                     "type":r.get("objectType"),"q":q})
seen=set();uniq=[]
for r in rows:
    if r["sys"] in seen: continue
    seen.add(r["sys"]);uniq.append(r)
print("候选",len(uniq))
for r in uniq[:28]:
    print("%-8s %-46s %-16s %-20s %s"%(r["sys"],str(r["title"])[:46],str(r["date"])[:16],str(r["type"])[:20],r["q"]))
json.dump(uniq,open(os.path.join(ROOT,"reports","vam_c109.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)