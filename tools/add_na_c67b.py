# -*- coding: utf-8 -*-
"""Cycle67b：北美再补 4 条（Maria Martinez 水罐、Ma Pe Wi 羚羊图、Tlingit 面具、Haida 渡鸦响器）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1986-1131","Cleveland Museum of Art — Water Jar (Olla), Maria Martinez, San Ildefonso Pueblo, before 1920, acc. 1986.1131",
  "https://openaccess-api.clevelandart.org/api/artworks/1986.1131","2026-11-23 API HTTP 200；陶器施化妆土 28.5×34cm；作者 Maria Martinez (c.1887–1980)"),
 ("cma-1928-313","Cleveland Museum of Art — Three Antelope, Ma Pe Wi (Velino Shije Herrera), 1920s, acc. 1928.313",
  "https://openaccess-api.clevelandart.org/api/artworks/1928.313","2026-11-23 API HTTP 200；纸本水粉 50.8×38.1cm；作者 Zia Pueblo, 1902–1973"),
 ("cma-1979-83","Cleveland Museum of Art — Mask, Tlingit, late 1800s–early 1900s, acc. 1979.83",
  "https://openaccess-api.clevelandart.org/api/artworks/1979.83","2026-11-23 API HTTP 200；桤木彩绘 21.4×17.2×8.9cm；说明含 Robert Joseph 1998 年追述"),
 ("cma-1921-1577","Cleveland Museum of Art — Raven Rattle, Haida, late 1800s–early 1900s, acc. 1921.1577",
  "https://openaccess-api.clevelandart.org/api/artworks/1921.1577","2026-11-23 API HTTP 200；木与颜料 31.8×9.3×11.2cm；说明含萨满与世俗酋长的双重使用")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('maria-martinez-olla','玛丽亚·马丁内斯黑陶水罐（olla）','作品','art-americas','20世纪','北美洲','综合','核心',
    '圣伊尔德丰索普韦布洛陶艺家 Maria Martinez 早期黑陶水罐，克利夫兰艺术博物馆藏（1986.1131）。','1920年以前',
    '被该馆称为「或许最著名的原住民艺术家」；她把原住民陶器从日用推向装饰艺术，黑亮釉色出自烧成技法。','sikyatki-jar,americas-art','cma-1986-1131'),
   ('ma-pe-wi-three-antelope','《三只羚羊》（Ma Pe Wi 绘）','作品','art-americas','20世纪','北美洲','绘画','重要',
    '齐亚普韦布洛画家 Ma Pe Wi（Velino Shije Herrera）纸上水粉，克利夫兰艺术博物馆藏（1928.313）。','1920年代',
    '三只羚羊跃过饰云纹的阶状形，上方有彩虹、雨云与太阳；用水彩等非传统媒材取自仪式的非神圣部分与陶绘母题。','maria-martinez-olla,americas-art','cma-1928-313'),
   ('tlingit-mask','特林吉特面具','作品','art-americas','19—20世纪','北美洲','雕塑','重要',
    '特林吉特桤木彩绘面具，克利夫兰艺术博物馆藏（1979.83）。','1800年代末—1900年代初',
    '面具身份已佚，或为某家族的神话祖先、或用于冬季仪式；该馆引 1998 年 Robert Joseph 的追述说明佩戴体验。','tlingit-totem-pole,haida-raven-rattle','cma-1979-83'),
   ('haida-raven-rattle','海达渡鸦响器','作品','art-americas','19—20世纪','北美洲','雕塑','重要',
    '海达木制彩绘响器，克利夫兰艺术博物馆藏（1921.1577）。','1800年代末—1900年代初',
    '渡鸦背负人形的响器或表现萨满作为（控天候、疗疾、寻兽）；后亦为世俗酋长于冬季仪式所用，成为权力象征。','tlingit-mask,americas-art','cma-1921-1577')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")