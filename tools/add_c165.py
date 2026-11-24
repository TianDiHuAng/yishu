# -*- coding: utf-8 -*-
"""Cycle165：非欧洲乐器 6 条（鼓/拇指琴/卡曼恰/里拉/弦鸣提琴/象牙号角）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1918-349","Cleveland Museum of Art — Tsuzumi Drum, 1800s, acc. 1918.349",
  "https://openaccess-api.clevelandart.org/api/artworks/1918.349","2026-11-24 API HTTP 200；木漆泥金(莳绘)、皮、铁与绳 直径20.4cm；日本江户至明治；说明含能乐伴奏、靠肩手持、以呼吸或唾液调节皮的湿度"),
 ("cma-1915-495","Cleveland Museum of Art — Lamellophone (chisanji), late 1800s, acc. 1915.495",
  "https://openaccess-api.clevelandart.org/api/artworks/1915.495","2026-11-24 API HTTP 200；木、铁与金属丝 19.1×10.2×6.4cm；刚果民主共和国或安哥拉、乔奎风格；说明含骑四足兽的人像与行商(pombeiro)推测"),
 ("cma-1918-353","Cleveland Museum of Art — Kamanche (incomplete), 1875-1900, acc. 1918.353",
  "https://openaccess-api.clevelandart.org/api/artworks/1918.353","2026-11-24 API HTTP 200；木、皮与骨 58.5×26.8cm；伊朗北部(高加索,也许阿塞拜疆,或克什米尔)；说明含卡曼恰一词10世纪起用于弓弦乐器、乐器名称的流变"),
 ("cma-1929-346","Cleveland Museum of Art — Lyre (ndongo, endongo, entongoli, or kissar), by 1928, acc. 1929.346",
  "https://openaccess-api.clevelandart.org/api/artworks/1929.346","2026-11-24 API HTTP 200；木、爬行动物皮、毛皮、布与天然纤维 直径31.8cm；乌干达甘达或索加风格；说明含东非常见里拉与多种名称"),
 ("cma-1929-347","Cleveland Museum of Art — Spike fiddle (endingidi or iningidi), 1900s, acc. 1929.347",
  "https://openaccess-api.clevelandart.org/api/artworks/1929.347","2026-11-24 API HTTP 200；木、蛇皮与植物纤维 44.2cm；乌干达或卢旺达-布隆迪；说明含单弦、学者认为约1904-1907年传入布干达王国"),
 ("cma-2010-448","Cleveland Museum of Art — Oliphant (Side-Blown Trumpet), late 1800s-early 1900s, acc. 2010.448",
  "https://openaccess-api.clevelandart.org/api/artworks/2010.448","2026-11-24 API HTTP 200；象牙 32×4×6cm；中非(刚果民主共和国最可能,或卡宾达、刚果共和国)、或为永贝风格；说明含象牙侧吹号多用于葬礼等庄重场合"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('cma-tsuzumi','鼓（tsuzumi，日本，江户至明治）','作品','music-instruments','19世纪','东亚','乐器','重要',
  '日本能乐等所用的小鼓，克利夫兰艺术博物馆藏（1918.349）。','1800年代',
  '木漆泥金（莳绘）、皮、铁与绳，直径20.4厘米；该馆称小鼓靠在一侧肩上、一手固定、另一手击面，并以呼吸或唾液调节皮的湿度；用于能乐等正式演出的伴奏，也用于传统民间音乐。',
  'koto-instrument,hitoyogiri-flute','cma-1918-349'),
 ('cma-chisanji','乔奎风格拇指琴（chisanji，中非）','作品','music-instruments','19世纪','非洲','乐器','重要',
  '饰有骑兽人像的拇指琴，克利夫兰艺术博物馆藏（1915.495）。','19世纪末',
  '木、铁与金属丝，尺寸19.1×10.2×6.4厘米；产地该馆写刚果民主共和国或安哥拉、乔奎风格；该馆称其造型是骑在奇特四足兽上的生动人像，其帽子表明他可能是从事长途贸易的行商（pombeiro）。',
  'kora-instrument,mangbetu-harp','cma-1915-495'),
 ('cma-kamanche','卡曼恰（伊朗北部，1875—1900，残件）','作品','music-instruments','19世纪','西亚·中亚','乐器','重要',
  '残缺的卡曼恰弓弦乐器，克利夫兰艺术博物馆藏（1918.353）。','1875—1900年',
  '木、皮与骨，尺寸58.5×26.8厘米；产地该馆写伊朗北部（高加索，也许是阿塞拜疆，或克什米尔）；该馆称卡曼恰是波斯语词，10世纪起用来称呼以弓发声的乐器，弓弦乐器由此传至拜占庭、中亚、远东与欧洲。',
  'cma-oud,cma-tanbur','cma-1918-353'),
 ('cma-uganda-lyre','乌干达里拉琴（ndongo/endongo/kissar）','作品','music-instruments','20世纪','东非','乐器','重要',
  '乌干达甘达或索加风格的里拉琴，克利夫兰艺术博物馆藏（1929.346）。','1928年前',
  '木、爬行动物皮、毛皮、布与天然纤维，直径31.8厘米；该馆称里拉在东非很常见，多种名称反映了许多族群使用这一乌干达类型；碗形木音箱蒙爬行动物皮，可能是巨蜥皮，弦连到横梁，横梁两端原饰山羊毛穗。',
  'drum-ngoma,kora-instrument','cma-1929-346'),
 ('cma-endingidi','乌干达弦鸣提琴（endingidi/iningidi）','作品','music-instruments','20世纪','东非','乐器','重要',
  '乌干达单弦提琴 endingidi，克利夫兰艺术博物馆藏（1929.347）。','1900年代',
  '木、蛇皮与植物纤维，全长44.2厘米；该馆称这是单弦的弦鸣乐器，学者认为约1904至1907年传入布干达王国，后传至卢旺达，在那里称 iningidi，由胡图族乐手演奏；至今仍见于婚礼或由布干达宫廷乐师演奏。',
  'cma-uganda-lyre,drum-ngoma','cma-1929-347'),
 ('cma-yombe-oliphant','永贝风格象牙侧吹号角（oliphant）','作品','music-instruments','19世纪','非洲','乐器','重要',
  '雕有永贝统治者像的象牙侧吹号角，克利夫兰艺术博物馆藏（2010.448）。','19世纪末—20世纪初',
  '象牙，尺寸32×4×6厘米；产地该馆写中非、刚果民主共和国（最可能）、卡宾达或刚果共和国，可能是永贝风格制作者；该馆称象牙侧吹号似乎多用于葬礼等庄重场合，吹口在内弯处，演奏者横持；顶部雕有身披贝壳项链与欧式斗篷、帽子的坐姿永贝统治者。',
  'kongo-prestige-cap,african-art','cma-2010-448'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
txt="\n".join(lines)
T=[t for t in T if "'%s'"%t[0] not in txt]
if T:
    close=max(i for i,l in enumerate(lines) if l.strip()=="]")
    lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
    io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
