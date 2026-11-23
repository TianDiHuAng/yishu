# -*- coding: utf-8 -*-
"""取 4 件作品的 creators 权威记录（姓名/生卒/传记），判断双源可行性（修复 list 字段）。"""
import json,subprocess
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
def flat(v):
    if v is None: return ""
    if isinstance(v,list): return " | ".join(flat(x) for x in v)
    return str(v).replace("\n"," ")
for acc in ["1918.328","1916.1043","1947.209","1933.220"]:
    d=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc)
    a=(d or {}).get("data") or {}
    print("======",acc,a.get("title"))
    for c in (a.get("creators") or []):
        bio=flat(c.get("biography"))
        print("  creator:",c.get("description"),"| role",c.get("role"),"| id",c.get("id"),"| bio_len",len(bio))
        if bio: print("    bio:",bio[:300])
    print("  provenance:",flat(a.get("provenance"))[:200])
    print("  inscriptions:",flat(a.get("inscriptions"))[:150])
    print("  cite:",flat(a.get("cite"))[:120])
    print("  series/desc_in: ",flat(a.get("digital_description"))[:80] if a.get("digital_description") else "-")