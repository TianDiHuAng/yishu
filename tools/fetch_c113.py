# -*- coding: utf-8 -*-
"""Cycle113：取 4 件乐器详情（Baffo 羽管键琴、西塔琴、诺森伯兰风笛、小提琴）。"""
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
ACC=["O58982","O86702","O58248","O93114"]
out={}
for s in ACC:
    r=(get("https://api.vam.ac.uk/v2/object/%s"%s) or {}).get("record") or {}
    rec={"title":flat(r.get("titles")),"date":flat(r.get("productionDates")),"place":flat(r.get("placesOfOrigin")),
         "mat":flat(r.get("materialsAndTechniques")),"desc":flat(r.get("physicalDescription")),
         "summary":flat(r.get("summaryDescription")),"objtype":flat(r.get("objectType")),
         "dims":[(d.get("dimension"),d.get("value"),d.get("unit")) for d in (r.get("dimensions") or [])]}
    out[s]=rec
    print("=====",s,"|",rec["objtype"],"|",rec["date"][:30],"|",str(rec["place"])[:30])
    print("  mat:",rec["mat"][:90],"| dims:",rec["dims"])
    print("  desc:",rec["desc"][:380])
    print("  summary:",rec["summary"][:300])
json.dump(out,open(os.path.join(ROOT,"reports","vam4_c113.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)