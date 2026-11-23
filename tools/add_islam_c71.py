# -*- coding: utf-8 -*-
"""Cycle71：伊斯兰再补 4 条（清真寺灯、米纳伊杯、光泽彩盘、伊兹尼克砖）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1944-236","Cleveland Museum of Art — Mosque Lamp, Iznik, 1585–95, acc. 1944.236",
  "https://openaccess-api.clevelandart.org/api/artworks/1944.236","2026-11-23 API HTTP 200；fritware 釉下彩 28.4×19.5cm；说明含「非照明用」与声学推测"),
 ("cma-1917-977","Cleveland Museum of Art — Mina'i Beaker with Seated Princes, Kashan, 1180–1220, acc. 1917.977",
  "https://openaccess-api.clevelandart.org/api/artworks/1917.977","2026-11-23 API HTTP 200；fritware 釉上彩 13.3×12.3cm；说明含首次真多彩"),
 ("cma-1951-289","Cleveland Museum of Art — Luster Dish with Seated Prince, Kashan, 1170–1220, acc. 1951.289",
  "https://openaccess-api.clevelandart.org/api/artworks/1951.289","2026-11-23 API HTTP 200；fritware 光泽彩 7.5×39cm；说明含蓝釉于光泽地上的稀有做法"),
 ("cma-2004-70","Cleveland Museum of Art — Tile Spandrel with Floral Sprays, Iznik, c. 1570–75, acc. 2004.70",
  "https://openaccess-api.clevelandart.org/api/artworks/2004.70","2026-11-23 API HTTP 200；fritware 红化妆土与釉下彩 76×29.9×2.5cm；说明含缺右半与铁红技术")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('iznik-mosque-lamp','伊兹尼克清真寺灯','作品','art-islamic','16世纪','西亚·中亚','综合','重要',
    '奥斯曼伊兹尼克釉下彩清真寺灯，克利夫兰艺术博物馆藏（1944.236）。','1585—95年',
    '通常作灯罩、内盛油灯；此件因不透光，主要功能**很可能不是照明**，而是悬于寺内或陵墓增添美感。','iznik-dish-artichokes,iznik-tile-spandrel','cma-1944-236'),
   ('minai-beaker','米纳伊人物杯（坐着的王子）','作品','art-islamic','12—13世纪','西亚·中亚','综合','重要',
    '卡尚米纳伊（mina’i）釉上彩杯，克利夫兰艺术博物馆藏（1917.977）。','1180—1220年',
    'mina’i 之名出自波斯语「珐琅」；以釉上彩首次实现真正多彩瓷；图样多写宫廷列坐与王子狩猎。','luster-dish-prince,iznik-mosque-lamp','cma-1917-977'),
   ('luster-dish-prince','卡尚光泽彩人物盘','作品','art-islamic','12—13世纪','西亚·中亚','综合','重要',
    '卡尚光泽彩陶盘，克利夫兰艺术博物馆藏（1951.289）。','1170—1220年',
    '卡尚与巴士拉、福斯塔特并为伊斯兰陶瓷中心；此盘以**光泽地为底、蓝釉为纹**的稀有做法受称许。','minai-beaker,islamic-art','cma-1951-289'),
   ('iznik-tile-spandrel','伊兹尼克花卉纹砖（拱肩）','作品','art-islamic','16世纪','西亚·中亚','建筑','重要',
    '奥斯曼伊兹尼克釉下彩拱肩砖，克利夫兰艺术博物馆藏（2004.70）。','约1570—75年',
    '与已失的右半原构成龛、窗或门上方的装饰拱；浓烈红色由**铁质浓稠化妆土**实现，为当时技术成就。','iznik-mosque-lamp,iznik-dish-artichokes','cma-2004-70')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")