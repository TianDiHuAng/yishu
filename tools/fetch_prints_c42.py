# -*- coding: utf-8 -*-
"""取 3 组双机构作品的完整记录（CMA + V&A），并写入 reports/prints_c42.json。"""
import json,subprocess,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
def flat(v):
    if v is None: return ""
    if isinstance(v,list): return " | ".join(flat(x) for x in v)
    if isinstance(v,dict): return str(v.get("description") or v.get("text") or v)
    return str(v).replace("\n"," ")
out={}
for acc,vid in [("1930.189","O129067"),("1948.306","O410702"),("1921.318","O420904")]:
    c=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc).get("data",{})
    v=get("https://api.vam.ac.uk/v2/museumobject/%s"%vid).get("record",{})
    out[acc]={
      "cma":{"title":c.get("title"),"date":c.get("creation_date"),"technique":c.get("technique"),
             "measurements":c.get("measurements"),"culture":c.get("culture"),"accession":acc,
             "credit":c.get("creditline"),"desc":re.sub("<[^>]+>","",c.get("description") or ""),
             "creators":[x.get("description") for x in (c.get("creators") or [])]},
      "vam":{"id":vid,"title":[t.get("title") for t in (v.get("titles") or [])][:2],
             "date":v.get("date"),"materials":[m.get("text") for m in (v.get("materials") or [])],
             "dims":[(d.get("dimension"),d.get("value"),d.get("unit")) for d in (v.get("dimensions") or [])][:3],
             "type":v.get("objectType")}}
    print("=====",acc,"/",vid)
    print("  CMA:",out[acc]["cma"]["title"],"|",out[acc]["cma"]["date"],"|",out[acc]["cma"]["creators"])
    print("   desc:",out[acc]["cma"]["desc"][:520])
    print("  V&A:",out[acc]["vam"]["title"],"|",out[acc]["vam"]["date"],"|",out[acc]["vam"]["materials"],out[acc]["vam"]["dims"])
json.dump(out,open("/e/ai_project/yishu/reports/prints_c42.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)