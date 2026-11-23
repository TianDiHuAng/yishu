# -*- coding: utf-8 -*-
"""Cycle64：北美再补 4 条（Tlingit 图腾柱、纳瓦霍 biil'éé、Sikyatki 罐、因纽特石版画）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1989-89","Cleveland Museum of Art — Totem Pole (model), Tlingit, c. 1880, acc. 1989.89",
  "https://openaccess-api.clevelandart.org/api/artworks/1989.89","2026-11-23 API HTTP 200；彩绘木雕 189.2×8.8cm；说明含 Kushda-Kaw 等故事序列"),
 ("cma-1929-921","Cleveland Museum of Art — Woman’s Two-Piece Dress (Biil’éé), Navajo, c. 1880–85, acc. 1929.921",
  "https://openaccess-api.clevelandart.org/api/artworks/1929.921","2026-11-23 API HTTP 200；羊毛挂毯 145×99cm；说明含 D. Y. Begay 的转述"),
 ("cma-1990-10","Cleveland Museum of Art — Jar, Ancestral Pueblo (Sikyatki style), 1400–1600, acc. 1990.10",
  "https://openaccess-api.clevelandart.org/api/artworks/1990.10","2026-11-23 API HTTP 200；陶器施化妆土 21.2×38.8cm；说明含「声与灵」观念"),
 ("cma-1972-1054","Cleveland Museum of Art — Devil Fish (stonecut), Peter Aliknak Banksland, Ulukhaktok, 1972, acc. 1972.1054",
  "https://openaccess-api.clevelandart.org/api/artworks/1972.1054","2026-11-23 API HTTP 200；石版 50.8×76.2cm；说明含强制定居背景与石版技法")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('tlingit-totem-pole','特林吉特图腾柱（模型）','作品','art-americas','19世纪','北美洲','雕塑','重要',
    '特林吉特人所作彩绘木雕图腾柱模型，克利夫兰艺术博物馆藏（1989.89）。','约1880年',
    '村落以高大图腾柱标示所有者等级与谱系；此小型模型曾属一位「银鲑氏族·渡鸦部落」的说故事者。','navajo-biilee-dress,americas-art','cma-1989-89'),
   ('navajo-biilee-dress','纳瓦霍两片式女装（biil’éé）','作品','art-americas','19世纪','北美洲','综合','重要',
    '纳瓦霍（Diné）羊毛挂毯女装，克利夫兰艺术博物馆藏（1929.921）。','约1880—85年',
    '由两片相同织片在侧缝与肩部相接；据当代织者 D. Y. Begay 转述，biil’éé 承载灵力、护佑并记述审美故事。','navajo-hubbell-rug,tlingit-totem-pole','cma-1929-921'),
   ('sikyatki-jar','西基亚茨基风格罐（祖先普韦布洛）','作品','art-americas','15—16世纪','北美洲','综合','重要',
    '祖先普韦布洛西基亚茨基风格陶罐，克利夫兰艺术博物馆藏（1990.10）。','1400—1600年',
    '器形硕大、表面经石磨精修、壁薄叩之「作响」；红橙色调异于更早的黑白偏好；为现代霍皮陶之祖。','hopi-canteen-katsina,americas-art','cma-1990-10'),
   ('inuit-devil-fish','因纽特石版画《魔鬼鱼》（Devil Fish）','作品','art-americas','20世纪','北美洲','绘画','重要',
    '因纽特艺术家 Peter Aliknak Banksland（1928—1998）石版作品，克利夫兰艺术博物馆藏（1972.1054）。','1972年',
    '石版（stonecut）为北极因纽特发展之法：石上绘图、铲除不印处、上墨压纸，一次仅得一版。','tlingit-totem-pole,americas-art','cma-1972-1054')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")