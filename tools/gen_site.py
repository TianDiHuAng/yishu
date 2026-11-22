# -*- coding: utf-8 -*-
"""gen_site.py — 从 data/site_entries.json 确定性渲染静态站点到项目根目录。
页面：index.html / entries/<id>.html / timeline.html / all-index.html / sources.html / assets/style.css
零 JavaScript；深色模式用 prefers-color-scheme；SVG 配色走 CSS 类。
"""
import json, os, html
from collections import defaultdict, Counter
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
OUT=ROOT

CSS = r"""
:root{
  --paper:#f7f3ea; --paper-2:#efe9dc; --card:#fffdf7; --ink:#26221c;
  --ink-soft:#5c554a; --ink-faint:#8b8275; --rule:#d8cfbd;
  --accent:#8c3b2e; --accent-soft:#b5654f; --gold:#9a7b3f;
  --svg-box:#e8dfcc; --svg-box-strong:#f0e2d2; --svg-accent:#8c3b2e;
  --svg-line:#5c554a; --svg-text:#26221c;
  --shadow:0 1px 2px rgba(40,32,20,.06),0 8px 30px rgba(40,32,20,.05);
  --serif:"Songti SC","STSong","Noto Serif CJK SC","Source Han Serif SC",Georgia,serif;
  --sans:"PingFang SC","Microsoft YaHei","Noto Sans CJK SC",system-ui,sans-serif;
  --mono:ui-monospace,SFMono-Regular,Menlo,Consolas,monospace;
  --maxw:1080px; --radius:10px;
}
@media (prefers-color-scheme: dark){
  :root{
    --paper:#161512; --paper-2:#1d1b17; --card:#211f1a; --ink:#ece5d6;
    --ink-soft:#b9b0a0; --ink-faint:#8a8172; --rule:#3a352c;
    --accent:#d98a72; --accent-soft:#c9775e; --gold:#c9a95f;
    --svg-box:#2c2820; --svg-box-strong:#3a2c22; --svg-accent:#d98a72;
    --svg-line:#b9b0a0; --svg-text:#ece5d6;
    --shadow:0 1px 2px rgba(0,0,0,.4),0 10px 34px rgba(0,0,0,.35);
  }
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--paper);color:var(--ink);font-family:var(--sans);
  font-size:16px;line-height:1.75;-webkit-font-smoothing:antialiased}
h1,h2,h3,h4{font-family:var(--serif);font-weight:700;line-height:1.25;margin:0 0 .5em}
h1{font-size:2.6rem;letter-spacing:.02em}
h2{font-size:1.6rem;margin-top:0}
h3{font-size:1.15rem}
p{margin:0 0 1em;text-wrap:pretty}
a{color:var(--accent);text-decoration:none;border-bottom:1px solid transparent;transition:.18s}
a:hover{border-bottom-color:var(--accent)}
.wrap{max-width:var(--maxw);margin:0 auto;padding:0 24px}
.site-head{border-bottom:1px solid var(--rule);background:var(--paper-2);position:sticky;top:0;z-index:10}
.site-head .wrap{display:flex;align-items:center;justify-content:space-between;height:64px;gap:20px}
.brand{font-family:var(--serif);font-weight:700;font-size:1.15rem;color:var(--ink);border:0;letter-spacing:.04em}
.brand small{display:block;font-family:var(--sans);font-size:.66rem;color:var(--ink-faint);letter-spacing:.14em;font-weight:400}
.nav{display:flex;gap:22px;flex-wrap:wrap;font-size:.9rem}
.nav a{color:var(--ink-soft);border:0}
.nav a:hover{color:var(--accent)}
.hero{padding:72px 0 48px;border-bottom:1px solid var(--rule)}
.hero .kicker{font-family:var(--mono);font-size:.72rem;letter-spacing:.2em;color:var(--accent);text-transform:uppercase}
.hero h1{margin:.4em 0}
.hero .lede{max-width:44em;font-size:1.15rem;color:var(--ink-soft)}
.section{padding:48px 0;border-bottom:1px solid var(--rule)}
.section:last-child{border-bottom:0}
.stats{display:grid;grid-template-columns:repeat(auto-fit,minmax(150px,1fr));gap:16px;margin:24px 0}
.stat{background:var(--card);border:1px solid var(--rule);border-radius:var(--radius);padding:18px 20px;box-shadow:var(--shadow)}
.stat .n{font-family:var(--serif);font-size:2.2rem;color:var(--accent);line-height:1}
.stat .l{font-size:.82rem;color:var(--ink-soft);margin-top:6px}
.cards{display:grid;grid-template-columns:repeat(auto-fill,minmax(260px,1fr));gap:16px}
.card{background:var(--card);border:1px solid var(--rule);border-radius:var(--radius);padding:20px 22px;box-shadow:var(--shadow);
  transition:transform .18s,border-color .18s}
.card:hover{transform:translateY(-3px);border-color:var(--accent-soft)}
.card h3{margin-bottom:.35em}
.card .meta{font-size:.76rem;color:var(--ink-faint);font-family:var(--mono)}
.card p{font-size:.9rem;color:var(--ink-soft);margin:.6em 0 0}
.tag{display:inline-block;font-size:.7rem;font-family:var(--mono);padding:2px 8px;border-radius:20px;border:1px solid var(--rule);color:var(--ink-soft);margin-right:6px}
.tag.core{color:var(--accent);border-color:var(--accent-soft)}
.l2{color:var(--gold)}
.breadcrumb{font-size:.82rem;color:var(--ink-faint);margin:24px 0 12px}
.breadcrumb a{color:var(--ink-soft)}
.entry-head{border-bottom:1px solid var(--rule);padding-bottom:24px;margin-bottom:32px}
.entry-head h1{margin:.2em 0}
.entry-tags{display:flex;gap:8px;flex-wrap:wrap;margin-top:14px}
.section-block{margin:0 0 34px}
.section-block h2{display:flex;align-items:baseline;gap:12px;border-bottom:2px solid var(--accent);padding-bottom:8px}
.section-block h2 .num{font-family:var(--mono);font-size:.8rem;color:var(--accent)}
.section-block p{color:var(--ink);font-size:1.02rem}
.svg-frame{background:var(--card);border:1px solid var(--rule);border-radius:var(--radius);padding:20px;box-shadow:var(--shadow);overflow-x:auto}
.svg-frame svg{width:100%;height:auto;display:block}
.svg-label{fill:var(--svg-text);font-family:var(--sans);font-size:15px;font-weight:600}
.svg-label-strong{fill:var(--accent);font-size:17px}
.svg-sub{fill:var(--ink-soft);font-family:var(--sans);font-size:12px}
.svg-caption{fill:var(--ink-faint);font-family:var(--sans);font-size:12px}
.svg-box{fill:var(--svg-box);stroke:var(--rule);stroke-width:1.5}
.svg-box-accent{fill:var(--svg-box-strong);stroke:var(--accent-soft);stroke-width:1.5}
.svg-box-muted{fill:var(--svg-box);stroke:var(--rule);stroke-width:1.5}
.svg-arrow{stroke:var(--svg-line);stroke-width:2}
.svg-arrowhead{fill:var(--svg-line)}
.rel-list{list-style:none;padding:0;display:flex;flex-wrap:wrap;gap:10px}
.rel-list a{display:inline-block;background:var(--paper-2);border:1px solid var(--rule);border-radius:6px;padding:6px 12px;font-size:.88rem}
.pending{background:var(--paper-2);border-left:3px solid var(--gold);padding:14px 18px;border-radius:0 8px 8px 0;font-size:.9rem;color:var(--ink-soft)}
.l3-block{background:var(--card);border:1px solid var(--accent-soft);border-radius:var(--radius);padding:22px;margin:0 0 34px}
.l3-block h2{font-size:1.3rem}
.controversy{border-left:3px solid var(--gold);padding:6px 0 6px 16px;margin:14px 0}
.controversy .issue{font-weight:600;color:var(--ink);margin-bottom:6px}
.controversy .view{font-size:.92rem;color:var(--ink-soft);margin:3px 0}
.controversy .view .holder{color:var(--accent);font-weight:600}
.data-table{margin:12px 0}
.badge-l3{background:var(--accent);color:var(--paper);padding:2px 8px;border-radius:4px;font-family:var(--mono);font-size:.7rem}
.pending ol{margin:.4em 0 0;padding-left:1.3em}
.footer{border-top:1px solid var(--rule);padding:32px 0;color:var(--ink-faint);font-size:.82rem}
table{width:100%;border-collapse:collapse;font-size:.92rem}
th,td{text-align:left;padding:9px 10px;border-bottom:1px solid var(--rule)}
th{font-family:var(--sans);color:var(--ink-soft);font-size:.82rem}
.eyebrow{font-family:var(--mono);font-size:.7rem;letter-spacing:.16em;color:var(--ink-faint);text-transform:uppercase}
.unit-group{margin-bottom:36px}
.unit-group h2{font-size:1.3rem;border-bottom:1px solid var(--rule);padding-bottom:8px}
.entry-link{display:flex;justify-content:space-between;gap:16px;padding:7px 0;border-bottom:1px dotted var(--rule)}
.entry-link .t{color:var(--ink)}
.entry-link .m{font-size:.78rem;color:var(--ink-faint);font-family:var(--mono);white-space:nowrap}
.ok{color:#3d7a4e} .no{color:var(--accent)}
@media(max-width:640px){h1{font-size:2rem}.nav{gap:12px}.hero{padding:48px 0 32px}}
@media print{.site-head{position:static}.card,.svg-frame{box-shadow:none}}
"""

