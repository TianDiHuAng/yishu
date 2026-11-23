# -*- coding: utf-8 -*-
"""寻找 CMA 与 V&A 同时收藏的同一作品（版画/铸件多印本），以构成双机构来源。"""
import json,subprocess,urllib.parse
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ARTISTS=["hokusai","hiroshige","utamaro","kuniyoshi","pissarro","whistler"]
for a in ARTISTS:
    cma=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=8&has_image=0"%urllib.parse.quote(a))
    ct=[(x.get("title"),x.get("creation_date"),x.get("accession_number")) for x in (cma or {}).get("data",[])]
    va=get("https://api.vam.ac.uk/v2/objects/search?q=%s&page_size=8"%urllib.parse.quote(a))
    vt=[(r.get("_primaryTitle"),r.get("_primaryDate"),r.get("systemNumber")) for r in (va or {}).get("records",[])]
    print("==",a)
    print("  CMA:",ct[:5])
    print("  V&A:",vt[:5])
    # 粗略交集（标题词重合）
    for t1,_,_ in ct:
        if not t1: continue
        w=set(str(t1).lower().replace("-"," ").split())
        for t2,_,_ in vt:
            if not t2: continue
            w2=set(str(t2).lower().replace("-"," ").split())
            common=w&w2-{"the","of","a","and","at","in","no"}
            if len([x for x in common if len(x)>3])>=2:
                print("   MATCH?",t1,"||",t2)