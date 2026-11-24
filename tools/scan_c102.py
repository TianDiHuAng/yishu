# -*- coding: utf-8 -*-
"""Cycle102：探测当代艺术（战后/抽象表现/波普/观念）。"""
import json,os,subprocess,urllib.parse,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
Q=["abstract expressionism","pop art","color field painting","contemporary sculpture","minimalism art","conceptual art","postwar painting","op art"]
rows=[]
for q in Q:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=8&has_image=0"%urllib.parse.quote(q))
    for a in (d or {}).get("data",[]):
        cul=str(a.get("culture") or ""); dt=str(a.get("creation_date") or "")
        # 只要 20 世纪中后
        yr=re.findall(r"\d{4}",dt)
        if not yr: continue
        if max(int(y) for y in yr) < 1940: continue
        desc=re.sub("<[^>]+>","",a.get("description") or "")
        if len(desc)<280: continue
        rows.append({"acc":a.get("accession_number"),"title":a.get("title"),"date":dt,
                     "culture":cul,"len":len(desc)})
seen=set(); uniq=[]
for r in rows:
    if r["acc"] in seen: continue
    seen.add(r["acc"]); uniq.append(r)
print("候选 %d"%len(uniq))
for r in uniq[:18]:
    print("%-10s %-46s %-14s %-38s %d"%(r["acc"],str(r["title"])[:46],str(r["date"])[:14],str(r["culture"])[:38],r["len"]))
json.dump(uniq,open(os.path.join(ROOT,"reports","contemp_c102.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)