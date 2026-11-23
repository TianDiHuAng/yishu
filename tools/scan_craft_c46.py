# -*- coding: utf-8 -*-
"""Cycle46 探测：CMA 中伊斯兰器物与中国青铜/玉器实例（要求策展说明较长）。"""
import json,subprocess,urllib.parse,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ROOT="/e/ai_project/yishu"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
Q=["islamic","iznik","minai","mosque lamp","tile mihrab","iran ceramic","ottoman",
   "chinese bronze","ritual vessel","jade cong","jade bi","shang dynasty bronze","han dynasty jade"]
rows=[]
for q in Q:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=8&has_image=0"%urllib.parse.quote(q))
    for a in (d or {}).get("data",[]):
        desc=re.sub("<[^>]+>","",a.get("description") or "")
        if len(desc)<250: continue
        rows.append({"acc":a.get("accession_number"),"title":a.get("title"),"date":a.get("creation_date"),
                     "culture":a.get("culture"),"type":a.get("type"),"tech":a.get("technique"),
                     "dims":a.get("measurements"),"len":len(desc)})
seen=set(); uniq=[]
for r in rows:
    if r["acc"] in seen: continue
    seen.add(r["acc"]); uniq.append(r)
print("候选:",len(uniq))
for r in uniq[:24]:
    print("%-10s %-40s %-12s %-28s %d"%(r["acc"],str(r["title"])[:40],str(r["date"])[:12],str(r["culture"])[:28],r["len"]))
json.dump(uniq,open(ROOT+"/reports/craft_c46.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)