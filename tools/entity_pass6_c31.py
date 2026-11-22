# -*- coding: utf-8 -*-
"""Cycle31 pass6：人工指定检索词（针对 D030 的 19 条「其余」未锚定条目）。
每条给定 1–2 个英文检索词，取前 4 个候选（含标签与描述）供人工判定，不自动采纳。"""
import json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from wd_api import search
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
QUERIES={
 "prehistoric-art":["prehistoric art","Prehistoric art"],
 "cave-art":["cave painting","Cave painting"],
 "paleolithic-sculpture":["Paleolithic art","prehistoric sculpture"],
 "egyptian-art":["art of ancient Egypt","Egyptian art"],
 "greek-art":["ancient Greek art","Greek art"],
 "roman-art":["Roman art","ancient Roman art"],
 "romanesque":["Romanesque art"],
 "renaissance":["Renaissance art","Italian Renaissance art"],
 "romanticism-art":["Romantic art","Romanticism art movement"],
 "realism-art":["Realism art movement","realism in art"],
 "gregorian-chant":["Gregorian chant"],
 "opera":["opera","opera genre"],
 "tonality":["tonality","tonal music"],
 "symphony":["symphony genre","symphony musical form"],
 "20th-century-classical":["20th-century classical music","modern classical music"],
 "minimalism-music":["minimal music","minimalist music"],
 "buddhist-art-india":["Buddhist art"],
 "khmer-art":["Cambodian art","Khmer art"],
 "zen-painting":["Zenga","Zen painting"],
}
out={}
for eid,terms in QUERIES.items():
    cands=[]
    for t in terms:
        s,err=search(t,"en",4)
        if err: cands.append({"query":t,"error":err}); continue
        for q,lbl,desc in s:
            cands.append({"query":t,"qid":q,"label":lbl,"desc":(desc or "")[:80]})
    out[eid]=cands
    print("==",eid)
    for c in cands[:6]:
        print("   ",c.get("qid"),c.get("label"),"|",c.get("desc"))
json.dump(out,open(os.path.join(ROOT,"reports","entity_pass6_c31.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)