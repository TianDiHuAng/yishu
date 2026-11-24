# -*- coding: utf-8 -*-
"""Cycle104：探测印象派/后印象派作品。"""
import json,os,subprocess,urllib.parse,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
Q=["impressionist painting","post-impressionism","vincent van gogh","paul gauguin","georges seurat","camille pissarro","alfred sisley","cezanne still life"]
rows=[]
for q in Q:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=8&has_image=0"%urllib.parse.quote(q))
    for a in (d or {}).get("data",[]):
        dt=str(a.get("creation_date") or ""); yr=re.findall(r"\d{4}",dt)
        if not yr: continue
        if max(int(y) for y in yr) < 1860 or min(int(y) for y in yr) > 1910: continue
        desc=re.sub("<[^>]+>","",a.get("description") or "")
        if len(desc)<280: continue
        rows.append({"acc":a.get("accession_number"),"title":a.get("title"),"date":dt,"len":len(desc)})
seen=set(); uniq=[]
for r in rows:
    if r["acc"] in seen: continue
    seen.add(r["acc"]); uniq.append(r)
print("候选 %d"%len(uniq))
for r in uniq[:18]:
    print("%-10s %-50s %-14s %d"%(r["acc"],str(r["title"])[:50],str(r["date"])[:14],r["len"]))
json.dump(uniq,open(os.path.join(ROOT,"reports","imp_c104.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)