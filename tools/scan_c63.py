# -*- coding: utf-8 -*-
"""Cycle63 探测：北美原住民（CMA 是否有可写件）+ 非洲余量。"""
import json,subprocess,urllib.parse,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ROOT="/e/ai_project/yishu"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
Q={"北美":["navajo","hopi","pueblo","tlingit","haida","inuit","plains indian","iroquois","mississippian","native american"],
   "非洲余":["ethiopian","kongo","asante","yoruba","benin","fang","luba","zulu"]}
out={}
for grp,qs in Q.items():
    rows=[]
    for q in qs:
        d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=8&has_image=0"%urllib.parse.quote(q))
        for a in (d or {}).get("data",[]):
            cul=str(a.get("culture") or "")
            if grp=="北美" and not re.search("North America|United States|Canada|Alaska|Navajo|Hopi|Pueblo|Tlingit|Haida|Inuit|Plains|Iroquois|Mississippian",cul,re.I): continue
            desc=re.sub("<[^>]+>","",a.get("description") or "")
            if len(desc)<250: continue
            rows.append({"acc":a.get("accession_number"),"title":a.get("title"),"date":a.get("creation_date"),
                         "culture":cul,"len":len(desc)})
    seen=set(); u=[]
    for r in rows:
        if r["acc"] in seen: continue
        seen.add(r["acc"]); u.append(r)
    out[grp]=u
    print("==",grp,len(u))
    for r in u[:10]:
        print("   %-10s %-44s %-12s %-40s %d"%(r["acc"],str(r["title"])[:44],str(r["date"])[:12],str(r["culture"])[:40],r["len"]))
json.dump(out,open(ROOT+"/reports/scan_c63.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)