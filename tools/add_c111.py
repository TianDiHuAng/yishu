# -*- coding: utf-8 -*-
"""Cycle111：V&A 4 条（萨摩亚树皮布、平克原住民挂毯、毛利亚麻斗篷、奥斯曼 nay 笛）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o133186","Victoria and Albert Museum — Tapa cloth, Samoa, 1800s, O133186",
  "https://api.vam.ac.uk/v2/object/O133186","2026-11-24 API HTTP 200；捶打树皮布 25.25×20.25英寸；说明含构树皮与妇女工序"),
 ("vam-o34305","Victoria and Albert Museum — Jimmy Pike / Victorian Tapestry Workshop, Two men sitting at a waterhole, 1989, O34305",
  "https://api.vam.ac.uk/v2/object/O34305","2026-11-24 API HTTP 200；棉经羊毛棉纬挂毯 17×20.5cm；说明含瓦尔马贾里人与大沙沙漠"),
 ("vam-o360650","Victoria and Albert Museum — Maori flax cloak, New Zealand, 19th c., O360650",
  "https://api.vam.ac.uk/v2/object/O360650","2026-11-24 API HTTP 200；搓捻亚麻斗篷 172.7×137.2cm；说明含黑缨与流苏"),
 ("vam-o304190","Victoria and Albert Museum — Nay (flute), Ottoman, 1860–1867, O304190",
  "https://api.vam.ac.uk/v2/object/O304190","2026-11-24 API HTTP 200；旋木嵌金属 长90cm；说明含三倍音域与 Mevlevi 舞乐"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('tapa-cloth-samoa','萨摩亚树皮布（tapa）','作品','art-oceania','19世纪','大洋洲','织物','核心',
  '萨摩亚树皮布，维多利亚与艾伯特博物馆藏（O133186）。','1800年代',
  '以南太平洋构树（Broussonetia papyrifera）皮制；妇女工序繁复：浸皮、捶打、拼合、日晒漂白；象征与实用兼用。','maori-flax-cloak,sepik-ancestral-figure','vam-o133186'),
 ('aboriginal-tapestry-pike','平克《水潭边的两人》（原住民挂毯）','作品','art-oceania','20世纪','大洋洲','织物','核心',
  '吉米·平克设计、维多利亚挂毯工坊织造，维多利亚与艾伯特博物馆藏（O34305）。','1989年',
  '瓦尔马贾里人艺术家平克，生于大沙沙漠边缘；高原俯视水潭与两人；1976年成立的工坊限量小挂毯之一。','tapa-cloth-samoa,oceania-art','vam-o34305'),
 ('maori-flax-cloak','毛利亚麻斗篷','作品','art-oceania','19世纪','大洋洲','织物','重要',
  '毛利搓捻亚麻斗篷，维多利亚与艾伯特博物馆藏（O360650）。','19世纪',
  '搓捻（twined）亚麻斗篷，缀黑缨与流苏；为毛利传统服饰，材料与工艺见记录。','maori-hei-tiki-1969,tapa-cloth-samoa','vam-o360650'),
 ('ottoman-nay-flute','奥斯曼 nay 笛','作品','music-instruments','19世纪','西亚·中亚','乐器','核心',
  '奥斯曼旋木嵌金属 nay 笛，维多利亚与艾伯特博物馆藏（O304190）。','1860—1867年',
  '三节旋木相接、嵌金属、共十二指孔；唇吹边棱发声；理论三倍音域；土耳其 nay 用于 Mevlevi 旋转舞乐。','guqin-instrument,kora-instrument','vam-o304190'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")