def load(p):
    with open(p,encoding="utf-8") as f: return json.load(f)

def esc(s): return html.escape(str(s), quote=True)

def depth_badge(e):
    lv=e.get("level","L1")
    return '<span class="tag l2">%s</span>'%lv if lv!="L1" else ""

def tier_badge(e):
    return '<span class="tag %s">%s</span>'%("core" if e["tier"]=="核心" else "", e["tier"])

def head(title, crumb=True):
    nav='<nav class="nav">'+"".join('<a href="%s">%s</a>'%(u,t) for u,t in [
        (REL+"index.html","首页"),(REL+"units.html","单元总览"),(REL+"timeline.html","时间线"),
        (REL+"people.html","人物"),(REL+"glossary.html","术语"),
        (REL+"all-index.html","全站索引"),(REL+"sources.html","来源库")])+'</nav>'
    return ("<!doctype html><html lang='zh-CN'><head><meta charset='utf-8'>"
        "<meta name='viewport' content='width=device-width,initial-scale=1'>"
        "<title>%s — 艺术史与音乐史导读</title><link rel='stylesheet' href='%sassets/style.css'></head><body>"%(esc(title),REL))+ \
        "<header class='site-head'><div class='wrap'><a class='brand' href='%sindex.html'>艺术史与音乐史导读<small>ART &amp; MUSIC HISTORY PRIMER</small></a>%s</div></header>"%(REL,nav)

