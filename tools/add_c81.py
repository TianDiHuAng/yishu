# -*- coding: utf-8 -*-
"""Cycle81：印度绘画再补 4 条（努尔普尔王肖像、穆拉德·巴赫什肖像宝石、乌特卡·纳伊卡、马鲁·拉吉尼）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-2013-324","Cleveland Museum of Art — Portrait of Raja Jagat Singh of Nurpur, probably 1619, acc. 2013.324",
  "https://openaccess-api.clevelandart.org/api/artworks/2013.324","2026-11-23 API HTTP 200；胶彩与金 19.1×11.6cm；说明含山国贵族在莫卧儿宫廷之罕与1624年斡旋"),
 ("cma-2013-327","Cleveland Museum of Art — Portrait of Murad Bakhsh (1624–61), c. 1635, acc. 2013.327",
  "https://openaccess-api.clevelandart.org/api/artworks/2013.327","2026-11-23 API HTTP 200；胶彩与金 画面4.3×3.5cm；说明含「肖像宝石」与1616年英国使节赠礼"),
 ("cma-1932-118","Cleveland Museum of Art — Utka Nayika (the heroine waiting), Pahari, c. 1800, acc. 1932.118",
  "https://openaccess-api.clevelandart.org/api/artworks/1932.118","2026-11-23 API HTTP 200；胶彩 16×10.2cm；说明含焦虑的手势与帕哈里人体比例"),
 ("cma-2018-168","Cleveland Museum of Art — Maru Ragini, from a Ragamala, 1650–80, acc. 2018.168",
  "https://openaccess-api.clevelandart.org/api/artworks/2018.168","2026-11-23 API HTTP 200；胶彩、墨与金 26×17.6cm；说明含拉贾斯坦民歌调式与骆驼骑士")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('jagat-singh-portrait','《努尔普尔王贾加特·辛格像》','作品','art-asia','17世纪','南亚','绘画','核心',
    '莫卧儿贾汉吉尔宫廷所绘山国王公像，克利夫兰艺术博物馆藏（2013.324）。','约1619年',
    '山国王公极少在莫卧儿宫廷任职，故此像属**罕见的帝国级莫卧儿绘画**；1624年王后为其叛乱求情。','murad-bakhsh-jewel,shri-raga-mewar','cma-2013-324'),
   ('murad-bakhsh-jewel','《穆拉德·巴赫什像》（肖像宝石）','作品','art-asia','17世纪','南亚','绘画','重要',
    '沙贾汗宫廷细密肖像，克利夫兰艺术博物馆藏（2013.327）。','约1635（边饰约1700年代）',
    '原嵌宝石作「肖像宝石」佩戴；此风尚与1616年英国使节所赠肖像细密画与浮雕宝石相关。','jagat-singh-portrait,panj-ganj-page','cma-2013-327'),
   ('utka-nayika','《乌特卡·纳伊卡》（等待情人的女主人公）','作品','art-asia','19世纪','南亚','绘画','重要',
    '帕哈里绘画，克利夫兰艺术博物馆藏（1932.118）。','约1800年',
    '夜色降临、雨云将至；以紧张的手势与不安的双足表现焦虑；叶铺成床而情人未至。','kausa-ragaputra,maru-ragini','cma-1932-118'),
   ('maru-ragini','《马鲁·拉吉尼》（Ragamala）','作品','art-asia','17世纪','南亚','绘画','重要',
    '拉贾斯坦或德干《旋律花环》之一，克利夫兰艺术博物馆藏（2018.168）。','1650—1680年',
    '拉杰普特武士持矛佩卡塔尔匕首与剑，与骆驼独立溪畔；其调式基于拉贾斯坦民歌，当地故事以骆驼骑士为主角。','kausa-ragaputra,utka-nayika','cma-2018-168')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")