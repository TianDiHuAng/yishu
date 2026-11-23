# -*- coding: utf-8 -*-
"""Cycle79：探测中国绘画作品（宋元明清）。"""
import json,os,subprocess,urllib.parse,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
Q=["chinese painting hanging scroll","ming painting","qing painting","yuan painting","song painting",
   "literati painting china","chinese landscape painting","handscroll china"]
rows=[]
for q in Q:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=8&has_image=0"%urllib.parse.quote(q))
    for a in (d or {}).get("data",[]):
        cul=str(a.get("culture") or "")
        t=str(a.get("technique") or "")
        if not re.search("China|Chinese",cul,re.I): continue
        if not re.search("ink|scroll|silk|paper|color",t,re.I): continue
        desc=re.sub("<[^>]+>","",a.get("description") or "")
        if len(desc)<280: continue
        rows.append({"acc":a.get("accession_number"),"title":a.get("title"),"date":a.get("creation_date"),
                     "culture":cul,"len":len(desc)})
seen=set(); uniq=[]
for r in rows:
    if r["acc"] in seen: continue
    seen.add(r["acc"]); uniq.append(r)
print("中国绘画候选 %d"%len(uniq))
for r in uniq[:16]:
    print("%-10s %-46s %-12s %-40s %d"%(r["acc"],str(r["title"])[:46],str(r["date"])[:12],str(r["culture"])[:40],r["len"]))
json.dump(uniq,open(os.path.join(ROOT,"reports","cnpaint_c79.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)