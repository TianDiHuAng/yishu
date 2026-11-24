# -*- coding: utf-8 -*-
"""Cycle135：CMA 取 4 件伊斯兰全文 + 查重。"""
import json,os,subprocess,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ACC=["1917.977","1926.22","1947.500.b","1964.41"]
out={}
for acc in ACC:
    a=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc).get("data",{})
    d=re.sub("<[^>]+>","",a.get("description") or "")
    out[acc]={"title":a.get("title"),"date":a.get("creation_date"),"culture":a.get("culture"),
              "tech":a.get("technique"),"dims":a.get("measurements"),"desc":d}
    print("=====",acc,"|",a.get("title"),"|",a.get("creation_date"),"|",a.get("culture"))
    print("  tech:",a.get("technique"),"| dims:",a.get("measurements"))
    print("  desc:",d[:800])
json.dump(out,open(os.path.join(ROOT,"reports","isl4_c135.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
sys.path.insert(0,os.path.join(ROOT,"tools"));from catalog import entries
ids={e['id'] for e in entries()}
for x in ["minai-beaker-princes","safavid-poppy-textile","safavid-shahnama-story","sasanian-horse-vessel"]:
    print("DUP?",x, x in ids)