# -*- coding: utf-8 -*-
"""Cycle131：中国家具/漆器 4 条（乾隆剔红卷轴盒、明式翘头案、圈背椅、炕桌）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1969-32","Cleveland Museum of Art — Carved Lacquer Scroll Box, Qianlong, 1736–95, acc. 1969.32",
  "https://openaccess-api.clevelandart.org/api/artworks/1969.32","2026-11-24 API HTTP 200；木胎朱漆剔红 59×14.7×14cm；说明含五爪龙与1787造办处记录"),
 ("cma-1955-42","Cleveland Museum of Art — Ming side table with everted ends, acc. 1955.42",
  "https://openaccess-api.clevelandart.org/api/artworks/1955.42","2026-11-24 API HTTP 200；红木贴面樟木 88×51.8cm；说明含榫卯与翘头"),
 ("cma-1955-40","Cleveland Museum of Art — Pair of Lohan roundback armchairs, huanghuali, acc. 1955.40",
  "https://openaccess-api.clevelandart.org/api/artworks/1955.40","2026-11-24 API HTTP 200；黄花梨 85.4×58.4cm；说明含苏作与河姆渡榫卯"),
 ("cma-1964-228","Cleveland Museum of Art — Kang table with dragons in clouds, huanghuali, acc. 1964.228",
  "https://openaccess-api.clevelandart.org/api/artworks/1964.228","2026-11-24 API HTTP 200；黄花梨与金属 29×97.2×69.2cm；说明含炕与南方榻"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('qianlong-carved-lacquer-scrollbox','乾隆剔红龙纹卷轴盒','作品','art-asia','18世纪','东亚','综合','核心',
  '乾隆木胎朱漆剔红卷轴盒，克利夫兰艺术博物馆藏（1969.32）。','1736—1795年',
  '两端五爪龙（唯帝王可用），龙穿云水；剔刻精细而构图整肃；曾盛乾隆及皇后与11位宠妃私像；苏州承制；造办处记录载1787年龙纹盒设计。','jiajing-carved-lacquer-jar,ming-side-table-everted','cma-1969-32'),
 ('ming-side-table-everted','明式翘头案','作品','art-asia','16—17世纪','东亚','综合','核心',
  '明式红木贴面樟木翘头案，克利夫兰艺术博物馆藏（1955.42）。','1500年代末—1600年代',
  '中国家具为榫卯框架的木工艺术；牙板饰云头角牙，腿足间嵌云头开光透雕；面窄而长、两端上翘（翘头）更显正式，或作供案。','ming-lohan-armchairs,kang-table-dragons','cma-1955-42'),
 ('ming-lohan-armchairs','明式圈背椅（罗汉式，一对）','作品','art-asia','16—18世纪','东亚','综合','核心',
  '黄花梨圈背椅一对，克利夫兰艺术博物馆藏（1955.40）。','1600—1700年代',
  '中国自席地而坐转为高足家具；地域风格各异；此马蹄背椅产于江苏，简约雅致为苏作风格；靠背以七块木拼接插入木销，榫卯技法最早见于河姆渡新石器残件。','ming-side-table-everted,kang-table-dragons','cma-1955-40'),
 ('kang-table-dragons','云龙纹炕桌','作品','art-asia','17—18世纪','东亚','综合','核心',
  '黄花梨嵌金属云龙纹炕桌，克利夫兰艺术博物馆藏（1964.228）。','1600—1700年代',
  '炕桌原置砖砌火炕（北方冬作卧居），日间两人对坐、桌置其间；南方暖地则用于木榻；明清多用黄花梨等珍稀硬木。','ming-lohan-armchairs,ming-side-table-everted','cma-1964-228'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")