# -*- coding: utf-8 -*-
"""Cycle45 探测：扩大 CMA 检索面 + 降低重合阈值，找更多同作品配对（输出候选供人工确认）。"""
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
    t=re.sub(r"\(.*?\)"," ",t).lower(); t=re.sub(r"[^a-z0-9 ]"," ",t)
    return [w for w in t.split() if len(w)>2]
STOP={"from","view","views","the","and","series","one","hundred","famous","edo","print","with","after","at","in","of","no","for","near"}
def key(t): return {w for w in fold(t) if w not in STOP}
SERIES=["Fugaku sanjurokkei","Meisho Edo hyakkei","Tokaido gojusan tsugi","Hyakunin isshu","Omi hakkei",
        "Yedo","Kyoto","Nihonbashi","Shinagawa","Kameido","Oji","Fuji","Edo hyakkei"]
va={}
for q in SERIES:
    d=get("https://api.vam.ac.uk/v2/objects/search?q=%s&page_size=50"%urllib.parse.quote(q))
    for r in (d or {}).get("records",[]):
        t=r.get("_primaryTitle")
        if t: va[r.get("systemNumber")]={"title":t,"date":r.get("_primaryDate")}
print("V&A 池:",len(va))
cma={}
for q in ["hiroshige","hokusai","ukiyo-e","Edo","Fuji","Tokai","woodblock"]:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=20&has_image=0"%urllib.parse.quote(q))
    for a in (d or {}).get("data",[]):
        if a.get("title"): cma[a.get("accession_number")]={"title":a["title"],"date":a.get("creation_date")}
print("CMA 池:",len(cma))
pairs=[]
for acc,c in cma.items():
    K=key(c["title"])
    if len(K)<2: continue
    for vid,v in va.items():
        KV=key(v["title"])
        if not KV: continue
        inter=K&KV
        if len(inter)>=2:
            sc=len(inter)/len(K|KV)
            if sc>=0.25:
                # 排除「系列名记录」：V&A 题名仅由系列词构成
                if KV<= {"fugaku","sanjurokkei","meisho","hyakkei","tokaido","gojusan","tsugi","hyakunin","isshu","omi","hakkei","thirty","six","views","mount","fuji","stations","hundred","poems"}:
                    continue
                pairs.append({"cma_acc":acc,"cma_title":c["title"],"cma_date":c["date"],
                              "vam_id":vid,"vam_title":v["title"],"vam_date":v["date"],"score":round(sc,2),"shared":sorted(inter)})
pairs.sort(key=lambda x:-x["score"])
print("候选:",len(pairs))
for p in pairs[:14]: print("  %.2f %-9s %-40s %-12s || %-8s %-42s %s"%(p["score"],p["cma_acc"],str(p["cma_title"])[:40],str(p["cma_date"])[:11],p["vam_id"],str(p["vam_title"])[:42],str(p["vam_date"])[:12]))
os.makedirs(ROOT+"/reports",exist_ok=True)
json.dump(pairs,open(ROOT+"/reports/pairs_c45.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)