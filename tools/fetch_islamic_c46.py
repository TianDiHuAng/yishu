# -*- coding: utf-8 -*-
"""Cycle46：取 4 件伊斯兰器物的完整 CMA 记录。"""
import json,subprocess,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ACC=["1944.485","1962.23","1995.17","1959.249"]
out={}
for acc in ACC:
    a=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc).get("data",{})
    d=re.sub("<[^>]+>","",a.get("description") or "")
    out[acc]={"title":a.get("title"),"date":a.get("creation_date"),"culture":a.get("culture"),
              "technique":a.get("technique"),"dims":a.get("measurements"),"credit":a.get("creditline"),
              "desc":d}
    print("=====",acc,a.get("title"),"|",a.get("creation_date"),"|",a.get("culture"))
    print("  tech:",a.get("technique"),"| dims:",a.get("measurements"))
    print("  desc:",d[:800])
json.dump(out,open("/e/ai_project/yishu/reports/islamic_c46.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)