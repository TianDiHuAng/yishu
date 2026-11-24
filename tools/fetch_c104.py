# -*- coding: utf-8 -*-
"""Cycle104：取 4 件印象/后印象作品全文（含创作者）+ 查重。"""
import json,os,subprocess,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ACC=["1947.209","1948.303","1990.7","1958.30"]
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
json.dump(out,open(os.path.join(ROOT,"reports","imp4_c104.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
sys.path.insert(0,os.path.join(ROOT,"tools"));from catalog import entries
ids={e['id'] for e in entries()}
for x in ["van-gogh-plane-trees","van-gogh-dr-gachet","pissarro-lock-pontoise","cezanne-wheelbarrow"]:
    print("DUP?",x, x in ids)