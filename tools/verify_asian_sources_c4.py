# -*- coding: utf-8 -*-
"""Cycle4 B1新增：南亚/东南亚/日本艺术（History of painting 权威大纲空白分支）来源核验。"""
import json,os,re,ssl,time,urllib.request
from concurrent.futures import ThreadPoolExecutor,as_completed
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); D=os.path.join(ROOT,"data")
ctx=ssl.create_default_context()
CAND=[
 ("enc-indian-art","Indian art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Indian_art","权威百科","Indian art"),
 ("enc-buddhist-art-india","Buddhist art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Buddhist_art","权威百科","Buddhist art"),
 ("enc-ajanta","Ajanta Caves","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Ajanta_Caves","权威百科","Ajanta"),
 ("enc-angkor","Angkor","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Angkor","权威百科","Angkor"),
 ("enc-khmer-art","Khmer art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Khmer_art","权威百科","Khmer"),
 ("enc-japanese-art","Japanese art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Japanese_art","权威百科","Japanese art"),
 ("enc-ukiyo-e","Ukiyo-e","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Ukiyo-e","权威百科","Ukiyo-e"),
 ("enc-zen-art","Zen painting","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Zen_painting","权威百科","Zen"),
 ("enc-history-painting","History of painting","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/History_of_painting","权威百科","South Asian"),
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
  sid,ok,n=f.result(); res[sid]=(ok,n); print(sid,"OK" if ok else "FAIL",n[:60])
added=[]
for it in CAND:
 sid,t,a,y,u,typ,kw=it; ok,n=res[sid]
 if ok and sid not in exist:
  data["sources"].append({"id":sid,"title":t,"author":a,"year":y,"url":u,"type":typ,"verified":True,"verified_note":n}); added.append(sid)
json.dump(data,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("added:",added)
