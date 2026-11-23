# -*- coding: utf-8 -*-
"""Cycle98：探测中国玉器实物，并先查重 id。"""
import json,os,subprocess,urllib.parse,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
Q=["chinese jade","jade bi disc","jade cong","jade dragon china","qing jade","han jade","jadeite china"]
rows=[]
for q in Q:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=8&has_image=0"%urllib.parse.quote(q))
    for a in (d or {}).get("data",[]):
        cul=str(a.get("culture") or ""); tech=str(a.get("technique") or "")
        if not re.search("China|Chinese",cul,re.I): continue
        if not re.search("jade",tech,re.I): continue
        desc=re.sub("<[^>]+>","",a.get("description") or "")
        if len(desc)<280: continue
        rows.append({"acc":a.get("accession_number"),"title":a.get("title"),"date":a.get("creation_date"),
                     "culture":cul,"len":len(desc)})
seen=set(); uniq=[]
for r in rows:
    if r["acc"] in seen: continue
    seen.add(r["acc"]); uniq.append(r)
print("候选 %d"%len(uniq))
for r in uniq[:16]:
    print("%-10s %-46s %-14s %-40s %d"%(r["acc"],str(r["title"])[:46],str(r["date"])[:14],str(r["culture"])[:40],r["len"]))
json.dump(uniq,open(os.path.join(ROOT,"reports","cnjade_c98.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)