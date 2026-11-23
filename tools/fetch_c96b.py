# -*- coding: utf-8 -*-
"""Cycle96 修正：fetch Wahaika 短棍（1964.455）作为第4件。"""
import json,os,subprocess,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA="Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
def get(u):
    p=subprocess.run(["curl","-sSL","-m","25","-A",UA,u],capture_output=True,text=True,encoding="utf-8",errors="replace")
    try: return json.loads(p.stdout)
    except Exception: return None
a=get("https://openaccess-api.clevelandart.org/api/artworks/1964.455").get("data",{})
d=re.sub("<[^>]+>","",a.get("description") or "")
print("=====",a.get("accession_number"),"|",a.get("title"),"|",a.get("creation_date"),"|",a.get("culture"))
print("  tech:",a.get("technique"),"| dims:",a.get("measurements"))
print("  desc:",d[:1200])