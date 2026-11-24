# -*- coding: utf-8 -*-
"""Cycle109：取 4 件伊斯兰织物详情（阿尔达比勒毯、乌沙克毯、萨法维丝织、奥斯曼丝绒）。"""
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
ACC=["O54307","O85243","O94015","O93545"]
out={}
for s in ACC:
    r=(get("https://api.vam.ac.uk/v2/object/%s"%s) or {}).get("record") or {}
    rec={"title":flat(r.get("titles")),"date":flat(r.get("productionDates")),
         "place":flat(r.get("placesOfOrigin")),"mat":flat(r.get("materialsAndTechniques")),
         "desc":flat(r.get("physicalDescription")),"summary":flat(r.get("summaryDescription")),
         "objtype":flat(r.get("objectType")),
         "dims":[(d.get("dimension"),d.get("value"),d.get("unit"),d.get("part")) for d in (r.get("dimensions") or [])]}
    out[s]=rec
    print("=====",s,"|",rec["objtype"],"|",rec["date"][:34])
    print("  title:",rec["title"][:80],"| place:",rec["place"][:40])
    print("  mat:",rec["mat"][:90])
    print("  dims:",rec["dims"])
    print("  desc:",rec["desc"][:430])
    print("  summary:",rec["summary"][:300])
json.dump(out,open(os.path.join(ROOT,"reports","vam4_c109.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)