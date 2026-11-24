# -*- coding: utf-8 -*-
"""Cycle187：给10个视觉艺术家人物条目追加盖蒂 ULAN 来源（梵高、多纳泰罗，及德加、马奈、透纳、康斯太勃尔、库尔贝、安格尔、米勒、柯罗）。
全部用前缀查询列出同名候选后，按职业与生卒年选定；只比对生卒年与职业；不改 when、不改正文。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
ULAN="https://vocab.getty.edu/ulan/"
TAG="（ULAN 对照，2026-11-24）"
M={
 'van-gogh':('500115588','Gogh, Vincent van','Dutch painter and draftsman, 1853-1890','生卒年1853—1890与本条目 when 一致；职业为画家与素描家，与本条目相容。ULAN 另有两条同名 art dealer（1866-1911、1820-1888），是同名他人，未采用。'),
 'donatello':('500026022','Donatello','Italian sculptor, ca. 1386-1466','ULAN 写作 ca. 1386-1466，与本条目 when（约1386—1466年）一致；职业为雕塑家，与本条目相容。ULAN 另有两条同名候选（active 20th century 的 artist、无年代的 Italian artist），不是同一人，未采用。'),
 'degas':('500115194','Degas, Edgar','French painter, sculptor, 1834-1917','生卒年1834—1917与本条目 when 一致；职业为画家与雕塑家，与本条目相容。'),
 'manet':('500010363','Manet, Edouard','French painter, printmaker, and draftsman, 1832-1883','生卒年1832—1883与本条目 when 一致；职业为画家、版画家与素描家，与本条目相容。ULAN 另有 Julie Manet（画家，1878-1966）等同姓候选，不是同一人，未采用。'),
 'turner':('500026846','Turner, Joseph Mallord William','English painter and draftsman, 1775-1851','生卒年1775—1851与本条目 when 一致；职业为画家与素描家，与本条目相容。ULAN 另有 Turner, Joseph（建筑师与建造者，约1729-1807），不是同一人，未采用。'),
 'constable':('500115382','Constable, John','English landscapist, 1776-1837','生卒年1776—1837与本条目 when 一致；ULAN 简介为风景画家，与本条目相容。ULAN 另有 Constable, John Charles（1817-1841），不是同一人，未采用。'),
 'courbet':('500010927','Courbet, Gustave','French painter and designer, 1819-1877','生卒年1819—1877与本条目 when 一致；职业为画家与设计师，与本条目相容。'),
 'ingres':('500028037','Ingres, Jean-Auguste-Dominique','French painter and draftsman, 1780-1867','生卒年1780—1867与本条目 when 一致；职业为画家与素描家，与本条目相容。ULAN 另有 Ingres, Jean-Marie-Joseph（建筑师、画家与雕塑家，1755-1814），不是同一人，未采用。'),
 'millet':('500012529','Millet, Jean-François','French painter and draftsman, 1814-1875','生卒年1814—1875与本条目 when 一致；职业为画家与素描家，与本条目相容。ULAN 另有 Millet, Jean-Baptiste（1831-1906）与 Millet, Jean François（风景画家，1666-1723），不是同一人，未采用。'),
 'corot':('500115390','Corot, Jean-Baptiste-Camille','French painter, 1796-1875','生卒年1796—1875与本条目 when 一致；职业为画家，与本条目相容。'),
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