FOOT="<footer class='footer'><div class='wrap'>静态知识库 · 数据驱动 · 机器校验 · 诚实标注 — 所有图示为自绘 SVG，不含作品图片。</div></footer></body></html>"

def entry_card(e):
    return ("<article class='card'><div class='meta'>%s · %s</div><h3><a href='%sentries/%s.html'>%s</a></h3>"
        "<p>%s</p><div style='margin-top:10px'>%s%s%s</div></article>")%(
        esc(e["era"]),esc(e["region"]),REL,esc(e["id"]),esc(e["title"]),
        esc(e["overview"][:90]+("…" if len(e["overview"])>90 else "")),
        depth_badge(e),tier_badge(e),
        ('<span class="tag">待核实</span>' if e.get("needs_verification") else ""))

def build_index(entries,units,cov):
    stats=Counter(e.get("level","L1") for e in entries)
    dom=defaultdict(list)
    for e in entries: dom[e["unit"]].append(e)
    total=len(entries)
    verified=sum(1 for e in entries if not e.get("needs_verification"))
    s=[head("首页",False)]
    s.append("<section class='hero'><div class='wrap'><div class='kicker'>Data-driven knowledge primer</div>"
        "<h1>艺术史与音乐史导读</h1><p class='lede'>一部可离线阅读、可机器校验的知识脉络库。以权威大纲取并集界定范围，"
        "以来源双源规则约束事实，所有图示均为自绘 SVG 抽象示意。 Coverage first, depth later.</p></div></section>")
    s.append("<section class='section'><div class='wrap'><div class='stats'>")
    for n,l in [(total,"条目总数"),(len(units),"知识单元"),(verified,"双源已核验"),
                (stats.get("L2",0)+stats.get("L3",0),"L2+ 深度条目"),(len(SOURCES),"来源库条目")]:
        s.append("<div class='stat'><div class='n'>%d</div><div class='l'>%s</div></div>"%(n,l))
    s.append("</div></div></section>")
    s.append("<section class='section'><div class='wrap'><h2>按知识单元浏览</h2><div class='cards'>")
    for uid,uname in units.items():
        if uid.startswith("music"): grp="音乐"
        elif uid.startswith("art-china"): grp="中国艺术"
        elif uid.startswith("art"): grp="艺术"
        else: grp="其他"
        s.append("<article class='card'><div class='meta'>%s · %d 条</div><h3><a href='units/%s.html'>%s</a></h3>"
            "<p><a href='all-index.html#%s'>全部条目 →</a></p></article>"%(grp,len(dom[uid]),esc(uid),esc(uname),esc(uid)))
    s.append("</div></div></section>")
    # 核心样板
    feat=[e for e in entries if e.get("level") in ("L2","L3")][:6]
    if feat:
        s.append("<section class='section'><div class='wrap'><h2>深度条目（L2+）</h2><div class='cards'>")
        for e in feat: s.append(entry_card(e))
        s.append("</div></div></section>")
    s.append(FOOT)
    open(os.path.join(OUT,"index.html"),"w",encoding="utf-8").write("".join(s))

