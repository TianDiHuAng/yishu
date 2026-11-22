# -*- coding: utf-8 -*-
"""体检 F（Cycle10）：六维 + 新增三项（页内锚点有效性 / sitemap与实体页一致 / 色对比度复算）。
来源文本重合度需联网抓取，本轮标记为"不可执行（网络降级）"。"""
import json,os,re,glob
from collections import Counter
from difflib import SequenceMatcher
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
R={}

# 1 死链（站内）
pat=re.compile(r'(?:href|src)\s*=\s*[\'"]([^\'"]+)[\'"]')
dead=[]
pages=[p for p in glob.glob(os.path.join(ROOT,"**","*.html"),recursive=True) if ".git" not in p]
for p in pages:
    for m in pat.finditer(open(p,encoding="utf-8").read()):
        ref=m.group(1)
        if ref.startswith(("http","mailto:","data:")): continue
        f=ref.split("#")[0]
        if not f: continue
        tgt=os.path.normpath(os.path.join(os.path.dirname(p),f))
        if not os.path.exists(tgt): dead.append([os.path.relpath(p,ROOT),ref])
R["dead_links"]=dead

# 2 过期数据（现状类措辞且无年份）
R["stale_data"]=[e["id"] for e in es if re.search(r"目前|现存|最新|现状|截至",e["overview"]+" ".join(e.get("sections",{}).values()))
                 and not re.search(r"20[0-2][0-9]|19[0-9]{2}",e["overview"]+" ".join(e.get("sections",{}).values()))]

# 3 重复（id/标题）
R["duplicates"]=[k for k,v in Counter(e["title"] for e in es).items() if v>1]

# 4 数据矛盾（when 与 overview 年份无交集）
yr=re.compile(r"(?:公元前\s*)?(\d{3,4})")
con=[]
for e in es:
    w=set(yr.findall(e["when"])); o=set(yr.findall(e["overview"]))
    if w and o and not (w&o) and "前" not in e["when"] and "前" not in e["overview"]: con.append([e["id"],e["when"],sorted(o)])
R["contradictions"]=con

# 5 孤儿
inb=Counter(r for e in es for r in e.get("related",[]))
R["orphans"]=[e["id"] for e in es if inb[e["id"]]==0]

# 6 来源重合度：需联网，标记
R["overlap"]="skipped: 内容来源（Wikipedia/Met/Tate）不可达，无法抓取正文比对；Wikidata 为结构化数据（无正文），不适用 n-gram 重合度。最近有效结果：Cycle5 抽样5条，重合 0%"

# 7 NEW 页内锚点有效性
anchor_bad=[]
for p in pages:
    h=open(p,encoding="utf-8").read()
    ids=set(re.findall(r"id=['\"]([^'\"]+)['\"]",h))
    for m in re.finditer(r"href=['\"]#([^'\"]+)['\"]",h):
        if m.group(1) not in ids: anchor_bad.append([os.path.relpath(p,ROOT),m.group(1)])
R["bad_anchors"]=anchor_bad

# 8 NEW sitemap 与实体页一致
sm=open(os.path.join(ROOT,"sitemap.xml"),encoding="utf-8").read()
base="https://tiandihuang.github.io/yishu/"
locs=[m.group(1).replace(base,"") for m in re.finditer(r"<loc>([^<]+)</loc>",sm)]
missing=[u for u in locs if not os.path.exists(os.path.join(ROOT,u))]
html_files=set(os.path.relpath(p,ROOT).replace("\\","/") for p in pages)
notlisted=sorted(html_files-set(locs))
R["sitemap_missing_files"]=missing
R["sitemap_unlisted_pages"]=notlisted

# 9 NEW 对比度复算（浅/深各5个令牌）
def lum(h):
    h=h.lstrip("#"); r,g,b=[int(h[i:i+2],16)/255 for i in (0,2,4)]
    f=lambda c: c/12.92 if c<=0.03928 else ((c+0.055)/1.055)**2.4
    return .2126*f(r)+.7152*f(g)+.0722*f(b)
def cr(a,b):
    la,lb=lum(a),lum(b); hi,lo=max(la,lb),min(la,lb); return round((hi+.05)/(lo+.05),2)
L={'paper':'#f7f3ea','card':'#fffdf7','ink':'#26221c','soft':'#5c554a','faint':'#6b6357','accent':'#8c3b2e','gold':'#7a5f2e'}
Dk={'paper':'#161512','card':'#211f1a','ink':'#ece5d6','soft':'#b9b0a0','faint':'#978d7e','accent':'#d98a72','gold':'#c9a95f'}
R["contrast"]={"light":{k:[cr(L[k],L['paper']),cr(L[k],L['card'])] for k in ('ink','soft','faint','accent','gold')},
               "dark":{k:[cr(Dk[k],Dk['paper']),cr(Dk[k],Dk['card'])] for k in ('ink','soft','faint','accent','gold')}}

la=os.path.join(ROOT,"reports","link_audit.json")
if os.path.exists(la):
    L=json.load(open(la,encoding="utf-8"))
    R["link_audit"]={"cross_domain":len(L.get("cross_domain",[])),"oneway":L.get("oneway_count"),"total_links":L.get("total_links")}
json.dump(R,open(os.path.join(ROOT,"reports","healthcheck_c10.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("=== 体检 F (Cycle10) ===")
for k in ("dead_links","stale_data","duplicates","contradictions","orphans","overlap","bad_anchors","sitemap_missing_files","sitemap_unlisted_pages"):
    v=R[k]; print(" %-24s %s"%(k, v if not isinstance(v,list) else "%d %s"%(len(v),v[:6])))
nfail=[(t,k,v) for t in ("light","dark") for k,v in R["contrast"][t].items() if min(v)<4.5]
print(" contrast below AA:",nfail if nfail else "none")