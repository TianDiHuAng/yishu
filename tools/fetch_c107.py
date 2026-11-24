# -*- coding: utf-8 -*-
"""Cycle107：取 4 件 V&A 详情（韩国民画虎鹊、马穆鲁克清真寺灯、米纳伊碗、日本印笼）。"""
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
ACC=["O22242","O1768","O85593","O76242"]
out={}
for s in ACC:
    r=(get("https://api.vam.ac.uk/v2/object/%s"%s) or {}).get("record") or {}
    rec={"title":flat(r.get("titles")),"date":flat(r.get("productionDates")),
         "place":flat(r.get("placesOfOrigin")),"mat":flat(r.get("materialsAndTechniques")),
         "dims":flat(r.get("dimensions")),"desc":flat(r.get("physicalDescription")),
         "summary":flat(r.get("summaryDescription")),"objtype":flat(r.get("objectType"))}
    out[s]=rec
    print("=====",s,"|",rec["objtype"],"|",rec["date"][:40])
    print("  title:",rec["title"][:90])
    print("  place:",rec["place"][:90])
    print("  mat:",rec["mat"][:120])
    print("  dims:",json.dumps(r.get("dimensions"),ensure_ascii=False)[:200])
    print("  desc:",rec["desc"][:520])
    print("  summary:",rec["summary"][:320])
json.dump(out,open(os.path.join(ROOT,"reports","vam4_c107.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)