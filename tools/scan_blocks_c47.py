# -*- coding: utf-8 -*-
"""Cycle47 探测：CMA 中非洲 / 前哥伦布美洲 / 大洋洲藏品的可写候选（说明>250字符）。"""
import json,subprocess,urllib.parse,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ROOT="/e/ai_project/yishu"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
Q={"非洲":["africa","benin","yoruba","kongo","kuba","akan","ethiopia"],
   "美洲":["maya","aztec","pre-columbian","andean","moche","nazca","inca","mississippian"],
   "大洋洲":["oceania","polynesia","melanesia","papua","hawaii","maori"]}
out={}
for grp,qs in Q.items():
    rows=[]
    for q in qs:
        d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=6&has_image=0"%urllib.parse.quote(q))
        for a in (d or {}).get("data",[]):
            desc=re.sub("<[^>]+>","",a.get("description") or "")
            if len(desc)<250: continue
            rows.append({"acc":a.get("accession_number"),"title":a.get("title"),"date":a.get("creation_date"),
                         "culture":a.get("culture"),"type":a.get("type"),"len":len(desc)})
    seen=set(); uniq=[]
    for r in rows:
        if r["acc"] in seen: continue
        seen.add(r["acc"]); uniq.append(r)
    out[grp]=uniq
    print("==",grp,len(uniq))
    for r in uniq[:10]:
        print("   %-10s %-40s %-14s %-34s %d"%(r["acc"],str(r["title"])[:40],str(r["date"])[:14],str(r["culture"])[:34],r["len"]))
json.dump(out,open(ROOT+"/reports/global_blocks_c47.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)