# -*- coding: utf-8 -*-
"""Cycle109：伊斯兰织物 4 条（阿尔达比勒毯、乌沙克毯、奥斯曼灯芯缎丝、布尔萨丝绒）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o54307","Victoria and Albert Museum — The Ardabil Carpet, Iran, 1539–1540, O54307",
  "https://api.vam.ac.uk/v2/object/O54307","2026-11-24 API HTTP 200；羊毛栽绒丝绸地 长约1040cm；说明含塔赫玛斯普为萨法维丁神祠所订"),
 ("vam-o85243","Victoria and Albert Museum — The Ushak Carpet, Usak, ca. 1500, O85243",
  "https://api.vam.ac.uk/v2/object/O85243","2026-11-24 API HTTP 200；羊毛 531×250cm；说明含伊朗原型与土耳其改织"),
 ("vam-o94015","Victoria and Albert Museum — Ottoman lampas silk, Turkey, 16th c., O94015",
  "https://api.vam.ac.uk/v2/object/O94015","2026-11-24 API HTTP 200；丝与金属线 lampas 120.5×67.4cm；说明含无人物纹与逊尼派多数"),
 ("vam-o93545","Victoria and Albert Museum — Ottoman silk velvet, Bursa, early 17th c., O93545",
  "https://api.vam.ac.uk/v2/object/O93545","2026-11-24 API HTTP 200；丝绒金属包线 178×67.5cm 重6kg；说明含 kemha/seraser 与布尔萨"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('ardabil-carpet','阿尔达比勒地毯','作品','art-islamic','16世纪','西亚·中亚','织物','核心',
  '萨法维羊毛栽绒毯，维多利亚与艾伯特博物馆藏（O54307）。','1539—1540年（回历946）',
  '沙阿·塔赫玛斯普为一对之一，献其先祖萨法维丁在阿尔达比勒的神祠；为现存最大最精的伊斯兰地毯之一。','ushak-carpet,islamic-art','vam-o54307'),
 ('ushak-carpet','乌沙克地毯','作品','art-islamic','16世纪','西亚·中亚','织物','核心',
  '奥斯曼乌沙克羊毛毯，维多利亚与艾伯特博物馆藏（O85243）。','约1500年',
  '大尺度橄榄形团花与蔷薇成排；中央团花为主；原型出自伊朗，15世纪末被土耳其织工采用。','ardabil-carpet,ottoman-silk-lampas','vam-o85243'),
 ('ottoman-silk-lampas','奥斯曼灯芯缎丝织（lampas）','作品','art-islamic','16世纪','西亚·中亚','织物','重要',
  '奥斯曼丝与金属线 lampas，维多利亚与艾伯特博物馆藏（O94015）。','16世纪',
  '丝地橄榄格纹；宫廷风格刻意避免人物纹，以维系逊尼派多数之支持，故取抽象纹样。','ottoman-silk-velvet,ardabil-carpet','vam-o94015'),
 ('ottoman-silk-velvet','布尔萨奥斯曼丝绒','作品','art-islamic','17世纪','西亚·中亚','织物','核心',
  '布尔萨丝绒金属包线，维多利亚与艾伯特博物馆藏（O93545）。','17世纪初',
  '奶油色石竹置深红地、错列排布；最贵重者为丝绒与 kemha/seraser 复合织物，常夹银或银鎏金线；布尔萨为织造中心。','ottoman-silk-lampas,ushak-carpet','vam-o93545'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")