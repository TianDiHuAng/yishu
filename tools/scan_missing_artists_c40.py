# -*- coding: utf-8 -*-
"""扫描：catalog 中缺失的重要艺术家，且 Cleveland 有 creators 传记正文（可作权威正文来源）。"""
import json,subprocess,urllib.parse,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__))) if False else None
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
ROOT="/e/ai_project/yishu"
import os
sys.path.insert(0,os.path.join(ROOT,"tools"))
from catalog import entries
have={e["id"] for e in entries()}
print("catalog entries:",len(have))
CAND=[("hokusai","Hokusai"),("hiroshige","Hiroshige"),("utamaro","Utamaro"),
      ("cezanne","Cézanne"),("manet","Manet"),("gauguin","Gauguin"),
      ("matisse","Matisse"),("picasso","Picasso"),("turner","Turner"),
      ("constable","Constable"),("klimt","Klimt"),("munch","Munch"),
      ("courbet","Courbet"),("ingres","Ingres"),("delacroix","Delacroix"),
      ("goya","Goya"),("velazquez","Velázquez"),("rembrandt","Rembrandt")]
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
for eid,q in CAND:
    if eid in have: print("%-12s EXISTS"%eid); continue
    d=get("https://openaccess-api.clevelandart.org/api/artworks/?q=%s&limit=3&has_image=0"%urllib.parse.quote(q))
    best=None
    for a in (d or {}).get("data",[]):
        for c in (a.get("creators") or []):
            bio=c.get("biography") or ""
            if len(bio)>(len(best[1]) if best else 0): best=(c.get("description"),bio,a.get("accession_number"),a.get("title"))
    if best: print("%-12s MISSING | creator=%s | bio=%d | via %s"%(
        eid,best[0],len(best[1]),best[2]))
    else: print("%-12s MISSING | no creator bio found"%eid)