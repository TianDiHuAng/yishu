# -*- coding: utf-8 -*-
"""Cycle96：大洋洲 4 条（毛利 hei-tiki、毛利 Wakahuia、阿斯马特战盾、塔米群岛木碗）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1969-107","Cleveland Museum of Art — Hei-tiki Neck Pendant, Māori, 1800s, acc. 1969.107",
  "https://openaccess-api.clevelandart.org/api/artworks/1969.107","2026-11-23 API HTTP 200；绿玉（pounamu）16.9×10.2cm；说明含 mana 与 Hine-te-Iwaiwa"),
 ("cma-1961-405","Cleveland Museum of Art — Treasure Box (Wakahuia), Māori, 1800s, acc. 1961.405",
  "https://openaccess-api.clevelandart.org/api/artworks/1961.405","2026-11-23 API HTTP 200；木与鲍鱼壳 17.2cm；说明含 tapu 与库克船长1769—70"),
 ("cma-1963-554","Cleveland Museum of Art — War Shield, Asmat, c. 1940, acc. 1963.554",
  "https://openaccess-api.clevelandart.org/api/artworks/1963.554","2026-11-23 API HTTP 200；彩绘木 176.5×60.3×7cm；说明含猎头与红白黑三色"),
 ("cma-1965-322","Cleveland Museum of Art — Bowl, Tami Islands, 1800s, acc. 1965.322",
  "https://openaccess-api.clevelandart.org/api/artworks/1965.322","2026-11-23 API HTTP 200；彩绘木 9.9×40.3×17.4cm；说明含骨质工具与家族花纹所有权"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('maori-hei-tiki','毛利 hei-tiki 颈坠','作品','art-oceania','19世纪','大洋洲','雕塑','核心',
  '毛利绿玉颈坠，克利夫兰艺术博物馆藏（1969.107）。','1800年代',
  '首领世袭并承载 mana；此坠为连接生者与前欧祖先的传家宝；或表现 Hine-te-Iwaiwa，生育守护者。','african-art,oceania-art','cma-1969-107'),
 ('maori-wakahuia','毛利 Wakahuia 宝盒','作品','art-oceania','19世纪','大洋洲','雕塑','核心',
  '毛利木雕鲍鱼壳宝盒，克利夫兰艺术博物馆藏（1961.405）。','1800年代',
  '浅浮雕螺旋与两端小人像；盛首领饰物；因首级与颈部为 tapu，故悬于屋梁；库克1769—70所见即此类。','maori-hei-tiki,oceania-art','cma-1961-405'),
 ('asmat-war-shield','阿斯马特战盾','作品','art-oceania','20世纪','大洋洲','雕塑','核心',
  '阿斯马特彩绘木战盾，克利夫兰艺术博物馆藏（1963.554）。','约1940年',
  '刻盾以盛宴庆祝、随即猎头；盾以祖先命名；用红树板根，施石灰白/赭红/炭黑；果象征人头，食果兽即猎头祖先。','oceania-art,african-art','cma-1963-554'),
 ('tami-bowl','塔米群岛木碗','作品','art-oceania','19世纪','大洋洲','综合','重要',
  '塔米群岛彩绘木碗，克利夫兰艺术博物馆藏（1965.322）。','1800年代',
  '以石斧、竹刀、树熊牙与猪/鹤鸵/狗骨为工具；用杜鹃木，刻纹深浅不一，多施石墨并抛光；花纹为家族所有。','asmat-war-shield,oceania-art','cma-1965-322'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")