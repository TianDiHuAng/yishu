# -*- coding: utf-8 -*-
"""Cycle60：units.html 增加 h2 分组（修复标题跳级，同时改善导航）。
分组：西方艺术史 / 中国艺术 / 其他地区艺术 / 西方音乐史 / 中国音乐 / 导读与术语 / 作品档案。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py"); s=io.open(P,encoding="utf-8").read()
old='''    s.append("<div class='cards'>")
    for uid,uname in units.items():
        g=dom.get(uid,[])
        if not g: continue
        l3=sum(1 for e in g if e.get("level")=="L3")
        core=sum(1 for e in g if e["tier"]=="核心")
        s.append("<article class='card'><div class='meta'>%d 条 · 核心 %d · L3 %d</div>"
                 "<h3><a href='units/%s.html'>%s</a></h3><p>%s</p></article>"%(
                 len(g),core,l3,esc(uid),esc(uname),
                 esc("、".join(e["title"] for e in g[:4])+("…" if len(g)>4 else ""))))
    s.append("</div></div>"+FOOT)'''
new='''    def _group(uid):
        if uid.startswith("art-china"): return "中国艺术"
        if uid in ("art-asia","art-africa","art-americas","art-oceania","art-islamic"): return "其他地区艺术"
        if uid=="music-china": return "中国音乐"
        if uid.startswith("music-"): return "西方音乐史"
        if uid=="work-archives": return "作品档案"
        if uid in ("overview-guide","comparative","glossary-tools"): return "导读、比较与术语"
        return "西方艺术史"
    ORDER=["西方艺术史","中国艺术","其他地区艺术","西方音乐史","中国音乐","作品档案","导读、比较与术语"]
    buckets=defaultdict(list)
    for uid,uname in units.items():
        if not dom.get(uid): continue
        buckets[_group(uid)].append((uid,uname))
    for grp in ORDER:
        items=buckets.get(grp,[])
        if not items: continue
        s.append("<h2 class='unit-group'>%s<span class='eyebrow'>%d 单元</span></h2>"%(esc(grp),len(items)))
        s.append("<div class='cards'>")
        for uid,uname in items:
            g=dom[uid]
            l3=sum(1 for e in g if e.get("level")=="L3")
            core=sum(1 for e in g if e["tier"]=="核心")
            s.append("<article class='card'><div class='meta'>%d 条 · 核心 %d · L3 %d</div>"
                     "<h3><a href='units/%s.html'>%s</a></h3><p>%s</p></article>"%(
                     len(g),core,l3,esc(uid),esc(uname),
                     esc("、".join(e["title"] for e in g[:4])+("…" if len(g)>4 else ""))))
        s.append("</div>")
    s.append("</div>"+FOOT)'''
assert old in s, "units index block not found"
s=s.replace(old,new)
# 组标题样式
old2=".cards{"
if ".unit-group{" not in s:
    s=s.replace(".cards{",".unit-group{display:flex;align-items:baseline;gap:12px;margin:34px 0 12px;border-bottom:1px solid var(--line);padding-bottom:6px}\n.cards{",1)
io.open(P,"w",encoding="utf-8").write(s)
print("units index grouped")
import py_compile; py_compile.compile(P,doraise=True); print("compiled")