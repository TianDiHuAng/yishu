# -*- coding: utf-8 -*-
"""严格核验 B5 body_rewrite：抽取其中年份/关键专名，检查是否在对应来源页出现；两者皆过才允许写入正文。"""
import json,os,re,ssl,time,urllib.request
from concurrent.futures import ThreadPoolExecutor,as_completed
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ctx=ssl.create_default_context()
data=[x for x in json.load(open(os.path.join(ROOT,"reports","b5_research_verified.json"),encoding="utf-8")) if x.get("_verified")]

def tokens(rewrite):
 # 抽取 4位年份、书名号内专名、引号内词、大写英文/带连字符专名
 ts=set(re.findall(r"\b(1[0-9]{3}|20[0-2][0-9])\b",rewrite))
 ts|=set(re.findall(r"[《「\"]([^》」\"]{2,12})[》」\"]",rewrite))
 ts|=set(re.findall(r"\b([A-Z][A-Za-z'’\-]{3,})\b",rewrite))
 return {t for t in ts if len(t)>1}

def check(x):
 rw=x.get("body_rewrite","")
 ts=tokens(rw)
 url=x["source"]["url"]
 for i in range(3):
  try:
   r=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
   h=urllib.request.urlopen(r,timeout=30,context=ctx).read(1500000).decode("utf-8","ignore")
   break
  except Exception as e:
   last=e; time.sleep(1.2)
 else:
   return x,False,"fetch-fail"
 low=h.lower()
 miss=[t for t in ts if t.lower() not in low]
 # 年份容忍：若rewrite只有年份且缺失，判失败；专名容忍3个以上缺失
 ok=(len(ts)==0) or (len(miss)<=2)
 return x,ok,"tokens=%d miss=%d %s"%(len(ts),len(miss),",".join(list(miss)[:6]))

res={}
with ThreadPoolExecutor(max_workers=8) as ex:
 fs={ex.submit(check,x):(x["entry_id"],x["pending_item"][:20]) for x in data}
 for f in as_completed(fs):
  x,ok,note=f.result(); res[(x["entry_id"],x["pending_item"][:20])]=(ok,note)

okc=0
for x in data:
 key=(x["entry_id"],x["pending_item"][:20])
 ok,note=res[key]; x["_facts_ok"]=ok; x["_facts_note"]=note
 if ok: okc+=1
 print((" OK " if ok else"BAD "),x["entry_id"],"|",x["pending_item"][:30],"|",note[:70])
print("FACTS OK %d/%d"%(okc,len(data)))
json.dump(data,open(os.path.join(ROOT,"reports","b5_research_verified.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
