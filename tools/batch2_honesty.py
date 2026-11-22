# -*- coding: utf-8 -*-
"""整批返工收尾：
1) 同步6个返工条目的 overview（首页卡片用）；
2) 对全部40条 batch2 L2 的"待核实"补一条批次级诚实声明。
"""
import json, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LD=os.path.join(ROOT,"data","l2")
batch=[e["id"] for e in json.load(open(os.path.join(ROOT,"batch2_input.json"),encoding="utf-8"))]
BATCH=set(batch)

def load(eid): return json.load(open(os.path.join(LD,eid+".json"),encoding="utf-8"))
def save(eid,o): json.dump(o,open(os.path.join(LD,eid+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)

ov={
 "realism-art":"反对浪漫化的历史与神话题材，主张客观描绘当下社会现实；库尔贝为代表。",
 "clerical-script":"由篆书简化而来，是汉字由古文字向今文字转变的关键；笔画形态术语待核。",
 "cursive-script":"张旭、怀素为代表书家，草书兼具强烈表现性与辨识门槛。",
 "roman-art":"以混凝土拱券与穹顶技术、写实肖像与历史叙事浮雕见长，万神殿为其建筑代表。",
 "donatello":"作品包括青铜《大卫》与《圣乔治》，推动古典雕塑复兴。",
 "romanesque":"以半圆拱与门楣、柱头叙事雕塑为特征，雕塑多用于教堂门楣与柱头。",
}
for eid,text in ov.items():
    o=load(eid); o["overview"]=text; save(eid,o)

NOTE=("【批次诚实声明】本条年代区间与部分技法术语源自 L1 种子，其中未被所引英文来源页逐字收录者"
      "已在正文改写为概括或列入本待核实节；精确年代与术语仍需第二独立来源（如专著/博物馆资料）确认。")
n=0
for eid in batch:
    p=os.path.join(LD,eid+".json")
    if not os.path.exists(p): continue
    o=json.load(open(p,encoding="utf-8"))
    s=o["sections"].get("待核实","")
    if NOTE not in s:
        o["sections"]["待核实"]=s+(" " if s else "")+NOTE
        save(eid,o); n+=1
print("synced overviews=%d; batch honesty note added to %d entries"%(len(ov),n))
