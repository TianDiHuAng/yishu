# -*- coding: utf-8 -*-
"""Cycle105：大洋洲 4 条（塞皮克祖像、塞皮克钩形像、库克礼斧、安布里姆等级像）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1971-150","Cleveland Museum of Art — Ancestral Figure, Sepik River, 1800s, acc. 1971.150",
  "https://openaccess-api.clevelandart.org/api/artworks/1971.150","2026-11-23 API HTTP 200；彩木·纤维·树皮布 105.4×12.2×12.8cm；说明含男子会所"),
 ("cma-1963-553","Cleveland Museum of Art — Hook Figure, Arambak, c. 1920–30, acc. 1963.553",
  "https://openaccess-api.clevelandart.org/api/artworks/1963.553","2026-11-23 API HTTP 200；彩木与货贝 207×6.4cm；说明含战神/猎神与附体"),
 ("cma-1940-1078","Cleveland Museum of Art — Ceremonial Adze, Mangaia, Cook Islands, 1800s, acc. 1940.1078",
  "https://openaccess-api.clevelandart.org/api/artworks/1940.1078","2026-11-23 API HTTP 200；木石纤维 10.2cm；说明含 K 纹与神授编绳纹样传说"),
 ("cma-1971-272","Cleveland Museum of Art — Grade Society Figure, Ambrym, Vanuatu, c. 1930, acc. 1971.272",
  "https://openaccess-api.clevelandart.org/api/artworks/1971.272","2026-11-23 API HTTP 200；蕨木 210.9cm；说明含等级庆典与 mana"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('sepik-ancestral-figure','塞皮克祖灵像','作品','art-oceania','19世纪','大洋洲','雕塑','核心',
  '巴布亚新几内亚塞皮克河彩木祖像，克利夫兰艺术博物馆藏（1971.150）。','1800年代',
  '塞皮克村落的社会与仪式生活以男子会所为中心； 裂口锣、讲台、笛等礼器存于此，最神圣者避妇女儿童。','oceania-art,maori-hei-tiki-1969','cma-1971-150'),
 ('sepik-hook-figure','塞皮克钩形祖像（阿拉姆巴克）','作品','art-oceania','20世纪','大洋洲','雕塑','核心',
  '塞皮克河中游阿拉姆巴克人彩木货贝像，克利夫兰艺术博物馆藏（1963.553）。','约1920—1930年',
  '抽象人像表战神与猎神；藏于男子会所；出征前以特制物擦拭以求神灵附体；钩为羽，中央为心（新月形肋），下为小腿。','sepik-ancestral-figure,oceania-art','cma-1963-553'),
 ('cook-ceremonial-adze','库克群岛礼斧','作品','art-oceania','19世纪','大洋洲','综合','重要',
  '曼加伊亚礼斧，克利夫兰艺术博物馆藏（1940.1078）。','1800年代',
  '铁器传入前以骨、贝、石、牙制工具；礼斧或表神祇；木柄刻 K 纹，石刃以细编椰绳缚之。','ambrym-grade-figure,oceania-art','cma-1940-1078'),
 ('ambrym-grade-figure','安布里姆等级社会祖像','作品','art-oceania','20世纪','大洋洲','雕塑','核心',
  '瓦努阿图安布里姆蕨木祖像，克利夫兰艺术博物馆藏（1971.272）。','约1930年',
  '瓦努阿图以巨像尊祖；常立于男子会社屋旁，配合个人晋升等级之庆典；蕨木干雕成，原覆泥灰上彩；巨头示 mana。','sepik-hook-figure,oceania-art','cma-1971-272'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")