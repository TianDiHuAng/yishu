# -*- coding: utf-8 -*-
"""Cycle70：乐器再补 4 条（琵琶、筝、一節切、曼贝图竖琴）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1918-344","Cleveland Museum of Art — Pipa, China (Qing), 1800s, acc. 1918.344",
  "https://openaccess-api.clevelandart.org/api/artworks/1918.344","2026-11-23 API HTTP 200；木、象牙、骨、肠弦 95.4×27.4×8cm；说明含琵琶名义与丝路传播"),
 ("cma-1918-359","Cleveland Museum of Art — Koto (Zither), Japan (Edo), early–mid 1800s, acc. 1918.359",
  "https://openaccess-api.clevelandart.org/api/artworks/1918.359","2026-11-23 API HTTP 200；木、彩漆、蒔绘、织物、丝弦 117.8cm；说明含装饰性用途"),
 ("cma-1921-914","Cleveland Museum of Art — End-blown Flute (Hitoyogiri), Japan (Meiji), late 1800s, acc. 1921.914",
  "https://openaccess-api.clevelandart.org/api/artworks/1921.914","2026-11-23 API HTTP 200；漆竹、金银蒔绘 33.5×2.6cm；说明含与普化尺八之别"),
 ("cma-1929-344","Cleveland Museum of Art — Figurative harp (domu or kundi), Mangbetu, by 1928, acc. 1929.344",
  "https://openaccess-api.clevelandart.org/api/artworks/1929.344","2026-11-23 API HTTP 200；木、皮革、纤维、金属、玻璃珠；柄36.9cm 鼓18.2cm；说明含 Paul Travis 1928 年采集")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('pipa-instrument','琵琶','作品','music-instruments','19世纪','东亚','音乐体裁','核心',
    '清代琵琶，克利夫兰艺术博物馆藏（1918.344）。','1800年代',
    '「琵琶」二字描述右手动作：pi（向前弹）、pa（向后挑）；用于戏曲与说唱合奏，并有高难度独奏曲目。','guqin-instrument,koto-instrument','cma-1918-344'),
   ('koto-instrument','筝（koto，日本）','作品','music-instruments','19世纪','东亚','音乐体裁','重要',
    '江户时代装饰性筝，克利夫兰艺术博物馆藏（1918.359）。','1800年代初至中期',
    '表面装饰极为繁复，说明它更可能作为**观赏对象**而非演奏乐器；纹样为菊与芒草、柴垣及一对蝴蝶。','pipa-instrument,hitoyogiri-flute','cma-1918-359'),
   ('hitoyogiri-flute','一節切（hitoyogiri 竹笛）','作品','music-instruments','19世纪','东亚','音乐体裁','重要',
    '明治时期漆竹笛，克利夫兰艺术博物馆藏（1921.914）。','1800年代末',
    '被视为尺八的一类，16—17世纪流行；较普化尺八更小、音量更弱，19世纪短暂复兴时称「小竹」。','koto-instrument,guqin-instrument','cma-1921.914'),
   ('mangbetu-harp','曼贝图竖琴（domu 或 kundi）','作品','music-instruments','20世纪','非洲','音乐体裁','重要',
    '刚果北部曼贝图风格五弦竖琴，克利夫兰艺术博物馆藏（1929.344）。','1928年以前',
    '北部刚果诸族皆有带人形装饰的五弦旋律竖琴；细长头骨为曼贝图特征；常为男女歌者伴奏。','drum-ngoma,kora-instrument','cma-1929-344')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")