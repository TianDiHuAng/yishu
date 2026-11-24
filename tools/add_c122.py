# -*- coding: utf-8 -*-
"""Cycle122：中国陶瓷/版印 4 条（元狮首罐、嘉靖剔彩罐、永乐甜白梅瓶、十竹斋画谱）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1962-154","Cleveland Museum of Art — Yuan jar with lion-head handles, Jingdezhen, acc. 1962.154",
  "https://openaccess-api.clevelandart.org/api/artworks/1962.154","2026-11-24 API HTTP 200；青花 39.4×37.5cm 口径15.6cm；说明含伊朗钴料与云肩纹"),
 ("cma-1972-14","Cleveland Museum of Art — Carved lacquer jar with dragon and phoenix, Jiajing, acc. 1972.14",
  "https://openaccess-api.clevelandart.org/api/artworks/1972.14","2026-11-24 API HTTP 200；剔彩 11.8cm；说明含福寿/龙凤/嘉靖款"),
 ("cma-1964-167","Cleveland Museum of Art — Meiping vase, Yongle, acc. 1964.167",
  "https://openaccess-api.clevelandart.org/api/artworks/1964.167","2026-11-24 API HTTP 200；白釉暗花 32.1cm 径20.3cm；说明含甜白与暗花"),
 ("cma-1984-45b","Cleveland Museum of Art — Ten Bamboo Studio Collection, Nanjing, 1633, acc. 1984.45",
  "https://openaccess-api.clevelandart.org/api/artworks/1984.45","2026-11-24 API HTTP 200；木版套印首版 23.7×27.9cm；说明含饾版拱花与日韩影响"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('yuan-lion-jar','元青花狮首罐','作品','art-ceramics','14世纪','中国','陶瓷','核心',
  '景德镇元青花罐，克利夫兰艺术博物馆藏（1962.154）。','1300年代',
  '造型有力、发色艳丽、线条坚挺，为元青花典范；钴料自伊朗（或卡尚）进口；云肩纹配凤穿花亦见伊尔汗装饰艺术；1330s 前已供内外销。','yuan-blue-white-jar,ilkhanid-flying-birds-bowl','cma-1962-154'),
 ('jiajing-carved-lacquer-jar','嘉靖剔彩龙凤罐','作品','art-ceramics','16世纪','中国','综合','核心',
  '嘉靖剔彩罐，克利夫兰艺术博物馆藏（1972.14）。','1522—1566年',
  '凤与龙间置「福」「壽」二字；黑/赭/绿/朱多层漆；类似同期五彩瓷；龙凤为宫廷徽记；底刻「大明嘉靖年制」。','qianlong-jade-mountain,chenghua-doucai-cup','cma-1972-14'),
 ('yongle-meiping-cloud','永乐甜白暗花梅瓶','作品','art-ceramics','15世纪','中国','陶瓷','核心',
  '景德镇永乐白釉暗花梅瓶，克利夫兰艺术博物馆藏（1964.167）。','1403—1424年',
  '胎上暗刻「hidden decoration (anhua)」；釉白莹润如「melting snow」，鉴藏家称 tianbai 甜白；用于宫廷祭祀。','yuan-lion-jar,chenghua-doucai-cup','cma-1964-167'),
 ('ten-bamboo-album','十竹斋书画谱（1633 初版）','作品','art-china-calligraphy','17世纪','中国','版画','核心',
  '南京胡正言十竹斋书画谱初版，克利夫兰艺术博物馆藏（1984.45）。','1633年',
  '17世纪初彩印臻于极致；「画一般印刷」质感、饾版对位精准、设色和谐；行销全国并影响日韩艺术。','chen-jiru-four-poems,china-calligraphy-history','cma-1984-45b'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")