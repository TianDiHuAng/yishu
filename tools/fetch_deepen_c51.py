# -*- coding: utf-8 -*-
"""Cycle51：取 5 件候选全文（莫切蝙蝠瓶、印加束腰外衣、约鲁巴头像、高丽菊纹瓶、缅甸 Kammavacha）。"""
import json,subprocess,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ACC=["2005.6","1957.136","1995.21","1918.454","1945.172"]
out={}
for acc in ACC:
    a=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc).get("data",{})
    d=re.sub("<[^>]+>","",a.get("description") or "")
    out[acc]={"title":a.get("title"),"date":a.get("creation_date"),"culture":a.get("culture"),
              "tech":a.get("technique"),"dims":a.get("measurements"),"desc":d}
    print("=====",acc,"|",a.get("title"),"|",a.get("creation_date"),"|",a.get("culture"))
    print("  tech:",a.get("technique"),"| dims:",a.get("measurements"))
    print("  desc:",d[:750])
json.dump(out,open("/e/ai_project/yishu/reports/deepen5_c51.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)