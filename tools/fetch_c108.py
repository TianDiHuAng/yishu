# -*- coding: utf-8 -*-
"""Cycle108：取 4 件 V&A 详情（广重《萨埵海》、花鸟版画、马穆鲁克错银铜盆、伊兹尼克釉砖）。"""
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
ACC=["O78132","O71685","O83883","O86971"]
out={}
for s in ACC:
    raw=get("https://api.vam.ac.uk/v2/object/%s"%s) or {}
    r=raw.get("record") or {}
    rec={"title":flat(r.get("titles")),"date":flat(r.get("productionDates")),
         "place":flat(r.get("placesOfOrigin")),"mat":flat(r.get("materialsAndTechniques")),
         "desc":flat(r.get("physicalDescription")),"summary":flat(r.get("summaryDescription")),
         "objtype":flat(r.get("objectType")),
         "dims":[(d.get("dimension"),d.get("value"),d.get("unit"),d.get("part")) for d in (r.get("dimensions") or [])],
         "maker":flat(r.get("artistMakerPerson"))}
    out[s]=rec
    print("=====",s,"|",rec["objtype"],"|",rec["date"][:36])
    print("  title:",rec["title"][:90])
    print("  place:",rec["place"][:70],"| mat:",rec["mat"][:80])
    print("  dims:",rec["dims"])
    print("  desc:",rec["desc"][:460])
    print("  summary:",rec["summary"][:280])
json.dump(out,open(os.path.join(ROOT,"reports","vam4_c108.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)