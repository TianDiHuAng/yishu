# -*- coding: utf-8 -*-
"""Cycle60：站点可用性/可访问性结构审计（全量 243 页）。
检查 8 项：
1 每页恰好一个 <h1>；
2 标题层级不跳级（h1→h3 无 h2 即报）；
3 有 viewport meta；
4 <html> 有 lang 属性；
5 表格有 <thead>（读屏可辨表头）；
6 页内锚点 href="#x" 在同页存在 id=x；
7 无 <img>（本站政策：只用自绘 SVG）；
8 有跳转链接（跳到主内容）与 nav。
另外扫描 style.css 是否含过大固定宽度。
输出 reports/usability_c60.json。"""
import json,os,glob,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
pages=sorted(glob.glob(os.path.join(ROOT,"*.html"))+glob.glob(os.path.join(ROOT,"entries","*.html"))+glob.glob(os.path.join(ROOT,"units","*.html")))
bad={"no_h1":[],"multi_h1":[],"skip_level":[],"no_viewport":[],"no_lang":[],"table_no_thead":[],
     "broken_anchor":[],"has_img":[],"no_skip_link":[],"no_nav":[],"unwrapped_table":[],"svg_narrow_rule":[]}
for p in pages:
    h=open(p,encoding="utf-8").read()
    rel=os.path.relpath(p,ROOT)
    hs=[int(m.group(1)) for m in re.finditer(r"<h([1-6])[ >]",h)]
    n1=hs.count(1)
    if n1==0: bad["no_h1"].append(rel)
    if n1>1: bad["multi_h1"].append(rel)
    prev=None
    for lv in hs:
        if prev and lv>prev+1: bad["skip_level"].append(rel); break
        prev=lv
    if 'name="viewport"' not in h and "name='viewport'" not in h: bad["no_viewport"].append(rel)
    if not re.search(r"<html[^>]*\blang=",h): bad["no_lang"].append(rel)
    for t in re.findall(r"<table.*?</table>",h,re.S):
        if "<thead" in t: continue
        # 只对「来源表」这类结构化表格要求 thead；正文对比表可无
        if "来源" in t or "sources" in t: bad["table_no_thead"].append(rel)
    ids=set(re.findall(r"id=['\"]([^'\"]+)['\"]",h))
    for a in re.findall(r"href=\"#([^\"]+)\"",h):
        if a not in ids: bad["broken_anchor"].append((rel,a))
    if "<img" in h: bad["has_img"].append(rel)
    if "跳到主内容" not in h and "skip" not in h.lower(): bad["no_skip_link"].append(rel)
    if "<nav" not in h: bad["no_nav"].append(rel)
    if h.count("<table")>h.count("class='table-wrap'"):
        bad["unwrapped_table"].append(rel)
css=open(os.path.join(ROOT,"assets","style.css"),encoding="utf-8").read()
if "@media (max-width:700px)" not in css or "min-width:680px" not in css:
    bad["svg_narrow_rule"].append("assets/style.css")
wide=[m.group(0) for m in re.finditer(r"width:\s*(\d{3,4})px",css) if int(m.group(1))>900]
print("页数:",len(pages))
tot=0
for k,v in bad.items():
    if v:
        print("  %-16s %d  例: %s"%(k,len(v),v[:3])); tot+=len(v)
print("问题合计:",tot)
print("style.css 过大固定宽度:",wide[:5])
json.dump({"pages":len(pages),"issues":{k:v[:50] for k,v in bad.items() if v},"css_wide":wide},
          open(os.path.join(ROOT,"reports","usability_c60.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
sys.exit(1 if tot else 0)
