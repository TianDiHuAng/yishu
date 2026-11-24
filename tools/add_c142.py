# -*- coding: utf-8 -*-
"""Cycle142：伊斯兰地毯 4 条（波兰式毯、萨尔廷毯、切尔西毯、开罗宫廷毯）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o85114","Victoria and Albert Museum — 'Polonaise' carpet, Isfahan, 1600–1625, O85114",
  "https://api.vam.ac.uk/v2/object/O85114","2026-11-24 API HTTP 200；丝金银线 259×144.8cm；说明含伊朗制与纳杰夫神祠毯"),
 ("vam-o54294","Victoria and Albert Museum — The Salting Carpet, Iran, 1560–1580, O54294",
  "https://api.vam.ac.uk/v2/object/O54294","2026-11-24 API HTTP 200；2.31×1.65m；说明含哈菲兹诗与夜莺"),
 ("vam-o85144","Victoria and Albert Museum — The Chelsea Carpet, Iran, 1500–1550, O85144",
  "https://api.vam.ac.uk/v2/object/O85144","2026-11-24 API HTTP 200；羊毛栽绒丝经 549×310cm 重40kg；说明含书籍艺术类比"),
 ("vam-o79396","Victoria and Albert Museum — Ottoman court carpet, Cairo, 1525–1550, O79396",
  "https://api.vam.ac.uk/v2/object/O79396","2026-11-24 API HTTP 200；羊毛 2180×2030cm 重18.5kg；说明含六片缝合与21相关件"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('polonaise-carpet','「波兰式」毯（伊斯法罕）','作品','art-islamic','17世纪','西亚·中亚','织物','核心',
  '伊斯法罕丝金银线毯，维多利亚与艾伯特博物馆藏（O85114）。','1600—1625年',
  '实为伊朗所制而误名「波兰式」；红线黄线丝地配金银线；纹样近于阿巴斯大帝献纳杰夫神祠巨毯；17世纪初经贸易/王室馈赠入欧。','ardabil-carpet,salting-carpet','vam-o85114'),
 ('salting-carpet','萨尔廷毯','作品','art-islamic','16世纪','西亚·中亚','织物','核心',
  '伊朗精美地毯，维多利亚与艾伯特博物馆藏（O54294）。','1560—1580年',
  '中央分瓣团花、金属线与粉色缠枝于红地，主区深蓝地填云带、莲与含兽首之花、褐鸟（或夜莺）；边饰绕哈菲兹（卒1389）波斯诗句，咏花园/夜莺/玫瑰/酒。','ardabil-carpet,polonaise-carpet','vam-o54294'),
 ('chelsea-carpet','切尔西毯','作品','art-islamic','16世纪','西亚·中亚','织物','核心',
  '伊朗羊毛栽绒丝经毯，维多利亚与艾伯特博物馆藏（O85144）。','1500—1550年',
  '萨法维朝前半，红地重复团花间填动物鸟树，主边往复纹；虽无铭，却与早期萨法维书籍艺术及狩猎毯相通；尺幅巨大而团花一统。','salting-carpet,polonaise-carpet','vam-o85144'),
 ('cairo-court-carpet','开罗奥斯曼宫廷毯','作品','art-islamic','16世纪','西亚·中亚','织物','核心',
  '开罗奥斯曼宫廷毯，维多利亚与艾伯特博物馆藏（O79396）。','1525—1550年',
  '绿松蓝大团花居中、四角四分一花，红地花卉；看似完整实由至少六大片缝合；与巴黎装饰艺术馆一方几近相同，另有华盛顿/开罗/斯德哥尔摩及V&A残片，共21件相关散藏各处。','ardabil-carpet,chelsea-carpet','vam-o79396'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")