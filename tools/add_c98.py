# -*- coding: utf-8 -*-
"""Cycle98：中国玉器 4 条（良渚璧、商琮、商玉戈、齐家三孔刀）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1917-974","Cleveland Museum of Art — Ceremonial Disc (Bi), Liangzhu, 3300–2200 BCE, acc. 1917.974",
  "https://openaccess-api.clevelandart.org/api/artworks/1917.974","2026-11-23 API HTTP 200；软玉 直径32cm；说明含璧琮配对与高等级葬仪"),
 ("cma-1915-630","Cleveland Museum of Art — Ceremonial Tube (Cong), Shang, c. 1600–1056 BCE, acc. 1915.630",
  "https://openaccess-api.clevelandart.org/api/artworks/1915.630","2026-11-23 API HTTP 200；软玉 20.6cm；说明含《周礼》祭地与史前功能未明"),
 ("cma-1983-2","Cleveland Museum of Art — Ceremonial Dagger-Axe (Ge) with Animal Masks, Shang, acc. 1983.2",
  "https://openaccess-api.clevelandart.org/api/artworks/1983.2","2026-11-23 API HTTP 200；软玉 4.4cm；说明含石英砂研磨与饕餮纹"),
 ("cma-2009-83","Cleveland Museum of Art — Ceremonial Blade (Dao) with Three Perforations, Qijia, acc. 2009.83",
  "https://openaccess-api.clevelandart.org/api/artworks/2009.83","2026-11-23 API HTTP 200；软玉 35.2cm；说明含2毫米薄度与齐家祭祀坑立置"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('liangzhu-bi-disc','良渚玉璧','作品','art-ancient','新石器时代','中国','雕塑','核心',
  '良渚文化软玉璧，克利夫兰艺术博物馆藏（1917.974）。','约公元前3300—2200年',
  '良渚以治玉著称；此大璧罕见，常置于墓主胸前；璧与琮为高等级墓葬必备的礼器配对。','shang-cong-tube,qijia-jade-dao','cma-1917-974'),
 ('shang-cong-tube','商代玉琮','作品','art-ancient','商代','中国','雕塑','核心',
  '商代软玉琮，克利夫兰艺术博物馆藏（1915.630）。','约公元前1600—1056年',
  '圆筒外套方体，为古代礼仪中最显赫的玉器之一；《周礼》记以苍璧礼天、黄琮礼地。','liangzhu-bi-disc,shang-jade-ge','cma-1915-630'),
 ('shang-jade-ge','商代玉戈（饕餮纹）','作品','art-ancient','商代','中国','雕塑','重要',
  '商代软玉戈，克利夫兰艺术博物馆藏（1983.2）。','约公元前1600—1050年',
  '玉极硬，以石英砂等细磨料附着工具研磨；戈形可能源自青铜兵器；刃自饕餮口部生出。','shang-zhou-bronzes,shang-cong-tube','cma-1983-2'),
 ('qijia-jade-dao','齐家文化三孔玉刀','作品','art-ancient','新石器—青铜时代','中国','雕塑','核心',
  '齐家文化软玉三孔刀，克利夫兰艺术博物馆藏（2009.83）。','约公元前2000—1700年',
  '抛光细腻、丝般光泽、仅厚2毫米；齐家祭祀坑出土同类刀原以刃立、平行排列。','liangzhu-bi-disc,shang-jade-ge','cma-2009-83'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")