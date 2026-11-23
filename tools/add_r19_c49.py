# -*- coding: utf-8 -*-
"""Cycle49：新增 check.py R19（关联对称性不变式）。
规则：每个条目的 related 中每一项都必须 (a) 存在于条目集合；(b) 反向指回本条目。
这样「单向关联」不可能悄悄回归——任何一次合并且漏掉反向，构建即失败。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","check.py"); s=io.open(P,encoding="utf-8").read()
if "R19" not in s:
    anchor="    # R18 来源库不变式"
    code='''    # R19 关联对称性：related 不得悬空，且必须双向
    byid={x["id"]:x for x in ENTRIES}
    for e in ENTRIES:
        for r in e.get("related",[]):
            t=byid.get(r)
            if t is None:
                err("R19",e["id"],"related 指向不存在的条目:%s"%r); continue
            if e["id"] not in t.get("related",[]):
                err("R19",e["id"],"单向关联（%s 未指回）"%r)

'''
    assert anchor in s
    s=s.replace(anchor, code+anchor, 1)
    io.open(P,"w",encoding="utf-8").write(s)
    print("R19 added")
import py_compile; py_compile.compile(P,doraise=True); print("py_compile OK")