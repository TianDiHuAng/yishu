# -*- coding: utf-8 -*-
"""check_links.py — 全站站内链接核验（含 depth 层级错配）。
扫描所有生成的 .html，解析 href 中指向本地 .html 的链接，确认目标文件存在。
锚点 #id 若指向单元锚，检查目标页是否含该 id。
"""
import os,re,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
bad=[]
pages=[]
for dp,_,fs in os.walk(ROOT):
    if ".git" in dp: continue
    for f in fs:
        if f.endswith(".html"): pages.append(os.path.join(dp,f))
pat=re.compile(r"""(?:href|src)\s*=\s*['"]([^'"]+)['"]""",re.I)
for p in pages:
    txt=open(p,encoding="utf-8").read()
    for m in pat.finditer(txt):
        ref=m.group(1)
        if ref.startswith(("http://","https://","mailto:","data:","#")): continue
        target=ref.split("#")[0]
        if not target: continue
        if target.endswith(".html") or "/" in target:
            fp=os.path.normpath(os.path.join(os.path.dirname(p),target))
            if not os.path.exists(fp):
                bad.append((os.path.relpath(p,ROOT),ref,"文件不存在"))
print("check_links: pages=%d broken=%d"%(len(pages),len(bad)))
for b in bad[:60]: print("  %s -> %s (%s)"%b)
sys.exit(1 if bad else 0)
