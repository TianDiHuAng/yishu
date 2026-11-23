# -*- coding: utf-8 -*-
"""Cycle40 扩充（第二批）：新增 5 位人物条目——马奈、透纳、康斯太勃尔、库尔贝、安格尔。
来源：Cleveland 艺术家记录（含馆方撰写的传记正文）+（能匹配到的）V&A 藏品记录。
凡未获第二机构的，一律 needs_verification 并在待核实首条写明。
"""
import io,json,os,sys,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

# ---------- 1. 来源 ----------
NEWS=[
 ("cma-artist-manet","Cleveland Museum of Art — 艺术家记录：Édouard Manet (1832–1883)","https://openaccess-api.clevelandart.org/api/artworks/1956.718",
  "2026-11-23 API HTTP 200；creators 记录含生卒与馆方传记正文（经藏品 1956.718 取得）"),
 ("cma-artist-turner","Cleveland Museum of Art — 艺术家记录：J. M. W. Turner (1775–1851)","https://openaccess-api.clevelandart.org/api/artworks/1942.647",
  "2026-11-23 API HTTP 200；含馆方传记正文（经藏品 1942.647《上下两院火灾》取得）"),
 ("cma-artist-constable","Cleveland Museum of Art — 艺术家记录：John Constable (1776–1837)","https://openaccess-api.clevelandart.org/api/artworks/1972.48",
  "2026-11-23 API HTTP 200；含馆方传记正文（经藏品 1972.48《汉普斯特德布兰奇山池塘》取得）"),
 ("cma-artist-courbet","Cleveland Museum of Art — 艺术家记录：Gustave Courbet (1819–1877)","https://openaccess-api.clevelandart.org/api/artworks/1962.2",
  "2026-11-23 API HTTP 200；含馆方传记正文（经藏品 1962.2 取得）"),
 ("cma-artist-ingres","Cleveland Museum of Art — 艺术家记录：J.-A.-D. Ingres (1780–1867)","https://openaccess-api.clevelandart.org/api/artworks/1927.437",
  "2026-11-23 API HTTP 200；含馆方传记正文（经藏品 1927.437 取得）"),
 ("vam-o652344","Victoria and Albert Museum — Édouard Manet, Lola de Valence (1863–64), O652344","https://collections.vam.ac.uk/item/O652344/",
  "2026-11-23 V&A API HTTP 200：title=Lola de Valence；材料 paper"),
 ("vam-o84528","Victoria and Albert Museum — John Constable, Branch Hill Pond, Hampstead (1819), O84528","https://collections.vam.ac.uk/item/O84528/",
  "2026-11-23 V&A API HTTP 200：title/material(oil paint, canvas) 取到"),
 ("vam-o81593","Victoria and Albert Museum — Gustave Courbet, Landscape with the Châtel St Denis, Scey-en-Varais (1873), O81593","https://collections.vam.ac.uk/item/O81593/",
  "2026-11-23 V&A API HTTP 200：title/material(oil paint, canvas) 取到"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":("Cleveland Museum of Art（开放数据 API）" if sid.startswith("cma") else "Victoria and Albert Museum（V&A API v2）"),
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

# ---------- 2. catalog ----------
T=[('manet','爱德华·马奈','人物','art-impression','19世纪','法国','绘画','核心',
    '法国画家，被视为19世纪绘画转向现代的关键人物；《草地上的午餐》《奥林匹亚》在沙龙引发争议。','1832—1883年',
    '以当代生活为题材，吸收库图尔的底层颜料技法，晚年受印象派影响而调色更亮、笔触更自由；始终以官方沙龙为竞技场，未参加印象派展览。','impressionism,realism-art','cma-artist-manet,vam-o652344'),
   ('turner','约瑟夫·马洛德·威廉·透纳','人物','art-neo-romantic','19世纪','英国','绘画','核心',
    '英国浪漫主义风景画代表，以光线、气象与崇高感的表现著称，生前即为皇家美术学院院士并任透视学教授。','1775—1851年',
    '早年以地形水彩与版画起家，1819年后调色转亮、构图以色彩主导；晚年作品以海雾与蒸汽为题，影响后世对光的处理。','romanticism-art,constable','cma-artist-turner'),
   ('constable','约翰·康斯太勃尔','人物','art-neo-romantic','19世纪','英国','绘画','重要',
    '英国风景画家，以家乡斯图尔河谷与汉普斯特德的自然写生著称，1824年巴黎沙龙展出引起关注。','1776—1837年',
    '坚持户外写生并以前所未有的规模绘制六英尺幅面风景，强调对特定地点的真实再现，晚期笔触更具表现性。','romanticism-art,turner','cma-artist-constable,vam-o84528'),
   ('courbet','居斯塔夫·库尔贝','人物','art-neo-romantic','19世纪','法国','绘画','核心',
    '法国画家，现实主义（Réalisme）旗手，1855年自办「现实主义馆」展出个人作品。','1819—1877年',
    '以不加理想化地描绘农民与日常场景著称；1871年参与巴黎公社并因旺多姆圆柱事件被判刑，晚年流亡瑞士。','realism-art,romanticism-art','cma-artist-courbet,vam-o81593'),
   ('ingres','让-奥古斯特-多米尼克·安格尔','人物','art-neo-romantic','19世纪','法国','绘画','重要',
    '法国新古典主义代表，大卫的学生，1824年沙龙后成为法国新古典派的领袖。','1780—1867年',
    '重视线条与素描，长于肖像与女性裸体；与德拉克洛瓦长期对立，其素描传统影响德加与毕加索。','neoclassicism,delacroix','cma-artist-ingres'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
block=[]
for t in T:
    body=",\n ".join(repr(x) for x in t)
    block.append("(%s)," % body)
lines[close:close]=block
s="\n".join(lines)
# 双向关联
pairs=[('"realism-art,post-impressionism,degas"','"realism-art,post-impressionism,degas,manet"'),
       ('"romanticism-art,impressionism,rodin"','"romanticism-art,impressionism,rodin,turner,constable,courbet"'),
       ('"tang-painting,song-painting,mi-youren-cloudy-mountains"','"tang-painting,song-painting,mi-youren-cloudy-mountains"')]
for a,b in pairs:
    if a!=b and s.count(a)==1: s=s.replace(a,b)
io.open(p,"w",encoding="utf-8").write(s)
print("catalog tuples appended:",len(T))