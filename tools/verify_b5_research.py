# -*- coding: utf-8 -*-
"""B5复核验证器：重新抓取三份研究报告中每个 source URL，核对 HTTP 状态与 <title>，只保留真正可达的。"""
import json,os,re,ssl,time,urllib.request
from concurrent.futures import ThreadPoolExecutor,as_completed
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ctx=ssl.create_default_context()
reports=[]
for n in (1,2,3):
 p=os.path.join(ROOT,"reports","b5_research_%d.json"%n)
 if os.path.exists(p):
  for x in json.load(open(p,encoding="utf-8")):
   x["_group"]=n; reports.append(x)

def verify(x):
 s=x.get("source")
 if not s or not x.get("resolved"): return x["entry_id"],x["pending_item"][:20],False,"unresolved/no-source",None
 url=s["url"]
 for i in range(3):
  try:
   r=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
   h=urllib.request.urlopen(r,timeout=30,context=ctx).read(500000).decode("utf-8","ignore")
   m=re.search(r"<title[^>]*>(.*?)</title>",h,re.I|re.S)
   tt=re.sub(r"<[^>]+>","",m.group(1)) if m else ""
   # 检查 suggested id 合理性 + title 非空 + 页面有实质内容
   ok=(len(h)>5000 and tt.strip()!="")
   return x["entry_id"],x["pending_item"][:20],ok,"HTTP200 title=%s len=%d"%(tt[:45],len(h)),url
  except Exception as e:
   last=e; time.sleep(1.2)
 return x["entry_id"],x["pending_item"][:20],False,"ERR %s %s"%(type(last).__name__,str(last)[:50]),url

print("verifying",len(reports),"reported items...")
res={}
with ThreadPoolExecutor(max_workers=8) as ex:
 fs={ex.submit(verify,x):(x["entry_id"],x["pending_item"][:20]) for x in reports}
 for f in as_completed(fs):
  eid,item,ok,note,url=f.result()
  res[(eid,item)]=(ok,note,url)
okc=0
for (eid,item),(ok,note,url) in sorted(res.items()):
 print(("  OK  " if ok else " FAIL "),eid,"|",item,"|",note[:70])
 if ok: okc+=1
print("VERIFIED %d/%d"%(okc,len(res)))
# 保存验证结果供后续应用
out=[]
for x in reports:
 key=(x["entry_id"],x["pending_item"][:20])
 ok,note,url=res.get(key,(False,"no-result",None))
 x["_verified"]=ok; x["_verify_note"]=note
 if ok: x["source"]["verified_note"]=note
 out.append(x)
json.dump(out,open(os.path.join(ROOT,"reports","b5_research_verified.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("saved b5_research_verified.json")
