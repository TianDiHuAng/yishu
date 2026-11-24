# -*- coding: utf-8 -*-
"""Cycle106：V&A 来源 4 条（韩国青瓷瓶/青瓷莲童碗/白瓷寿纹扁壶/卡尚米哈拉布釉砖）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-O16589","Victoria and Albert Museum — Long-necked celadon bottle with inlays and underglaze copper red, Korea, 1200–1250, O16589",
  "https://api.vam.ac.uk/v2/object/O16589","2026-11-24 API HTTP 200；高句丽青瓷 高35cm；说明含镶嵌黑白与铜红"),
 ("vam-O22279","Victoria and Albert Museum — Celadon Bowl with Raised Lotus and Boy Design, Korea, 1200–1250, O22279",
  "https://api.vam.ac.uk/v2/object/O22279","2026-11-24 API HTTP 200；青瓷 高7.4cm；说明含模印莲童与三支烧痕"),
 ("vam-O22419","Victoria and Albert Museum — White Porcelain Flask with Raised Design and Inscription of 壽, Korea, 1750–1800, O22419",
  "https://api.vam.ac.uk/v2/object/O22419","2026-11-24 API HTTP 200；白瓷 高15.1cm；说明含蝙蝠/寿字与谚文底款"),
 ("vam-O67415","Victoria and Albert Museum — Salting Mihrab, Kashan, ca. 1300, O67415",
  "https://api.vam.ac.uk/v2/object/O67415","2026-11-24 API HTTP 200；熔块胎釉上彩 高62cm；说明含墓葬标志与米哈拉布"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('korean-celadon-bottle','高丽青瓷镶嵌长颈瓶','作品','art-asia','13世纪','东亚','陶瓷','核心',
  '高丽青瓷镶嵌铜红长颈瓶，维多利亚与艾伯特博物馆藏（O16589）。','1200—1250年',
  '球腹长颈、一侧小环耳；釉下黑白镶嵌：四圆开光内菊/牡丹，间以柳树；肩足莲瓣、颈叶纹、口沿方回纹；局部铜红。','korean-celadon-bowl-lotus,yuan-blue-white-jar','vam-O16589'),
 ('korean-celadon-bowl-lotus','高丽青瓷莲童纹碗','作品','art-asia','13世纪','东亚','陶瓷','核心',
  '高丽青瓷模印镶嵌碗，维多利亚与艾伯特博物馆藏（O22279）。','1200—1250年',
  '外壁素净，内壁模印莲瓣、三童戏莲，近口沿镶嵌缠枝；玉青色釉；圈足留三支烧痕。','korean-celadon-bottle,korean-white-flask-longevity','vam-O22279'),
 ('korean-white-flask-longevity','朝鲜白瓷寿纹扁壶','作品','art-asia','18世纪','东亚','陶瓷','重要',
  '朝鲜白瓷堆白蝙蝠与「寿」字扁壶，维多利亚与艾伯特博物馆藏（O22419）。','1750—1800年',
  '堆白蝙蝠环「壽」字成竖框；施透明釉；圈足刻谚文款；白瓷由高岭土与碎岩高温烧成，高丽朝已始。','korean-celadon-bowl-lotus,yuan-blue-white-jar','vam-O22419'),
 ('kashan-salting-mihrab','卡尚「萨尔廷」米哈拉布釉砖','作品','art-islamic','14世纪','西亚·中亚','陶瓷','核心',
  '卡尚熔块胎釉上彩单块米哈拉布，维多利亚与艾伯特博物馆藏（O67415）。','约1300年',
  '釉上光泽彩与钴蓝；边框环铭文，龛内悬灯；拱形为清真寺米哈拉布（朝向麦加之龛）的缩微，用作墓葬标志。','islamic-art,korean-celadon-bottle','vam-O67415'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")