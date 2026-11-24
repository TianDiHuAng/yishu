# -*- coding: utf-8 -*-
"""Cycle146：埃及 4 条（青蛙女神赫奎特、女像柱镜、装饰西图拉瓶、巴肯穆特棺）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1976-5","Cleveland Museum of Art — Statue of Heqat, the Frog Goddess, c. 2950 BCE, acc. 1976.5",
  "https://openaccess-api.clevelandart.org/api/artworks/1976.5","2026-11-24 API HTTP 200；石灰华 15.4×14.7×15.5cm；说明含前王朝动物雕塑与助产神"),
 ("cma-1983-196","Cleveland Museum of Art — Caryatid Mirror, Dynasty 18, acc. 1983.196",
  "https://openaccess-api.clevelandart.org/api/artworks/1983.196","2026-11-24 API HTTP 200；青铜 38.9×20cm；说明含裸女柄镜与哈托尔"),
 ("cma-1932-32","Cleveland Museum of Art — Decorated Situla, Ptolemaic, 305–30 BCE, acc. 1932.32",
  "https://openaccess-api.clevelandart.org/api/artworks/1932.32","2026-11-24 API HTTP 200；青铜 28.3cm(连柄45.2)；说明含来世双重角色与爱犬Nefer"),
 ("cma-1914-561","Cleveland Museum of Art — Coffin of Bakenmut, Thebes, Dyn. 21–22, acc. 1914.561",
  "https://openaccess-api.clevelandart.org/api/artworks/1914.561","2026-11-24 API HTTP 200；彩绘梧桐木 208×68cm；说明含棺饰取代墓室装饰"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('heqat-frog-goddess','青蛙女神赫奎特像','作品','art-ancient','公元前30世纪','埃及','雕塑','核心',
  '前王朝石灰华青蛙像，克利夫兰艺术博物馆藏（1976.5）。','约公元前2950年',
  '前王朝动物像多于人像；此蛙立于埃及动物雕塑大传统之始；雕者顺石材天然纹理增其圆浑；小陶蛙为早期神庙常见供品；其前王朝宗教义未明，后世多指助产女神赫奎特（Heqat）。','minnefer-statue,canopic-jar-26','cma-1976-5'),
 ('caryatid-mirror','女像柱镜','作品','art-ancient','公元前16—13世纪','埃及','金属器','核心',
  '第十八王朝青铜镜，克利夫兰艺术博物馆藏（1983.196）。','约公元前1540—1296年',
  '椭圆镜盘，柄为裸体少女：三分为辫发、宽领与珠带；立于十字基座、左足略前、手垂体侧；头顶纸莎草伞托盘；裸女柄镜为第18王朝中期时尚，此或同类之最；十字基座罕见；图像关联爱与美之神哈托尔（希腊等同阿佛洛狄忒），其侍从称 nefrut。','minnefer-statue,amenemhat-statue','cma-1983-196'),
 ('decorated-situla','装饰西图拉礼瓶','作品','art-ancient','托勒密时期','埃及','金属器','核心',
  '托勒密青铜西图拉瓶，克利夫兰艺术博物馆藏（1932.32）。','公元前305—前30年',
  '豪华仪式用瓶；两面场景示亡者来世双重角色：一面受家人献供，一面向神献供；一侧亡者 Padiamennebnesuttawy 携爱犬 Nefer（「善/美者」）坐低椅，长子 Amenhotep 献香与水；另侧亡者向神献面包蔬肉。','canopic-jar-26,minnefer-statue','cma-1932-32'),
 ('bakenmut-coffin','巴肯穆特棺','作品','art-ancient','公元前11—9世纪','埃及','综合','核心',
  '底比斯彩绘梧桐木棺，克利夫兰艺术博物馆藏（1914.561）。','约公元前1000—900年',
  '第21—22王朝为阿蒙祭司及家人所制彩绘木棺最精者之一；法老改葬北方三角洲、底比斯墓地治安松弛；富者棺与随葬置西岸崖凿无名无饰家族墓；往昔用于墓室的装饰皆倾注于棺；各面满布宗教场景、葬仪神祇、护身咒与魔法符号。','canopic-jar-26,amenhotep-tomb-relief','cma-1914-561'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")