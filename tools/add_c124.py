# -*- coding: utf-8 -*-
"""Cycle124：玛雅 4 条（战事瓶、宫宴筒瓶、Chamá 神祇筒瓶、Ulúa 大理石圈足瓶）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-2012-32","Cleveland Museum of Art — Maya vessel with battle scene, Nebaj, acc. 2012.32",
  "https://openaccess-api.clevelandart.org/api/artworks/2012.32","2026-11-24 API HTTP 200；陶与泥浆 17.2×15.4cm；说明含献俘与可可饮"),
 ("cma-1967-203","Cleveland Museum of Art — Maya cylindrical vessel with palace scene, acc. 1967.203",
  "https://openaccess-api.clevelandart.org/api/artworks/1967.203","2026-11-24 API HTTP 200；泥浆彩陶 径19cm 高19.1cm；说明含王登阶与豹皮"),
 ("cma-1954-391","Cleveland Museum of Art — Chamá cylinder with deities (God K), acc. 1954.391",
  "https://openaccess-api.clevelandart.org/api/artworks/1954.391","2026-11-24 API HTTP 200；泥浆彩陶 口15.5×16.5 高16.6cm；说明含风格爆炸与God K"),
 ("cma-1990-170","Cleveland Museum of Art — Ulúa marble ring-base vessel, Honduras, acc. 1990.170",
  "https://openaccess-api.clevelandart.org/api/artworks/1990.170","2026-11-24 API HTTP 200；大理石 9.5×13.5×10.1cm；说明含蝙蝠头柄与涡卷"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('maya-battle-vessel-nebaj','玛雅战事纹瓶（Nebaj）','作品','art-americas','古典晚期','美洲','陶瓷','核心',
  'Nebaj 地区彩绘陶瓶，克利夫兰艺术博物馆藏（2012.32）。','600—900年',
  '战后献俘场景：面朝前之主回顾十名武士——有被剥战装者、有戴繁头冠与豹皮衣者；口沿铭文献此器以饮可可。','maya-deer-vessel,americas-art','cma-2012-32'),
 ('maya-palace-cylinder','玛雅宫宴筒瓶','作品','art-americas','古典晚期','美洲','陶瓷','核心',
  '玛雅彩绘筒瓶，克利夫兰艺术博物馆藏（1967.203）。','600—900年',
  '或纪念王之大事：王立于阶前御座旁、双腿为地上輿框；手势与腰间豹皮使王与侍从视觉相系；细瓷亦为赠礼与随葬。','maya-battle-vessel-nebaj,americas-art','cma-1967-203'),
 ('chama-deities-cylinder','Chamá 神祇筒瓶（God K）','作品','art-americas','古典晚期','美洲','陶瓷','重要',
  '危地马拉 Kixpek Chamá 风格筒瓶，克利夫兰艺术博物馆藏（1954.391）。','600—900年',
  '600—900年玛雅城邦激增互动竞争；各地以独特陶绘风格为身份，风格数爆增、彩陶为时代标志；本瓶绘王之守护神 God K。','maya-palace-cylinder,maya-battle-vessel-nebaj','cma-1954-391'),
 ('ulua-ring-vessel','Ulúa 大理石圈足瓶','作品','art-americas','古典晚期','美洲','雕塑','重要',
  '洪都拉斯乌卢阿谷大理石瓶，克利夫兰艺术博物馆藏（1990.170）。','约600—1000年',
  '乌卢阿以白大理石低浮雕器著称，柄雕蝙蝠/猫/鸟/猴等首；本件以涡卷刻工之锐与座部三角镂空见长。','chama-deities-cylinder,americas-art','cma-1990-170'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")