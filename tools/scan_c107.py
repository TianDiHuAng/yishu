# -*- coding: utf-8 -*-
"""Cycle107：V&A 检索（韩国绘画/佛教、日本漆器、伊斯兰釉陶）。"""
import json,os,subprocess,urllib.parse
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","20","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try:return json.loads(p.stdout)
    except Exception:return None
Q=["korean painting","korean buddhist sculpture","japanese lacquer","japanese inro","islamic mina'i bowl","mamluk glass","ottoman tile iznik","indian miniature painting"]
rows=[]
for q in Q:
    d=get("https://api.vam.ac.uk/v2/objects/search?q=%s&page_size=6"%urllib.parse.quote(q))
    for r in (d or {}).get("records",[]):
        rows.append({"sys":r.get("systemNumber"),"title":r.get("_primaryTitle"),"date":r.get("_primaryDate"),
                     "type":r.get("objectType"),"q":q})
seen=set();uniq=[]
for r in rows:
    if r["sys"] in seen: continue
    seen.add(r["sys"]);uniq.append(r)
print("候选",len(uniq))
for r in uniq[:30]:
    print("%-8s %-48s %-16s %-20s %s"%(r["sys"],str(r["title"])[:48],str(r["date"])[:16],str(r["type"])[:20],r["q"]))
json.dump(uniq,open(os.path.join(ROOT,"reports","vam_c107.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)