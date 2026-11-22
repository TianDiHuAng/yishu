# -*- coding: utf-8 -*-
"""体检F 来源文本重合度：抽5条，抓来源页，比对正文8字中文n-gram重合率（防大段搬用）。"""
import json,os,re,ssl,urllib.request,time,random
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
ctx=ssl.create_default_context()
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
byid={e["id"]:e for e in es}
random.seed(20261127)
ids=random.sample([e["id"] for e in es if e.get("sections")],5)
def fetch(u):
 for i in range(2):
  try:
   r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"})
   return urllib.request.urlopen(r,timeout=25,context=ctx).read(900000).decode("utf-8","ignore")
  except Exception as e:
   last=e; time.sleep(1)
 return ""
def cn_ngrams(s,n=8):
 s=re.sub(r"[^\u4e00-\u9fff]","",s)
 return {s[i:i+n] for i in range(len(s)-n+1)}
out=[]
for eid in ids:
 e=byid[eid]
 body="".join(e["sections"][k] for k in ["时代背景","风格特征","技法或形式分析"])
 grams=cn_ngrams(body)
 hits=0; total=0
 for sid in e["sources"][:3]:
  s=json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))
  src=next((x for x in s["sources"] if x["id"]==sid),None)
  if not src: continue
  h=fetch(src["url"])
  # 英文页无中文n-gram，重合自然为0；中文页才比较
  ch=cn_ngrams(h)
  if ch:
   total+=len(grams); hits+=len(grams&ch)
 out.append([eid,len(grams),hits,total,round(hits/total,3) if total else 0.0])
 print(eid,"ngrams",len(grams),"overlap",hits,"/",total)
json.dump(out,open(os.path.join(ROOT,"reports","overlap_c5.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("max overlap ratio:",max(x[4] for x in out) if out else 0)
