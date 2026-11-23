# -*- coding: utf-8 -*-
"""Cycle80：取 4 件印度绘画。"""
import json,os,subprocess,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ACC=["1931.451","1984.65","1998.102","2001.111"]
out={}
for acc in ACC:
    a=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc).get("data",{})
    d=re.sub("<[^>]+>","",a.get("description") or "")
    out[acc]={"title":a.get("title"),"date":a.get("creation_date"),"culture":a.get("culture"),
              "tech":a.get("technique"),"dims":a.get("measurements"),"desc":d}
    print("=====",acc,"|",a.get("title"),"|",a.get("creation_date"),"|",a.get("culture"))
    print("  tech:",a.get("technique"),"| dims:",a.get("measurements"))
    print("  desc:",d[:860])
json.dump(out,open(os.path.join(ROOT,"reports","inpaint4_c80.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)