# -*- coding: utf-8 -*-
"""Cycle144：V&A 取 4 件浮世绘详情 + 查重。"""
import json,os,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def get(u):
    p=subprocess.run(["curl","-sSL","-m","20","-A","Mozilla/5.0",u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try:return json.loads(p.stdout)
    except Exception:return None
def flat(x):
    if isinstance(x,list): return "; ".join(str(i) for i in x)
    return str(x) if x else ""
ACC=["O71806","O71692","O76529","O73124"]
out={}
for s in ACC:
    r=(get("https://api.vam.ac.uk/v2/object/%s"%s) or {}).get("record") or {}
    rec={"title":flat(r.get("titles")),"date":flat(r.get("productionDates")),"place":flat(r.get("placesOfOrigin")),
         "mat":flat(r.get("materialsAndTechniques")),"desc":flat(r.get("physicalDescription")),
         "summary":flat(r.get("summaryDescription")),"objtype":flat(r.get("objectType")),
         "dims":[(d.get("dimension"),d.get("value"),d.get("unit")) for d in (r.get("dimensions") or [])]}
    out[s]=rec
    print("=====",s,"|",rec["objtype"],"|",rec["date"][:20])
    print("  title:",rec["title"][:70],"| dims:",rec["dims"])
    print("  desc:",rec["desc"][:300])
    print("  summary:",rec["summary"][:380])
json.dump(out,open(os.path.join(ROOT,"reports","vam4_c144.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
sys.path.insert(0,os.path.join(ROOT,"tools"));from catalog import entries
ids={e['id'] for e in entries()}
for x in ["utamaro-plum-blind","kunisada-dressing-room","hiroshige-sumida-snow","hokusai-36views"]:
    print("DUP?",x, x in ids)