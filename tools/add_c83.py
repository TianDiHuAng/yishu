# -*- coding: utf-8 -*-
"""Cycle83：中国书法 4 条（越山道宗、宋理宗/马麟、兰亭漆板、陈继儒）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-2003-353","Cleveland Museum of Art — Yueshan Daozong, Calligraphy in Semi-Cursive Style, c. 1660–1709, acc. 2003.353",
  "https://openaccess-api.clevelandart.org/api/artworks/2003.353","2026-11-23 API HTTP 200；纸本水墨 28.6×64.1cm；说明含黄檗宗与万福寺第七代住持"),
 ("cma-1961-421-2","Cleveland Museum of Art — Emperor Lizong, Poem by Wang Wei in Cursive Script, 1256, acc. 1961.421.2",
  "https://openaccess-api.clevelandart.org/api/artworks/1961.421.2","2026-11-23 API HTTP 200；绢本册页 25.1×25.3cm；说明含帝书与马麟画合装一扇"),
 ("cma-1974-72","Cleveland Museum of Art — Gathering at Lanting (Orchid Pavilion), lacquer panel, 1400s–1500s, acc. 1974.72",
  "https://openaccess-api.clevelandart.org/api/artworks/1974.72","2026-11-23 API HTTP 200；朱漆雕板 48.5×21cm；说明含曲水流觞与王羲之观鹅"),
 ("cma-2004-65","Cleveland Museum of Art — Chen Jiru, Four Poems in Running Script, 1500s–1600s, acc. 2004.65",
  "https://openaccess-api.clevelandart.org/api/artworks/2004.65","2026-11-23 API HTTP 200；金笺手卷 27×195cm；说明含与董其昌风格相近及焚儒服拒征"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('yueshan-daizong-calligraphy','越山道宗行草书轴','作品','art-china-calligraphy','17世纪','东亚','书法','重要',
  '中国福建僧越山道宗行草书轴，克利夫兰艺术博物馆藏（2003.353）。','约1660—1709年',
  '笔致圆转并连笔连字；越山赴日后任黄檗宗万福寺僧职，后为该寺第七代住持。','zen-painting,japanese-art,china-calligraphy-history','cma-2003-353'),
 ('lizong-wangwei-album','宋理宗书王维诗册页','作品','art-china-calligraphy','13世纪','中国','书法','核心',
  '南宋理宗书、马麟画合装一扇之册页，克利夫兰艺术博物馆藏（1961.421.2）。','1256年',
  '帝书引王维诗句，马麟以淡墨与渲染回应；与杭州宫廷、文官和寺院间的禅美学互动有关。','song-painting,china-painting-history','cma-1961-421-2'),
 ('lanting-lacquer-panel','兰亭雅集朱漆雕板','作品','art-china-calligraphy','15—16世纪','中国','书法','重要',
  '明式朱漆雕板，克利夫兰艺术博物馆藏（1974.72）。','1400—1500年代',
  '刻353年兰亭修禊、曲水流觞；主纹「王羲之观鹅」上移至画面上段。','china-calligraphy-history,running-script','cma-1974-72'),
 ('chen-jiru-four-poems','陈继儒行书四诗卷','作品','art-china-calligraphy','16—17世纪','中国','书法','核心',
  '陈继儒金笺行书手卷，克利夫兰艺术博物馆藏（2004.65）。','1500—1600年代',
  '四诗写心绪；字用浓墨厚重处示节奏，可见停笔再蘸墨的瞬间；书风近董其昌。','dong-qichang-qingbian,china-calligraphy-history','cma-2004-65'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")