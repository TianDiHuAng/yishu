# -*- coding: utf-8 -*-
"""Cycle153：人物 2 条（米勒 / 柯罗）。来源 CMA 艺术家记录（经藏品 1972.19 / 1963.91 取得）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-artist-millet","Cleveland Museum of Art — 艺术家记录：Jean-François Millet (1814–1875)",
  "https://openaccess-api.clevelandart.org/api/artworks/1972.19","2026-11-24 API HTTP 200；含馆方传记正文（经藏品 1972.19《田间归来》取得）"),
 ("cma-artist-corot","Cleveland Museum of Art — 艺术家记录：Jean Baptiste Camille Corot (1796–1875)",
  "https://openaccess-api.clevelandart.org/api/artworks/1963.91","2026-11-24 API HTTP 200；含馆方传记正文（经藏品 1963.91《罗马平原的切尔瓦拉》取得）"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('millet','让-弗朗索瓦·米勒','人物','art-neo-romantic','19世纪','法国','绘画','重要',
  '法国画家，1840年代末起专注描绘农民与乡村生活，1849年定居巴比松。','1814—1875年',
  '出身富裕农家，先在瑟堡随肖像画家学习，1837年靠城市津贴赴巴黎入美术学院，不久离开；早期以华托、布歇风格的粉彩小画谋生；1840年代末转向农民题材，在1848年革命背景下带有政治意味；1850—51年沙龙展出《播种者》受到关注，保守派指责他夸大农民的贫困，共和派与左翼则称其为对劳动阶层的有尊严的呈现；晚年取得成功，1867年巴黎世博会回顾展奠定声誉，次年获荣誉军团勋章。',
  'realism-art,courbet','cma-artist-millet'),
 ('corot','让·巴蒂斯特·卡米耶·柯罗','人物','art-neo-romantic','19世纪','法国','绘画','重要',
  '法国风景画家，1825—28年住罗马，早期风格结构严谨，1850年代起转向银灰色调的朦胧风景。','1796—1875年',
  '先随父从事服装业八年，1821年妹妹去世后获得的津贴使他得以专心绘画；1822年起师从米夏隆，其后师从贝尔坦；1825年首次赴意大利；1827年首次向巴黎沙龙送展；1840年代风格转向更复杂的光效与更暗的土绿色调；1850年代初再次转变，形成银灰色调与漫射光效；他把户外作品作为完成画的蓝本，但自由改编构图、光线与色彩，并称这类画室构成的风景为「paysage composé」；晚年转向单个人物。',
  'romanticism-art,corot-la-cervara','cma-artist-corot'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 2")
