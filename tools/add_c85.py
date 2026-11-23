# -*- coding: utf-8 -*-
"""Cycle85：西方乐器/演奏图像 4 条（布拉克、杜蒙、朗克雷、杜萨特）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1968-196","Cleveland Museum of Art — Georges Braque, Violin, early 1914, acc. 1968.196",
  "https://openaccess-api.clevelandart.org/api/artworks/1968.196","2026-11-23 API HTTP 200；剪纸拼贴与炭笔 71.8×51.8cm；说明含1912年发明的 拼贴纸（papier collé）"),
 ("cma-1942-1139","Cleveland Museum of Art — François Dumont, Portrait of a Woman at a Harpsichord, c. 1788, acc. 1942.1139",
  "https://openaccess-api.clevelandart.org/api/artworks/1942.1139","2026-11-23 API HTTP 200；象牙水彩细密画 直径7.3cm；说明含索菲·阿尔努归属争议"),
 ("cma-2018-1058","Cleveland Museum of Art — Nicolas Lancret, Man Playing a Cello, c. 1725–30, acc. 2018.1058",
  "https://openaccess-api.clevelandart.org/api/artworks/2018.1058","2026-11-23 API HTTP 200；红粉笔 20.7×16cm；说明含右手运弓握法的特写"),
 ("cma-1943-562","Cleveland Museum of Art — Cornelis Dusart, Violin Player Seated in the Inn, 1685, acc. 1943.562",
  "https://openaccess-api.clevelandart.org/api/artworks/1943.562","2026-11-23 API HTTP 200；蚀刻 版口28.1×25cm；说明含酒馆场景与西勒诺斯典故"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('braque-violin-collage','布拉克《小提琴》拼贴画','作品','music-instruments','20世纪','欧洲','综合','核心',
  '布拉克1914年初剪纸拼贴画，克利夫兰艺术博物馆藏（1968.196）。','1914年初',
  '以报纸、仿木纹纸与花纹纸片加上炭笔勾线构成小提琴与玻璃杯；主题置于交错平面中。','cubism,picasso','cma-1968-196'),
 ('dumont-harpsichord-miniature','杜蒙《羽管键琴前的女子》细密画','作品','music-instruments','18世纪','欧洲','绘画','重要',
  '法国象牙水彩细密画，克利夫兰艺术博物馆藏（1942.1139）。','约1788年',
  '女子身份不明；两件 被归于他人的副本定名为索菲·阿尔努；弹琴被视为贵族女性的必要修养。','baroque-music,rococo','cma-1942-1139'),
 ('lancret-cello-drawing','朗克雷《演奏大提琴的男子》','作品','music-instruments','18世纪','欧洲','绘画','重要',
  '法国红粉笔素描，克利夫兰艺术博物馆藏（2018.1058）。','约1725—1730年',
  '为户外音乐会油画所作的人物稿；右上角特意刻画运弓之手的位置与紧握。','baroque-music,rococo','cma-2018-1058'),
 ('dusart-violin-tavern','杜萨特《酒馆中的小提琴手》','作品','music-instruments','17世纪','欧洲','绘画','重要',
  '荷兰蚀刻版画，克利夫兰艺术博物馆藏（1943.562）。','1685年',
  '音乐、欢笑与酒构成酒馆场景；站立者的姿态令人联想到西勒诺斯，警示纵酒。','baroque-music,rembrandt,vermeer','cma-1943-562'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")