# -*- coding: utf-8 -*-
"""Cycle69：新增单元「乐器（跨文化）」+ 4 条乐器条目（科拉、西塔、古琴、恩戈马鼓）。
这些条目直接填 B2「非西方音乐」缺口：此前音乐类条目几乎全为西方体裁 + 中国音乐史。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1918-352","Cleveland Museum of Art — Kora, West Africa, before 1918, acc. 1918.352",
  "https://openaccess-api.clevelandart.org/api/artworks/1918.352","2026-11-23 API HTTP 200；葫芦、木、皮革、弦、绳 111.8cm；说明含21弦与修补痕"),
 ("cma-1918-346","Cleveland Museum of Art — Sitar, Eastern India (Bengal/Bangladesh), c. 1850, acc. 1918.346",
  "https://openaccess-api.clevelandart.org/api/artworks/1918.346","2026-11-23 API HTTP 200；葫芦与木、象牙、骨、铜品、铁弦 95.2×15.3cm"),
 ("cma-1918-371","Cleveland Museum of Art — Guqin by Zhang Ruixiu of Suzhou, 1584, acc. 1918.371",
  "https://openaccess-api.clevelandart.org/api/artworks/1918.371","2026-11-23 API HTTP 200；木、漆、螺钿、丝弦 123.5×18.1×4.5cm；内款涉严澂（1547–1625）"),
 ("cma-1929-343","Cleveland Museum of Art — Drum (ngoma), Eastern Africa, by 1928, acc. 1929.343",
  "https://openaccess-api.clevelandart.org/api/artworks/1929.343","2026-11-23 API HTTP 200；木、皮革、植物纤维 40cm/径31.2cm；说明含乌干达鼓中「心」")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

p=os.path.join(ROOT,"tools","catalog.py"); s=io.open(p,encoding="utf-8").read()
if '"music-instruments"' not in s:
    anchor=' ("work-archives","作品档案"),\n])'
    assert anchor in s
    s=s.replace(anchor,' ("music-instruments","乐器（跨文化）"),\n'+anchor)
    io.open(p,"w",encoding="utf-8").write(s); print("unit added")

T=[('kora-instrument','科拉琴（kora）','作品','music-instruments','19—20世纪','西非','音乐体裁','重要',
    '西非的21弦葫芦竖琴—琉特，克利夫兰艺术博物馆藏（1918.352）。','1918年以前',
    '弦沿长颈系结、以指弹拨，声在半球形葫芦体内共鸣；背面针脚显示葫芦曾多处修补。','sitar-instrument,drum-ngoma','cma-1918-352'),
   ('sitar-instrument','西塔琴（sitar）','作品','music-instruments','19世纪','南亚','音乐体裁','重要',
    '东印度（孟加拉／孟加拉国）所制西塔，克利夫兰艺术博物馆藏（1918.346）。','约1850年',
    '与维纳琴不同，西塔有可移动的金属品（frets），移位即变音高；宫廷演奏中常为主奏之器。','kora-instrument,guqin-instrument','cma-1918-346'),
   ('guqin-instrument','古琴（张瑞修制，1584）','作品','music-instruments','16世纪','东亚','音乐体裁','核心',
    '明万历十二年（1584）苏州张瑞修所制七弦琴，克利夫兰艺术博物馆藏（1918.371）。','1584年',
    '中国最受尊崇的乐器，可上溯楚文化约两千五百年；此琴内款记为海虞严澂（1547—1625）所作。','china-music-history,sitar-instrument','cma-1918-371'),
   ('drum-ngoma','恩戈马鼓（ngoma）','作品','music-instruments','20世纪','东非','音乐体裁','重要',
    '东非木腔蒙皮鼓，克利夫兰艺术博物馆藏（1929.343）。','1928年以前',
    '名称出自刚果语「鼓」；双重蒙皮以植物纤维绷紧，仅击第一层即共鸣；乌干达鼓内藏仅制作者知的仪式「心」。','kora-instrument,guqin-instrument','cma-1929-343')]
lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")