def build_entry(e,entries):
    byid={x["id"]:x for x in entries}
    s=[head(e["title"])]
    s.append("<div class='wrap'><div class='breadcrumb'><a href='%sindex.html'>首页</a> / "
        "<a href='%sall-index.html#%s'>%s</a> / %s</div>"%(REL,REL,esc(e["unit"]),esc(UNITS.get(e["unit"],e["unit"])),esc(e["title"])))
    s.append("<div class='entry-head'><h1>%s</h1><div class='entry-tags'>%s%s<span class='tag'>%s</span>"
        "<span class='tag'>%s</span><span class='tag'>%s</span></div></div>"%(
        esc(e["title"]),depth_badge(e),tier_badge(e),esc(e["kind"]),esc(e["era"]),esc(e["region"])))
    lv=e.get("level","L1")
    if lv=="L1":
        s.append("<div class='section-block'><h2><span class='num'>01</span>定义</h2><p>%s</p></div>"%esc(e["def"]))
        s.append("<div class='section-block'><h2><span class='num'>02</span>时间或位置</h2><p>%s（%s）</p></div>"%(esc(e["when"]),esc(e["region"])))
        s.append("<div class='section-block'><h2><span class='num'>03</span>概述</h2><p>%s</p></div>"%esc(e["overview"]))
        if e.get("related"):
            s.append("<div class='section-block'><h2><span class='num'>04</span>相关条目</h2><ul class='rel-list'>")
            for r in e["related"]:
                if r in byid: s.append("<li><a href='%s.html'>%s</a></li>"%(esc(r),esc(byid[r]["title"])))
            s.append("</ul></div>")
        if e.get("needs_verification"):
            s.append("<div class='pending'><strong>待核实</strong><p>%s</p></div>"%esc(e.get("pending_notes","")))
    else:
        sec=e.get("sections",{})
        names=["时代背景","风格特征","代表人物与作品","技法或形式分析","与前后风格的关系和争论","一图","待核实"]
        for i,nm in enumerate(names,1):
            s.append("<div class='section-block'><h2><span class='num'>%02d</span>%s</h2>"%(i,esc(nm)))
            if nm=="一图":
                s.append("<p>%s</p><div class='svg-frame'>%s</div>"%(esc(sec.get(nm,"")),e.get("svg","")))
            elif nm=="待核实":
                notes=sec.get(nm,"")
                s.append("<div class='pending'>%s</div>"%esc(notes))
            else:
                s.append("<p>%s</p>"%esc(sec.get(nm,"")))
            s.append("</div>")
        if lv=="L3" and e.get("l3"):
            l3=e["l3"]
            s.append("<div class='l3-block'><h2><span class='badge-l3'>L3 深度</span> 争议、数据与复杂图示</h2>")
            for c in l3.get("controversies",[]):
                s.append("<div class='controversy'><div class='issue'>%s</div>"%esc(c.get("issue","")))
                for v in c.get("views",[]):
                    s.append("<div class='view'><span class='holder'>%s：</span>%s</div>"%(esc(v.get("holder","")),esc(v.get("basis",""))))
                s.append("</div>")
            if l3.get("data"):
                s.append("<h3>关键数据（均有来源）</h3><table class='data-table'><thead><tr><th>项目</th><th>数值/事实</th><th>说明</th></tr></thead><tbody>")
                for d in l3["data"]:
                    s.append("<tr><td>%s</td><td>%s</td><td>%s</td></tr>"%(esc(d.get("label","")),esc(d.get("value","")),esc(d.get("note",""))))
                s.append("</tbody></table>")
            if l3.get("complex_diagram_note"):
                s.append("<p class='eyebrow'>复杂图示说明：%s</p>"%esc(l3["complex_diagram_note"]))
            s.append("</div>")
        if e.get("related"):
            s.append("<div class='section-block'><h2><span class='num'>08</span>相关条目</h2><ul class='rel-list'>")
            for r in e["related"]:
                if r in byid: s.append("<li><a href='%s.html'>%s</a></li>"%(esc(r),esc(byid[r]["title"])))
            s.append("</ul></div>")
    # 反向引用（谁引用了本条目）
    inb=[x for x in entries if e["id"] in x.get("related",[])]
    if inb:
        s.append("<div class='section-block'><h2>被以下条目引用</h2><ul class='rel-list'>")
        for x in inb[:40]:
            s.append("<li><a href='%s.html'>%s</a></li>"%(esc(x["id"]),esc(x["title"])))
        s.append("</ul></div>")
    # 来源
    s.append("<section class='section'><div class='wrap'><h2>来源</h2><table><thead><tr><th>标题</th><th>机构/作者</th><th>类型</th><th>核验</th></tr></thead><tbody>")
    for sid in e.get("sources",[]):
        src=SM.get(sid)
        if not src: continue
        s.append("<tr><td><a href='%s' rel='noopener'>%s</a></td><td>%s</td><td>%s</td><td class='%s'>%s</td></tr>"%(
            esc(src["url"]),esc(src["title"]),esc(src["author"]),esc(src["type"]),
            "ok" if src["verified"] else "no","已核验" if src["verified"] else "未核验"))
    s.append("</tbody></table></div></section>")
    s.append("</div>"+FOOT)
    os.makedirs(os.path.join(OUT,"entries"),exist_ok=True)
    open(os.path.join(OUT,"entries",e["id"]+".html"),"w",encoding="utf-8").write("".join(s))

