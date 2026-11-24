# -*- coding: utf-8 -*-
"""Cycle142：V&A 取 4 件伊斯兰地毯详情 + 查重。"""
import json,os,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def get(u):
    p=subprocess.run(["curl","-sSL","-m","20","-A","Mozilla/5.0",u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try:return json.loads(p.stdout)
    except Exception:return None
def flat(x):
    if isinstance(x,list): return "; ".join(str(i) for i in x)
    return str(x) if x else ""
ACC=["O85114","O54294","O85144","O66858"]
out={}
for s in ACC:
    r=(get("https://api.vam.ac.uk/v2/object/%s"%s) or {}).get("record") or {}
    rec={"title":flat(r.get("titles")),"date":flat(r.get("productionDates")),"place":flat(r.get("placesOfOrigin")),
         "mat":flat(r.get("materialsAndTechniques")),"desc":flat(r.get("physicalDescription")),
         "summary":flat(r.get("summaryDescription")),"objtype":flat(r.get("objectType")),
         "dims":[(d.get("dimension"),d.get("value"),d.get("unit")) for d in (r.get("dimensions") or [])]}
    out[s]=rec
    print("=====",s,"|",rec["objtype"],"|",rec["date"][:22],"|",str(rec["place"])[:22])
    print("  title:",rec["title"][:50],"| dims:",rec["dims"])
    print("  desc:",rec["desc"][:320])
    print("  summary:",rec["summary"][:380])
json.dump(out,open(os.path.join(ROOT,"reports","vam4_c142.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
sys.path.insert(0,os.path.join(ROOT,"tools"));from catalog import entries
ids={e['id'] for e in entries()}
for x in ["polonaise-carpet","salting-carpet","chelsea-carpet","isfahan-carpet-1550"]:
    print("DUP?",x, x in ids)