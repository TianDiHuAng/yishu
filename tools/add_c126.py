# -*- coding: utf-8 -*-
"""Cycle126：商周青铜 4 条（爵、东周狩猎壶、鎛钟、西周壶）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1960-78","Cleveland Museum of Art — Pair of Jue wine cups, Shang Anyang, acc. 1960.78",
  "https://openaccess-api.clevelandart.org/api/artworks/1960.78","2026-11-24 API HTTP 200；青铜 20.3×19.7cm；说明含爵为灌祭与器类名目"),
 ("cma-1975-62","Cleveland Museum of Art — Hu jar with hunting scenes, Eastern Zhou, acc. 1975.62",
  "https://openaccess-api.clevelandart.org/api/artworks/1975.62","2026-11-24 API HTTP 200；青铜 25.5cm；说明含最早 pictorial scenes 之一"),
 ("cma-1962-44","Cleveland Museum of Art — Bo zhong bell, Eastern Zhou, acc. 1962.44",
  "https://openaccess-api.clevelandart.org/api/artworks/1962.44","2026-11-24 API HTTP 200；青铜 41.4cm；说明含椭圆截面双音"),
 ("cma-1944-61","Cleveland Museum of Art — Hu wine vessel with cover, Western Zhou, acc. 1944.61",
  "https://openaccess-api.clevelandart.org/api/artworks/1944.61","2026-11-24 API HTTP 200；青铜 46.1cm 带盖；说明含盖倒置为杯与龙凤阴阳"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('shang-jue-cups','商代青铜爵（对）','作品','art-ancient','公元前12世纪','中国','金属器','核心',
  '安阳期青铜爵一对，克利夫兰艺术博物馆藏（1960.78）。','约公元前1200年',
  '爵用于灌祭；商王室祖先崇拜中酒食为要；器类各有专名：爵/斝（温酒）/方卣/觚（喇叭口注酒）。','shang-jia-vessel,shang-zhou-bronzes','cma-1960-78'),
 ('eastern-zhou-hu-jar','东周狩猎纹壶','作品','art-ancient','公元前5—3世纪','中国','金属器','核心',
  '战国青铜壶，克利夫兰艺术博物馆藏（1975.62）。','公元前481—221年',
  '六条低浮雕横带；狩猎纹为中国艺术最早 pictorial scenes 之一；执矛剑猎人对圆纹猫科；另带交缠龙纹与双鸟小鱼带。','bo-zhong-bell,western-zhou-hu-vessel','cma-1975-62'),
 ('bo-zhong-bell','东周鎛钟','作品','art-ancient','公元前5世纪初','中国','乐器','核心',
  '东周青铜鎛钟，克利夫兰艺术博物馆藏（1962.44）。','公元前400年代初',
  '椭圆截面中国钟独特：敲沿或敲心可得两音；悬奏常成套按音高大小排；顶为双身蛇缠双虎之悬环，钟身蟠蛇枚，下兽面角交抽象鸟纹。','lai-zhong-bell,yayue','cma-1962-44'),
 ('western-zhou-hu-vessel','西周壶（带盖）','作品','art-ancient','公元前10—9世纪','中国','金属器','核心',
  '西周青铜壶，克利夫兰艺术博物馆藏（1944.61）。','约公元前1000—900年',
  '三带装饰：颈带凤鸟、盖与足带几何龙纹；龙凤或表阴阳，宗教/世俗皆宜；盖倒置成杯；颈部柱状「耳」示以绳携行。','lai-zhong-bell,shang-jue-cups','cma-1944-61'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")