def build_units_index(entries,units):
    """单元总览索引页 units.html"""
    dom=defaultdict(list)
    for e in entries: dom[e["unit"]].append(e)
    s=[head("单元总览")]
    s.append("<div class='wrap'><h1>单元总览</h1><p class='eyebrow'>共 %d 个知识单元 · %d 条目</p>"%(len(units),len(entries)))
    s.append("<div class='cards'>")
    for uid,uname in units.items():
        g=dom.get(uid,[])
        if not g: continue
        l3=sum(1 for e in g if e.get("level")=="L3")
        core=sum(1 for e in g if e["tier"]=="核心")
        s.append("<article class='card'><div class='meta'>%d 条 · 核心 %d · L3 %d</div>"
                 "<h3><a href='units/%s.html'>%s</a></h3><p>%s</p></article>"%(
                 len(g),core,l3,esc(uid),esc(uname),
                 esc("、".join(e["title"] for e in g[:4])+("…" if len(g)>4 else ""))))
    s.append("</div></div>"+FOOT)
    open(os.path.join(OUT,"units.html"),"w",encoding="utf-8").write("".join(s))

def build_unit_pages(entries,units,cov):
    """每单元一页：统计 + 分级条目 + 时间线片段 + 缺口提示（本地数据，不新增断言）。"""
    os.makedirs(os.path.join(OUT,"units"),exist_ok=True)
    dom=defaultdict(list)
    for e in entries: dom[e["unit"]].append(e)
    order={"核心":0,"重要":1,"补充":2}
    for uid,uname in units.items():
        g=sorted(dom.get(uid,[]),key=lambda e:(order[e["tier"]],e["id"]))
        if not g: continue
        lv=Counter(e.get("level","L2") for e in g)
        tiers=Counter(e["tier"] for e in g)
        regions=sorted({r for e in g for r in [e["region"]]})
        media=Counter(m for e in g for m in e["medium"].split(","))
        pend=[e for e in g if e.get("needs_verification")]
        s=[head(uname)]
        s.append("<div class='wrap'><div class='breadcrumb'><a href='%sunits.html'>单元总览</a> / %s</div>"%(REL,esc(uname)))
        s.append("<h1>%s</h1>"%esc(uname))
        s.append("<div class='stats'>")
        for n,l in [(len(g),"条目"),(tiers.get("核心",0),"核心"),(lv.get("L3",0),"L3 深度"),
                    (len(media),"媒介类型"),(len(pend),"待核实")]:
            s.append("<div class='stat'><div class='n'>%d</div><div class='l'>%s</div></div>"%(n,l))
        s.append("</div>")
        # 分期/地区/媒介概览
        s.append("<div class='section-block'><h2><span class='num'>01</span>本单元构成</h2>")
        s.append("<p>地区：%s</p>"%esc("、".join(regions)))
        s.append("<p>媒介分布：%s</p>"%esc("、".join("%s %d"%(k,v) for k,v in media.most_common())))
        s.append("<p>层级：L2 %d · L3 %d</p>"%(lv.get("L2",0),lv.get("L3",0)))
        s.append("</div>")
        # 分级条目
        s.append("<div class='section-block'><h2><span class='num'>02</span>条目（按重要性）</h2>")
        cur=None
        for e in g:
            if e["tier"]!=cur:
                if cur is not None: s.append("</ul>")
                cur=e["tier"]; s.append("<h3>%s</h3><ul class='rel-list'>"%esc(cur))
            s.append("<li><a href='%sentries/%s.html'>%s</a> <span class='m' style='color:var(--ink-faint);font-size:.76rem'>%s</span></li>"%(
                REL,esc(e["id"]),esc(e["title"]),esc(e["when"])))
        if cur is not None: s.append("</ul>")
        s.append("</div>")
        # 时间线片段
        def ykey(e):
            import re
            m=re.search(r"(\d{1,5})",e["when"])
            if not m: return 99999
            v=int(m.group(1))
            if "前" in e["when"][:m.end()+2]: return -v
            return v
        s.append("<div class='section-block'><h2><span class='num'>03</span>本单元时间线</h2>")
        for e in sorted(g,key=ykey):
            s.append("<div class='entry-link'><a class='t' href='%sentries/%s.html'>%s</a><span class='m'>%s</span></div>"%(
                REL,esc(e["id"]),esc(e["title"]),esc(e["when"])))
        s.append("</div>")
        # 待核实（诚实提示，不新增内容）
        if pend:
            s.append("<div class='section-block'><h2><span class='num'>04</span>待核实条目</h2><ul>")
            for e in pend[:20]:
                s.append("<li><a href='%sentries/%s.html'>%s</a>：%s</li>"%(REL,esc(e["id"]),esc(e["title"]),esc((e.get("pending_notes") or "")[:90])))
            s.append("</ul></div>")
        s.append("</div>"+FOOT)
        open(os.path.join(OUT,"units",uid+".html"),"w",encoding="utf-8").write("".join(s))

