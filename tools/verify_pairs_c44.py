# -*- coding: utf-8 -*-
"""Cycle44 核对：4 组疑似同作品（CMA↔V&A）的完整记录。"""
import json,subprocess,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
PAIRS=[("1940.986","O420241"),("1985.312","O423295"),("1985.327","O422853"),("1930.190","O424258")]
out={}
for acc,vid in PAIRS:
    a=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc).get("data",{})
    v=get("https://api.vam.ac.uk/v2/museumobject/%s"%vid).get("record",{})
    d=re.sub("<[^>]+>","",a.get("description") or "")
    rec={"cma":{"title":a.get("title"),"date":a.get("creation_date"),"technique":a.get("technique"),
                "dims":a.get("measurements"),"acc":acc,"desc":d,
                "creators":[x.get("description") for x in (a.get("creators") or [])]},
         "vam":{"title":[t.get("title") for t in (v.get("titles") or [])],
                "date":v.get("date"),"materials":[m.get("text") for m in (v.get("materials") or [])],
                "dims":[(x.get("dimension"),x.get("value"),x.get("unit")) for x in (v.get("dimensions") or [])][:2],
                "id":vid}}
    out[acc]=rec
    print("=====",acc,"/",vid)
    print("  CMA:",rec["cma"]["title"],"|",rec["cma"]["date"],"|",rec["cma"]["dims"],"|",rec["cma"]["creators"])
    print("   desc:",rec["cma"]["desc"][:480])
    print("  V&A:",rec["vam"]["title"],"|",rec["vam"]["date"],"|",rec["vam"]["dims"])
json.dump(out,open("/e/ai_project/yishu/reports/pairs_detail_c44.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)