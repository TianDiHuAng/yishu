# -*- coding: utf-8 -*-
"""Cycle91：日本佛教雕塑 4 条。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1950-86","Cleveland Museum of Art — Miroku Bosatsu (Buddha of the Future), Asuka, late 600s, acc. 1950.86",
  "https://openaccess-api.clevelandart.org/api/artworks/1950.86","2026-11-23 API HTTP 200；铸青铜存鎏金 45.8cm；说明含6世纪佛教传入日本"),
 ("cma-1961-48","Cleveland Museum of Art — Nikkō Bosatsu (Sun Bodhisattva), Heian, c. 800, acc. 1961.48",
  "https://openaccess-api.clevelandart.org/api/artworks/1961.48","2026-11-23 API HTTP 200；日本粗榧木存彩与金 46.7cm；说明含与月菩萨成对"),
 ("cma-1973-85","Cleveland Museum of Art — Seated Buddha, Heian, 1100s, acc. 1973.85",
  "https://openaccess-api.clevelandart.org/api/artworks/1973.85","2026-11-23 API HTTP 200；木胎漆金 145.4cm；说明含兴福寺周围小寺与左手缺失"),
 ("cma-1960-197","Cleveland Museum of Art — Amida Nyorai, Kamakura, 1269, acc. 1960.197",
  "https://openaccess-api.clevelandart.org/api/artworks/1960.197","2026-11-23 API HTTP 200；桧木漆彩金嵌水晶眼 94.6cm；说明含像内文献与四天王寺33日成造"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('miroku-asuka','飞鸟期弥勒菩萨像','作品','art-asia','7世纪','日本','雕塑','核心',
  '日本飞鸟期铸青铜弥勒菩萨像，克利夫兰艺术博物馆藏（1950.86）。','7世纪末',
  '佛教6世纪传入日本；对末世出现的未来佛的信仰，为贵族提供永恒救赎许诺。','buddhist-art-india,japanese-art','cma-1950-86'),
 ('nikko-bodhisattva','日光菩萨木像','作品','art-asia','9世纪','日本','雕塑','重要',
  '平安期日本粗榧木彩绘金饰菩萨像，克利夫兰艺术博物馆藏（1961.48）。','约公元800年',
  '流畅衣纹与曲姿取自中国佛教雕塑；单块黄檗木纹与细腻雕刻的结合为日本创新；原与月光菩萨成对。','buddhist-art-india,japanese-art','cma-1961-48'),
 ('kofukuji-seated-buddha','兴福寺周边坐佛像','作品','art-asia','12世纪','日本','雕塑','核心',
  '平安期木胎漆金坐佛，克利夫兰艺术博物馆藏（1973.85）。','12世纪',
  '由多块中空木件拼合、再覆漆与金箔；右手施无畏印；左手为后配，原手印不明。','buddhist-art-india,japanese-art','cma-1973-85'),
 ('amida-shitennoji','四天王寺阿弥陀佛像','作品','art-asia','13世纪','日本','雕塑','核心',
  '镰仓期桧木漆彩金、嵌水晶眼阿弥陀佛像，克利夫兰艺术博物馆藏（1960.197）。','1269年',
  '呈迎接姿态；像内文献含《阿弥陀经》、结缘名簿与33日造成记录。','buddhist-art-india,japanese-art','cma-1960-197'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")