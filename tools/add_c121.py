# -*- coding: utf-8 -*-
"""Cycle121：清代玉器 4 条（玉山/龙耳杯/玉卧牛/玉马）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1941-594","Cleveland Museum of Art — Miniature Mountain with Daoist Paradise, Qianlong, acc. 1941.594",
  "https://openaccess-api.clevelandart.org/api/artworks/1941.594","2026-11-24 API HTTP 200；带褐斑青玉 17.5cm；说明含道教仙山与饮玉屑露"),
 ("cma-1920-424","Cleveland Museum of Art — Cup with Dragon Handles, Kangxi, acc. 1920.424",
  "https://openaccess-api.clevelandart.org/api/artworks/1920.424","2026-11-24 API HTTP 200；灰绿白玉 径14.6cm；说明含三龙抓沿/寿字/陆子刚款"),
 ("cma-1962-223","Cleveland Museum of Art — Reclining Water Buffalo, Kangxi, acc. 1962.223",
  "https://openaccess-api.clevelandart.org/api/artworks/1962.223","2026-11-24 API HTTP 200；玉 6.2×7.7cm；说明含奢侈品受众扩大"),
 ("cma-1952-480","Cleveland Museum of Art — Horse (jade), Qing, 1600s, acc. 1952.480",
  "https://openaccess-api.clevelandart.org/api/artworks/1952.480","2026-11-24 API HTTP 200；玉 3.4cm；说明含文人案头清玩"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('qianlong-jade-mountain','乾隆玉雕仙山','作品','art-ancient','18世纪','中国','雕塑','核心',
  '乾隆青玉带褐斑玉山，克利夫兰艺术博物馆藏（1941.594）。','1736—1795年',
  '大料玉雕山形，表寻仙访道之境；玉被认为有灵性，古用于墓葬保体存魂；道士晨饮玉屑露以求长生。','liangzhu-bi-disc,shang-jade-ge','cma-1941-594'),
 ('kangxi-jade-dragon-cup','康熙玉龙耳杯','作品','art-ancient','17—18世纪','中国','雕塑','核心',
  '康熙灰绿白玉杯，克利夫兰艺术博物馆藏（1920.424）。','1662—1722年',
  '三龙抓沿、外壁「寿」字；龙耳饮杯为精英奢侈品；色工近苏州供宫廷/士绅/商人作坊；乐观署款陆子刚或借名招客。','qianlong-jade-mountain,qing-jade-horse','cma-1920-424'),
 ('kangxi-jade-buffalo','康熙玉卧牛','作品','art-ancient','17—18世纪','中国','雕塑','重要',
  '康熙玉卧牛，克利夫兰艺术博物馆藏（1962.223）。','1642—1722年',
  '明清奢侈品受众扩大至女性/商人/在野文人；帝室赞助与城市人口增长促消费；competitive market 中竞艺觅客。','kangxi-jade-dragon-cup,qing-jade-horse','cma-1962-223'),
 ('qing-jade-horse','清代玉马','作品','art-ancient','17世纪','中国','雕塑','重要',
  '清代玉马，克利夫兰艺术博物馆藏（1952.480）。','1600年代',
  '科举取仕，文人官员案头置珍玩以遣兴显品味；文房清玩（镇纸/印盒/笔架/水滴/玉山等）材质自玉至瓷，明清亦成藏品。','kangxi-jade-buffalo,qianlong-jade-mountain','cma-1952-480'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")