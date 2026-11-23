# -*- coding: utf-8 -*-
"""取 4 件候选作品的完整 CMA 记录 + Europeana 检索结果，供撰写条目用。"""
import json,subprocess,urllib.parse,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ACC=["1918.328","1916.1043","1947.209","1933.220"]
for acc in ACC:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc)
    if not d or "data" not in d: print("==",acc,"FAIL"); continue
    a=d["data"]
    print("======",acc,"======")
    for k in ["title","creation_date","creation_date_earliest","creation_date_latest","technique","department",
              "culture","measurements","accession_number","url","creditline","type","artists","provenance"]:
        v=a.get(k)
        if k=="artists" and v: print("  artists:",[(x.get("description"),x.get("birth_year"),x.get("death_year")) for x in v])
        elif k=="provenance": print("  provenance len:",len(v or ""))
        else: print("  %-22s"%k, str(v)[:150])
    desc=re.sub(r"<[^>]+>","",a.get("description") or "")
    print("  DESCRIPTION:",desc[:900])
    # Europeana
    q=urllib.parse.quote('"%s"'%a.get("title"))
    e=get("https://api.europeana.eu/record/v2/search.json?wskey=api2demo&query=%s&rows=3&profile=rich"%q)
    items=(e or {}).get("items",[])
    print("  EUROPEANA hits:",len(items))
    for it in items[:2]:
        print("    -",str(it.get("title"))[:70],"| provider",it.get("provider"),"| dataProvider",it.get("dataProvider"))