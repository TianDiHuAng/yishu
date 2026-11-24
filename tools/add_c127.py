# -*- coding: utf-8 -*-
"""Cycle127：日朝绘画 4 条（李昰应兰石屏、金禔雪景、渡边始兴潇湘八景、优陀念佛缘起绘卷）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-2015-138","Cleveland Museum of Art — Yi Ha-eung, Orchids and Rocks (8-panel screen), 1897–98, acc. 2015.138",
  "https://openaccess-api.clevelandart.org/api/artworks/2015.138","2026-11-24 API HTTP 200；绢本水墨八曲屏 185×52.6cm；说明含摄政与四君子"),
 ("cma-1987-187","Cleveland Museum of Art — Kim Si, Snowscape with Figures, 1584, acc. 1987.187",
  "https://openaccess-api.clevelandart.org/api/artworks/1987.187","2026-11-24 API HTTP 200；绢本水墨立轴 53×67.3cm；说明含稀少早期朝鲜画与心景（记录生卒存疑）"),
 ("cma-1960-284","Cleveland Museum of Art — Watanabe Shikō, Eight Views of Xiao-Xiang, early–mid 1700s, acc. 1960.284",
  "https://openaccess-api.clevelandart.org/api/artworks/1960.284","2026-11-24 API HTTP 200；纸本水墨六曲屏 150×356cm；说明含狩野派与中国题材"),
 ("cma-1956-87","Cleveland Museum of Art — Illustrated Miraculous Origins of the Yūzū Nenbutsu School, early 1300s, acc. 1956.87",
  "https://openaccess-api.clevelandart.org/api/artworks/1956.87","2026-11-24 API HTTP 200；纸本墨彩金绘卷 29.7×1232.4cm；说明含良忍与念佛互益"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('korean-orchids-rocks','李昰应《兰石图》八曲屏','作品','art-asia','19世纪','东亚','绘画','核心',
  '李昰应绢本水墨八曲屏，克利夫兰艺术博物馆藏（2015.138）。','1897—1898年',
  '李昰应（1820—1898）为高宗摄政（1866—73），亦为19世纪末文人画复兴名家、兰画巨擘；纯用水墨写悬崖垂兰，兰为四君子之一。','korean-snowscape-figures,korean-white-flask-longevity','cma-2015-138'),
 ('korean-snowscape-figures','金禔《雪景人物图》','作品','art-asia','16世纪','东亚','绘画','核心',
  '金禔绢本水墨立轴，克利夫兰艺术博物馆藏（1987.187）。','1584年',
  '早期朝鲜画罕存之例；父金安老失势后隐居为画人；孤学者处雪树雪山中，非理想化隐逸，而是家世荣光成往昔的「心景」。','korean-orchids-rocks,japan-eight-views-xiaoxiang','cma-1987-187'),
 ('japan-eight-views-xiaoxiang','渡边始兴《潇湘八景图》','作品','art-asia','18世纪','东亚','绘画','核心',
  '渡边始兴纸本水墨六曲屏（一对之一），克利夫兰艺术博物馆藏（1960.284）。','1700年代早—中期',
  '京都出身、多能善变；此屏反映狩野派训练：单色墨、雄健笔、取中国传统而非日本题材；取景宏阔以喻中国地景之大于日本。','japan-miraculous-origins,korean-snowscape-figures','cma-1960-284'),
 ('japan-miraculous-origins','《优陀念佛缘起绘卷》','作品','art-asia','14世纪','东亚','绘画','核心',
  '镰仓期纸本墨彩金绘卷（两卷之第二），克利夫兰艺术博物馆藏（1956.87）。','1300年代初',
  '首卷述良忍生平，本卷自其临终起，述奉其教之效验；良忍主一切互相关联、彼此称念阿弥陀名号之精神利益。','amida-descent-painting,japanese-art','cma-1956-87'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")