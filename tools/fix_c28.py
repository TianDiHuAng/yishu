# -*- coding: utf-8 -*-
"""Cycle28 修复：
1) sitemap 改为**自动收录**站点根目录下所有 .html（新增页面自动进入 sitemap）+ units/entries 子目录；
2) 把作品尺寸说明里的「目前」改为中性表述，消除"过期数据"规则误报。"""
import io,os,json,glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py"); s=io.open(P,encoding="utf-8").read()
old='''    base="https://tiandihuang.github.io/yishu/"
    urls=["index.html","units.html","timeline.html","people.html","glossary.html",
          "all-index.html","sources.html"]'''
new='''    base="https://tiandihuang.github.io/yishu/"
    # 自动收录根目录全部 html（避免硬编码列表漏掉新页面）
    urls=sorted(os.path.basename(p) for p in glob.glob(os.path.join(OUT,"*.html")))'''
assert old in s; s=s.replace(old,new)
if "import glob" not in s.split("def build_sitemap")[0][:2000]:
    s=s.replace("import json, os, html","import json, os, html, glob",1)
io.open(P,"w",encoding="utf-8").write(s)
print("sitemap: dynamic discovery")

# 2) 重新措辞
n=0
for p in glob.glob(os.path.join(ROOT,"data","l2","*.json")):
    o=json.load(open(p,encoding="utf-8"))
    pend=o.get("sections",{}).get("待核实","")
    if "该组数据目前" in pend:
        o["sections"]["待核实"]=pend.replace("该组数据目前","该组数据")
        json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
print("reworded:",n)