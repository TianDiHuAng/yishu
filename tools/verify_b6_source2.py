# -*- coding: utf-8 -*-
import json,os,re,ssl,time,urllib.request
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__))); D=os.path.join(ROOT,"data")
ctx=ssl.create_default_context()
CAND=[("enc-zeng-hou-yi-bells","Marquis Yi of Zeng bells","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Marquis_Yi_of_Zeng_bells","权威百科","Zeng")]
def verify(it):
 sid,t,a,y,u,typ,kw=it
 for i in range(3):
  try:
   r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"})
   h=urllib.request.urlopen(r,timeout=30,context=ctx).read(600000).decode("utf-8","ignore")
   m=re.search(r"<title[^>]*>(.*?)</title>",h,re.I|re.S); tt=re.sub(r"<[^>]+>","",m.group(1)) if m else ""
   return sid,kw.lower() in (tt+" "+h[:200000]).lower(),"HTTP200 <title>=%s"%tt[:50]
  except Exception as e:
   last=e; time.sleep(1.3)
 return sid,False,"ERR %s"%str(last)[:50]
p=os.path.join(D,"sources.json"); data=json.load(open(p,encoding="utf-8")); exist={s["id"] for s in data["sources"]}
sid,t,a,y,u,typ,kw=CAND[0]; sid,ok,n=verify((sid,t,a,y,u,typ,kw)); print(sid,"OK" if ok else "FAIL",n)
if ok and sid not in exist:
 data["sources"].append({"id":sid,"title":t,"author":a,"year":y,"url":u,"type":typ,"verified":True,"verified_note":n})
 json.dump(data,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2); print("added")
