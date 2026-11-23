# -*- coding: utf-8 -*-
"""Cycle54 收尾（工程部分）：①状态页公开预备来源数量；②不变式盘点接入 audit_all 成为第 10 步。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# ① 状态页
P=os.path.join(ROOT,"tools","gen_site.py"); s=io.open(P,encoding="utf-8").read()
old='''    s.append("<p>来源库受 <b>R18 不变式</b>约束：库内必须全部 verified；不可核验者移入隔离区且不得被引用。</p>")'''
new='''    s.append("<p>来源库受 <b>R18 不变式</b>约束：库内必须全部 verified；不可核验者移入隔离区且不得被引用。</p>")
    _res=0
    try:
        import json as _j2
        _res=len(_j2.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","data","sources_reserve.json"),encoding="utf-8")).get("sources",[]))
    except Exception: pass
    if _res:
        s.append("<p>另有 <b>%d 条预备来源</b>（已核验但当前未被任何条目引用），见 data/sources_reserve.json；"
                 "它们不计入上列来源总数，以免虚增。</p>"%_res)'''
assert old in s
s=s.replace(old,new)
io.open(P,"w",encoding="utf-8").write(s)
print("status page: reserve note added")

# ② audit_all 第 10 步
A=os.path.join(ROOT,"tools","audit_all.py"); a=io.open(A,encoding="utf-8").read()
if "invariants_c54.py" not in a:
    old2=' ("overlay_guard.py（覆盖层不得改基础字段）","tools/overlay_guard.py"),'
    assert old2 in a
    a=a.replace(old2,old2+'\n ("invariants_c54.py（不变式盘点：死重/孤儿/L3/单元页）","tools/invariants_c54.py"),')
    io.open(A,"w",encoding="utf-8").write(a); print("audit_all: invariants step added")
import py_compile; py_compile.compile(P,doraise=True); py_compile.compile(A,doraise=True); print("compiled")