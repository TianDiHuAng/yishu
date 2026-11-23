# -*- coding: utf-8 -*-
"""Cycle84：欧洲巴洛克 4 条（佩德罗·德·梅纳、索尔达尼、卡拉瓦乔、拉图尔）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-2009-81","Cleveland Museum of Art — Pedro de Mena, Saint Peter of Alcántara, c. 1663–70, acc. 2009.81",
  "https://openaccess-api.clevelandart.org/api/artworks/2009.81","2026-11-23 API HTTP 200；彩绘木、象牙与玻璃 72.2×32×32cm；说明含分层工序与威尼斯玻璃眼"),
 ("cma-1992-230","Cleveland Museum of Art — Massimiliano Soldani, Apollo and Daphne, c. 1700, acc. 1992.230",
  "https://openaccess-api.clevelandart.org/api/artworks/1992.230","2026-11-23 API HTTP 200；陶土 55.5×34.2×21.9cm；说明含据贝尼尼1622—25大理石稿"),
 ("cma-1976-2","Cleveland Museum of Art — Caravaggio, The Crucifixion of Saint Andrew, 1606–7, acc. 1976.2",
  "https://openaccess-api.clevelandart.org/api/artworks/1976.2","2026-11-23 API HTTP 200；布面油画 202.5×152.7cm；说明含美国唯一祭坛画"),
 ("cma-1951-454","Cleveland Museum of Art — Georges de La Tour, Saint Peter Repentant, 1645, acc. 1951.454",
  "https://openaccess-api.clevelandart.org/api/artworks/1951.454","2026-11-23 API HTTP 200；布面油画 114×95cm；说明含与卡拉瓦乔关系未明"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('pedro-de-mena-peter','佩德罗·德·梅纳《圣佩德罗·德·阿尔坎塔拉》','作品','art-baroque','17世纪','欧洲','雕塑','核心',
  '西班牙彩绘木雕，克利夫兰艺术博物馆藏（2009.81）。','约1663—1670年',
  '由主雕刻师与工匠协作完成；粗布以黄色笔触表现，玻璃眼可能来自威尼斯，加上睫毛以求逼真。','baroque,velazquez,rodin','cma-2009-81'),
 ('soldani-apollo-daphne','索尔达尼《阿波罗与达芙妮》','作品','art-baroque','18世纪','欧洲','雕塑','重要',
  '佛罗伦萨陶土小稿，克利夫兰艺术博物馆藏（1992.230）。','约1700年',
  '取材达芙妮化月桂的瞬间；以动态构图、转瞬即逝与形体转化体现1600年代意大利关注；据贝尼尼1622—25大理石像。','baroque,caravaggio','cma-1992-230'),
 ('caravaggio-andrew','卡拉瓦乔《圣安德烈受难》','作品','art-baroque','17世纪','欧洲','绘画','核心',
  '那不勒斯祭坛画，克利夫兰艺术博物馆藏（1976.2）。','1606—1607年',
  '以亲密、私人的受难场景替代公开酷刑；强烈明暗暗示神在场；该馆称为画家在美国的唯一祭坛画。','caravaggio,baroque','cma-1976-2'),
 ('la-tour-peter','拉图尔《悔悟的圣彼得》','作品','art-baroque','17世纪','欧洲','绘画','核心',
  '法国布面油画，克利夫兰艺术博物馆藏（1951.454）。','1645年',
  '红眼与不确定灯火写长夜焦虑；色彩沉静、形体简朴；与卡拉瓦乔的关系该馆称仍不清楚。','caravaggio,rembrandt','cma-1951-454'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")