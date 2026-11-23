# -*- coding: utf-8 -*-
"""Cycle82：中国绘画 4 条（王翚、董其昌、蓝瑛、仇英）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1953-629","Cleveland Museum of Art — Wang Hui, Tall Bamboo and Distant Mountains after Wang Meng, 1694, acc. 1953.629",
  "https://openaccess-api.clevelandart.org/api/artworks/1953.629","2026-11-23 API HTTP 200；纸本水墨立轴 79.6×39.4cm；说明含1686—1712多次临仿王蒙"),
 ("cma-1980-10","Cleveland Museum of Art — Dong Qichang, Mt. Qingbian, 1617, acc. 1980.10",
  "https://openaccess-api.clevelandart.org/api/artworks/1980.10","2026-11-23 API HTTP 200；纸本水墨立轴 225×67.6cm；说明含气/势与笔墨独立"),
 ("cma-1970-128","Cleveland Museum of Art — Lan Ying, Zhi and Xu's Pure Conversation, 1643, acc. 1970.128",
  "https://openaccess-api.clevelandart.org/api/artworks/1970.128","2026-11-23 API HTTP 200；纸本水墨立轴 141×56cm；说明含赠僧无云与明亡前一年"),
 ("cma-1978-67","Cleveland Museum of Art — Qiu Ying, Garden for Solitary Enjoyment, 1515–52, acc. 1978.67",
  "https://openaccess-api.clevelandart.org/api/artworks/1978.67","2026-11-23 API HTTP 200；绢本设色手卷 28×518.5cm；说明含司马光独乐园与苏州作坊模板"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('wang-hui-bamboo','王翚《仿王蒙高竹远山图》','作品','art-china-painting','17世纪','中国','绘画','核心',
  '王翚纸本水墨立轴，克利夫兰艺术博物馆藏（1953.629）。','1694年',
  '王翚自1686至1712年间多次临仿王蒙；此轴将高士自亭中移入溪畔山景，并把题识一并摹入。','du-jin-lin-bu,juran-buddhist-retreat','cma-1953-629'),
 ('dong-qichang-qingbian','董其昌《青弁图》','作品','art-china-painting','17世纪','中国','绘画','核心',
  '董其昌纸本水墨立轴，克利夫兰艺术博物馆藏（1980.10）。','1617年',
  '山形被组织为近乎抽象的结构，气与势贯穿全画；笔墨获得独立于所绘物象的生命。','zhao-mengfu-river-village,du-jin-lin-bu','cma-1980-10'),
 ('lan-ying-pure-conversation','蓝瑛《支许清谈图》','作品','art-china-painting','17世纪','中国','绘画','重要',
  '蓝瑛纸本水墨立轴，克利夫兰艺术博物馆藏（1970.128）。','1643年',
  '为禅僧无云所作，绘六朝高僧支遁与道士许询；以古人友谊类比己与僧人交谊，时在明亡前一年。','du-jin-lin-bu,zhao-mengfu-river-village','cma-1970-128'),
 ('qiu-ying-garden','仇英《独乐园图》','作品','art-china-painting','16世纪','中国','绘画','核心',
  '仇英绢本设色手卷，克利夫兰艺术博物馆藏（1978.67）。','1515—1552年',
  '图写司马光1073年退居洛阳所筑独乐园；七处建筑各关联一位历史人物；后成苏州作坊摹本范式。','chen-hongshou-album,du-jin-lin-bu','cma-1978-67'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")