# -*- coding: utf-8 -*-
"""Cycle74：中国陶瓷再补 4 条（唐三彩镇墓俑、青白瓷碗、定窑鸭纹碗、成化斗彩杯）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-2000-118-1","Cleveland Museum of Art — Tomb Guardian with Animal Head (sancai), Tang, early 700s, acc. 2000.118.1",
  "https://openaccess-api.clevelandart.org/api/artworks/2000.118.1","2026-11-23 API HTTP 200；三彩釉陶 92.3×43.8×41.9cm；说明含出丧游行与孝道"),
 ("cma-2020-173-1-a","Cleveland Museum of Art — Qingbai Ware Bowl, Southern Song, 1100s–1200s, acc. 2020.173.1.a",
  "https://openaccess-api.clevelandart.org/api/artworks/2020.173.1.a","2026-11-23 API HTTP 200；青白瓷配银扣 8.2×14.5cm；说明含三种釉色对三种材质的模仿"),
 ("cma-1929-995","Cleveland Museum of Art — Bowl with Ducks among Waves and Reeds, Ding ware, 1100s, acc. 1929.995",
  "https://openaccess-api.clevelandart.org/api/artworks/1929.995","2026-11-23 API HTTP 200；奶油釉白瓷 20.3×5.4cm；说明含倒烧与「泪痕」"),
 ("cma-1957-61","Cleveland Museum of Art — Wine Cup with Children at Play, Chenghua, 1465–87, acc. 1957.61",
  "https://openaccess-api.clevelandart.org/api/artworks/1957.61","2026-11-23 API HTTP 200；釉下青花加釉上彩（斗彩） 高4.8cm；说明含二次烧工艺")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('tang-tomb-guardian','唐三彩镇墓兽','作品','art-ceramics','8世纪','中国','雕塑','核心',
    '陕西（推定西安）唐三彩釉陶镇墓兽，克利夫兰艺术博物馆藏（2000.118.1）。','700年代初',
    '兽面长双角，另一件人面巨耳；用于守墓门、辟邪并防亡魂游荡；出丧时先经街市游行。','jun-numbered-bulb-bowl,yuan-blue-white-jar','cma-2000-118-1'),
   ('qingbai-silver-bowl','青白瓷银扣碗','作品','art-ceramics','12—13世纪','中国','综合','重要',
    '南宋青白瓷碗，配银扣，克利夫兰艺术博物馆藏（2020.173.1.a）。','1100—1200年代',
    '深釉仿黑漆、青瓷比绿玉、青白瓷则仿银；口沿银带强化「贵重」观感；莲纹亦可能指佛教语境。','ding-tea-bowl,ding-duck-bowl','cma-2020-173-1-a'),
   ('ding-duck-bowl','定窑鸭纹碗','作品','art-ceramics','12世纪','中国','综合','重要',
    '曲阳定窑刻花碗，克利夫兰艺术博物馆藏（1929.995）。','1100年代',
    '胎薄釉润，上品为北宋宫廷选用；倒烧故口沿无釉，可加铜或金银包边；釉流成「泪痕」。','ding-tea-bowl,qingbai-silver-bowl','cma-1929-995'),
   ('chenghua-doucai-cup','成化斗彩儿童纹杯','作品','art-ceramics','15世纪','中国','综合','核心',
    '景德镇成化款斗彩酒杯，克利夫兰艺术博物馆藏（1957.61）。','1465—1487年',
    '高仅约两英寸；先以钴蓝勾线、施釉烧成青花，再于釉上加彩二次入窑；胎极薄透、质轻。','yuan-blue-white-jar,jun-numbered-bulb-bowl','cma-1957-61')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")