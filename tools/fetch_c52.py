# -*- coding: utf-8 -*-
"""Cycle52：取 5 件全文（约鲁巴 Gelede 面具、阿散蒂纪念头像、帕拉卡斯披巾、奇穆抬舆靠背、高丽青瓷盏）。"""
import json,subprocess,re
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
ACC=["1975.168","1990.22","1946.226","1952.233","2025.180"]
out={}
for acc in ACC:
    a=get("https://openaccess-api.clevelandart.org/api/artworks/%s"%acc).get("data",{})
    d=re.sub("<[^>]+>","",a.get("description") or "")
    out[acc]={"title":a.get("title"),"date":a.get("creation_date"),"culture":a.get("culture"),
              "tech":a.get("technique"),"dims":a.get("measurements"),"desc":d}
    print("=====",acc,"|",a.get("title"),"|",a.get("creation_date"),"|",a.get("culture"))
    print("  tech:",a.get("technique"),"| dims:",a.get("measurements"))
    print("  desc:",d[:750])
json.dump(out,open("/e/ai_project/yishu/reports/deepen5_c52.json","w",encoding="utf-8"),ensure_ascii=False,indent=1)