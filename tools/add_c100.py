# -*- coding: utf-8 -*-
"""Cycle100：中世纪 4 条（奥弗涅宝座圣母、巴黎象牙镜背、哥特牙雕匣板、彩窗供养人）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-2012-52","Cleveland Museum of Art — Virgin and Child in Majesty, Auvergne, c. 1150–1200, acc. 2012.52",
  "https://openaccess-api.clevelandart.org/api/artworks/2012.52","2026-11-23 API HTTP 200；彩绘木（核桃木）40×22×24cm；说明含 Sedes Sapientiae 与道成肉身"),
 ("cma-1940-1200","Cleveland Museum of Art — Mirror Case with a Couple Playing Chess, Paris, 1325–50, acc. 1940.1200",
  "https://openaccess-api.clevelandart.org/api/artworks/1940.1200","2026-11-23 API HTTP 200；象牙 直径10.2cm；说明含巴黎奢华象牙与棋=爱与战"),
 ("cma-1978-39","Cleveland Museum of Art — Three Panels from a Casket with Courtly Romances, 1330–50, acc. 1978.39",
  "https://openaccess-api.clevelandart.org/api/artworks/1978.39","2026-11-23 API HTTP 200；象牙 13×26.2×1cm；说明含比武/爱之城堡/青春之泉"),
 ("cma-1919-1","Cleveland Museum of Art — Pair of Stained Glass Panels with Donors, c. 1480, acc. 1919.1",
  "https://openaccess-api.clevelandart.org/api/artworks/1919.1","2026-11-23 API HTTP 200；金属着色玻璃与银黄 156×43.5cm；说明含供养人与家族礼拜堂"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('auvergne-virgin-majesty','奥弗涅「宝座圣母」','作品','art-medieval','12世纪','欧洲','雕塑','核心',
  '奥弗涅彩绘木「智慧宝座」圣母像，克利夫兰艺术博物馆藏（2012.52）。','约1150—1200年',
  '属 Sedes Sapientiae（智慧宝座）群像；圣母坐宝座又成为圣子的宝座，示道成肉身与救赎中介。','gothic,paris-mirror-chess','cma-2012-52'),
 ('paris-mirror-chess','巴黎象牙镜背（对弈情侣）','作品','art-medieval','14世纪','欧洲','雕塑','核心',
  '巴黎象牙镜背，克利夫兰艺术博物馆藏（1940.1200）。','1325—1350年',
  '象牙为宫廷最珍视之材；巴黎为奢华象牙中心；绘男女对弈，棋在中世纪图像中兼喻爱与战。','gothic-casket-panels,auvergne-virgin-majesty','cma-1940-1200'),
 ('gothic-casket-panels','哥特象牙匣板（宫廷传奇）','作品','art-medieval','14世纪','欧洲','雕塑','核心',
  '法国哥特象牙匣三块板，克利夫兰艺术博物馆藏（1978.39）。','约1330—1350年',
  '盖板绘比武，右侧为「爱之城堡」，侧板有青春之泉、高文与狮子、兰斯洛特渡剑桥；源自《玫瑰传奇》等。','paris-mirror-chess,auvergne-virgin-majesty','cma-1978-39'),
 ('stained-glass-donors-pair','彩窗供养人一对','作品','art-medieval','15世纪','欧洲','综合','重要',
  '法国金属着色与银黄彩窗，克利夫兰艺术博物馆藏（1919.1）。','约1480年',
  '画男性（甲胄）与女性（珠饰华服）供养人，望向已失的中央画面；或为家族礼拜堂而设。','auvergne-virgin-majesty,gothic-casket-panels','cma-1919-1'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")