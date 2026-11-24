# -*- coding: utf-8 -*-
"""Cycle130：罗马雕塑 4 条（奥克塔维娅像、俄瑞斯忒斯石棺、安东尼朝像、西勒诺斯床榻像）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1925-943","Cleveland Museum of Art — Portrait bust of Claudia Octavia, Roman, 50–70 CE, acc. 1925.943",
  "https://openaccess-api.clevelandart.org/api/artworks/1925.943","2026-11-24 API HTTP 200；大理石 38.2cm；说明含stola与塔西佗评语"),
 ("cma-1928-856","Cleveland Museum of Art — Roman sarcophagus with Orestes, c. 100–125 CE, acc. 1928.856",
  "https://openaccess-api.clevelandart.org/api/artworks/1928.856","2026-11-24 API HTTP 200；希腊大理石 210cm；说明含三联俄瑞斯忒斯与四季"),
 ("cma-1952-260","Cleveland Museum of Art — Portrait head of a noble/official, Antonine, 175–200 CE, acc. 1952.260",
  "https://openaccess-api.clevelandart.org/api/artworks/1952.260","2026-11-24 API HTTP 200；大理石 38.2cm；说明含钻孔瞳仁始于哈德良朝"),
 ("cma-1974-88","Cleveland Museum of Art — Silenus bust for a couch, Roman, 1–125 CE, acc. 1974.88",
  "https://openaccess-api.clevelandart.org/api/artworks/1974.88","2026-11-24 API HTTP 200；青铜 11cm；说明含fulcrum与鹿皮醉态"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('claudia-octavia-bust','克劳狄娅·屋大维娅胸像','作品','art-ancient','公元1世纪','意大利','雕塑','核心',
  '罗马大理石后妃像，克利夫兰艺术博物馆藏（1925.943）。','公元50—70年',
  '理想化面容与繁复发型或指尼禄元配皇后奥克塔维娅（54—62在位）；外袍stola示已婚上层女性；塔西佗称其「贵族气而有德」，终被休弃放逐赐死。','roman-athlete-statue,vespasian-recut-head','cma-1925-943'),
 ('roman-sarcophagus','俄瑞斯忒斯石棺','作品','art-ancient','公元2世纪','意大利','雕塑','核心',
  '罗马希腊大理石石棺，克利夫兰艺术博物馆藏（1928.856）。','约100—125年',
  '正面俄瑞斯忒斯三现、皆持短剑：弑母克吕泰涅斯特拉与奸夫埃癸斯托斯以报父仇；左三复仇女神栖阿伽门农墓；右在德尔斐阿波罗庙赎罪（三足鼎与岩）；盖四卧女象四季（冬春夏秋，依衣饰与篮中之物）。','vespasian-recut-head,roman-athlete-statue','cma-1928-856'),
 ('antonine-portrait-head','安东尼朝官员肖像','作品','art-ancient','公元2世纪','意大利','雕塑','核心',
  '罗马大理石卷发蓄须男子像，克利夫兰艺术博物馆藏（1952.260）。','175—200年',
  '或为贵族/官员；钻孔瞳仁与虹膜通常不早于哈德良朝（117—38，崇希腊文化）；深雕须发至安东尼朝（138—92）仍盛。','claudia-octavia-bust,roman-athlete-statue','cma-1952-260'),
 ('silenus-couch-bust','西勒诺斯床榻像','作品','art-ancient','公元1—2世纪','意大利','雕塑','重要',
  '罗马青铜西勒诺斯像（床榻扶手件），克利夫兰艺术博物馆藏（1974.88）。','公元1—125年',
  '为古罗马卧榻fulcrum（扶手）之一部；西勒诺斯为巴克斯之师；长卷须、浓眉、常春藤果冠；鹿皮袍以蹄系、滑落肩上示醉态；罗马卧榻制多承希腊。','roman-sarcophagus,claudia-octavia-bust','cma-1974-88'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")