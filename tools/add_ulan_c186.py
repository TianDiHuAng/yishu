# -*- coding: utf-8 -*-
"""Cycle186：给3个核心视觉艺术家人物条目（米开朗基罗、卡拉瓦乔、康定斯基）追加盖蒂 ULAN 来源。
这3位在 c185 精确标签查询中落空，本轮改用前缀查询，并从同名候选中按职业与生卒年选定。
只比对生卒年与职业；不改 when、不改正文。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
ULAN="https://vocab.getty.edu/ulan/"
TAG="（ULAN 对照，2026-11-24）"
M={
 'michelangelo':('500010654','Buonarroti, Michelangelo','Italian sculptor, painter, architect, 1475-1564','生卒年1475—1564与本条目 when 一致；职业为雕塑家、画家与建筑师，与本条目相容。ULAN 另有同名候选（Michelangelo dell\'Ocha、Buonarroti, Michelangelo, II 等），职业或年代不符，未采用。'),
 'caravaggio':('500115312','Caravaggio, Michelangelo Merisi da','Italian painter, 1571-1610','生卒年1571—1610与本条目 when 一致；职业为画家，与本条目相容。ULAN 另有同名候选（Caravaggio, Cecco del；Caravaggio, Gianni），年代或职业不符，未采用。'),
 'kandinsky':('500021093','Kandinsky, Vassily','Russian painter, 1866-1944','生卒年1866—1944与本条目 when 一致；职业为画家，与本条目相容。ULAN 标签拼写为 Vassily，与常见写法 Wassily 不同，此前精确标签查询因此落空。'),
}
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for eid,(num,label,bio,_) in M.items():
    sid="ulan-"+num
    if sid not in have:
        sd["sources"].append({"id":sid,"title":"Getty ULAN — %s, %s"%(label,num),"author":"J. Paul Getty Trust（Union List of Artist Names，开放词表）","year":"2026","url":ULAN+num,"type":"权威机构词表（人物名称与生平）","verified":True,
            "verified_note":"2026-11-24 经 vocab.getty.edu SPARQL 接口取回该人物的标签与简介（%s），编号与标签匹配，生卒年已与库内条目对照"%bio})
        have.add(sid)
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
for eid,(num,label,bio,note) in M.items():
    p=os.path.join(D,"l2",eid+".json")
    j=json.load(open(p,encoding="utf-8"))
    sid="ulan-"+num
    if sid not in j["sources"]: j["sources"].append(sid)
    t=j["sections"].get("待核实","")
    if TAG not in t: j["sections"]["待核实"]=t+TAG+"ULAN 简介："+bio+"。"+note
    json.dump(j,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("l2 updated",len(M))
