# -*- coding: utf-8 -*-
"""Cycle161：文艺复兴 3 条（克拉纳赫×2 / 布龙齐诺）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1953-143","Cleveland Museum of Art — Lucas Cranach the Elder, The Baptism of Christ, 1530s, acc. 1953.143",
  "https://openaccess-api.clevelandart.org/api/artworks/1953.143","2026-11-24 API HTTP 200；木板油画 画心15×20.5cm；题款拉丁文刻于云上；说明含路德宗教艺术观与风景元素"),
 ("cma-1958-425","Cleveland Museum of Art — Lucas Cranach the Elder, Hunting near Hartenfels Castle, 1540, acc. 1958.425",
  "https://openaccess-api.clevelandart.org/api/artworks/1958.425","2026-11-24 API HTTP 200；木板油画后转至纤维板 画心116.8×170.2cm；签名为带翼蛇并题1540；说明含萨克森选帝侯狩猎场景"),
 ("cma-1972-121","Cleveland Museum of Art — Agnolo Bronzino, Portrait of a Woman, c. 1550, acc. 1972.121",
  "https://openaccess-api.clevelandart.org/api/artworks/1972.121","2026-11-24 API HTTP 200；木板油画 画心60×48.8cm；说明含美第奇宫廷画师身份、手势与服饰描述"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('cranach-baptism-of-christ','克拉纳赫《基督受洗》（1530年代）','作品','art-renaissance','16世纪','德国','油画','重要',
  '老卢卡斯·克拉纳赫的小幅木板油画，克利夫兰艺术博物馆藏（1953.143）。','1530年代',
  '该馆说明：画面以极细的笔触描绘，包含16世纪德国艺术风景的典型元素——茂密的森林、山顶城市与远山；克拉纳赫与宗教改革者马丁·路德关系密切，使基督教图像适应路德的信念，即宗教艺术必须叙述经文；福音书记载基督受洗时天开、鸽子降下并有声音说话，克拉纳赫把这句话以拉丁文直接画在云上。',
  'northern-renaissance,renaissance','cma-1953-143'),
 ('cranach-hartenfels-hunt','克拉纳赫《哈滕费尔斯城堡附近的狩猎》（1540）','作品','art-renaissance','16世纪','德国','油画','重要',
  '老卢卡斯·克拉纳赫署名并题年的狩猎场景，克利夫兰艺术博物馆藏（1958.425）。','1540年',
  '该馆说明：萨克森的新教统治者委托了这幅热闹的狩猎图，背景是他们的居所哈滕费尔斯城堡；左下角的约翰·腓特烈穿深绿狩猎服，正给十字弓上弦，等待侍从与猎犬把牡鹿赶过河；他的妻子萨碧勒选帝侯夫人站在右侧，准备第一箭的仪式性射击；萨克森选帝侯热衷以猎犬狩猎，这类场合经过精心排练，并以号角信号协调；克拉纳赫题了年份，签名是右下的带翼蛇，右角的1577为库存编号。',
  'northern-renaissance,renaissance','cma-1958-425'),
 ('bronzino-portrait-of-a-woman','布龙齐诺《女子肖像》（约1550）','作品','art-renaissance','16世纪','意大利·佛罗伦萨','油画','重要',
  '布龙齐诺的宫廷肖像，克利夫兰艺术博物馆藏（1972.121）。','约1550年',
  '该馆说明：布龙齐诺是佛罗伦萨公爵科西莫一世·德·美第奇的宫廷画师；这位女子无法确定身份，很可能与美第奇宫廷有关；与该展厅多数肖像一样，布龙齐诺强调财富、地位与宫廷的雅致，而非个性或个体化的表情；朴素的背景进一步突出了这件小幅作品的纪念碑性与宏伟；放在胸前、手指优雅张开的手可追溯到古希腊表示端庄的姿势，此处强调高位女性的得体举止；她穿着以平针绣装饰的亚麻护颈，部分与袖口一起镶有精细花边。',
  'mannerism,renaissance','cma-1972-121'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
txt="\n".join(lines)
T=[t for t in T if "'%s'"%t[0] not in txt]
if T:
    close=max(i for i,l in enumerate(lines) if l.strip()=="]")
    lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
    io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
