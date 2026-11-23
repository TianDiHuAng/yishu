# -*- coding: utf-8 -*-
"""Cycle87：希腊罗马 4 条（库罗斯、赫拉克勒斯、运动员像、韦斯巴芗头像）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1953-125","Cleveland Museum of Art — Torso of a Kouros, c. 550 BCE, acc. 1953.125",
  "https://openaccess-api.clevelandart.org/api/artworks/1953.125","2026-11-23 API HTTP 200；大理石 62.5cm；说明含埃及影响与希腊化发展"),
 ("cma-2000-6","Cleveland Museum of Art — Statuette of Herakles, 510–500 BCE, acc. 2000.6",
  "https://openaccess-api.clevelandart.org/api/artworks/2000.6","2026-11-23 API HTTP 200；实心青铜 21.5cm；说明含从运动员到赫拉克勒斯的再认定"),
 ("cma-1924-1046","Cleveland Museum of Art — Statue of an Athlete, 1–100 CE, acc. 1924.1046",
  "https://openaccess-api.clevelandart.org/api/artworks/1924.1046","2026-11-23 API HTTP 200；大理石 173.9cm；说明含罗马摹希腊与支撑结构"),
 ("cma-1929-998","Cleveland Museum of Art — Portrait Head of Vespasian Recut from Nero, 64–79 CE, acc. 1929.998",
  "https://openaccess-api.clevelandart.org/api/artworks/1929.998","2026-11-23 API HTTP 200；大理石 40×21.6×24.9cm；说明含记忆抹除与1973年分离"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('kouros-torso','库罗斯青年像残躯','作品','art-ancient','公元前6世纪','希腊','雕塑','核心',
  '古希腊古风时期大理石库罗斯残躯，克利夫兰艺术博物馆藏（1953.125）。','约公元前550年',
  '裸体青年直立、双臂贴身、一足略前；类型可能受埃及影响，后按希腊路线发展。','greek-art,egyptian-art','cma-1953-125'),
 ('herakles-bronze','赫拉克勒斯青铜小像','作品','art-ancient','公元前6世纪','希腊','雕塑','核心',
  '希腊实心青铜小像，克利夫兰艺术博物馆藏（2000.6）。','公元前510—前500年',
  '曾被认为是运动员，今更可能表现赫拉克勒斯的击打姿态；强调年轻化和理想面容。','greek-art,roman-art','cma-2000-6'),
 ('roman-athlete-statue','罗马运动员像','作品','art-ancient','公元1世纪','意大利','雕塑','重要',
  '罗马大理石运动员像，克利夫兰艺术博物馆藏（1924.1046）。','公元1—100年',
  '追溯公元前5世纪希腊原型，罗马工匠改用大理石并加支撑（树干与撑杆）以求稳固。','roman-art,greek-art','cma-1924-1046'),
 ('vespasian-recut-head','韦斯巴芗头像（由尼禄像改刻）','作品','art-ancient','公元1世纪','意大利','雕塑','核心',
  '罗马大理石头像，克利夫兰艺术博物馆藏（1929.998）。','公元64—79年',
  '古代由尼禄像改刻为韦斯巴芗；后脑发际线缩短，下唇后削等尼禄特征仍存。','roman-art,greek-art','cma-1929-998'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")