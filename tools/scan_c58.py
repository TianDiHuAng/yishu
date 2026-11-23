# -*- coding: utf-8 -*-
"""Cycle58 探测：泰国素可泰/宋加洛、越南、埃塞俄比亚（换用更具体的检索词）。"""
import json,subprocess,urllib.parse,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ROOT="/e/ai_project/yishu"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
Q={"泰国":["sukhothai","sawankhalok","si satchanalai","thai sawankhalok jar","celadon thailand"],
   "越南":["vietnamese jar","le dynasty ceramic","chu dau","bat trang","vietnamese blue and white"],
   "埃塞俄比亚":["ethiopian cross","ethiopian manuscript","ethiopian icon","lakai","tellem","nubian",
                 "ethiopia painting"]}
out={}
for grp,qs in Q.items():
    rows=[]
    for q in qs:
        d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=6&has_image=0"%urllib.parse.quote(q))
        for a in (d or {}).get("data",[]):
            desc=re.sub("<[^>]+>","",a.get("description") or "")
            cul=str(a.get("culture") or "")
            if grp=="泰国" and not re.search("Thai|Sukhothai|Sawankhalok|Si Satchanalai",cul): continue
            if grp=="越南" and not re.search("Vietnam|Viet",cul): continue
            if grp=="埃塞俄比亚" and not re.search("Ethiopia",cul): continue
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
json.dump(out,open(ROOT+"/reports/scan_c58.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)