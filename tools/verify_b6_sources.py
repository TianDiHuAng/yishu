# -*- coding: utf-8 -*-
"""Cycle2 B6：核验两条最可靠的近期动态来源，验证通过加入 sources.json。"""
import json,os,re,ssl,time,urllib.request
from concurrent.futures import ThreadPoolExecutor,as_completed
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); D=os.path.join(ROOT,"data")
ctx=ssl.create_default_context()
CAND=[
 ("news-xiamen-wuwangdu","厦门大学武王墩楚墓礼乐考古研究进展","厦门大学新闻网","2025","https://news.xmu.edu.cn/info/1003/513182.htm","官方机构","武王墩"),
 ("news-shell-trumpet","Sounding the 6,000-year-old shell trumpets of Catalonia","Phys.org","2025","https://phys.org/news/2025-12-year-shell-trumpets-catalonia.html","学术媒体","shell trumpets"),
]
def verify(it):
 sid,t,a,y,u,typ,kw=it
 for i in range(3):
  try:
   r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"})
   h=urllib.request.urlopen(r,timeout=30,context=ctx).read(600000).decode("utf-8","ignore")
   m=re.search(r"<title[^>]*>(.*?)</title>",h,re.I|re.S)
   tt=re.sub(r"<[^>]+>","",m.group(1)) if m else ""
   return sid,kw.lower() in (tt+" "+h[:200000]).lower(),"HTTP200 <title>=%s"%tt[:60]
  except Exception as e:
   last=e; time.sleep(1.3)
 return sid,False,"ERR %s"%str(last)[:60]
p=os.path.join(D,"sources.json"); data=json.load(open(p,encoding="utf-8")); exist={s["id"] for s in data["sources"]}
res={}
with ThreadPoolExecutor(max_workers=2) as ex:
 fs={ex.submit(verify,it):it[0] for it in CAND}
 for f in as_completed(fs):
  sid,ok,n=f.result(); res[sid]=(ok,n); print(sid,"OK" if ok else "FAIL",n[:70])
added=[]
for it in CAND:
 sid,t,a,y,u,typ,kw=it; ok,n=res[sid]
 if ok and sid not in exist:
  data["sources"].append({"id":sid,"title":t,"author":a,"year":y,"url":u,"type":typ,"verified":True,"verified_note":n}); added.append(sid)
json.dump(data,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("added:",added)
