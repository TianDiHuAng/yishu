# -*- coding: utf-8 -*-
"""Cycle111：取 4 件详情（澳洲原住民盾、原住民挂毯、波利尼西亚笛、树皮布）。"""
import json,os,subprocess
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","20","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try:return json.loads(p.stdout)
    except Exception:return None
def flat(x):
    if isinstance(x,list): return "; ".join(str(i) for i in x)
    return str(x) if x else ""
ACC=["O369795","O34305","O304190","O133186"]
out={}
for s in ACC:
    r=(get("https://api.vam.ac.uk/v2/object/%s"%s) or {}).get("record") or {}
    rec={"title":flat(r.get("titles")),"date":flat(r.get("productionDates")),
         "place":flat(r.get("placesOfOrigin")),"mat":flat(r.get("materialsAndTechniques")),
         "desc":flat(r.get("physicalDescription")),"summary":flat(r.get("summaryDescription")),
         "objtype":flat(r.get("objectType")),
         "dims":[(d.get("dimension"),d.get("value"),d.get("unit"),d.get("part")) for d in (r.get("dimensions") or [])]}
    out[s]=rec
    print("=====",s,"|",rec["objtype"],"|",rec["date"][:34],"|",rec["place"][:34])
    print("  title:",rec["title"][:80],"| mat:",rec["mat"][:70])
    print("  dims:",rec["dims"])
    print("  desc:",rec["desc"][:430])
    print("  summary:",rec["summary"][:320])
json.dump(out,open(os.path.join(ROOT,"reports","vam4_c111.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)