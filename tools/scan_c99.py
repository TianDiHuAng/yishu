# -*- coding: utf-8 -*-
"""Cycle99：探测东南亚艺术（高棉/印尼/泰国/缅甸/越南）。"""
import json,os,subprocess,urllib.parse,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
Q=["khmer sculpture","angkor","indonesian art","thai buddha","burmese buddha","vietnamese ceramic","champa sculpture","southeast asian art"]
rows=[]
for q in Q:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=8&has_image=0"%urllib.parse.quote(q))
    for a in (d or {}).get("data",[]):
        cul=str(a.get("culture") or "")
        if not re.search("Cambodia|Khmer|Thailand|Thai|Indonesia|Java|Burma|Myanmar|Vietnam|Champa|Southeast|Siam|Laos",cul,re.I): continue
        desc=re.sub("<[^>]+>","",a.get("description") or "")
        if len(desc)<280: continue
        rows.append({"acc":a.get("accession_number"),"title":a.get("title"),"date":a.get("creation_date"),
                     "culture":cul,"len":len(desc)})
seen=set(); uniq=[]
for r in rows:
    if r["acc"] in seen: continue
    seen.add(r["acc"]); uniq.append(r)
print("候选 %d"%len(uniq))
for r in uniq[:18]:
    print("%-10s %-46s %-14s %-42s %d"%(r["acc"],str(r["title"])[:46],str(r["date"])[:14],str(r["culture"])[:42],r["len"]))
json.dump(uniq,open(os.path.join(ROOT,"reports","seasia_c99.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)