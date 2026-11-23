# -*- coding: utf-8 -*-
"""取 4 件「填补覆盖缺口」候选的完整 CMA 记录（印度克什米尔佛像／马图拉栏楯／明陈洪绶册页／元河村渔乐）。"""
import json,subprocess,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ACC=["1966.30","1977.34","1979.27","1978.66"]
out={}
for acc in ACC:
    a=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc).get("data",{})
    d=re.sub("<[^>]+>","",a.get("description") or "")
    out[acc]={"title":a.get("title"),"date":a.get("creation_date"),"technique":a.get("technique"),
              "measurements":a.get("measurements"),"culture":a.get("culture"),"accession":acc,
              "credit":a.get("creditline"),"creators":[x.get("description") for x in (a.get("creators") or [])],
              "desc":d}
    print("=====",acc,a.get("title"),"|",a.get("creation_date"),"|",a.get("culture"),"|",a.get("technique"))
    print("   dims:",a.get("measurements"))
    print("   desc:",d[:600])
json.dump(out,open("/e/ai_project/yishu/reports/gap_works_c43.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)