# -*- coding: utf-8 -*-
"""Cycle38（收尾打磨）：
1) sources.html 顶部增加「隔离来源」说明（若 data/sources_quarantine.json 存在）；
2) status.html 的「来源构成」段补一句不变式说明（R18：库内必全 verified、隔离区不得引用）。
"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py"); s=io.open(P,encoding="utf-8").read()

# 1) sources 页
old='''    s=[head("来源库")]
    s.append("<div class='wrap'><h1>来源库</h1><p class='eyebrow'>%d 条 · 已核验 %d 条</p>"%(
        len(SOURCES),sum(1 for x in SOURCES if x["verified"])))'''
new='''    s=[head("来源库")]
    s.append("<div class='wrap'><h1>来源库</h1><p class='eyebrow'>%d 条 · 全部已核验</p>"%len(SOURCES))
    _q=None
    try:
        import json as _j
        _q=_j.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)),"..","data","sources_quarantine.json"),encoding="utf-8"))
    except Exception: pass
    if _q and _q.get("sources"):
        s.append("<p class='pending'>隔离来源 %d 条：这些来源经尝试但当前无法核验（页面 404 / 反爬壳页 / 限流 / 403），"
                 "已移出本库并**禁止被任何条目引用**（check.py R18 强制）。原因与记录见 "
                 "data/sources_quarantine.json，来源通道恢复后可重新核验。</p>"%len(_q["sources"]))'''
assert old in s, "sources page anchor missing"
s=s.replace(old,new)

# 2) status 页
old2='''    s.append("<p>身份锚点仅用于确认“条目所指的实体”，<b>不作为事实依据</b>；见 <a href='entities.html'>实体对照</a>。</p>")'''
new2='''    s.append("<p>身份锚点仅用于确认「条目所指的实体」，<b>不作为事实依据</b>；见 <a href='entities.html'>实体对照</a>。</p>")
    s.append("<p>来源库受 <b>R18 不变式</b>约束：库内必须全部 verified；不可核验者移入隔离区且不得被引用。</p>")'''
assert old2 in s, "status page anchor missing"
s=s.replace(old2,new2)
io.open(P,"w",encoding="utf-8").write(s)
print("sources/status pages updated")