# -*- coding: utf-8 -*-
"""Cycle65：①修 5 处正文 URL 的 `wiki/QQ` 双 Q 打字错误；②修正审计正则（不再把括号 URL 截断）。"""
import io,json,os,glob,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
n=0
for p in glob.glob(os.path.join(ROOT,"data","l2","*.json")):
    o=json.load(open(p,encoding="utf-8"))
    ch=False
    for k,v in (o.get("sections") or {}).items():
        if isinstance(v,str) and "wiki/QQ" in v:
            o["sections"][k]=re.sub(r"wiki/QQ(\d+)", r"wiki/Q\1", v); ch=True
    if ch:
        json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
        print("fixed",o["id"])
print("overlays fixed:",n)

A=os.path.join(ROOT,"tools","enc_audit_c65.py"); s=io.open(A,encoding="utf-8").read()
old='    for u in set(re.findall(r"https?://[^\\s　，。）)]+",body)):'
new='    for u in set(re.findall(r"https?://[^\\s　，。）]+(?<![),])" ,body)):'
if old in s:
    s=s.replace(old,new); io.open(A,"w",encoding="utf-8").write(s); print("regex updated")
else:
    print("regex pattern not found (manual check needed)")
import py_compile
try: py_compile.compile(A,doraise=True); print("compiled")
except Exception as e: print("compile fail",str(e)[:120])