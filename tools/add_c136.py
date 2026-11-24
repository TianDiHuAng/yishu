# -*- coding: utf-8 -*-
"""Cycle136：非洲 4 条（Bangwa lefem 纪念像、Bamana chi wara、约鲁巴 Èṣù 舞杖、Bamileke 珠饰凳）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1987-62","Cleveland Museum of Art — Commemorative figure (lefem), Bangwa, Cameroon, mid-1800s–1910, acc. 1987.62",
  "https://openaccess-api.clevelandart.org/api/artworks/1987.62","2026-11-24 API HTTP 200；木 92.1×20.3cm；说明含Lefem会社与王室神龛"),
 ("cma-1965-325","Cleveland Museum of Art — Chi wara headdress, Bamana, early–mid 1900s, acc. 1965.325",
  "https://openaccess-api.clevelandart.org/api/artworks/1965.325","2026-11-24 API HTTP 200；木·货贝·玻璃珠·金属 44.5×66cm；说明含农耕兽与成对舞"),
 ("cma-2018-34","Cleveland Museum of Art — Dance staff for Èṣù (Ògò Èlégba), Yorùbá, 1800s, acc. 2018.34",
  "https://openaccess-api.clevelandart.org/api/artworks/2018.34","2026-11-24 API HTTP 200；木皮革货贝种子纤维 62cm；说明含跨界/市场/生育"),
 ("cma-2006-138","Cleveland Museum of Art — Prestige stool (Kuo fo), Bamileke, Cameroon, possibly 1800s, acc. 2006.138",
  "https://openaccess-api.clevelandart.org/api/artworks/2006.138","2026-11-24 API HTTP 200；木棉纤维玻璃珠靛蓝 51×38×43cm；说明含travel stool与豹纹"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('lefem-commemorative-figure','Bangwa 王室纪念像（lefem）','作品','art-africa','19—20世纪','非洲','雕塑','核心',
  '喀麦隆 Bangwa 木雕纪念像，克利夫兰艺术博物馆藏（1987.62）。','1800年代中—1910',
  '生前所雕的理想化像作在世替身/中介；着王服（鬃布帽、珠链、褶裙、角杯、已断烟斗）；由秘密会社 Lefem 保管，置王室神龛，见证对祖颅的献祭以护国安民、祈丰产，亦现于葬礼与王仪。','luba-bowl-figure,african-art','cma-1987-62'),
 ('chi-wara-headdress','Bamana chi wara 头饰','作品','art-africa','20世纪','非洲','雕塑','核心',
  '马里 Bamana 木雕头饰，克利夫兰艺术博物馆藏（1965.325）。','1900年代早—中期',
  'chi wara 为神话「农耕兽」，教 Bamana 耕作；雕纹显肌理，示其为兼人/羚羊/食蚁兽的农神；戴进口金属珠耳环鼻环；成对男女头饰缚于编篮帽上，男舞者于农赛与婚礼伴女子歌起舞。','kora-instrument,african-art','cma-1965-325'),
 ('esu-dance-staff','约鲁巴 Èṣù 舞杖（Ògò Èlégba）','作品','art-africa','19世纪','非洲','雕塑','核心',
  '尼日利亚约鲁巴木雕舞杖，克利夫兰艺术博物馆藏（2018.34）。','1800年代',
  'Èṣù（Èlégba）为约鲁巴万神殿最复杂之神：众神信使、献祭承载者、仪式生活守护者，关联十字路口/市场/家门；成对男女罕见地喻其可性别互转、化死为生（生育）、化解两性张力；男持此神专用礼笛；大量货贝示其带来财富。','gelede-mask-yoruba,african-art','cma-2018-34'),
 ('kuofo-prestige-stool','Bamileke 珠饰「Kuo fo」凳','作品','art-africa','19世纪','非洲','综合','核心',
  '喀麦隆 Bandjoun Bamileke 珠饰木凳，克利夫兰艺术博物馆藏（2006.138）。','或1800年代',
  '珠饰木凳/宝座为喀麦隆草原诸王国最常见艺式之一；原属王室库藏的「行凳（travel stool）」，用于宫内较私密的小仪式；豹纹印证王权，暗喻王可暂化为此可怖猛兽。','lefem-commemorative-figure,african-art','cma-2006-138'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")