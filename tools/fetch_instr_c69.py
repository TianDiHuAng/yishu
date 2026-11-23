# -*- coding: utf-8 -*-
"""Cycle69：取 4 件乐器候选全文（科拉、西塔、古琴、恩戈马鼓）。"""
import json,os,subprocess,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ACC=["1918.352","1918.346","1918.371","1929.343"]
out={}
for acc in ACC:
    a=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc).get("data",{})
    d=re.sub("<[^>]+>","",a.get("description") or "")
    out[acc]={"title":a.get("title"),"date":a.get("creation_date"),"culture":a.get("culture"),
              "tech":a.get("technique"),"dims":a.get("measurements"),"desc":d,
              "creators":[x.get("description") for x in (a.get("creators") or [])]}
    print("=====",acc,"|",a.get("title"),"|",a.get("creation_date"),"|",a.get("culture"))
    print("  tech:",a.get("technique"),"| dims:",a.get("measurements"),"| creators:",out[acc]["creators"])
    print("  desc:",d[:750])
json.dump(out,open(os.path.join(ROOT,"reports","instr4_c69.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)