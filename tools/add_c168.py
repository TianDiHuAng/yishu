# -*- coding: utf-8 -*-
"""Cycle168：音乐题材美术作品 3 条（普雷勒 / 邦万 / 奥赫特费尔特）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1976-7","Cleveland Museum of Art — Friedrich Preller, Musicale at the Prellers', 1838, acc. 1976.7",
  "https://openaccess-api.clevelandart.org/api/artworks/1976.7","2026-11-24 API HTTP 200；铅笔纸本 纸张31.3×41.4cm；题款含画家字母组合与1838（其中8由9改成）；说明含家庭音乐聚会、钢琴为聚会中心、两位姐妹与戴眼罩的奥琳达"),
 ("cma-2010-166","Cleveland Museum of Art — François Bonvin, Woman at the Spinet, 1860, acc. 2010.166",
  "https://openaccess-api.clevelandart.org/api/artworks/2010.166","2026-11-24 API HTTP 200；黑色粉笔加棕红粉笔与擦笔 纸张42×30.5cm；题款F. Bonvin 1860；说明含弹琴女子很可能是塞琳·普吕奈尔、粉红康乃馨或暗示音乐与情感的短暂"),
 ("cma-1991-23","Cleveland Museum of Art — Jacob Ochtervelt, A Musical Company, c. 1668, acc. 1991.23",
  "https://openaccess-api.clevelandart.org/api/artworks/1991.23","2026-11-24 API HTTP 200；布面油画 画心58.5×48.9cm；说明含场景很可能是妓院、竖笛与小提琴不看谱演奏被视为较粗俗并与妓女相联系、对比德·霍赫的优雅音乐"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('preller-musicale','普雷勒《普雷勒家的音乐会》（1838）','作品','art-neo-romantic','19世纪','德国','素描','重要',
  '普雷勒画家庭音乐聚会的铅笔素描，克利夫兰艺术博物馆藏（1976.7）。','1838年',
  '该馆说明：此画描绘德国风景画家普雷勒夫妇家中的一次午后或晚间聚会，钢琴是这次家庭社交的中心；围着钢琴的年轻女子中有两位姐妹，其中戴眼罩的是奥琳达，她跟普雷勒学画，与画家一家很亲近。',
  'romanticism-art,romantic-music','cma-1976-7'),
 ('bonvin-woman-at-spinet','邦万《斯皮耐琴前的女子》（1860）','作品','art-neo-romantic','19世纪','法国','素描','重要',
  '邦万画弹琴女子的粉笔素描，克利夫兰艺术博物馆藏（2010.166）。','1860年',
  '该馆说明：女子弹琴是邦万反复画的题材；画中弹琴者很可能是21岁的音乐家塞琳·普吕奈尔，她于1860年嫁给年长许多的画家，不到三年后离开；脚边的粉红康乃馨或许暗示音乐与情感的短暂。',
  'realism-art,romantic-music','cma-2010-166'),
 ('ochtervelt-musical-company','奥赫特费尔特《音乐聚会》（约1668）','作品','art-baroque','17世纪','荷兰','油画','重要',
  '奥赫特费尔特画室内音乐场景的油画，克利夫兰艺术博物馆藏（1991.23）。','约1668年',
  '该馆说明：画中人物神态平静优雅，但这个室内场景很可能是妓院，背景一排女子肖像是线索；音乐描绘提供另一条线索：竖笛与小提琴不看谱演奏，被视为较粗俗并与卖淫相联系，而该馆德·霍赫的作品中则是优雅而复杂的演奏。',
  'baroque,baroque-music','cma-1991-23'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
txt="\n".join(lines)
T=[t for t in T if "'%s'"%t[0] not in txt]
if T:
    close=max(i for i,l in enumerate(lines) if l.strip()=="]")
    lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
    io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
