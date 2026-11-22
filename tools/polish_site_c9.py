# -*- coding: utf-8 -*-
"""Cycle9（本地轮）：站点可访问性与可用性改造
1) 跳转链接 skip-link + 主内容 id；2) :focus-visible 焦点样式；3) nav aria-label；
4) 完善 @media print；5) 条目页页内目录（TOC，七节锚点）；6) 生成 sitemap.xml。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py")
s=io.open(P,encoding="utf-8").read()

# ---- 1) CSS：焦点样式 / skip-link / 打印 ----
old_print="@media print{.site-head{position:static}.card,.svg-frame{box-shadow:none}}"
new_print='''@media print{.site-head{position:static}.card,.svg-frame{box-shadow:none}
  .nav,.rel-list,.breadcrumb{display:none}a{border:0;color:var(--ink)}
  body{font-size:11pt}.section{padding:18px 0}}
:focus-visible{outline:3px solid var(--accent);outline-offset:2px;border-radius:4px}
.skip{position:absolute;left:-9999px;top:0;background:var(--card);color:var(--ink);
  padding:10px 16px;z-index:99;border:1px solid var(--rule);border-radius:0 0 8px 0}
.skip:focus{left:0}
.toc{background:var(--card);border:1px solid var(--rule);border-radius:var(--radius);padding:16px 20px;margin:0 0 28px}
.toc ol{margin:.4em 0 0;padding-left:1.4em;columns:2;column-gap:28px}
.toc a{font-size:.92rem}'''
assert old_print in s
s=s.replace(old_print,new_print)

# ---- 2) head()：skip-link + aria + main 起点 ----
old_head='''        "<header class='site-head'><div class='wrap'><a class='brand' href='%sindex.html'>艺术史与音乐史导读<small>ART &amp; MUSIC HISTORY PRIMER</small></a>%s</div></header>"%(REL,nav)'''
new_head='''        "<a class='skip' href='#main'>跳到主内容</a>"\\
        "<header class='site-head'><div class='wrap'><a class='brand' href='%sindex.html'>艺术史与音乐史导读<small>ART &amp; MUSIC HISTORY PRIMER</small></a>%s</div></header>"%(REL,nav)\\
        + "<main id='main'>"'''
assert old_head in s
s=s.replace(old_head,new_head)
# nav aria-label
s=s.replace("""nav='<nav class="nav">'""","""nav='<nav class="nav" aria-label="主导航">'""")

# ---- 3) FOOT：闭合 main ----
old_foot='FOOT="<footer class=\'footer\'>'
new_foot='FOOT="</main><footer class=\'footer\'>'
assert old_foot in s
s=s.replace(old_foot,new_foot)

# ---- 4) 条目页 TOC（L2/L3 七节 + L1 四节）----
old_l2='''    else:
        sec=e.get("sections",{})
        names=["时代背景","风格特征","代表人物与作品","技法或形式分析","与前后风格的关系和争论","一图","待核实"]'''
new_l2='''    else:
        sec=e.get("sections",{})
        names=["时代背景","风格特征","代表人物与作品","技法或形式分析","与前后风格的关系和争论","一图","待核实"]
        s.append("<nav class='toc' aria-label='页内目录'><div class='eyebrow'>页内目录</div><ol>")
        for i,nm in enumerate(names,1):
            s.append("<li><a href='#sec-%02d'>%s</a></li>"%(i,esc(nm)))
        s.append("</ol></nav>")'''
assert old_l2 in s
s=s.replace(old_l2,new_l2)

# 七节 h2 加 id
old_h2='''            s.append("<div class='section-block'><h2><span class='num'>%02d</span>%s</h2>"%(i,esc(nm)))'''
new_h2='''            s.append("<div class='section-block'><h2 id='sec-%02d'><span class='num'>%02d</span>%s</h2>"%(i,i,esc(nm)))'''
assert old_h2 in s
s=s.replace(old_h2,new_h2)

# ---- 5) main()：生成 sitemap.xml ----
old_gen='    print("generated index.html + %d entry pages + timeline/all-index/sources + style.css"%n)'
new_gen='''    build_sitemap(entries)
    print("generated index.html + %d entry pages + indexes + sitemap.xml"%n)'''
assert old_gen in s
s=s.replace(old_gen,new_gen)

sitemap_fn='''
def build_sitemap(entries):
    # 站点根：GitHub Pages 默认地址（用户 TianDiHuAng / 仓库 yishu）
    base="https://tiandihuang.github.io/yishu/"
    urls=["index.html","units.html","timeline.html","people.html","glossary.html",
          "all-index.html","sources.html"]
    urls+= ["units/%s.html"%u for u in UNITS]
    urls+= ["entries/%s.html"%e["id"] for e in entries]
    body=["<?xml version='1.0' encoding='UTF-8'?>","<urlset xmlns='http://www.sitemaps.org/schemas/sitemap/0.9'>"]
    for u in urls:
        body.append("<url><loc>%s%s</loc></url>"%(base,u))
    body.append("</urlset>")
    open(os.path.join(OUT,"sitemap.xml"),"w",encoding="utf-8").write("\\n".join(body))
    open(os.path.join(OUT,"robots.txt"),"w",encoding="utf-8").write("User-agent: *\\nAllow: /\\nSitemap: %ssitemap.xml\\n"%base)

'''
s=s.replace("def main():", sitemap_fn+"def main():")
io.open(P,"w",encoding="utf-8").write(s)
print("gen_site.py: a11y + toc + print + sitemap")