# -*- coding: utf-8 -*-
"""Cycle132：中世纪 4 条（但以理狮坑、拜占庭象牙、奥托差遣使徒、狮与蛇怪柱头）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1962-247","Cleveland Museum of Art — Daniel in the Lion's Den, Saint-Aignan-sur-Cher, c. 1125–50, acc. 1962.247",
  "https://openaccess-api.clevelandart.org/api/artworks/1962.247","2026-11-24 API HTTP 200；石灰岩 72.4×68.6×36.2cm；说明含罗曼式柱头与教堂"),
 ("cma-1925-1293","Cleveland Museum of Art — Byzantine ivory plaque (Stroganoff Ivory), 950–1025, acc. 1925.1293",
  "https://openaccess-api.clevelandart.org/api/artworks/1925.1293","2026-11-24 API HTTP 200；象牙 25.3×17.2cm；说明含宝座圣母与道成肉身"),
 ("cma-1967-65","Cleveland Museum of Art — Christ's Mission to the Apostles, Ottonian, c. 970–980, acc. 1967.65",
  "https://openaccess-api.clevelandart.org/api/artworks/1967.65","2026-11-24 API HTTP 200；象牙 18.2×9.9cm；说明含十二使徒与福音书封"),
 ("cma-1972-20","Cleveland Museum of Art — Engaged capital with lion and basilisk, N. Italy, 1175–1200, acc. 1972.20",
  "https://openaccess-api.clevelandart.org/api/artworks/1972.20","2026-11-24 API HTTP 200；大理石 30.2×33×29.3cm；说明含蛇怪与魔鬼象征"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('daniel-lions-relief','《但以理在狮坑》柱头','作品','art-medieval','12世纪','欧洲','雕塑','核心',
  '罗曼式石灰岩柱头，克利夫兰艺术博物馆藏（1962.247）。','约1125—1150年',
  '《旧约》：但以理因独信一神被投入狮坑，因信仰奇迹免害；此作但以理居中、两侧狮群、神遣天使相救；原为法国中部圣艾尼昂教堂内部装饰柱头之一。','lion-basilisk-capital,auvergne-virgin-majesty','cma-1962-247'),
 ('byzantine-ivory-plaque','拜占庭象牙圣母宝座（斯特罗加诺夫象牙）','作品','art-medieval','10—11世纪','欧洲','雕塑','核心',
  '拜占庭君士坦丁堡象牙板，克利夫兰艺术博物馆藏（1925.1293）。','950—1025年',
  '圣母坐高背宝座，二天使在上；宝座圣母传统可溯至6世纪；基督一手祝福一手持卷，作无表情的超自然孩童，示道成肉身之秘。','ivory-virgin-child-paris,ottonian-mission-apostles','cma-1925-1293'),
 ('ottonian-mission-apostles','《基督差遣使徒》（奥托）','作品','art-medieval','10世纪','欧洲','雕塑','核心',
  '奥托期象牙板，克利夫兰艺术博物馆藏（1967.65）。','约970—980年',
  '基督全身居中，两侧各六使徒半身像成纵列；大眼、微张口，似将开口委以使徒传福音之命；或原为贵重福音书封的中央饰。','byzantine-ivory-plaque,limoges-gospel-cover','cma-1967-65'),
 ('lion-basilisk-capital','狮与蛇怪附壁柱头','作品','art-medieval','12世纪','欧洲','雕塑','重要',
  '北意大利大理石柱头，克利夫兰艺术博物馆藏（1972.20）。','1175—1200年',
  '蛇怪（basilisk）为半鸡半蛇的想象动物，据中世纪博物志可一瞥致死；常作魔鬼之象征，于道成肉身与末日审判时为基督践踏。','daniel-lions-relief,auvergne-virgin-majesty','cma-1972-20'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")