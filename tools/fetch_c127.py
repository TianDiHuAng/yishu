# -*- coding: utf-8 -*-
"""Cycle127：CMA 取 4 件日朝绘画全文 + 查重。"""
import json,os,subprocess,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ACC=["2015.138","1987.187","1960.284","1956.87"]
out={}
for acc in ACC:
    a=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc).get("data",{})
    d=re.sub("<[^>]+>","",a.get("description") or "")
    cr=[x.get("description") for x in (a.get("creators") or [])]
    out[acc]={"title":a.get("title"),"date":a.get("creation_date"),"culture":a.get("culture"),
              "tech":a.get("technique"),"dims":a.get("measurements"),"desc":d,"creators":cr}
    print("=====",acc,"|",a.get("title"),"|",a.get("creation_date"),"|",cr)
    print("  tech:",a.get("technique"),"| dims:",a.get("measurements"))
    print("  desc:",d[:820])
json.dump(out,open(os.path.join(ROOT,"reports","jk4_c127.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
sys.path.insert(0,os.path.join(ROOT,"tools"));from catalog import entries
ids={e['id'] for e in entries()}
for x in ["korean-orchids-rocks","korean-snowscape-figures","japan-eight-views-xiaoxiang","japan-miraculous-origins"]:
    print("DUP?",x, x in ids)