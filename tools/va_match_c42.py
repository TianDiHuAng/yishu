# -*- coding: utf-8 -*-
"""为 4 个首选候选在 V&A 中按标题检索，判断能否构成双机构来源。"""
import json,subprocess,urllib.parse
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def va(q):
    u="https://api.vam.ac.uk/v2/objects/search?q=%s&page_size=4"%urllib.parse.quote(q)
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: d=json.loads(p.stdout)
    except Exception: return []
    return [(r.get("_primaryTitle"),r.get("_primaryDate"),r.get("systemNumber"),r.get("objectType")) for r in d.get("records",[])]
TESTS=[("South Wind Clear Sky","South Wind, Clear Sky"),
       ("Sudden Shower Ohashi","Sudden Shower over Shin-Ohashi"),
       ("Standing Buddha Kashmir","Standing Buddha"),
       ("River and Mountains Clear Autumn","River and Mountains"),
       ("Fisherman's Joy","Fisherman"),
       ("Paintings after Ancient Masters","Chen Hongshou")]
for q,label in TESTS:
    print("==",label,"| query:",q)
    for t in va(q)[:4]: print("    ",t)