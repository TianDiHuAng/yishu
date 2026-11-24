# -*- coding: utf-8 -*-
"""Cycle123：印度2+埃及2（查重通过）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-2021-11","Cleveland Museum of Art — Portrait of Maharaja Rai Singh of Bikaner, c. 1610, acc. 2021.11",
  "https://openaccess-api.clevelandart.org/api/artworks/2021.11","2026-11-24 API HTTP 200；胶彩与金 25.4×38.1cm；说明含侍阿克巴/女嫁贾汉吉尔"),
 ("cma-2018-174","Cleveland Museum of Art — Drawing of a Man's Head, Kishangarh, c. 1780, acc. 2018.174",
  "https://openaccess-api.clevelandart.org/api/artworks/2018.174","2026-11-24 API HTTP 200；胶彩与金 22.6×16.5cm；说明含肖像草稿惯例"),
 ("cma-1930-735","Cleveland Museum of Art — Relief of Nyankhnesut, Saqqara, c. 2311–2281 BCE, acc. 1930.735",
  "https://openaccess-api.clevelandart.org/api/artworks/1930.735","2026-11-24 API HTTP 200；彩绘石灰岩 98.7×80.6cm；说明含15馆藏分散与2000年定位"),
 ("cma-1914-661","Cleveland Museum of Art — Block Statue of Djedbastetiufankh, Dyn. 25–26, acc. 1914.661",
  "https://openaccess-api.clevelandart.org/api/artworks/1914.661","2026-11-24 API HTTP 200；石灰岩 26.1×14×19.2cm；说明含块像几不可碎与波斯期袍"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('rai-singh-bikaner','比卡内尔王公莱·辛格像','作品','art-asia','17世纪','南亚','绘画','重要',
  '拉贾斯坦比卡内尔王公肖像，克利夫兰艺术博物馆藏（2021.11）。','约1610年',
  '肥胖拉杰普特王，左臂下系带长袍为多数印度教徒之俗；浆果色衣配绿松石背景喻天堂；或依 Nur Muhammad 底稿；曾侍阿克巴、女嫁贾汉吉尔。','shri-raga-mewar,jagat-singh-hunting','cma-2021-11'),
 ('rajasthan-head-drawing','基什加尔人头画稿','作品','art-asia','18世纪','南亚','绘画','重要',
  '基什加尔人头画稿，克利夫兰艺术博物馆藏（2018.174）。','约1780年',
  '头像习作，或为成品肖像之稿；画师常先画人物草稿备后用；眉/眼/须重勾勒，面部则以柔色塑形。','utka-nayika,rai-singh-bikaner','cma-2018-174'),
 ('nyankhnesut-relief','尼安赫涅苏特坐像浮雕','作品','art-ancient','公元前23世纪','埃及','雕塑','核心',
  '萨卡拉第六王朝彩绘石灰岩浮雕，克利夫兰艺术博物馆藏（1930.735）。','约公元前2311—2281年',
  '高官 Nyankhnesut 墓浮雕散于15馆数私藏；2000年埃政府发掘定出墓址；题材以食物生产与供墓为中心，农事 activities 皆有标注。','amenhotep-tomb-relief,canopic-jar-26','cma-1930-735'),
 ('djedbastetiufankh-block-statue','杰德巴斯特提乌凡赫块状雕像','作品','art-ancient','公元前7世纪','埃及','雕塑','重要',
  '晚期25—26王朝石灰岩块像，克利夫兰艺术博物馆藏（1914.661）。','约公元前664—610年',
  '块像紧凑之形几乎不可碎；表现蹲坐抱膝、长袍贴体如立方；同期 Ankh-Hor 半身为行进像托 naos。','amenemhat-statue,minnefer-statue','cma-1914-661'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")