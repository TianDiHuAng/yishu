# -*- coding: utf-8 -*-
"""Cycle61（修正）：表格包裹后处理 + CSS，插在 main 的 generated 打印之前。"""
import io,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py"); s=io.open(P,encoding="utf-8").read()

HELPER='''def postprocess_tables():
    """后处理：为所有页面的表格包一层可横向滚动容器（幂等）。"""
    n=0
    files=glob.glob(os.path.join(OUT,"*.html"))+glob.glob(os.path.join(OUT,"entries","*.html"))+glob.glob(os.path.join(OUT,"units","*.html"))
    for p in files:
        h=io.open(p,encoding="utf-8").read()
        if "<table" not in h or "class='table-wrap'" in h: continue
        new=re.sub(r"<table(.*?)</table>", lambda m: "<div class='table-wrap'><table%s</table></div>"%m.group(1), h, flags=re.S)
        if new!=h:
            io.open(p,"w",encoding="utf-8").write(new); n+=1
    return n

'''
if "def postprocess_tables(" not in s:
    a="def build_status(entries):"
    assert a in s, "build_status anchor missing"
    s=s.replace(a, HELPER+a, 1)

anchor='    print("generated index.html + %d entry pages + indexes + sitemap.xml"%n)'
assert anchor in s, "generated print anchor missing"
if "postprocess_tables()" not in s:
    s=s.replace(anchor, '    _wrapped=postprocess_tables()\n    print("表格容器包裹：%d 页"%_wrapped)\n'+anchor, 1)

if "import io" not in s.split("\n")[0:6][0] and ", io" not in s.split("\n")[0:6][0]:
    pass
s=s.replace("import json, os, html, glob, re","import json, os, html, glob, re, io",1)

if ".table-wrap{" not in s:
    s=s.replace("table{width:100%;border-collapse:collapse;font-size:.92rem}",
      "table{width:100%;border-collapse:collapse;font-size:.92rem}\n"
      ".table-wrap{overflow-x:auto;-webkit-overflow-scrolling:touch;margin:12px 0}\n"
      ".table-wrap table{margin:0}\n"
      "th,td{word-break:break-word;overflow-wrap:anywhere}",1)
io.open(P,"w",encoding="utf-8").write(s)
print("gen_site patched")
import py_compile; py_compile.compile(P,doraise=True); print("compiled")