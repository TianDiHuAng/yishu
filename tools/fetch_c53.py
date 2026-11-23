# -*- coding: utf-8 -*-
"""Cycle53：取 5 件全文（纳斯卡人首纹碗、朝鲜朝蜀葵形杯、朝鲜朝婚礼袍、占婆行星神、占婆飞天托架）。"""
import json,subprocess,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ACC=["2009.435","1969.85","1918.552","1935.147","1990.34"]
out={}
for acc in ACC:
    a=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc).get("data",{})
    d=re.sub("<[^>]+>","",a.get("description") or "")
    out[acc]={"title":a.get("title"),"date":a.get("creation_date"),"culture":a.get("culture"),
              "tech":a.get("technique"),"dims":a.get("measurements"),"desc":d}
    print("=====",acc,"|",a.get("title"),"|",a.get("creation_date"),"|",a.get("culture"))
    print("  tech:",a.get("technique"),"| dims:",a.get("measurements"))
    print("  desc:",d[:800])
json.dump(out,open("/e/ai_project/yishu/reports/deepen5_c53.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)