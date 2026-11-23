# -*- coding: utf-8 -*-
"""Cycle84：取 4 件欧洲雕塑/版画。"""
import json,os,subprocess,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ACC=["2009.81","1992.230","1976.2","1951.454"]
out={}
for acc in ACC:
    a=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc).get("data",{})
    d=re.sub("<[^>]+>","",a.get("description") or "")
    out[acc]={"title":a.get("title"),"date":a.get("creation_date"),"culture":a.get("culture"),
              "tech":a.get("technique"),"dims":a.get("measurements"),"desc":d,
              "creators":[x.get("description") for x in (a.get("creators") or [])]}
    print("=====",acc,"|",a.get("title"),"|",a.get("creation_date"),"|",a.get("culture"))
    print("  tech:",a.get("technique"),"| dims:",a.get("measurements"),"| creators:",out[acc]["creators"])
    print("  desc:",d[:900])
json.dump(out,open(os.path.join(ROOT,"reports","eur4_c84.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)