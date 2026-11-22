# -*- coding: utf-8 -*-
"""Cycle6 B4作品档案缺口：核验代表作来源（≥2/条）。"""
import json,os,re,ssl,time,urllib.request
from concurrent.futures import ThreadPoolExecutor,as_completed
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); D=os.path.join(ROOT,"data")
ctx=ssl.create_default_context()
CAND=[
 ("enc-starry-night","The Starry Night","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/The_Starry_Night","权威百科","Starry Night"),
 ("enc-moma","Museum of Modern Art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Museum_of_Modern_Art","权威百科","Museum of Modern Art"),
 ("enc-birth-venus","The Birth of Venus","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/The_Birth_of_Venus","权威百科","Birth of Venus"),
 ("enc-uffizi","Uffizi","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Uffizi","权威百科","Uffizi"),
 ("enc-sistine-ceiling","Sistine Chapel ceiling","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Sistine_Chapel_ceiling","权威百科","Sistine Chapel ceiling"),
 ("enc-guernica","Guernica (Picasso)","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Guernica_(Picasso)","权威百科","Guernica"),
 ("enc-rite-spring","The Rite of Spring","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/The_Rite_of_Spring","权威百科","Rite of Spring"),
 ("enc-night-watch","The Night Watch","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/The_Night_Watch","权威百科","Night Watch"),
 ("enc-pearl-earring","Girl with a Pearl Earring","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Girl_with_a_Pearl_Earring","权威百科","Pearl Earring"),
 ("enc-the-scream","The Scream","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/The_Scream","权威百科","The Scream"),
]
def verify(it):
 sid,t,a,y,u,typ,kw=it
 for i in range(3):
  try:
   r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"})
   h=urllib.request.urlopen(r,timeout=30,context=ctx).read(700000).decode("utf-8","ignore")
   m=re.search(r"<title[^>]*>(.*?)</title>",h,re.I|re.S); tt=re.sub(r"<[^>]+>","",m.group(1)) if m else ""
   return sid,kw.lower() in (tt+" "+h[:250000]).lower(),"HTTP200 <title>=%s"%tt[:50]
  except Exception as e:
   last=e; time.sleep(1.3)
 return sid,False,"ERR %s"%str(last)[:50]
p=os.path.join(D,"sources.json"); data=json.load(open(p,encoding="utf-8")); exist={s["id"] for s in data["sources"]}
res={}
with ThreadPoolExecutor(max_workers=6) as ex:
 fs={ex.submit(verify,it):it[0] for it in CAND}
 for f in as_completed(fs):
  sid,ok,n=f.result(); res[sid]=(ok,n); print(sid,"OK" if ok else "FAIL",n[:55])
added=[]
for it in CAND:
 sid,t,a,y,u,typ,kw=it; ok,n=res[sid]
 if ok and sid not in exist:
  data["sources"].append({"id":sid,"title":t,"author":a,"year":y,"url":u,"type":typ,"verified":True,"verified_note":n}); added.append(sid)
json.dump(data,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("added:",added)
