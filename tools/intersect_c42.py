# -*- coding: utf-8 -*-
"""系统比对：CMA 候选标题 ↔ V&A 藏品标题（规范化后相等/高度重叠 + 年代一致）→ 找同作品双机构对。"""
import json,subprocess,urllib.parse,re,os
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ROOT="/e/ai_project/yishu"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
def norm(t):
    t=re.sub(r"\(.*?\)","",str(t or "")).lower()
    t=re.sub(r"[^a-z0-9 ]"," ",t)
    return " ".join(w for w in t.split() if len(w)>2)
QUERIES=["japanese print","chinese painting","india sculpture","islamic art","japanese lacquer","korean"]
cands={}
for q in QUERIES:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=10&has_image=0"%urllib.parse.quote(q))
    for a in (d or {}).get("data",[]):
        if len(a.get("description") or "")<200: continue
        cands[a.get("accession_number")]={"title":a.get("title"),"date":a.get("creation_date"),
            "culture":a.get("culture"),"desc":re.sub("<[^>]+>","",a.get("description") or "")}
print("候选:",len(cands))
pairs=[]
for acc,c in cands.items():
    q=c["title"]
    if not q: continue
    va=get("https://api.vam.ac.uk/v2/objects/search?q=%s&page_size=5"%urllib.parse.quote(str(q)[:80]))
    for r in (va or {}).get("records",[]):
        vt=r.get("_primaryTitle") or ""
        if norm(vt)==norm(q) and norm(vt):
            pairs.append({"cma_acc":acc,"cma_title":q,"cma_date":c["date"],
                          "vam_id":r.get("systemNumber"),"vam_title":vt,"vam_date":r.get("_primaryDate"),
                          "vam_type":r.get("objectType")})
            break
print("同作品双机构对:",len(pairs))
for p in pairs: print("  ",p["cma_acc"],"|",p["cma_title"][:44],"|",p["cma_date"],"||",p["vam_id"],p["vam_date"])
os.makedirs(ROOT+"/reports",exist_ok=True)
json.dump({"candidates":cands,"pairs":pairs},open(ROOT+"/reports/asia_c42.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)