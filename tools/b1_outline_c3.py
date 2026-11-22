# -*- coding: utf-8 -*-
"""B1 权威大纲再对照：抓取 Outline of music / Outline of art，提取章节标题，与 scope 比对找缺口。"""
import json,os,re,ssl,urllib.request,time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ctx=ssl.create_default_context()
def fetch(u):
 for i in range(3):
  try:
   r=urllib.request.Request(u,headers={"User-Agent":"Mozilla/5.0"})
   return urllib.request.urlopen(r,timeout=30,context=ctx).read(800000).decode("utf-8","ignore")
  except Exception as e:
   last=e; time.sleep(1.2)
 raise last
def headings(html):
 # 抓 <h2>/<h3> 标题（去标签）
 out=[]
 for m in re.finditer(r"<h[23][^>]*>(.*?)</h[23]>",html,re.I|re.S):
  t=re.sub(r"<[^>]+>","",m.group(1))
  t=re.sub(r"\[.*?\]","",t).strip()
  if t and len(t)<60: out.append(t)
 return out
res={}
for key,u in [("music","https://en.wikipedia.org/wiki/Outline_of_music"),("art","https://en.wikipedia.org/wiki/Outline_of_art")]:
 try:
  h=fetch(u); hs=headings(h)
  res[key]=hs
  print("===",key,len(hs),"headings ==")
  for x in hs[:35]: print("  -",x)
 except Exception as e: print(key,"FAIL",str(e)[:70])
json.dump(res,open(os.path.join(ROOT,"reports","b1_outlines_c3.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
