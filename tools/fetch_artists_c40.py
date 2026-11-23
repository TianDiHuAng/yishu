# -*- coding: utf-8 -*-
"""取 5 位画家的 CMA 传记全文 + V&A 藏品命中（判断能否构成双机构来源）。"""
import json,subprocess,urllib.parse,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
TARGET={"manet":"Manet","turner":"Turner","constable":"Constable","courbet":"Courbet","ingres":"Ingres"}
out={}
for eid,q in TARGET.items():
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=4&has_image=0"%urllib.parse.quote(q))
    rec=None
    for a in (d or {}).get("data",[]):
        for c in (a.get("creators") or []):
            if q.lower() in (c.get("description") or "").lower() and (c.get("biography") or ""):
                rec=(c.get("description"),re.sub("<[^>]+>","",c["biography"]),a.get("accession_number"),a.get("title"),a)
                break
        if rec: break
    va=get("https://api.vam.ac.uk/v2/objects/search?q=%s&page_size=4"%urllib.parse.quote(q))
    vhits=[(r.get("_primaryTitle"),r.get("_primaryDate"),r.get("systemNumber")) for r in (va or {}).get("records",[])[:3]]
    out[eid]={"cma":rec,"va":vhits}
    print("=====",eid)
    if rec:
        print("  CMA:",rec[0],"| via",rec[2],rec[3])
        print("  BIO:",rec[1][:700])
    print("  V&A:",vhits)
json.dump(out,open("/e/ai_project/yishu/reports/artists_c40.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)