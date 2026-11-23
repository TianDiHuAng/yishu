# -*- coding: utf-8 -*-
"""Cycle59 探测：埃塞俄比亚（十字/圣像/织物/Lakai）、刚果、阿散蒂余量。"""
import json,subprocess,urllib.parse,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ROOT="/e/ai_project/yishu"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
Q={"埃塞":["ethiopian","lakai","ethiopia textile","ethiopian icon","ethiopia cross","gondar"],
   "刚果":["kongo","nkisi","dibu","minkisi","loango"],
   "阿散蒂":["asante","akan","adinkra","kente cloth"]}
out={}
for grp,qs in Q.items():
    rows=[]
    for q in qs:
        d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=8&has_image=0"%urllib.parse.quote(q))
        for a in (d or {}).get("data",[]):
            cul=str(a.get("culture") or "")
            if grp=="埃塞" and not re.search("Ethiopia",cul): continue
            if grp=="刚果" and not re.search("Kongo|Congo|Loango|Yombe|Vili",cul): continue
            if grp=="阿散蒂" and not re.search("Asante|Akan",cul): continue
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
    for r in u[:8]:
        print("   %-10s %-44s %-12s %-36s %d"%(r["acc"],str(r["title"])[:44],str(r["date"])[:12],str(r["culture"])[:36],r["len"]))
json.dump(out,open(ROOT+"/reports/scan_c59.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)