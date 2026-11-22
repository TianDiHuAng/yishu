# -*- coding: utf-8 -*-
"""Cycle8（本地轮）：gen_site.py 增量改造
1) 时间线按时期分组（带锚点）；
2) 新增「人物索引」（按生年排序）与「术语表」（按标题排序）两页，补全 WORKFLOW 阶段5 页面类型；
3) 条目页增加「反向引用」（被哪些条目引用）导航；
4) 导航加入 人物 / 术语 入口。
"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py")
s=io.open(P,encoding="utf-8").read()

# --- 1) 导航 ---
old='''        (REL+"index.html","首页"),(REL+"units.html","单元总览"),(REL+"timeline.html","时间线"),
        (REL+"all-index.html","全站索引"),(REL+"sources.html","来源库")])+'</nav>\''''
new='''        (REL+"index.html","首页"),(REL+"units.html","单元总览"),(REL+"timeline.html","时间线"),
        (REL+"people.html","人物"),(REL+"glossary.html","术语"),
        (REL+"all-index.html","全站索引"),(REL+"sources.html","来源库")])+'</nav>\''''
assert old in s
s=s.replace(old,new)

# --- 2) 时间线分组 ---
old_tl_start='def build_timeline(entries):'
i=s.index(old_tl_start); j=s.index('def build_sources():')
new_tl='''def _band(e):
    """把条目归入时期分组（本地启发式，仅用于时间线分组，不改变数据）。"""
    w=e["when"]
    if any(k in w for k in ["旧石器","新石器","公元前","战国","先秦","远古","商周"]): return "古代"
    if any(k in w for k in ["中世纪","拜占庭","罗马式","哥特","5—15","5—14","魏晋","敦煌"]): return "中世纪"
    if any(k in w for k in ["14—16","15世纪","16世纪","唐代","宋代","元代","明代","汉","唐","宋","元","明","文艺复兴"]): return "文艺复兴与宋元明"
    if any(k in w for k in ["17","18","19","清","巴洛克","洛可可","古典","浪漫"]): return "17—19世纪"
    if any(k in w for k in ["20","当代","至今","19末"]): return "20世纪—当代"
    return "跨期/术语"

BANDS=["古代","中世纪","文艺复兴与宋元明","17—19世纪","20世纪—当代","跨期/术语"]

def build_timeline(entries):
    import re
    def key(e):
        m=re.search(r"(\\d{1,5})",e["when"])
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
        m=re.search(r"(\\d{3,4})",e["when"])
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

'''
s=s[:i]+new_tl+s[j:]

# --- 3) 条目页反向引用 ---
old_rel='''        if e.get("related"):
            s.append("<div class='section-block'><h2><span class='num'>0%d</span>相关条目</h2><ul class='rel-list'>")'''
# L1 分支的相关条目（num 04）与 L2 分支（num 08）分别处理：在文件尾统一插入反链更简单
# 采用：在 "来源" section 之前插入反链
anchor='''    # 来源
    s.append("<section class='section'><div class='wrap'><h2>来源</h2>'''
assert anchor in s
back='''    # 反向引用（谁引用了本条目）
    inb=[x for x in entries if e["id"] in x.get("related",[])]
    if inb:
        s.append("<div class='section-block'><h2>被以下条目引用</h2><ul class='rel-list'>")
        for x in inb[:40]:
            s.append("<li><a href='%s.html'>%s</a></li>"%(esc(x["id"]),esc(x["title"])))
        s.append("</ul></div>")
'''+anchor
s=s.replace(anchor,back)

# --- 4) main 调用 ---
old_main='build_index(entries,UNITS,None); build_units_index(entries,UNITS); build_all_index(entries,UNITS); build_timeline(entries); build_sources()'
new_main='build_index(entries,UNITS,None); build_units_index(entries,UNITS); build_all_index(entries,UNITS); build_timeline(entries); build_sources(); build_people_index(entries); build_glossary(entries)'
assert old_main in s
s=s.replace(old_main,new_main)

io.open(P,"w",encoding="utf-8").write(s)
print("gen_site.py: timeline grouped + people/glossary pages + backlinks")