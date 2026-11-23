# -*- coding: utf-8 -*-
"""Cycle95：非洲面具/雕像 4 条（Luba 持碗女像、Dogon 女像、Dogon satimbe 面具、Kuba bwoom 面具）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-2010-454","Cleveland Museum of Art — Female Bowl-Bearing Figure, Luba style, late 1800s–early 1900s, acc. 2010.454",
  "https://openaccess-api.clevelandart.org/api/artworks/2010.454","2026-11-23 API HTTP 200；木、玻璃珠、包钉、纤维、铁 40.8×16.1×27.3cm；说明含 mpemba 白垩与「美影响效力」"),
 ("cma-1976-172","Cleveland Museum of Art — Female Figure, Dogon style, c. 1940, acc. 1976.172",
  "https://openaccess-api.clevelandart.org/api/artworks/1976.172","2026-11-23 API HTTP 200；木 74.9cm；说明含三种解释"),
 ("cma-1960-169","Cleveland Museum of Art — Face Mask with Female Figure (satimbe), Dogon, acc. 1960.169",
  "https://openaccess-api.clevelandart.org/api/artworks/1960.169","2026-11-23 API HTTP 200；木与有机物 111.1cm；说明含 dama 与六十年 sigi"),
 ("cma-1935-304","Cleveland Museum of Art — Mask (Bwoom), Kuba style, mid–late 1800s, acc. 1935.304",
  "https://openaccess-api.clevelandart.org/api/artworks/1935.304","2026-11-23 API HTTP 200；木与颜料 43.3×31.2×28.3cm；说明含三面具组合与建国叙事"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('luba-bowl-figure','卢巴持碗女像','作品','art-africa','19—20世纪','非洲','雕塑','核心',
  '卢巴风格木雕持碗女像，克利夫兰艺术博物馆藏（2010.454）。','1800年代末—1900年代初',
  '卢巴美学认为「器物的美影响其效力」；像身残留 mpemba 白垩，说明曾盛圣粉；腰间胸前有菱形瘢纹。','kongo-nkisi-nkondi,african-art','cma-2010-454'),
 ('dogon-female-figure','多贡女像（举臂）','作品','art-africa','20世纪','非洲','雕塑','核心',
  '多贡风格木雕女像，克利夫兰艺术博物馆藏（1976.172）。','约1940年',
  '举臂可能指 Amma 所造第一个存在；另一说与求雨有关（黑化像象征祈求乌云）；第三说关联播种仪式。','dogon-satimbe-mask,african-art','cma-1976-172'),
 ('dogon-satimbe-mask','多贡 satimbe 面具（顶立女像）','作品','art-africa','20世纪','非洲','雕塑','重要',
  '多贡铁匠雕刻者木面具，克利夫兰艺术博物馆藏（1960.169）。','1900年代初至中期',
  '用于 dama 终丧仪式，面具化身祖先；顶部举臂女像为神话人物 Yasigine，关乎首次 sigi（每60年一次）。','dogon-female-figure,african-art','cma-1960-169'),
 ('kuba-bwoom-mask','库巴 bwoom 面具','作品','art-africa','19世纪','非洲','雕塑','核心',
  '库巴风格木彩绘面具，克利夫兰艺术博物馆藏（1935.304）。','1800年代中—后期',
  '与一女一男面具组成三件，为王国的建立重演的主角；在京外则见于男子入会仪式等非王室场合。','luba-bowl-figure,african-art','cma-1935.304'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")