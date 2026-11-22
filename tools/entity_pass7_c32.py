# -*- coding: utf-8 -*-
"""Cycle32 pass7：中国专题条目的别名检索（中文同义词），列出候选供人工判定。"""
import json,os,sys
sys.path.insert(0,os.path.dirname(os.path.abspath(__file__)))
from wd_api import search
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
Q={
 "china-painting-history":["中国绘画","中国绘画史","中国画"],
 "tang-painting":["唐朝绘画","唐代绘画"],
 "song-painting":["宋朝绘画","宋代绘画"],
 "yuan-painting":["元朝绘画","元代绘画"],
 "ming-painting":["明朝绘画","明代绘画"],
 "qing-painting":["清朝绘画","清代绘画"],
 "xieyi":["写意","写意画"],
 "yangshao-painted-pottery":["仰韶文化","彩陶"],
 "chinese-jade-art":["玉器","中国玉文化"],
 "shang-zhou-bronzes":["青铜器","中国青铜器"],
 "dunhuang-art":["敦煌莫高窟","敦煌"],
 "six-dynasties-art":["魏晋南北朝","六朝"],
 "china-music-history":["中国音乐","中国音乐史"],
 "pipa":["琵琶"],
 "wuwangdu-chu-music-archaeology":["武王墩"],
}
out={}
for eid,terms in Q.items():
    cands=[]
    for t in terms:
        s,err=search(t,"zh",4)
        if err: continue
        for q,lbl,desc in s:
            if any(c["qid"]==q for c in cands): continue
            cands.append({"query":t,"qid":q,"label":lbl,"desc":(desc or "")[:70]})
    out[eid]=cands
    print("==",eid,"|",[(c["qid"],c["label"],c["desc"][:34]) for c in cands[:4]])
json.dump(out,open(os.path.join(ROOT,"reports","entity_pass7_c32.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)