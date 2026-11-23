# -*- coding: utf-8 -*-
"""Cycle94：现代名作 4 条（毕加索《人生》、布拉克《埃斯塔克港》、莫奈《睡莲》、毕加索《瓶、杯、叉》）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1945-24","Cleveland Museum of Art — Pablo Picasso, La Vie, 1903, acc. 1945.24",
  "https://openaccess-api.clevelandart.org/api/artworks/1945.24","2026-11-23 API HTTP 200；布面油画 196.5×129.2cm；说明含蓝色时期与 Casagemas 之死"),
 ("cma-2020-104","Cleveland Museum of Art — Georges Braque, The Port of l'Estaque, the Pier, 1906, acc. 2020.104",
  "https://openaccess-api.clevelandart.org/api/artworks/2020.104","2026-11-23 API HTTP 200；布面油画 59.7×73cm；说明含野兽派与互补色"),
 ("cma-1960-81","Cleveland Museum of Art — Claude Monet, Water Lilies (Agapanthus), c. 1915–26, acc. 1960.81",
  "https://openaccess-api.clevelandart.org/api/artworks/1960.81","2026-11-23 API HTTP 200；布面油画 201.3×425.6cm；说明含吉维尼花园与无地平线"),
 ("cma-1972-8","Cleveland Museum of Art — Pablo Picasso, Bottle, Glass, Fork, 1911–12, acc. 1972.8",
  "https://openaccess-api.clevelandart.org/api/artworks/1972.8","2026-11-23 API HTTP 200；布面油画 72×52.7cm；说明含分析立体主义与字母数字"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('picasso-la-vie','毕加索《人生》（La Vie）','作品','art-modern','20世纪','欧洲','绘画','核心',
  '毕加索蓝色时期布面油画，克利夫兰艺术博物馆藏（1945.24）。','1903年',
  '1901年友人 Casagemas 自杀后开始蓝色时期；本画被视为贫困劳苦或「生命循环」的象征，苦难与社会疏离主题至此达到顶点。','picasso,cubism','cma-1945-24'),
 ('braque-estaque-port','布拉克《埃斯塔克港：码头》','作品','art-modern','20世纪','欧洲','绘画','核心',
  '布拉克野兽派时期布面油画，克利夫兰艺术博物馆藏（2020.104）。','1906年',
  '24岁首访南法所作；起伏山峦与短促有力笔触，常用互补色对比，可见其兴奋。','fauvism,braque-violin-collage','cma-2020-104'),
 ('monet-water-lilies-agapanthus','莫奈《睡莲（百子莲）》','作品','art-modern','20世纪','欧洲','绘画','核心',
  '莫奈大型布面油画，克利夫兰艺术博物馆藏（1960.81）。','约1915—1926年',
  '专注吉维尼自建花园池塘的瞬间光效；去除地平与岸线，以巨大横幅暗示无边际的水面。','monet,impressionism','cma-1960-81'),
 ('picasso-bottle-glass-fork','毕加索《瓶、杯、叉》','作品','art-modern','20世纪','欧洲','绘画','核心',
  '毕加索分析立体主义布面油画，克利夫兰艺术博物馆藏（1972.8）。','1911—1912年',
  '描绘咖啡馆桌面之物；碎裂的多视点与交叠平面构成分析立体主义；字母「fe 20」「EAN」含义仅作者知。','cubism,braque-estaque-port','cma-1972-8'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")