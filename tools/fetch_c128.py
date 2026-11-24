# -*- coding: utf-8 -*-
"""Cycle128：取 4 件日本小件详情（根付、刀镡、印笼、输出用书桌盒）+ 查重。"""
import json,os,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def get(u):
    p=subprocess.run(["curl","-sSL","-m","20","-A","Mozilla/5.0",u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try:return json.loads(p.stdout)
    except Exception:return None
def flat(x):
    if isinstance(x,list): return "; ".join(str(i) for i in x)
    return str(x) if x else ""
ACC=["O492598","O39087","O120429","O77643"]
out={}
for s in ACC:
    r=(get("https://api.vam.ac.uk/v2/object/%s"%s) or {}).get("record") or {}
    rec={"title":flat(r.get("titles")),"date":flat(r.get("productionDates")),"place":flat(r.get("placesOfOrigin")),
         "mat":flat(r.get("materialsAndTechniques")),"desc":flat(r.get("physicalDescription")),
         "summary":flat(r.get("summaryDescription")),"objtype":flat(r.get("objectType")),
         "dims":[(d.get("dimension"),d.get("value"),d.get("unit")) for d in (r.get("dimensions") or [])]}
    out[s]=rec
    print("=====",s,"|",rec["objtype"],"|",rec["date"][:24],"|",str(rec["place"])[:24])
    print("  mat:",rec["mat"][:100],"| dims:",rec["dims"])
    print("  desc:",rec["desc"][:380])
    print("  summary:",rec["summary"][:420])
json.dump(out,open(os.path.join(ROOT,"reports","vam4_c128.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
sys.path.insert(0,os.path.join(ROOT,"tools"));from catalog import entries
ids={e['id'] for e in entries()}
for x in ["netsuke-dancer","tsuba-shakudo","inro-autumn-plants","nagasaki-writing-box"]:
    print("DUP?",x, x in ids)