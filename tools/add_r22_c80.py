# -*- coding: utf-8 -*-
"""Cycle80：新增 check.py R22 — 来源 id 与条目 id 必须匹配 ^[a-z0-9-]+$。
（本轮之前「点号 id」已复发三次：cma-1921.914、cma-1998.102、cma-1972.9。）"""
import io,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","check.py"); s=io.open(P,encoding="utf-8").read()
if "R22" not in s:
    anchor="    # R21 when 表述规范"
    code='''    # R22 id 格式：条目 id 与来源 id 只允许小写字母、数字与连字符（禁点号/大写/下划线）
    _idre=re.compile(r"^[a-z0-9-]+$")
    for e in ENTRIES:
        if not _idre.match(e["id"]):
            err("R22",e["id"],"条目 id 含非法字符")
        for sid in e.get("sources",[]):
            if not _idre.match(sid):
                err("R22",e["id"],"来源 id 含非法字符:%s"%sid)
    for x in S:
        if not _idre.match(x["id"]):
            err("R22",x["id"],"来源库 id 含非法字符")

'''
    assert anchor in s
    s=s.replace(anchor, code+anchor, 1)
    io.open(P,"w",encoding="utf-8").write(s)
    print("R22 added")
import py_compile; py_compile.compile(P,doraise=True); print("compiled")