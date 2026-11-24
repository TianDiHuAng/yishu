# -*- coding: utf-8 -*-
"""Cycle147：伊斯兰玻璃 4 条（马穆鲁克瓶1350、狮纹杯、卡利格拉菲瓶1347、Qijlis灯1320）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o813","Victoria and Albert Museum — Mamluk gilded and enamelled bottle, c. 1350, O813",
  "https://api.vam.ac.uk/v2/object/O813","2026-11-24 API HTTP 200；描金珐琅玻璃 44.5×21.5cm；说明含凤凰与匿名苏丹献辞"),
 ("vam-o829","Victoria and Albert Museum — Mamluk enamelled beaker, 1250–1350, O829",
  "https://api.vam.ac.uk/v2/object/O829","2026-11-24 API HTTP 200；描金珐琅玻璃 14.6×8.0cm；说明含红狮白章与「荣耀归于吾主苏丹王」"),
 ("vam-o624","Victoria and Albert Museum — Mamluk gilded bottle, 1347–1370, O624",
  "https://api.vam.ac.uk/v2/object/O624","2026-11-24 API HTTP 200；吹制描金珐琅玻璃；说明含Saif al-Din Jurji与双重圆章"),
 ("vam-o1502","Victoria and Albert Museum — Mosque lamp of Qijlis, 1320–1330, O1502",
  "https://api.vam.ac.uk/v2/object/O1502","2026-11-24 API HTTP 200；描金珐琅玻璃 28.9×25.4cm；说明含剑徽与「安拉之寺」经文"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('mamluk-glass-bottle-1350','马穆鲁克描金珐琅瓶（约1350）','作品','art-islamic','14世纪','西亚·中亚','玻璃','核心',
  '埃及马穆鲁克描金珐琅玻璃瓶，维多利亚与艾伯特博物馆藏（O813）。','约1350年',
  '撇足与颈环；颈部凤凰作纹章姿，红绿黄珐琅花卉；铭为匿名苏丹献辞；世俗珐琅玻璃鲜有完好存世；主纹为蓝彩大字铭，约1300—1350典型；口下与高足顶的线脚示……（记录截断）。','mamluk-mosque-lamp,mamluk-glass-beaker','vam-o813'),
 ('mamluk-glass-beaker','马穆鲁克狮纹玻璃杯','作品','art-islamic','13—14世纪','西亚·中亚','玻璃','核心',
  '马穆鲁克描金珐琅玻璃杯，维多利亚与艾伯特博物馆藏（O829）。','1250—1350年',
  '横饰带：白圆章内红狮马穆鲁克徽、蓝地阿拉伯铭「荣耀归于吾主苏丹王」；上下透明玻璃上红描鱼与叶；两白圆章各红狮或指王室徽记。','mamluk-mosque-lamp,mamluk-glass-bottle-1350','vam-o829'),
 ('mamluk-glass-bottle-1347','马穆鲁克描金瓶（1347—70）','作品','art-islamic','14世纪','西亚·中亚','玻璃','核心',
  '马穆鲁克吹制描金玻璃瓶，维多利亚与艾伯特博物馆藏（O624）。','1347—1370年',
  '长颈撇口、球腹窄足；纹以金描；圆章与矩形开光交替，圆章外绕双股辫纹；开光书法颂 Sayf al-Din Jurji（曾侍苏丹哈桑，14世纪中）；V&A购入时称同类最大最精之一。（记录无尺寸）','mamluk-glass-bottle-1350,mamluk-glass-beaker','vam-o624'),
 ('mamluk-lamp-1320','Qijlis 清真寺灯（1320—30）','作品','art-islamic','14世纪','西亚·中亚','玻璃','核心',
  '马穆鲁克描金珐琅玻璃清真寺灯，维多利亚与艾伯特博物馆藏（O1502）。','1320—1330年',
  '为高官、前苏丹军械师 Qijlis 所制；其徽为剑，见于大圆章；章间引《古兰经》「安拉之寺」句；电力之前照明为奢侈，为宗教建筑供灯被视为一种……（记录截断）。','mamluk-mosque-lamp,mamluk-glass-bottle-1347','vam-o1502'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")