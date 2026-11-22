# -*- coding: utf-8 -*-
"""Cycle7（本地工作）：为 gen_site.py 增加「单元总览页」。
每单元一页 units/<unit>.html：统计、按重要性分组条目、该单元的时间线片段、覆盖缺口提示。
同时把导航加「单元总览」入口，并让首页单元卡片指向单元页。"""
import io, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py")
s=io.open(P,encoding="utf-8").read()

# 1) 导航增加「单元总览」
old_nav='''        (REL+"index.html","首页"),(REL+"timeline.html","时间线"),
        (REL+"all-index.html","全站索引"),(REL+"sources.html","来源库")])+'</nav>\''''
new_nav='''        (REL+"index.html","首页"),(REL+"units.html","单元总览"),(REL+"timeline.html","时间线"),
        (REL+"all-index.html","全站索引"),(REL+"sources.html","来源库")])+'</nav>\''''
assert old_nav in s, "nav anchor missing"
s=s.replace(old_nav,new_nav)

# 2) 新增 build_units() 与 build_unit_pages()
anchor='def build_all_index(entries,units):'
assert anchor in s
code = '''def build_units_index(entries,units):
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
            m=re.search(r"(\\d{1,5})",e["when"])
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

'''
s=s.replace(anchor,code+anchor)

# 3) 首页单元卡片指向单元页
old_card='''        s.append("<article class='card'><div class='meta'>%s · %d 条</div><h3>%s</h3>"
            "<p><a href='all-index.html#%s'>查看本单元条目 →</a></p></article>"%(grp,len(dom[uid]),esc(uname),esc(uid)))'''
new_card='''        s.append("<article class='card'><div class='meta'>%s · %d 条</div><h3><a href='units/%s.html'>%s</a></h3>"
            "<p><a href='all-index.html#%s'>全部条目 →</a></p></article>"%(grp,len(dom[uid]),esc(uid),esc(uname),esc(uid)))'''
assert old_card in s, "index card anchor missing"
s=s.replace(old_card,new_card)

# 4) main() 调用
old_main='build_index(entries,UNITS,None); build_all_index(entries,UNITS); build_timeline(entries); build_sources()'
new_main='build_index(entries,UNITS,None); build_units_index(entries,UNITS); build_all_index(entries,UNITS); build_timeline(entries); build_sources()'
assert old_main in s
s=s.replace(old_main,new_main)
# 单元页在 REL="../" 之后生成（条目页同段）
old_loop='    for e in entries: build_entry(e,entries)'
new_loop='    build_unit_pages(entries,UNITS,None)\n    for e in entries: build_entry(e,entries)'
assert old_loop in s
s=s.replace(old_loop,new_loop)

io.open(P,"w",encoding="utf-8").write(s)
print("gen_site.py: unit overview pages added")