def build_all_index(entries,units):
    dom=defaultdict(list)
    for e in entries: dom[e["unit"]].append(e)
    s=[head("全站索引")]
    s.append("<div class='wrap'><h1>全站索引</h1><p class='eyebrow'>按知识单元 · 共 %d 条</p>"%len(entries))
    for uid,uname in units.items():
        s.append("<div class='unit-group' id='%s'><h2>%s</h2>"%(esc(uid),esc(uname)))
        for e in sorted(dom[uid],key=lambda x:x["title"]):
            s.append("<div class='entry-link'><a class='t' href='entries/%s.html'>%s %s</a>"
                "<span class='m'>%s · %s</span></div>"%(esc(e["id"]),esc(e["title"]),depth_badge(e),
                esc(e["era"]),esc(e["medium"])))
        s.append("</div>")
    s.append("</div>"+FOOT)
    open(os.path.join(OUT,"all-index.html"),"w",encoding="utf-8").write("".join(s))

def _band(e):
    """把条目归入时期分组（本地启发式，仅用于时间线分组，不改变数据）。
    优先用 era 字段（人工填写的时代标签），回退到 when（年代文本）。"""
    w=(e.get("era") or "") + " " + e["when"]
    if any(k in w for k in ["旧石器","新石器","公元前","战国","先秦","远古","商周"]): return "古代"
    if any(k in w for k in ["中世纪","拜占庭","罗马式","哥特","5—15","5—14","魏晋","敦煌"]): return "中世纪"
    if any(k in w for k in ["14—16","15世纪","16世纪","唐代","宋代","元代","明代","汉","唐","宋","元","明","文艺复兴"]): return "文艺复兴与宋元明"
    if any(k in w for k in ["20世纪","当代","至今","19末","19—20","2025"]): return "20世纪—当代"
    if any(k in w for k in ["17","18","19","清","巴洛克","洛可可","古典","浪漫"]): return "17—19世纪"
    return "跨期/术语"

