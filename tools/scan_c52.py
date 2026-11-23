# -*- coding: utf-8 -*-
"""Cycle52 探测：约鲁巴/伊费、阿散蒂、纳斯卡/奇穆、朝鲜（高丽/朝鲜朝）陶瓷。"""
import json,subprocess,urllib.parse,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ROOT="/e/ai_project/yishu"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
Q={"约鲁巴/伊费":["yoruba","ife","osun","gelede"],
   "阿散蒂":["asante","akan","goldweight","kente"],
   "纳斯卡/奇穆":["nazca","chimu","paracas","peru textile"],
   "朝鲜":["goryeo celadon","joseon","korean buncheong","korean white porcelain"]}
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
    for r in u[:6]:
        print("   %-10s %-44s %-12s %-32s %d"%(r["acc"],str(r["title"])[:44],str(r["date"])[:12],str(r["culture"])[:32],r["len"]))
json.dump(out,open(ROOT+"/reports/deepen2_c52.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)