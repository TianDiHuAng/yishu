# -*- coding: utf-8 -*-
"""Cycle103：取 4 件新古典/浪漫作品全文（含创作者）+ 查重。"""
import json,os,subprocess,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ACC=["1942.647","1962.37","1983.14","1937.575"]
out={}
for acc in ACC:
    a=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc).get("data",{})
    d=re.sub("<[^>]+>","",a.get("description") or "")
    cr=[x.get("description") for x in (a.get("creators") or [])]
    out[acc]={"title":a.get("title"),"date":a.get("creation_date"),"culture":a.get("culture"),
              "tech":a.get("technique"),"dims":a.get("measurements"),"desc":d,"creators":cr}
    print("=====",acc,"|",a.get("title"),"|",a.get("creation_date"),"|",cr)
    print("  tech:",a.get("technique"),"| dims:",a.get("measurements"))
    print("  desc:",d[:900])
json.dump(out,open(os.path.join(ROOT,"reports","neo4_c103.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)