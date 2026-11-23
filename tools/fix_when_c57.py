# -*- coding: utf-8 -*-
"""Cycle57：①规范 6 条 when 的中文表述；②新增 check.py R21：when 不得含拉丁字母。
（本轮先试的"正文年份 vs when"启发式信噪比太差，弃用，理由记入 D061。）"""
import io,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","catalog.py"); s=io.open(P,encoding="utf-8").read()
FIX=[("'约1940s—1950s'","'约1940年代—1950年代'"),
     ("'约1950s—1970s'","'约1950年代—1970年代'"),
     ("'约1960s—1970s'","'约1960年代—1970年代'"),
     ("'约1960s—至今'","'约1960年代—至今'"),
     ("'early 1830s（系列作于1829—1833年）'","'1830年代初（系列作于1829—1833年）'"),
     ("'热释光测年 20—620 CE'","'热释光测年 公元20—620年'")]
n=0
for a,b in FIX:
    c=s.count(a)
    if c==1: s=s.replace(a,b); n+=1
    else: print("SKIP",a,"count",c)
io.open(P,"w",encoding="utf-8").write(s)
print("when normalized:",n)

C=os.path.join(ROOT,"tools","check.py"); cs=io.open(C,encoding="utf-8").read()
if "R21" not in cs:
    anchor="    # R19 关联对称性"
    code='''    # R21 when 表述规范：不得出现拉丁字母（本站统一中文表述，如 1940年代 / 公元620年）
    for e in ENTRIES:
        w=str(e.get("when","") or "")
        if re.search(r"[A-Za-z]",w):
            err("R21",e["id"],"when 含拉丁字母:%s"%w[:30])

'''
    assert anchor in cs
    cs=cs.replace(anchor, code+anchor, 1)
    if "import re" not in cs.split("\n\n")[0]:
        cs=cs.replace("import json,os,sys","import json,os,sys,re",1)
        if "import re" not in cs: cs="import re\n"+cs
    io.open(C,"w",encoding="utf-8").write(cs)
    print("R21 added")
import py_compile; py_compile.compile(P,doraise=True); py_compile.compile(C,doraise=True); print("compiled")