# -*- coding: utf-8 -*-
"""Cycle43 探测：变音折叠后的标题比对（unidecode 替代：unicodedata 归一化），
在 CMA 亚洲候选与 V&A 藏品间找更多「同作品双机构」配对。仅探测，不写库。"""
import json,subprocess,urllib.parse,re,unicodedata,os
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ROOT="/e/ai_project/yishu"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
def fold(t):
    t=unicodedata.normalize("NFKD",str(t or ""))
    t="".join(c for c in t if not unicodedata.combining(c))
    t=re.sub(r"\(.*?\)","",t).lower()
    t=re.sub(r"[^a-z0-9 ]"," ",t)
    return [w for w in t.split() if len(w)>3]
def sim(a,b):
    A,B=set(fold(a)),set(fold(b))
    if not A or not B: return 0.0
    return len(A&B)/len(A|B)
cands={}
for q in ["japanese print","chinese painting","india sculpture","islamic art","japanese lacquer","korean","persian"]:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=12&has_image=0"%urllib.parse.quote(q))
    for a in (d or {}).get("data",[]):
        if len(a.get("description") or "")<200: continue
        cands[a.get("accession_number")]={"title":a.get("title"),"date":a.get("creation_date"),
            "culture":a.get("culture"),"type":a.get("type")}
print("候选:",len(cands))
pairs=[]
for acc,c in cands.items():
    if not c["title"]: continue
    va=get("https://api.vam.ac.uk/v2/objects/search?q=%s&page_size=6"%urllib.parse.quote(str(c["title"])[:70]))
    best=None
    for r in (va or {}).get("records",[]):
        s=sim(c["title"],r.get("_primaryTitle"))
        if s>=0.6 and (best is None or s>best[0]): best=(s,r)
    if best:
        s,r=best
        pairs.append({"cma_acc":acc,"cma_title":c["title"],"cma_date":c["date"],
                      "vam_id":r.get("systemNumber"),"vam_title":r.get("_primaryTitle"),
                      "vam_date":r.get("_primaryDate"),"sim":round(s,2)})
print("疑似配对:",len(pairs))
for p in sorted(pairs,key=lambda x:-x["sim"]): print("  %.2f %-9s %-40s %-12s || %-8s %-38s %s"%(p["sim"],p["cma_acc"],str(p["cma_title"])[:40],str(p["cma_date"])[:12],p["vam_id"],str(p["vam_title"])[:38],str(p["vam_date"])[:12]))
os.makedirs(ROOT+"/reports",exist_ok=True)
json.dump(pairs,open(ROOT+"/reports/pairs_c43.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)