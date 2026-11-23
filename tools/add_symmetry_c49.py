# -*- coding: utf-8 -*-
"""Cycle49：在 build_scope.py 中加入 related 对称化（在内存完成，不触碰 catalog 文本）。
1) 建立 id 集合；
2) 丢弃指向不存在条目的 related（并打印）；
3) 双向补全：若 A→B 则 B→A；
4) 结果写入 data/entries.json，并输出补全条数。
这样 3 条单元导览的反向关联自动补上，也彻底避免「手改文本」类事故。"""
import io,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","build_scope.py"); s=io.open(P,encoding="utf-8").read()

FN='''def symmetrize(es):
    """related 双向补全 + 清理悬空引用（在内存中完成）。返回 (补全条数, 悬空列表)。"""
    ids={e["id"] for e in es}
    by={e["id"]:e for e in es}
    dangling=[]
    for e in es:
        keep=[]
        for r in e.get("related",[]):
            if r==e["id"]: continue
            if r in ids: keep.append(r)
            else: dangling.append((e["id"],r))
        e["related"]=list(dict.fromkeys(keep))
    added=0
    for e in es:
        for r in list(e["related"]):
            tgt=by[r]
            if e["id"] not in tgt["related"]:
                tgt["related"].append(e["id"]); added+=1
    return added,dangling

'''
if "def symmetrize(" not in s:
    anchor='es=entries()'
    assert anchor in s
    s=s.replace(anchor,'es=entries()\n'+FN+'_added,_dangling=symmetrize(es)\nprint("related 对称化：新增 %d 条；悬空引用 %d 条%s"%(_added,len(_dangling),(" → %s"%_dangling[:5]) if _dangling else ""))',1)
io.open(P,"w",encoding="utf-8").write(s)
print("build_scope: symmetrize step inserted")

import py_compile
py_compile.compile(P,doraise=True); print("py_compile OK")