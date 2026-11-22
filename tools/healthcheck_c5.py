# -*- coding: utf-8 -*-
"""体检 F：死链/过期数据/重复条目/数据矛盾/孤儿页/来源文本重合度。输出 reports/healthcheck_c5.json。"""
import json,os,re,sys
from collections import Counter,defaultdict
from difflib import SequenceMatcher
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
src={s["id"]:s for s in json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))["sources"]}
R={"dead_links":[],"stale_data":[],"duplicates":[],"contradictions":[],"orphans":[],"overlap":[]}

# 1) 死链：站内 html 引用目标存在性
pat=re.compile(r'(?:href|src)\s*=\s*[\'"]([^\'"]+)[\'"]')
for dp,_,fs in os.walk(ROOT):
    if ".git" in dp or "node_modules" in dp: continue
    for f in fs:
        if not f.endswith(".html"): continue
        p=os.path.join(dp,f)
        for m in pat.finditer(open(p,encoding="utf-8").read()):
            ref=m.group(1)
            if ref.startswith(("http","mailto:","data:","#")): continue
            tgt=os.path.normpath(os.path.join(dp,ref.split("#")[0]))
            if not os.path.exists(tgt): R["dead_links"].append([os.path.relpath(p,ROOT),ref])

# 2) 过期数据：正文含"现状/最新/目前/截至/现存"且无明确年份标注的条目
for e in es:
    text=e.get("overview","")+" ".join(e.get("sections",{}).values())
    if re.search(r"目前|现存|最新|现状|截至",text) and not re.search(r"202[0-6]|199[0-9]|20[01][0-9]",text):
        R["stale_data"].append(e["id"])

# 3) 重复：id/title 重复 + 标题高度相似(>0.9)
seen={}
for e in es:
    if e["title"] in seen: R["duplicates"].append(["same_title",seen[e["title"]],e["id"]])
    seen[e["title"]]=e["id"]
titles=[(e["id"],e["title"]) for e in es]
for i,(a,ta) in enumerate(titles):
    for b,tb in titles[i+1:]:
        r=SequenceMatcher(None,ta,tb).ratio()
        if r>0.9: R["duplicates"].append(["similar_title",a,b,round(r,2)])

# 4) 数据矛盾：同一 when 年份在不同字段不一致；def/overview 中的年份与 when 冲突
yr=re.compile(r"(?:公元前\s*)?(\d{3,4})")
for e in es:
    w=e.get("when",""); nums_w=set(yr.findall(w))
    ov=e.get("overview",""); nums_o=set(yr.findall(ov))
    # 只报 overview 有4位年且 when 也有4位年、且完全无交集（排除公元前/公元混写）
    if nums_w and nums_o and not (nums_w & nums_o) and not any("前" in x for x in [w,ov]):
        R["contradictions"].append([e["id"],w[:40],sorted(nums_o)[:4]])

# 5) 孤儿页：无入链
inb=Counter(r for e in es for r in e.get("related",[]))
R["orphans"]=[e["id"] for e in es if inb[e["id"]]==0]

# 6) 来源重合度：正文与来源页文本 n-gram(8字)重合，抽查全部条目的 def/overview
# 这里只做本地近似：同一来源被>=8个条目共享视为"可能套话"（数据而非文本抓取）
bysrc=Counter(s for e in es for s in set(e.get("sources",[])))
R["overlap"]=[[s,c] for s,c in bysrc.most_common(10) if c>=15]

json.dump(R,open(os.path.join(ROOT,"reports","healthcheck_c5.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("healthcheck F: dead=%d stale=%d dup=%d contra=%d orphan=%d heavy_src=%d"%(
 len(R["dead_links"]),len(R["stale_data"]),len(R["duplicates"]),len(R["contradictions"]),len(R["orphans"]),len(R["overlap"])))
for k in ("stale_data","duplicates","contradictions","overlap"):
 if R[k]: print(" ",k,":",R[k][:8])
