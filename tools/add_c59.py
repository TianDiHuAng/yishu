# -*- coding: utf-8 -*-
"""Cycle59：新增 4 条（埃塞银护身符项链、Harar 新娘项链、刚果 nkisi nkondi、刚果基督像）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-2025-152","Cleveland Museum of Art — Necklace (ashän ketab) with amulet pendants (tälsäm), Ethiopia, acc. 2025.152",
  "https://openaccess-api.clevelandart.org/api/artworks/2025.152","2026-11-23 API HTTP 200；银合金；说明含伊斯兰护符实践与 Harar/Aksum 工艺"),
 ("cma-2025-155","Cleveland Museum of Art — Necklace (muriya), probably Harar, Ethiopia, acc. 2025.155",
  "https://openaccess-api.clevelandart.org/api/artworks/2025.155","2026-11-23 API HTTP 200；镀金银、树脂；说明含穆斯林女性专用与嫁妆"),
 ("cma-2010-432","Cleveland Museum of Art — Male figure (nkisi nkondi), Kongo, acc. 2010.432",
  "https://openaccess-api.clevelandart.org/api/artworks/2010.432","2026-11-23 API HTTP 200；木、金属化玻璃、铁、象牙等 46×25.7×19.2cm；说明含解除灵力的两种可能"),
 ("cma-2010-445","Cleveland Museum of Art — Corpus (Crucified Christ), Kongo, acc. 2010.445",
  "https://openaccess-api.clevelandart.org/api/artworks/2010.445","2026-11-23 API HTTP 200；铜合金 16.5×12.5×2.5cm；说明含几何化风格与穿孔手足")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('ethiopian-amulet-necklace','埃塞俄比亚护符项链（ashän ketab）','作品','art-africa','19—20世纪','非洲','综合','重要',
    '埃塞俄比亚银合金护符项链，克利夫兰艺术博物馆藏（2025.152）；由多个盒形护符（tälsäm）组成。','1800年代末或1900年代初',
    '盒形护符用以辟邪与挡「恶眼」，与伊斯兰护符实践相关；镂空与珠化工艺见於 Harar 与 Aksum。','ethiopian-harar-necklace,african-art','cma-2025-152'),
   ('ethiopian-harar-necklace','哈勒尔新娘项链（muriya）','作品','art-africa','19—20世纪','非洲','综合','重要',
    '埃塞俄比亚哈勒尔地区的镀金银项链，克利夫兰艺术博物馆藏（2025.155）。','1800年代末或1900年代初',
    '当地穆斯林女性专用，属嫁妆；球形银珠近于穆斯林念珠，琥珀或柯巴脂兼示婚姻身份与舶来品渠道。','ethiopian-amulet-necklace,african-art','cma-2025-155'),
   ('kongo-nkisi-nkondi','刚果灵力像（nkisi nkondi）','作品','art-africa','19—20世纪','非洲','雕塑','重要',
    '刚果工匠与祭司（nganga）所制木雕灵力像，克利夫兰艺术博物馆藏（2010.432）。','1800年代末—1900年代初',
    '现存的只是「壳」：赋予灵力的材料已被取走；取走或出于用途终结，或出于反殖民抵抗。','kongo-crucifix,african-art','cma-2010-432'),
   ('kongo-corpus','刚果基督受难像（Corpus）','作品','art-africa','19—20世纪','非洲','雕塑','重要',
    '刚果人以铜合金铸成的基督像，克利夫兰艺术博物馆藏（2010.445）。','1800年代末—1900年代初',
    '以几何化风格融合基督教理念与刚果既有艺匠传统；手足穿孔直指十字架受难图像。','kongo-nkisi-nkondi,kongo-crucifix','cma-2010-445')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")