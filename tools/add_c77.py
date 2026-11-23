# -*- coding: utf-8 -*-
"""Cycle77：伊斯兰写本/细密画 4 条（大蒙古列王纪叶、设拉子对页、塞尔柱古兰经叶、复合《五宝》页）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1943-658","Cleveland Museum of Art — Bahram Gur Slays a Dragon, Great Mongol Shahnama, Tabriz, 1330–35, acc. 1943.658",
  "https://openaccess-api.clevelandart.org/api/artworks/1943.658","2026-11-23 API HTTP 200；纸本不透明水彩、墨、金 45.8×34.4cm；说明含中国式山石与龙"),
 ("cma-1956-10","Cleveland Museum of Art — Royal Reception in a Landscape, Shiraz, 1444, acc. 1956.10",
  "https://openaccess-api.clevelandart.org/api/artworks/1956.10","2026-11-23 API HTTP 200；纸本不透明水彩、墨、金银；说明含对页另一半在 CMA 1945.169"),
 ("cma-1933-488","Cleveland Museum of Art — Folio from a Qur'an, Seljuq, 1100s, acc. 1933.488",
  "https://openaccess-api.clevelandart.org/api/artworks/1933.488","2026-11-23 API HTTP 200；纸本墨、金与彩色 30.6×20cm；说明含两边经文出处"),
 ("cma-2013-315-2","Cleveland Museum of Art — Page from the Panj Ganj of Jami, acc. 2013.315.2",
  "https://openaccess-api.clevelandart.org/api/artworks/2013.315.2","2026-11-23 API HTTP 200；胶彩、墨与金；说明含赫拉特抄写与德干绘画的两段工序")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('great-mongol-shahnama-folio','《大蒙古列王纪》巴赫拉姆屠龙叶','作品','art-islamic','14世纪','西亚·中亚','绘画','核心',
    '伊儿汗国大不里士《列王纪》写本对页，克利夫兰艺术博物馆藏（1943.658）。','1330—1335年',
    '绘前伊斯兰时代的萨珊君主巴赫拉姆·古尔（420—438 在位）刺龙；山石、树干与龙取法中国样式。','shiraz-frontispiece,quran-folio-seljuq','cma-1943-658'),
   ('shiraz-frontispiece','设拉子《列王纪》对页（左半）','作品','art-islamic','15世纪','西亚·中亚','绘画','重要',
    '帖木儿朝设拉子《列王纪》双页卷首左半，克利夫兰艺术博物馆藏（1956.10）。','1444年',
    '画面并不图解史诗叙事，而很可能描绘**订制该写本的宫廷观众**；对页另一半在同馆（1945.169）。','great-mongol-shahnama-folio,panj-ganj-page','cma-1956-10'),
   ('quran-folio-seljuq','塞尔柱《古兰经》写本叶','作品','art-islamic','12世纪','西亚·中亚','书法','重要',
    '东波斯装饰性库法体《古兰经》叶，克利夫兰艺术博物馆藏（1933.488）。','1100年代',
    '正面为《大事章》56:1—26 共23行，背面为《至仁主章》55:73—78 共23行；边框饰金蓝圆章。','great-mongol-shahnama-folio,islamic-art','cma-1933-488'),
   ('panj-ganj-page','贾米《五宝》复合册页','作品','art-islamic','16—17世纪','南亚','绘画','核心',
    '贾米《五宝》诗集的册页，克利夫兰艺术博物馆藏（2013.315.2）。','文本约1500—1520；绘画与边饰1603—07',
    '文本由 Sultan-Ali Mashhadi 在赫拉特为 Badi al-Zaman Mirza 抄写；绘画与边饰由 Mushfiq 在德干为莫卧儿大臣 Abd al-Rahim 补作。','shiraz-frontispiece,great-mongol-shahnama-folio','cma-2013-315-2')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")