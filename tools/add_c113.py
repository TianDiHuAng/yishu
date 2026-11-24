# -*- coding: utf-8 -*-
"""Cycle113：乐器 4 条（Baffo 羽管键琴、Maler 鲁特琴、诺森伯兰风笛、斯特拉迪瓦里小提琴）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o58982","Victoria and Albert Museum — Giovanni Baffo harpsichord, Venice, 1574, O58982",
  "https://api.vam.ac.uk/v2/object/O58982","2026-11-24 API HTTP 200；松木箱柏木音板 223×90.7cm；说明含伊斯兰纹样与50键"),
 ("vam-o122435","Victoria and Albert Museum — Lute by Laux Maler, Bologna, ca. 1540, O122435",
  "https://api.vam.ac.uk/v2/object/O122435","2026-11-24 API HTTP 200；枫木肋 56×33×16.8cm；说明含仅肋为原件与Maler"),
 ("vam-o58248","Victoria and Albert Museum — Northumberland bagpipe, Newcastle, ca. 1830, O58248",
  "https://api.vam.ac.uk/v2/object/O58248","2026-11-24 API HTTP 200；乌木象牙黄铜桃花心木 多部件；说明含风箱驱动与室内演奏"),
 ("vam-o93114","Victoria and Albert Museum — Stradivari violin, Cremona, 1699, O93114",
  "https://api.vam.ac.uk/v2/object/O93114","2026-11-24 API HTTP 200；枫木背松木面 全长59cm；说明含琴头出自另一琴"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('baffo-harpsichord','巴福羽管键琴（威尼斯，1574）','作品','music-instruments','16世纪','欧洲','乐器','核心',
  '威尼斯巴福制羽管键琴，维多利亚与艾伯特博物馆藏（O58982）。','1574年',
  '50键GG/BB至c3、两列同音弦；柏木音板哥特窗花圆饰；饰伊斯兰纹样与古典母题；末端被截。','maler-lute,stradivari-violin','vam-o58982'),
 ('maler-lute','马勒鲁特琴（博洛尼亚，约1540）','作品','music-instruments','16世纪','欧洲','乐器','核心',
  '博洛尼亚 Laux Maler 制鲁特琴，维多利亚与艾伯特博物馆藏（O122435）。','约1540年',
  '十一根花纹枫木肋以犊皮/布/胶拼合；仅肋为原件；颈与琴头约1967年补配；Maler 或为其时最伟大的制琴师。','baffo-harpsichord,stradivari-violin','vam-o122435'),
 ('northumberland-bagpipe','诺森伯兰风笛（约1830）','作品','music-instruments','19世纪','欧洲','乐器','核心',
  '纽卡斯尔诺森伯兰风笛，维多利亚与艾伯特博物馆藏（O58248）。','约1830年',
  '乌木管、象牙箍、黄铜键；封闭式旋律管四铜键加四持续管；以风箱而非口吹驱动，音色柔和，多室内演奏。','baffo-harpsichord,maler-lute','vam-o58248'),
 ('stradivari-violin','斯特拉迪瓦里小提琴（1699）','作品','music-instruments','17世纪','欧洲','乐器','核心',
  '克雷莫纳斯特拉迪瓦里小提琴，维多利亚与艾伯特博物馆藏（O93114）。','1699年',
  '两块松木面板、双线镶边；背为两块枫木；漆非原漆；颈为后配；琴头出自另一琴。','maler-lute,baffo-harpsichord','vam-o93114'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")