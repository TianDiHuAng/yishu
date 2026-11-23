# -*- coding: utf-8 -*-
"""在 Cleveland 开放 API 中检索候选作品（看是否有足够长的策展描述），
以及 Met 中同域作品（结构化事实）。仅检索，不写库。"""
import json,subprocess,urllib.parse
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
QUE=["van gogh","rodin","degas","chinese painting","ming dynasty","hokusai","turner","constable"]
for q in QUE:
    u="https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=6&has_image=0"%urllib.parse.quote(q)
    d=get(u)
    if not d: print("==",q,"FAIL"); continue
    print("==",q,"n=",len(d.get("data",[])))
    for a in d.get("data",[])[:4]:
        desc=(a.get("description") or "")
        print("   %-42s | %s | %s | desc=%d"%(str(a.get("title"))[:42],str(a.get("creation_date"))[:12],
              str(a.get("accession_number")),len(desc)))
        if len(desc)>150: print("      ",desc[:200].replace("\n"," "))