# -*- coding: utf-8 -*-
"""Cycle72：伊斯兰再补 4 条（多棱执壶、鸟形水器、飞鸟纹碗、钢制铭文板）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1945-27","Cleveland Museum of Art — Twelve-sided Ewer with Sphinxes, Khurasan, 1300–1350, acc. 1945.27",
  "https://openaccess-api.clevelandart.org/api/artworks/1945.27","2026-11-23 API HTTP 200；锤揲铜嵌银 44.8cm；说明含人首铭文"),
 ("cma-1948-458","Cleveland Museum of Art — Bird-shaped Vessel, Iran (Seljuq), 1100s, acc. 1948.458",
  "https://openaccess-api.clevelandart.org/api/artworks/1948.458","2026-11-23 API HTTP 200；青铜铸件嵌蓝玻璃 17.5×9.5cm；说明含 aquamanile 假说"),
 ("cma-1915-589","Cleveland Museum of Art — Bowl with Flying Birds, probably Kashan, 1280–1400, acc. 1915.589",
  "https://openaccess-api.clevelandart.org/api/artworks/1915.589","2026-11-23 API HTTP 200；fritware 釉下彩（Sultanabad） 11.2×22cm；说明含中国母题与西摩格"),
 ("cma-1994-1","Cleveland Museum of Art — Inscription Plaque, Iran (Safavid), c. 1693, acc. 1994.1",
  "https://openaccess-api.clevelandart.org/api/artworks/1994.1","2026-11-23 API HTTP 200；锻造钢镂空 27×35cm；说明含沙阿苏莱曼二世陵与33:56")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('khurasan-ewer','呼罗珊多棱执壶（狮与斯芬克斯）','作品','art-islamic','13—14世纪','西亚·中亚','综合','重要',
    '伊儿汗国呼罗珊锤揲铜嵌银执壶，克利夫兰艺术博物馆藏（1945.27）。','1300—1350年',
    '流与颈作伏狮与坐狮浮雕，腹部上下分别环列有翼兔形兽与斯芬克斯；底部一圈「人首铭文」。','wade-cup,islamic-art','cma-1945-27'),
   ('seljuq-bird-vessel','塞尔柱鸟形水器','作品','art-islamic','12世纪','西亚·中亚','综合','重要',
    '伊朗塞尔柱青铜鸟形器，克利夫兰艺术博物馆藏（1948.458）。','1100年代',
    '或为中世纪净手用水器（aquamanile）：水自胸前孔注入、由可动喙部倒出；蓝绿眼珠或为辟邪。','khurasan-ewer,islamic-art','cma-1948-458'),
   ('sultanabad-bowl','苏丹纳巴德飞鸟纹碗','作品','art-islamic','13—14世纪','西亚·中亚','综合','重要',
    '伊儿汗国（或为卡尚）釉下彩碗，克利夫兰艺术博物馆藏（1915.589）。','1280—1400年',
    '中国母题（龙、凤、莲）在伊儿汗期进入波斯艺术；凤凰与《列王纪》中的西摩格相类比；平口沿受中国器形影响。','minai-beaker,luster-dish-prince','cma-1915-589'),
   ('safavid-steel-plaque','萨法维钢制铭文板','作品','art-islamic','17世纪','西亚·中亚','建筑','重要',
    '伊朗萨法维锻造钢镂空铭文板，克利夫兰艺术博物馆藏（1994.1）。','约1693年',
    '据说原饰于沙阿苏莱曼二世（1666—93 在位）陵墓；铭文为《古兰经》33:56；钢材强度使繁复镂空成为可能。','iznik-tile-spandrel,islamic-art','cma-1994-1')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")