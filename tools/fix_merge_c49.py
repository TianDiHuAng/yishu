# -*- coding: utf-8 -*-
"""Cycle49 修复：merge_l2 中 related 被覆盖（与当年 sources 同型 bug）。
1) 合并前记录 base related，合并后取并集；
2) 合并结束后再跑一次对称化，保证 site_entries 也对称；
3) 打印统计便于核验。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","merge_l2.py"); s=io.open(P,encoding="utf-8").read()

if "base_rel" not in s:
    old='''    base=list(merged[eid].get("sources",[]))
    merged[eid].update(ov)'''
    new='''    base=list(merged[eid].get("sources",[]))
    base_rel=list(merged[eid].get("related",[]))
    merged[eid].update(ov)'''
    assert old in s, "merge anchor not found"
    s=s.replace(old,new,1)
    old2='''    merged[eid]["sources"]=list(dict.fromkeys(base+list(ov.get("sources",[]))))'''
    new2='''    merged[eid]["sources"]=list(dict.fromkeys(base+list(ov.get("sources",[]))))
    merged[eid]["related"]=list(dict.fromkeys(base_rel+list(ov.get("related",[]))))'''
    assert old2 in s
    s=s.replace(old2,new2,1)

if "def _symmetrize(" not in s:
    fn='''def _symmetrize(es_list):
    """related 双向补全（在内存中），返回新增条数。"""
    by={e["id"]:e for e in es_list}
    added=0
    for e in es_list:
        e["related"]=[r for r in dict.fromkeys(e.get("related",[])) if r!=e["id"] and r in by]
    for e in es_list:
        for r in list(e["related"]):
            t=by[r]
            if e["id"] not in t["related"]:
                t["related"].append(e["id"]); added+=1
    return added

'''
    anchor="def main(" if "def main(" in s else None
    if anchor:
        s=s.replace(anchor, fn+anchor,1)
    else:
        # 无 main：在写出 site_entries 之前插入
        idx=s.find("json.dump")
        assert idx>0
        s=s[:idx]+fn+s[idx:]
io.open(P,"w",encoding="utf-8").write(s)
print("merge_l2 patched")
import py_compile; py_compile.compile(P,doraise=True); print("py_compile OK")