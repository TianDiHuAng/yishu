# -*- coding: utf-8 -*-
"""Cycle12（本地）：条目页加「同单元前后条目」导航（按时间线键排序），
提升可达性；不改动任何语义断言。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py")
s=io.open(P,encoding="utf-8").read()

# 复用 _band/时间键：新增一个通用排序键函数（模块级）
anchor="def build_entry(e,entries):"
assert anchor in s
helper='''def _era_key(e):
    import re
    m=re.search(r"(\\d{1,5})",e.get("when",""))
    if not m: return (2,0)
    v=int(m.group(1))
    return (0,-v) if "前" in e.get("when","")[:m.end()+2] else (0,v)

def build_entry(e,entries):'''
s=s.replace(anchor,helper,1)

# 在“被以下条目引用”之前插入前后导航
old="    # 反向引用（谁引用了本条目）"
nav='''    # 同单元前后条目（按年代先后）
    sib=sorted([x for x in entries if x["unit"]==e["unit"]],key=_era_key)
    idx=[x["id"] for x in sib].index(e["id"]) if e["id"] in [x["id"] for x in sib] else -1
    if idx>=0 and len(sib)>1:
        prev=sib[idx-1] if idx>0 else None
        nxt=sib[idx+1] if idx<len(sib)-1 else None
        s.append("<div class='section-block'><h2>同单元前后条目</h2><ul class='rel-list'>")
        if prev: s.append("<li>← <a href='%s.html'>%s</a></li>"%(esc(prev["id"]),esc(prev["title"])))
        s.append("<li><a href='%sunits/%s.html'>%s（单元总览）</a></li>"%(REL,esc(e["unit"]),esc(UNITS.get(e["unit"],e["unit"]))))
        if nxt: s.append("<li><a href='%s.html'>%s</a> →</li>"%(esc(nxt["id"]),esc(nxt["title"])))
        s.append("</ul></div>")
'''+old
assert old in s
s=s.replace(old,nav,1)
io.open(P,"w",encoding="utf-8").write(s)
print("gen_site.py: sibling prev/next nav added")