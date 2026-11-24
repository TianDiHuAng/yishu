# -*- coding: utf-8 -*-
"""Cycle120：V&A 取 4 件详情（Van Diemen 漆盒、Kashan 砖1262、Iznik 砖板1660、Harp-lute-guitar）+ 查重。"""
import json,os,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","20","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try:return json.loads(p.stdout)
    except Exception:return None
def flat(x):
    if isinstance(x,list): return "; ".join(str(i) for i in x)
    return str(x) if x else ""
ACC=["O18899","O85590","O103140","O58979"]
out={}
for s in ACC:
    r=(get("https://api.vam.ac.uk/v2/object/%s"%s) or {}).get("record") or {}
    rec={"title":flat(r.get("titles")),"date":flat(r.get("productionDates")),"place":flat(r.get("placesOfOrigin")),
         "mat":flat(r.get("materialsAndTechniques")),"desc":flat(r.get("physicalDescription")),
         "summary":flat(r.get("summaryDescription")),"objtype":flat(r.get("objectType")),
         "dims":[(d.get("dimension"),d.get("value"),d.get("unit")) for d in (r.get("dimensions") or [])]}
    out[s]=rec
    print("=====",s,"|",rec["objtype"],"|",rec["date"][:28],"|",str(rec["place"])[:30])
    print("  title:",rec["title"][:70],"| mat:",rec["mat"][:80])
    print("  dims:",rec["dims"])
    print("  desc:",rec["desc"][:380])
    print("  summary:",rec["summary"][:300])
json.dump(out,open(os.path.join(ROOT,"reports","vam4_c120.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
sys.path.insert(0,os.path.join(ROOT,"tools"));from catalog import entries
ids={e['id'] for e in entries()}
for x in ["vandiem-lacquer-box","kashan-tile-1262","iznik-panel-1660","harp-lute-guitar-va"]:
    print("DUP?",x, x in ids)