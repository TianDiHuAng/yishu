# -*- coding: utf-8 -*-
"""Cycle3 QC收尾：补 baroque-music 的 Bach/Vivaldi 来源；修正【已复核】标注中被截断的URL显示。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")
# 1) 新增 Vivaldi 来源
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8"))
if not any(s["id"]=="enc-vivaldi-four-seasons" for s in sd["sources"]):
 sd["sources"].append({"id":"enc-vivaldi-four-seasons","title":"The Four Seasons (Vivaldi)","author":"Wikipedia contributors",
   "year":"2026","url":"https://en.wikipedia.org/wiki/The_Four_Seasons_(Vivaldi)","type":"权威百科",
   "verified":True,"verified_note":"B5收尾HTTP200; <title>=The Four Seasons (Vivaldi); 含Four Seasons"})
 json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
# 2) baroque-music overlay 补来源
p=os.path.join(LD,"baroque-music.json"); o=json.load(open(p,encoding="utf-8"))
for sid in ("enc-bach","enc-vivaldi-four-seasons"):
 if sid not in o["sources"]: o["sources"].append(sid)
json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
# 3) 修正标注中被截断的URL：把 "【已复核】...（https://...[:48]）" 换成完整URL from sources.json
smap={s["id"]:s["url"] for s in sd["sources"]}
import re
fixed=0
for fp in os.listdir(LD):
 if not fp.endswith(".json"): continue
 fp=os.path.join(LD,fp); ov=json.load(open(fp,encoding="utf-8"))
 pend=ov.get("sections",{}).get("待核实","")
 if "【已复核】" not in pend: continue
 def repl(m):
  global fixed
  sid=m.group(1); full=smap.get(sid)
  if full and full!=m.group(2):
   fixed+=1; return "第二来源 %s（%s）"%(sid,full)
  return m.group(0)
 new=re.sub(r"第二来源 ([a-z0-9-]+)（(https?://[^）]*)）",repl,pend)
 ov["sections"]["待核实"]=new
 json.dump(ov,open(fp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("Vivaldi source added; baroque-music sources patched; truncated URLs fixed:",fixed)
