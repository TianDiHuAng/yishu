# -*- coding: utf-8 -*-
"""Cycle106：取 4 件 V&A 对象详情字段。"""
import json,os,subprocess
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","20","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try:return json.loads(p.stdout)
    except Exception:return None
ACC=["O16589","O22279","O22419","O67415"]
out={}
for s in ACC:
    d=get("https://api.vam.ac.uk/v2/object/%s"%s)
    r=(d or {}).get("record") or {}
    def flat(x):
        if isinstance(x,list): return "; ".join(str(i) for i in x)
        return str(x) if x else ""
    rec={"title":flat(r.get("titles")),"date":flat(r.get("productionDates")),
         "place":flat(r.get("placesOfOrigin")),"mat":flat(r.get("materialsAndTechniques")),
         "dims":flat(r.get("dimensions")),"desc":flat(r.get("physicalDescription")),
         "summary":flat(r.get("summaryDescription")),"objtype":flat(r.get("objectType")),
         "museum":flat(r.get("museumNumber"))}
    out[s]=rec
    print("=====",s,"|",rec["objtype"],"|",rec["date"][:40])
    print("  title:",rec["title"][:80])
    print("  place:",rec["place"][:80])
    print("  mat:",rec["mat"][:100])
    print("  dims:",rec["dims"][:120])
    print("  desc:",rec["desc"][:500])
    print("  summary:",rec["summary"][:300])
json.dump(out,open(os.path.join(ROOT,"reports","vam4_c106.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)