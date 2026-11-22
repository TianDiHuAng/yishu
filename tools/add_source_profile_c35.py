# -*- coding: utf-8 -*-
"""Cycle35：条目页新增「来源构成」徽标（内容来源 / 结构化事实 / 身份锚点 分别计数）。
读者可据此判断该条目的证据强度；不改变任何内容。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py"); s=io.open(P,encoding="utf-8").read()

fn='''def source_profile(e):
    """统计条目来源构成：content=内容来源, fact=结构化事实, anchor=身份锚点。"""
    n={"content":0,"fact":0,"anchor":0,"missing":0}
    for sid in e.get("sources",[]):
        s=SM.get(sid)
        if not s: n["missing"]+=1; continue
        t=str(s.get("type",""))
        if "身份锚点" in t: n["anchor"]+=1
        elif "结构化数据" in t: n["fact"]+=1
        else: n["content"]+=1
    return n

'''
if "def source_profile(" not in s:
    a="def build_entry(e,entries):"
    assert a in s
    s=s.replace(a, fn+a, 1)

old='''        esc(e["title"]),depth_badge(e),tier_badge(e),esc(e["kind"]),esc(e["era"]),esc(e["region"])))'''
new='''        esc(e["title"]),depth_badge(e),tier_badge(e),esc(e["kind"]),esc(e["era"]),esc(e["region"])))
    sp=source_profile(e)
    prof=" <span class='tag'>%d 来源：内容 %d · 结构化 %d · 锚点 %d</span>"%(
        sum(sp[k] for k in ("content","fact","anchor")), sp["content"], sp["fact"], sp["anchor"])
    s.append(prof+"</div>")'''
assert old in s, "entry tags anchor missing"
# 注意：原行以 ")</div></div>" 结束一次，改为先补充 profile 再闭合
s=s.replace(old+'''</div>''', new)
io.open(P,"w",encoding="utf-8").write(s)
print("source profile badge added")
chk=io.open(P,encoding="utf-8").read()
print("has source_profile:", "def source_profile(" in chk, "| used:", chk.count("source_profile(e)")>=1)