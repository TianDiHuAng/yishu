# -*- coding: utf-8 -*-
"""Cycle44：按系列批量比对浮世绘（CMA ↔ V&A）。
思路：V&A 的浮世绘题名常以「英文题名 (日文罗马字)」并给系列名，故可用系列名检索，
再以折叠后的罗马字/关键词重合度 + 年代一致性判定「同作品」。仅探测，输出候选供人工确认。"""
import json,subprocess,urllib.parse,re,unicodedata,os
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ROOT="/e/ai_project/yishu"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","30","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
def fold(t):
    t=unicodedata.normalize("NFKD",str(t or ""))
    t="".join(c for c in t if not unicodedata.combining(c))
    t=re.sub(r"\(.*?\)"," ",t).lower()
    t=re.sub(r"[^a-z0-9 ]"," ",t)
    return [w for w in t.split() if len(w)>2]
STOP={"from","view","views","the","and","series","one","hundred","famous","edo","print","with","after"}
def key(t):
    return {w for w in fold(t) if w not in STOP}
SERIES=[("Fugaku sanjurokkei","36 Views"),("Meisho Edo hyakkei","100 Edo"),
        ("Tokaido gojusan tsugi","53 Stations"),("Hyakunin isshu","100 Poems"),
        ("Omi hakkei","8 Views Omi")]
va={}
for q,label in SERIES:
    d=get("https://api.vam.ac.uk/v2/objects/search?q=%s&page_size=50"%urllib.parse.quote(q))
    recs=d.get("records",[]) if d else []
    print("V&A series",label,"→",len(recs),"records")
    for r in recs:
        t=r.get("_primaryTitle") or ""
        if t: va[r.get("systemNumber")]={"title":t,"date":r.get("_primaryDate")}
# CMA 侧
cma={}
for q in ["hokusai","hiroshige","ukiyo-e print","Edo print","woodblock print japan"]:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=15&has_image=0"%urllib.parse.quote(q))
    for a in (d or {}).get("data",[]):
        if not a.get("title"): continue
        cma[a.get("accession_number")]={"title":a["title"],"date":a.get("creation_date"),
            "desc":a.get("description") or ""}
print("CMA 候选:",len(cma),"| V&A 池:",len(va))
pairs=[]
for acc,c in cma.items():
    K=key(c["title"])
    if len(K)<2: continue
    best=None
    for vid,v in va.items():
        KV=key(v["title"])
        if not KV: continue
        inter=K&KV
        if len(inter)>=2:
            score=len(inter)/len(K|KV)
            if best is None or score>best[0]: best=(score,vid,v,inter)
    if best and best[0]>=0.34:
        pairs.append({"cma_acc":acc,"cma_title":c["title"],"cma_date":c["date"],
                      "vam_id":best[1],"vam_title":best[2]["title"],"vam_date":best[2]["date"],
                      "score":round(best[0],2),"shared":sorted(best[3])})
print("候选配对:",len(pairs))
for p in sorted(pairs,key=lambda x:-x["score"]):
    print("  %.2f %-9s %-42s %-12s || %-8s %-44s %s"%(p["score"],p["cma_acc"],str(p["cma_title"])[:42],str(p["cma_date"])[:12],p["vam_id"],str(p["vam_title"])[:44],str(p["vam_date"])[:14]))
os.makedirs(ROOT+"/reports",exist_ok=True)
json.dump({"va_pool":va,"pairs":pairs},open(ROOT+"/reports/pairs_c44.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)