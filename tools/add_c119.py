# -*- coding: utf-8 -*-
"""Cycle119：埃及/伊斯兰 4 条（飞鸟碗、卡诺普罐、阿门涅姆赫特三世、米奈赫布）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1915-589","Cleveland Museum of Art — Bowl with Flying Birds, Ilkhanid, 1280–1400, acc. 1915.589",
  "https://openaccess-api.clevelandart.org/api/artworks/1915.589","2026-11-24 API HTTP 200；熔块胎釉下彩 11.2×22cm；说明含中国母题与Sultanabad"),
 ("cma-1921-1021","Cleveland Museum of Art — Canopic Jar with Jackal's Head, Dynasty 26, acc. 1921.1021",
  "https://openaccess-api.clevelandart.org/api/artworks/1921.1021","2026-11-24 API HTTP 200；石灰华 高42.6cm；说明含荷鲁斯四子"),
 ("cma-1960-56","Cleveland Museum of Art — Statue of Amenemhat III, Dynasty 12, acc. 1960.56",
  "https://openaccess-api.clevelandart.org/api/artworks/1960.56","2026-11-24 API HTTP 200；花岗闪长岩 51.2×19.8cm；说明含超大风耳与写实"),
 ("cma-1996-28","Cleveland Museum of Art — Statue of Minemheb, Dynasty 18, acc. 1996.28",
  "https://openaccess-api.clevelandart.org/api/artworks/1996.28","2026-11-24 API HTTP 200；花岗闪长岩 45×16.6×28.3cm；说明含像中像与狒狒托特"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('ilkhanid-flying-birds-bowl','伊尔汗飞鸟纹碗','作品','art-islamic','13—14世纪','西亚·中亚','陶瓷','核心',
  '伊朗（或卡尚）苏丹纳巴德式熔块胎碗，克利夫兰艺术博物馆藏（1915.589）。','1280—1400年',
  '伊尔汗期中国母题入波斯：龙凤莲花；凤等同《列王纪》之 simurgh；灰地白浆、平沿承中国器；中亚至埃及均有出土或仿制。','minai-bowl-kashan,islamic-art','cma-1915-589'),
 ('canopic-jar-26','第二十六王朝卡诺普罐','作品','art-ancient','公元前7—6世纪','埃及','雕塑','核心',
  '豺头卡诺普罐，克利夫兰艺术博物馆藏（1921.1021）。','公元前664—前525年',
  '木乃伊化取肝肺胃肠分置四罐；荷鲁斯四子各护一脏；本罐豺头为 Duamutef（护胃）。','minnefer-statue,amenemhat-statue','cma-1921-1021'),
 ('amenemhat-statue','阿门涅姆赫特三世像','作品','art-ancient','公元前19世纪','埃及','雕塑','核心',
  '中王国第十二王朝花岗闪长岩王像，克利夫兰艺术博物馆藏（1960.56）。','约公元前1859—前1814年',
  '无铭而凭浓眉/颧骨/凹颊/突颌认出；超大风耳象征倾听民愿；为防凸肢折断双手平贴裙前。','minnefer-statue,canopic-jar-26','cma-1960-56'),
 ('minemheb-statue','米奈赫布像（像中像）','作品','art-ancient','公元前14世纪','埃及','雕塑','核心',
  '第十八王朝花岗闪长岩跪像，克利夫兰艺术博物馆藏（1996.28）。','约公元前1391—前1353年',
  '米奈赫布为阿蒙霍特普三世三十年庆典筹备官员，像铭以「庆典神庙营建首长」为主衔；跪捧小坛，坛上蹲狒狒托特。','minnefer-statue,amenemhat-statue','cma-1996-28'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")