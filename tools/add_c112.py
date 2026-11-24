# -*- coding: utf-8 -*-
"""Cycle112：非洲 4 条（马林凯 suruku 盔面具、彭德 gambanda 女面、卢巴 nkishi 灵力像、布瓦水牛面具）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-2004-84","Cleveland Museum of Art — Helmet Mask (suruku), Malinke, mid–late 1800s, acc. 2004.84",
  "https://openaccess-api.clevelandart.org/api/artworks/2004.84","2026-11-23 API HTTP 200；木与或树脂 47cm；说明含 Korè 会社与成人礼"),
 ("cma-2008-150","Cleveland Museum of Art — Female Mask (Gambanda), Pende, early 1900s, acc. 2008.150",
  "https://openaccess-api.clevelandart.org/api/artworks/2008.150","2026-11-23 API HTTP 200；木纤维颜料 27×22×28.5cm；说明含酋长之妻与发型"),
 ("cma-1974-212","Cleveland Museum of Art — Figure (Nkishi), Luba, late 1800s–early 1900s, acc. 1974.212",
  "https://openaccess-api.clevelandart.org/api/artworks/1974.212","2026-11-23 API HTTP 200；木有机材纤维玻璃珠 22.4×10.7×12.4cm；说明含 mankishi 灵力物"),
 ("cma-1969-2","Cleveland Museum of Art — Buffalo Mask, Bwa, early–mid 1900s, acc. 1969.2",
  "https://openaccess-api.clevelandart.org/api/artworks/1969.2","2026-11-23 API HTTP 200；木纤维颜料铁 69.8cm；说明含灌木水牛与护佑"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('malinke-helmet-mask','马林凯 suruku 盔面具','作品','art-africa','19世纪','非洲','雕塑','核心',
  '马林凯「鬣狗」盔面具，克利夫兰艺术博物馆藏（2004.84）。','1800年代中—后期',
  '兼具兽与人特征；属 Korè 会社（六大会社之一，源自巴姆巴拉）；用于男童割礼与成人礼，或为会社各级之标识。','bwa-buffalo-mask,kuba-bwoom-mask','cma-2004-84'),
 ('gambanda-female-mask','彭德 gambanda 女面具','作品','art-africa','20世纪','非洲','雕塑','核心',
  '彭德风格女面具，克利夫兰艺术博物馆藏（2008.150）。','1900年代初',
  '代表酋长之妻 gambanda；依彭德性别面相观，表现女子理想的平静顺从；数百小辫仿时髦发型；雕刻家世袭、常村外作业。','luba-bowl-figure,malinke-helmet-mask','cma-2008-150'),
 ('nkishi-power-figure','卢巴 nkishi 灵力像','作品','art-africa','19—20世纪','非洲','雕塑','核心',
  '卢巴 mankishi 半身灵力像，克利夫兰艺术博物馆藏（1974.212）。','1800年代末—1900年代初',
  '布覆颅腔内藏物示其为灵力物 mankishi；由仪式专家用于治疗/护佑/占卜/裁断；多由仪式专家而非职业艺匠雕成。','luba-bowl-figure,kongo-nkisi-nkondi','cma-1974-212'),
 ('bwa-buffalo-mask','布瓦水牛面具','作品','art-africa','20世纪','非洲','雕塑','核心',
  '布瓦水牛面具，克利夫兰艺术博物馆藏（1969.2）。','1900年代早—中期',
  '布瓦面具以人/兽/奇幻特征表护佑的灌木精灵；角与吻示为灌木水牛；旱季于成人礼/长老葬礼/集市/丰收与年度更新仪式起舞。','malinke-helmet-mask,gambanda-female-mask','cma-1969-2'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")