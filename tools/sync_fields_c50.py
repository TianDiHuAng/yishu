# -*- coding: utf-8 -*-
"""Cycle50：消除「覆盖层静默改写 catalog」的字段漂移。
做法：把覆盖层的值**并入 catalog**（唯一字符串替换，count==1 才改），再从覆盖层**删除该基础字段**，
使 catalog 成为唯一真值，覆盖层只保留深度字段（level/sections/svg/needs_verification/pending_notes/sources/related）。
"""
import json,os,glob,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); P=os.path.join(ROOT,"tools","catalog.py")
aud=json.load(open(os.path.join(ROOT,"reports","overlay_field_audit_c50.json"),encoding="utf-8"))
mism=aud["mismatch"]
catalog=io.open(P,encoding="utf-8").read()
changed=[]; failed=[]; stripped=0
ov_cache={}
for m in mism:
    eid,f,old,new=m["id"],m["field"],m["catalog"],m["overlay"]
    if not isinstance(old,str) or not isinstance(new,str):
        failed.append((eid,f,"非字符串")); continue
    # 在 catalog 中定位唯一出现
    hit=False
    for q in (chr(34),chr(39)):
        old_tok=q+old+q
        if catalog.count(old_tok)==1:
            catalog=catalog.replace(old_tok,q+new+q); changed.append((eid,f)); hit=True; break
    if not hit:
        failed.append((eid,f,"找不到唯一匹配（两种引号均失败或出现多次）")); continue
    # 从覆盖层删除该字段
    op=os.path.join(D,"l2",eid+".json")
    if op not in ov_cache: ov_cache[op]=json.load(open(op,encoding="utf-8"))
    o=ov_cache[op]
    if f in o: del o[f]; stripped+=1
io.open(P,"w",encoding="utf-8").write(catalog)
for op,o in ov_cache.items():
    json.dump(o,open(op,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("并入 catalog:",len(changed),"| 覆盖层删除字段:",stripped,"| 失败:",len(failed))
for f in failed: print("  FAIL",f)
import py_compile; py_compile.compile(P,doraise=True); print("py_compile OK")