BANDS=["古代","中世纪","文艺复兴与宋元明","17—19世纪","20世纪—当代","跨期/术语"]

def build_timeline(entries):
    import re
    def key(e):
        m=re.search(r"(\d{1,5})",e["when"])
        if not m: return 99999
        v=int(m.group(1))
        if "前" in e["when"][:m.end()+2]: return -v
        return v
    s=[head("时间线")]
    s.append("<div class='wrap'><h1>时间线</h1><p class='eyebrow'>按时期分组、组内按起始年代排序 · 共 %d 条</p>"%len(entries))
    s.append("<p class='eyebrow'>分组为阅读用启发式划分，不替代各条目自身的断代说明。</p>")
    s.append("<div class='rel-list' style='margin:14px 0 24px'>")
    for b in BANDS:
        n=sum(1 for e in entries if _band(e)==b)
        if n: s.append("<a href='#band-%s'>%s（%d）</a>"%(esc(b),esc(b),n))
    s.append("</div>")
    for b in BANDS:
        g=sorted([e for e in entries if _band(e)==b],key=key)
        if not g: continue
        s.append("<div class='unit-group' id='band-%s'><h2>%s · %d 条</h2>"%(esc(b),esc(b),len(g)))
        for e in g:
            s.append("<div class='entry-link'><a class='t' href='entries/%s.html'>%s %s</a><span class='m'>%s</span></div>"%(
                esc(e["id"]),esc(e["title"]),depth_badge(e),esc(e["when"])))
        s.append("</div>")
    s.append("</div>"+FOOT)
    open(os.path.join(OUT,"timeline.html"),"w",encoding="utf-8").write("".join(s))

def build_people_index(entries):
    import re
    ppl=[e for e in entries if e["kind"]=="人物"]
    def birth(e):
        m=re.search(r"(\d{3,4})",e["when"])
        return int(m.group(1)) if m else 99999
    ppl.sort(key=lambda e:(birth(e),e["title"]))
    s=[head("人物索引")]
    s.append("<div class='wrap'><h1>人物索引</h1><p class='eyebrow'>%d 位 · 按条目所记起始年代排序</p>"%len(ppl))
    s.append("<div class='unit-group'>")
    for e in ppl:
        s.append("<div class='entry-link'><a class='t' href='entries/%s.html'>%s %s</a><span class='m'>%s · %s</span></div>"%(
            esc(e["id"]),esc(e["title"]),depth_badge(e),esc(e["when"]),esc(e["region"])))
    s.append("</div></div>"+FOOT)
    open(os.path.join(OUT,"people.html"),"w",encoding="utf-8").write("".join(s))

