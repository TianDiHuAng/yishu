# -*- coding: utf-8 -*-
"""Cycle2 B4缺口：核验比较/导读类条目所需的新来源。"""
import json,os,re,ssl,time,urllib.request
from concurrent.futures import ThreadPoolExecutor,as_completed
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); D=os.path.join(ROOT,"data")
ctx=ssl.create_default_context()
CAND=[
 ("enc-impressionist-music","Impressionist music","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Impressionist_music","权威百科","Impressionist music"),
 ("enc-art-history","Art history","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Art_history","权威百科","Art history"),
 ("enc-musicology","Musicology","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Musicology","权威百科","Musicology"),
 ("enc-art-criticism","Art criticism","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Art_criticism","权威百科","Art criticism"),
 ("enc-modern-contemporary","Modern art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Modern_art","权威百科","Modern art"),
 ("enc-postmodern","Postmodern art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Postmodern_art","权威百科","Postmodern"),
 ("enc-baroque-art","Baroque art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Baroque_art","权威百科","Baroque"),
 ("enc-romantic-art","Romantic art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Romantic_art","权威百科","Romantic"),
]
def verify(it):
 sid,t,a,y,u,typ,kw=it
 for i in range(3):
  try:
   r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"})
   h=urllib.request.urlopen(r,timeout=30,context=ctx).read(600000).decode("utf-8","ignore")
   m=re.search(r"<title[^>]*>(.*?)</title>",h,re.I|re.S)
   tt=re.sub(r"<[^>]+>","",m.group(1)) if m else ""
   return sid,kw.lower() in (tt+" "+h[:200000]).lower(),"HTTP200 <title>=%s"%tt[:50]
  except Exception as e:
   last=e; time.sleep(1.3)
 return sid,False,"ERR %s"%str(last)[:50]
p=os.path.join(D,"sources.json"); data=json.load(open(p,encoding="utf-8")); exist={s["id"] for s in data["sources"]}
res={}
with ThreadPoolExecutor(max_workers=5) as ex:
 fs={ex.submit(verify,it):it[0] for it in CAND}
 for f in as_completed(fs):
  sid,ok,n=f.result(); res[sid]=(ok,n); print(sid,"OK" if ok else "FAIL",n[:60])
added=[]
for it in CAND:
 sid,t,a,y,u,typ,kw=it; ok,n=res[sid]
 if ok and sid not in exist:
  data["sources"].append({"id":sid,"title":t,"author":a,"year":y,"url":u,"type":typ,"verified":True,"verified_note":n}); added.append(sid)
json.dump(data,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("added:",added)
