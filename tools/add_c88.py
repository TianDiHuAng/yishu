# -*- coding: utf-8 -*-
"""Cycle88：意大利/德国巴洛克 4 条（皮热、帕罗迪、多西亚 Spring、利斯 Cupid）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1964-36","Cleveland Museum of Art — Pierre Puget, Study for The Blessed Alessandro Sauli, 1663–68, acc. 1964.36",
  "https://openaccess-api.clevelandart.org/api/artworks/1964.36","2026-11-23 API HTTP 200；陶土 69.7cm；说明含热那亚教堂大型雕像小稿与改革家身份"),
 ("cma-2018-257","Cleveland Museum of Art — Filippo Parodi, Sleeping Christ Child, c. 1675, acc. 2018.257",
  "https://openaccess-api.clevelandart.org/api/artworks/2018.257","2026-11-23 API HTTP 200；大理石 63×102×42cm；说明含抛光差异与死亡隐喻"),
 ("cma-1999-213","Cleveland Museum of Art — Doccia Porcelain Factory / Soldani, Spring, mid-1700s, acc. 1999.213",
  "https://openaccess-api.clevelandart.org/api/artworks/1999.213","2026-11-23 API HTTP 200；瓷 40.6×55.9cm；说明含1743年购模型与1708四季浮雕"),
 ("cma-1971-100","Cleveland Museum of Art — Johann Liss, Cupid (Amor), c. 1630, acc. 1971.100",
  "https://openaccess-api.clevelandart.org/api/artworks/1971.100","2026-11-23 API HTTP 200；布面油画 87.7×65.7cm；说明含威尼斯色彩与卡拉瓦乔明暗"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('puget-sauli-study','皮热《圣阿莱桑德罗·绍利》小稿','作品','art-baroque','17世纪','欧洲','雕塑','重要',
  '法国雕塑家皮热为热那亚教堂大型像所作陶土小稿，克利夫兰艺术博物馆藏（1964.36）。','1663—1668年',
  '王室改革家绍利扭转身体、神情专注；摊开的书指向其改革事业。','baroque,pedro-de-mena-peter','cma-1964-36'),
 ('parodi-sleeping-christ','帕罗迪《睡着的基督圣婴》','作品','art-baroque','17世纪','欧洲','雕塑','核心',
  '意大利大理石雕塑，克利夫兰艺术博物馆藏（2018.257）。','约1675年',
  '以抛光差异区分肌肤（柔和发亮）与头发/稻草（粗糙吸光）；睡眠隐喻死亡，引向对基督人性受难的冥想。','baroque,caravaggio','cma-2018-257'),
 ('doccia-spring-relief','多西亚瓷厂《春》浮雕','作品','art-baroque','18世纪','欧洲','雕塑','重要',
  '佛罗伦萨近郊多西亚瓷厂烧制瓷浮雕，克利夫兰艺术博物馆藏（1999.213）。','18世纪中期',
  '瓷厂1743年购得索尔达尼后裔手中的模型，其中包括1708为费迪南多·德·美第奇所作四季浮雕；本件为其中《春》。','soldani-apollo-daphne,baroque','cma-1999-213'),
 ('liss-cupid','利斯《丘比特》','作品','art-baroque','17世纪','欧洲','绘画','核心',
  '德国画家约翰·利斯布面油画，克利夫兰艺术博物馆藏（1971.100）。','约1630年',
  '曾学于荷兰与安特卫普，约1620年赴罗马与威尼斯；色彩与运笔承威尼斯传统，强烈明暗受卡拉瓦乔影响。','caravaggio,baroque','cma-1971-100'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")