def build_glossary(entries):
    terms=[e for e in entries if e["kind"]=="术语"]
    terms.sort(key=lambda e:e["title"])
    s=[head("术语表")]
    s.append("<div class='wrap'><h1>术语表</h1><p class='eyebrow'>%d 条 · 按标题排序（暂按字符序，非严格音序）</p>"%len(terms))
    s.append("<table><thead><tr><th>术语</th><th>定义</th><th>单元</th></tr></thead><tbody>")
    for e in terms:
        s.append("<tr><td><a href='entries/%s.html'>%s</a></td><td>%s</td><td>%s</td></tr>"%(
            esc(e["id"]),esc(e["title"]),esc(e["def"]),esc(UNITS.get(e["unit"],e["unit"]))))
    s.append("</tbody></table></div>"+FOOT)
    open(os.path.join(OUT,"glossary.html"),"w",encoding="utf-8").write("".join(s))

def build_sources():
    s=[head("来源库")]
    s.append("<div class='wrap'><h1>来源库</h1><p class='eyebrow'>%d 条 · 已核验 %d 条</p>"%(
        len(SOURCES),sum(1 for x in SOURCES if x["verified"])))
    s.append("<table><thead><tr><th>id</th><th>标题</th><th>机构/作者</th><th>年份</th><th>类型</th><th>核验</th></tr></thead><tbody>")
    for x in sorted(SOURCES,key=lambda a:a["id"]):
        s.append("<tr><td><code>%s</code></td><td><a href='%s'>%s</a></td><td>%s</td><td>%s</td><td>%s</td>"
            "<td class='%s' title='%s'>%s</td></tr>"%(esc(x["id"]),esc(x["url"]),esc(x["title"]),
            esc(x["author"]),esc(x["year"]),esc(x["type"]),"ok" if x["verified"] else "no",
            esc(x.get("verified_note","")),"已核验" if x["verified"] else "未核验"))
    s.append("</tbody></table></div>"+FOOT)
    open(os.path.join(OUT,"sources.html"),"w",encoding="utf-8").write("".join(s))

def build_css():
    os.makedirs(os.path.join(OUT,"assets"),exist_ok=True)
    open(os.path.join(OUT,"assets","style.css"),"w",encoding="utf-8").write(CSS)

def main():
    global REL,SM,SOURCES,UNITS
    entries=load(os.path.join(D,"site_entries.json"))["entries"]
    SOURCES=load(os.path.join(D,"sources.json"))["sources"]
    SM={x["id"]:x for x in SOURCES}
    import sys; sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
    UNITS=__import__("catalog").UNITS
    REL=""  # 所有页面在根目录，条目页用相对文件名（同级 entries/ 用 ../ 需修正）
    # 根目录页面引用 assets/ 与 entries/；条目页在 entries/ 内，需 ../
    build_css()
    # 根页面
    REL=""
    build_index(entries,UNITS,None); build_units_index(entries,UNITS); build_all_index(entries,UNITS); build_timeline(entries); build_sources(); build_people_index(entries); build_glossary(entries)
    # 条目页（在 entries/ 子目录，相对路径需 ../
    REL="../"
    # 但条目页的 head/breadcrumb 用 REL 前缀；entry_card 内链在根页面已生成，无影响
    build_unit_pages(entries,UNITS,None)
    for e in entries: build_entry(e,entries)
    # 修正：head() 的 brand/nav 在条目页应使用 ../ 前缀。build_entry 已用 head() 且 REL='../'，正确。
    # 来源表链接为绝对 URL，不受影响。
    n=len(entries)
    print("generated index.html + %d entry pages + timeline/all-index/sources + style.css"%n)

if __name__=="__main__": main()
