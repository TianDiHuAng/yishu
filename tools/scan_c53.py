# -*- coding: utf-8 -*-
"""Cycle53 探测：纳斯卡、朝鲜朝（白瓷/粉青）、泰国/越南陶瓷。"""
import json,subprocess,urllib.parse,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ROOT="/e/ai_project/yishu"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
Q={"纳斯卡":["nazca","nasca","paracas pottery"],
   "朝鲜朝":["joseon","chosen white porcelain","buncheong","korean porcelain"],
   "泰国越南":["sukhothai","sawankhalok","vietnamese ceramic","champa","ban chiang"]}
out={}
for grp,qs in Q.items():
    rows=[]
    for q in qs:
        d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=6&has_image=0"%urllib.parse.quote(q))
        for a in (d or {}).get("data",[]):
            desc=re.sub("<[^>]+>","",a.get("description") or "")
            if len(desc)<250: continue
            rows.append({"acc":a.get("accession_number"),"title":a.get("title"),"date":a.get("creation_date"),
                         "culture":a.get("culture"),"len":len(desc)})
    seen=set(); u=[]
    for r in rows:
        if r["acc"] in seen: continue
        seen.add(r["acc"]); u.append(r)
    out[grp]=u
    print("==",grp,len(u))
    for r in u[:8]:
        print("   %-10s %-44s %-12s %-34s %d"%(r["acc"],str(r["title"])[:44],str(r["date"])[:12],str(r["culture"])[:34],r["len"]))
json.dump(out,open(ROOT+"/reports/scan_c53.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)