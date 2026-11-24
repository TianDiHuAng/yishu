# -*- coding: utf-8 -*-
"""Cycle117：非洲/织物 4 条（肯特布×2 V&A、马诺面具、Gelede 面具 CMA）。查重。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o263818","Victoria and Albert Museum — Kente cloth, Ghana, 1900–1949, O263818",
  "https://api.vam.ac.uk/v2/object/O263818","2026-11-24 API HTTP 200；棉条织纬浮 185×118cm；说明含 Asante/Ewe 条织传统"),
 ("vam-o164606","Victoria and Albert Museum — Kente cloth, Ghana, mid-20th c., O164606",
  "https://api.vam.ac.uk/v2/object/O164606","2026-11-24 API HTTP 200；手织棉 19条幅 283×200cm；说明含叶纹纬浮与错位排布"),
 ("cma-1953-457","Cleveland Museum of Art — Mano mask, Liberia, acquired 1933–37 by George Harley, acc. 1953.457",
  "https://openaccess-api.clevelandart.org/api/artworks/1953.457","2026-11-23 API HTTP 200；木铜合金纤维布皮革牙珠树脂铁玻璃珠 28×15.2cm；说明含11类型与森林精灵"),
 ("cma-1975-168-1","Cleveland Museum of Art — Gelede mask, Yorùbá, c. 1945–1950, acc. 1975.168.1",
  "https://openaccess-api.clevelandart.org/api/artworks/1975.168.1","2026-11-23 API HTTP 200；木与颜料 77.7cm；说明含 Ìyá Nlá 与鳄鱼冠饰"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"V&A / Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('kente-cloth-va1900','肯特布（Kente，1900—49）','作品','art-africa','20世纪','非洲','织物','核心',
  '加纳棉质条织肯特布，维多利亚与艾伯特博物馆藏（O263818）。','1900—1949年',
  '窄幅手织条拼缝成整布；Asante/Ewe 男织工用小双综手织机；条幅错位排布仿大织机效果；历史上为王室与精英专属。','kente-cloth-va1950,ottoman-silk-lampas','vam-o263818'),
 ('kente-cloth-va1950','肯特布（Kente，20世纪中）','作品','art-africa','20世纪','非洲','织物','核心',
  '加纳手织棉肯特布，维多利亚与艾伯特博物馆藏（O164606）。','20世纪中期',
  '由19条约10cm宽条幅拼成；中部纬浮叶纹；裁后纹样能否对齐是织工技艺之证。','kente-cloth-va1900,ardabil-carpet','vam-o164606'),
 ('mano-mask-liberia','马诺面具（利比里亚）','作品','art-africa','20世纪','非洲','雕塑','重要',
  '利比里亚马诺风格面具，克利夫兰艺术博物馆藏（1953.457）。','1900年代初（1933—37 前收集）',
  '马诺面具为森林精灵之显形，可分11大类（社会控制/政治司法/调停/教育/竞技/娱乐）；由医疗传教士 George Harley 在利比里亚收集。','gambanda-female-mask,bwa-buffalo-mask','cma-1953-457'),
 ('gelede-mask-yoruba','约鲁巴 Gelede 面具','作品','art-africa','20世纪','非洲','雕塑','核心',
  '约鲁巴 Gelede 会社面具，克利夫兰艺术博物馆藏（1975.168.1）。','约1945—1950年',
  '成对面具用于年度假面游行敬 Ìyá Nlá（大母）；画「美丽少女」而头巾上蹲鳄鱼（关联女巫与雷神），活动尾在表演中摆动；多次重漆以保持鲜艳。','gambanda-female-mask,mano-mask-liberia','cma-1975-168-1'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")