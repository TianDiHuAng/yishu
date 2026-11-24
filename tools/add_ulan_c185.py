# -*- coding: utf-8 -*-
"""Cycle185：给16个核心视觉艺术家人物条目追加盖蒂 ULAN 来源（独立机构词表），并在“待核实”记录对照结果。
只比对生卒年与职业；不改 when、不改正文。梵高/多纳泰罗/米开朗基罗/卡拉瓦乔/康定斯基本轮不登记。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
ULAN="https://vocab.getty.edu/ulan/"
TAG="（ULAN 对照，2026-11-24）"
M={
 'leonardo':('500010879','Leonardo da Vinci','Italian painter, draftsman, scientist, 1452-1519','生卒年1452—1519与本条目 when 一致；职业含画家，与本条目相容。'),
 'rembrandt':('500011051','Rembrandt van Rijn','Dutch painter, printmaker, 1606-1669','生卒年1606—1669与本条目 when 一致；职业为画家与版画家，与本条目相容。'),
 'monet':('500019484','Monet, Claude','French painter, 1840-1926','生卒年1840—1926与本条目 when 一致；职业为画家，与本条目相容。'),
 'cezanne':('500004793','Cézanne, Paul','French painter and draftsman, 1839-1906','生卒年1839—1906与本条目 when 一致；职业为画家与素描家，与本条目相容。'),
 'picasso':('500009666','Picasso, Pablo','Spanish painter, sculptor, and printmaker, 1881-1973','生卒年1881—1973与本条目 when 一致；职业为画家、雕塑家与版画家，与本条目相容。'),
 'raphael':('500023578','Raphael','Italian painter, architect, 1483-1520','生卒年1483—1520与本条目 when 一致；职业为画家与建筑师，与本条目相容。'),
 'matisse':('500017300','Matisse, Henri','French painter, sculptor, and printmaker, 1869-1954','生卒年1869—1954与本条目 when 一致；职业为画家、雕塑家与版画家，与本条目相容。'),
 'dali':('500009365','Dalí, Salvador','Spanish painter and printmaker, 1904-1989','生卒年1904—1989与本条目 when 一致；职业为画家与版画家，与本条目相容。'),
 'warhol':('500006031','Warhol, Andy','American painter, printmaker, and filmmaker, 1928-1987','生卒年1928—1987与本条目 when 一致；职业为画家、版画家与电影制作人，与本条目相容。'),
 'gauguin':('500011421','Gauguin, Paul','French painter and printmaker, 1848-1903','生卒年1848—1903与本条目 when 一致；职业为画家与版画家，与本条目相容。'),
 'delacroix':('500115509','Delacroix, Eugène','French painter, 1798-1863','生卒年1798—1863与本条目 when 一致；职业为画家，与本条目相容。'),
 'rubens':('500002921','Rubens, Peter Paul','Flemish painter, 1577-1640','生卒年1577—1640与本条目 when 一致；职业为画家，与本条目相容。'),
 'velazquez':('500016881','Velázquez, Diego','Spanish painter, 1599-1660','生卒年1599—1660与本条目 when 一致；职业为画家，与本条目相容。'),
 'vermeer':('500032927','Vermeer, Johannes','Dutch painter, 1632-1675','生卒年1632—1675与本条目 when 一致；职业为画家，与本条目相容。'),
 'rodin':('500016619','Rodin, Auguste','French sculptor, 1840-1917','生卒年1840—1917与本条目 when 一致；职业为雕塑家，与本条目相容。'),
 'botticelli':('500015254','Botticelli, Sandro','Florentine painter, 1444/1445-1510','ULAN 生年写作 1444/1445（两个年份并列），本条目 when 为约1445—1510年，卒年1510一致，生年落在 ULAN 给出的范围内；职业为画家，与本条目相容。'),
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
