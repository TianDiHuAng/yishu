# -*- coding: utf-8 -*-
"""Cycle145：印度细密画 4 条（奥朗则布像、穆罕默德·阿里·贝格像、阿毗萨里卡·纳伊卡、巴尔万特·辛格）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o113934","Victoria and Albert Museum — The Mughal emperor Alamgir (Aurangzeb), 1698–99, O113934",
  "https://api.vam.ac.uk/v2/object/O113934","2026-11-24 API HTTP 200；纸本不透明水彩金 33.9×22.8cm；说明含1110AH与素白苦行"),
 ("vam-o16065","Victoria and Albert Museum — Muhammad Ali Beg, ambassador, by Hashim, ca. 1631, O16065",
  "https://api.vam.ac.uk/v2/object/O16065","2026-11-24 API HTTP 200；纸本不透明水彩 38.7×26.4cm；说明含沙阿阿巴斯使节与波斯铭"),
 ("vam-o72339","Victoria and Albert Museum — Abhisarika Nayika, Pahari, ca. 1760, O72339",
  "https://api.vam.ac.uk/v2/object/O72339","2026-11-24 API HTTP 200；纸本不透明水彩 36×25.5cm；说明含八纳伊卡与风雨夜赴约"),
 ("vam-o96492","Victoria and Albert Museum — Raja Balwant Singh, by Nainsukh, ca. 1750, O96492",
  "https://api.vam.ac.uk/v2/object/O96492","2026-11-24 API HTTP 200；纸本不透明水彩金 25×37.5cm；说明含Nainsukh与宫廷娱乐"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('mughal-alamgir-portrait','莫卧儿皇帝奥朗则布像','作品','art-asia','17世纪','南亚','绘画','核心',
  '莫卧儿皇帝奥朗则布（Alamgir）像，维多利亚与艾伯特博物馆藏（O113934）。','1698—1699年（1110 AH）',
  '晚年奥朗则布乘帕輿、四肩夫抬行于绿丘；面白、通身素白无饰（仅绿金条纹头巾带），合其晚年苦行；缩肩、双手举起若祈祷；二侍随行持伞与日扇。','rai-singh-bikaner,jagat-singh-hunting','vam-o113934'),
 ('mughal-muhammad-ali-beg','伊朗使节穆罕默德·阿里·贝格像','作品','art-asia','17世纪','南亚','绘画','核心',
  '穆罕默德·阿里·贝格像（Hashim作），维多利亚与艾伯特博物馆藏（O16065）。','约1631年',
  '沙阿·阿巴斯遣莫卧儿宫廷之使节，1631年3月新年入朝、留至1633年10月；王室画师 Hashim 绘；绿底、边饰花卉昆虫；波斯铭「使节穆罕默德·阿里·贝格之像，Hashim 作」。','mughal-alamgir-portrait,pahari-balwant-singh','vam-o16065'),
 ('pahari-abhisarika-nayika','帕哈里《阿毗萨里卡·纳伊卡》','作品','art-asia','18世纪','南亚','绘画','核心',
  '帕哈里细密画，维多利亚与艾伯特博物馆藏（O72339）。','约1760年',
  '「赴约的女主角」冒风雨黑夜赴情人约：曲缘山坡树下、远处云电、树下有蛇；破碎饰物落于近蛇处；帕哈里（旁遮普山地）常绘「八纳伊卡」，写女子种种恋爱情态。','pahari-balwant-singh,utka-nayika','vam-o72339'),
 ('pahari-balwant-singh','帕哈里《巴尔万特·辛格王》','作品','art-asia','18世纪','南亚','绘画','核心',
  '帕哈里画师 Nainsukh 作，维多利亚与艾伯特博物馆藏（O96492）。','约1750年',
  '巴尔万特·辛格坐左侧宝座华盖下、吸水烟，观右侧乐舞（舞者与乐师）；背景留白；王（1724—1763）自1740年代起为 Nainsukh 的赞助人，后者绘其多种宫廷活动。','pahari-abhisarika-nayika,mughal-muhammad-ali-beg','vam-o96492'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")