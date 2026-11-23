# -*- coding: utf-8 -*-
"""Cycle58：新增 4 条（埃塞俄比亚福音书页、十二使徒双联画；阿散蒂金衡砝码、灵魂圆盘）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1999-212","Cleveland Museum of Art — Leaf from a Gospel Book with Saint Luke, Ethiopia (Tigray), c. 1440–80, acc. 1999.212",
  "https://openaccess-api.clevelandart.org/api/artworks/1999.212","2026-11-23 API HTTP 200；犊皮纸墨与蛋彩 37×25cm；说明含吉兹文题记与圣路加"),
 ("cma-2023-4","Cleveland Museum of Art — Diptych with Twelve Apostles & St. Paul, Ethiopia (Gondär), c. 1700, acc. 2023.4",
  "https://openaccess-api.clevelandart.org/api/artworks/2023.4","2026-11-23 API HTTP 200；蛋彩、木、织物 39×51cm；说明含宫廷作坊风格与印度输入衣料"),
 ("cma-1961-399","Cleveland Museum of Art — Gold Weight (abrammuo): Fish, Asante, 1800s, acc. 1961.399",
  "https://openaccess-api.clevelandart.org/api/artworks/1961.399","2026-11-23 API HTTP 200；铜合金 2.8×6.6×0.4cm；说明含1600年以来的衡金用途与谚语图像"),
 ("cma-1944-290","Cleveland Museum of Art — Disk Pendant (akrafokɔnmu), Asante, 1800s (before 1871), acc. 1944.290",
  "https://openaccess-api.clevelandart.org/api/artworks/1944.290","2026-11-23 API HTTP 200；金 7×7.6×1.6cm；说明含 akrafo、kradware 与1924年之前停产")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('ethiopian-gospel-leaf','埃塞俄比亚福音书页（圣路加）','作品','art-africa','15世纪','非洲','绘画','重要',
    '埃塞俄比亚提格雷地区的福音书写本单页，克利夫兰艺术博物馆藏（1999.212）。','约1440—1480年',
    '满页细密画绘圣路加及其象征牛；色彩鲜亮、几何图案欢快；题记为吉兹文。','ethiopian-diptych,african-art','cma-1999-212'),
   ('ethiopian-diptych','十二使徒与圣保罗双联画','作品','art-africa','18世纪','非洲','绘画','重要',
    '埃塞俄比亚贡德尔地区的木胎蛋彩双联画，克利夫兰艺术博物馆藏（2023.4）。','约1700年',
    '绘十三位圣者，尺寸适用于教堂或精英居所；属1600年代初至1700年代中宫廷作坊的浓彩风格。','ethiopian-gospel-leaf,african-art','cma-2023-4'),
   ('asante-goldweight','阿散蒂金衡砝码（鱼形）','作品','art-africa','19世纪','非洲','雕塑','重要',
    '加纳阿散蒂金匠所作铜合金衡器，克利夫兰艺术博物馆藏（1961.399）。','1800年代',
    '至少自1600年起用于称量金粉与金块；王廷收藏最丰，平民常仅十余枚；图像分几何与具象两类，后者多以谚语为据。','asante-soul-disc,asante-memorial-head','cma-1961-399'),
   ('asante-soul-disc','阿散蒂灵魂圆盘（akrafokɔnmu）','作品','art-africa','19世纪','非洲','综合','重要',
    '加纳阿散蒂金匠行会所作金圆盘，克利夫兰艺术博物馆藏（1944.290）。','1800年代（1871年前；插针为后加）',
    '为 akrafo（「灵魂之人」）官员佩于胸前以示等级与职守；造型或受北非伊斯兰金币影响，同心水波纹影响其构图。','asante-goldweight,asante-memorial-head','cma-1944-290')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")