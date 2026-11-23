# -*- coding: utf-8 -*-
"""Cycle69：探测非西方乐器（填 B2 音乐缺口）。"""
import json,os,subprocess,urllib.parse,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
Q=["drum africa","kora","mbira","balafon","gong southeast asia","gamelan","sitar","biwa","shamisen",
   "erhu","guqin","pipa instrument","koto","shakuhachi","harp africa","lute islamic","rebab"]
rows=[]
for q in Q:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=6&has_image=0"%urllib.parse.quote(q))
    for a in (d or {}).get("data",[]):
        t=str(a.get("title") or "").lower()
        cul=str(a.get("culture") or "")
        if not re.search("drum|kora|mbira|balafon|gong|gamelan|sitar|biwa|shamisen|erhu|qin|pipa|koto|shakuhachi|harp|lute|rebab|zither|flute|trumpet|bell",t): continue
        desc=re.sub("<[^>]+>","",a.get("description") or "")
        if len(desc)<250: continue
        rows.append({"acc":a.get("accession_number"),"title":a.get("title"),"date":a.get("creation_date"),
                     "culture":cul,"len":len(desc)})
seen=set(); uniq=[]
for r in rows:
    if r["acc"] in seen: continue
    seen.add(r["acc"]); uniq.append(r)
print("乐器候选 %d"%len(uniq))
for r in uniq[:20]:
    print("%-10s %-44s %-12s %-40s %d"%(r["acc"],str(r["title"])[:44],str(r["date"])[:12],str(r["culture"])[:40],r["len"]))
json.dump(uniq,open(os.path.join(ROOT,"reports","instr_c69.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)