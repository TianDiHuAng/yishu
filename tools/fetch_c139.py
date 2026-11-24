# -*- coding: utf-8 -*-
"""Cycle139：取 4 件 V&A 日本武具详情 + 查重。"""
import json,os,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def get(u):
    p=subprocess.run(["curl","-sSL","-m","20","-A","Mozilla/5.0",u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try:return json.loads(p.stdout)
    except Exception:return None
def flat(x):
    if isinstance(x,list): return "; ".join(str(i) for i in x)
    return str(x) if x else ""
ACC=["O119925","O75791","O182770","O92843"]
out={}
for s in ACC:
    r=(get("https://api.vam.ac.uk/v2/object/%s"%s) or {}).get("record") or {}
    rec={"title":flat(r.get("titles")),"date":flat(r.get("productionDates")),"place":flat(r.get("placesOfOrigin")),
         "mat":flat(r.get("materialsAndTechniques")),"desc":flat(r.get("physicalDescription")),
         "summary":flat(r.get("summaryDescription")),"objtype":flat(r.get("objectType")),
         "dims":[(d.get("dimension"),d.get("value"),d.get("unit")) for d in (r.get("dimensions") or [])]}
    out[s]=rec
    print("=====",s,"|",rec["objtype"],"|",rec["date"][:24],"|",str(rec["place"])[:22])
    print("  mat:",rec["mat"][:80],"| dims:",rec["dims"])
    print("  desc:",rec["desc"][:340])
    print("  summary:",rec["summary"][:380])
json.dump(out,open(os.path.join(ROOT,"reports","vam4_c139.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
sys.path.insert(0,os.path.join(ROOT,"tools"));from catalog import entries
ids={e['id'] for e in entries()}
for x in ["japanese-armour-1800","japanese-armour-1859","kabuto-helmet-1700","japanese-sword-1300"]:
    print("DUP?",x, x in ids)