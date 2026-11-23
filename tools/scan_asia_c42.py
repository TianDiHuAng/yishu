# -*- coding: utf-8 -*-
"""扫描：CMA 亚洲/工艺类候选（description 较长），并在 V&A 中按标题查同作品或同系列。"""
import json,subprocess,urllib.parse
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
QUERIES=[("Japanese","japanese print"),("Chinese","chinese painting"),("India","india sculpture"),
         ("Islamic","islamic art"),("Korea","korean"),("Japan lacquer","japanese lacquer")]
seen=set(); rows=[]
for label,q in QUERIES:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=10&has_image=0"%urllib.parse.quote(q))
    for a in (d or {}).get("data",[]):
        desc=a.get("description") or ""
        if len(desc)<200: continue
        acc=a.get("accession_number")
        if acc in seen: continue
        seen.add(acc)
        rows.append({"acc":acc,"title":a.get("title"),"date":a.get("creation_date"),
                     "culture":a.get("culture"),"type":a.get("type"),"desc_len":len(desc),
                     "desc":desc[:400]})
print("候选:",len(rows))
for r in rows[:20]:
    print("%-9s %-44s %-14s %s | %d"%(r["acc"],str(r["title"])[:44],str(r["date"])[:14],str(r["culture"])[:30],r["desc_len"]))
json.dump(rows,open("/e/ai_project/yishu/reports/asia_candidates_c42.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)