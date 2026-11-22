# -*- coding: utf-8 -*-
"""Cycle35 修正：把来源构成徽标真正插入 entry-head（上次锚点没对上）。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py")
s=io.open(P,encoding="utf-8").read()
old='''        "<span class='tag'>%s</span><span class='tag'>%s</span></div></div>"%(
        esc(e["title"]),depth_badge(e),tier_badge(e),esc(e["kind"]),esc(e["era"]),esc(e["region"])))'''
new='''        "<span class='tag'>%s</span><span class='tag'>%s</span>%s</div></div>"%(
        esc(e["title"]),depth_badge(e),tier_badge(e),esc(e["kind"]),esc(e["era"]),esc(e["region"]),
        "<span class='tag'>%d 来源：内容 %d · 结构化 %d · 锚点 %d</span>"%(
            sum(source_profile(e)[k] for k in ("content","fact","anchor")),
            source_profile(e)["content"],source_profile(e)["fact"],source_profile(e)["anchor"])))'''
assert old in s, "entry-head args not found"
s=s.replace(old,new)
io.open(P,"w",encoding="utf-8").write(s)
print("badge inserted into entry-head")
chk=io.open(P,encoding="utf-8").read()
print("has '%d 来源：内容':", "%d 来源：内容" in chk)