# -*- coding: utf-8 -*-
"""Cycle80：印度绘画 4 条（Ragamala 三例 + 黑天诞生）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1931-451","Cleveland Museum of Art — Shri Raga, from a Ragamala, Mewar, c. 1695, acc. 1931.451",
  "https://openaccess-api.clevelandart.org/api/artworks/1931.451","2026-11-23 API HTTP 200；胶彩与金 34.4×22.5cm；说明含阿马尔·辛格二世以自己的肖像替换通用王者"),
 ("cma-1984-65","Cleveland Museum of Art — The Birth of Krishna, from a Sursagar of Surdas, 1705–10, acc. 1984.65",
  "https://openaccess-api.clevelandart.org/api/artworks/1984.65","2026-11-23 API HTTP 200；胶彩、墨与金 33.6×22.2cm；说明含盲诗人苏尔达斯与第5诗节"),
 ("cma-1998-102","Cleveland Museum of Art — Maharana Jagat Singh II Hunting, 1747, acc. 1998.102",
  "https://openaccess-api.clevelandart.org/api/artworks/1998.102","2026-11-23 API HTTP 200；胶彩与金 42.5×47cm；说明含背面题记与驱兽方式"),
 ("cma-2001-111","Cleveland Museum of Art — Kausa Ragaputra of Malkos, from a Ragamala, Pahari, c. 1750, acc. 2001.111",
  "https://openaccess-api.clevelandart.org/api/artworks/2001.111","2026-11-23 API HTTP 200；胶彩、墨与金 18×14.8cm；说明含调式与「旋律花环」组画")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('shri-raga-mewar','《室利拉格》（Ragamala，梅瓦尔）','作品','art-asia','17世纪','南亚','绘画','核心',
    '梅瓦尔（拉贾斯坦）《旋律花环》组画之一，克利夫兰艺术博物馆藏（1931.451）。','约1695年',
    '绘王者夫妇听诵；赞助人阿马尔·辛格二世以自己的肖像替换通用的王者形象。','kausa-ragaputra,sursagar-krishna','cma-1931-451'),
   ('sursagar-krishna','《黑天诞生》（苏尔达斯《苏尔萨加尔》）','作品','art-asia','18世纪','南亚','绘画','核心',
    '梅瓦尔《苏尔萨加尔》写本插图，克利夫兰艺术博物馆藏（1984.65）。','1705—10年',
    '盲诗人苏尔达斯在右下小屋击铙诵诗；第5诗节题于页上；画面铺陈黑天降生的庆贺场面。','shri-raga-mewar,jagat-singh-hunting','cma-1984-65'),
   ('jagat-singh-hunting','《贾加特·辛格二世狩猎图》','作品','art-asia','18世纪','南亚','绘画','重要',
    '梅瓦尔乌代浦宫廷狩猎图，克利夫兰艺术博物馆藏（1998.102）。','1747年',
    '画面大于一般印度绘画；背面题记列王名与同行者；仆役放爆竹驱兽至中央射台。','sursagar-krishna,shri-raga-mewar','cma-1998.102'),
   ('kausa-ragaputra','《考萨拉格普特拉》（Ragamala，帕哈里）','作品','art-asia','18世纪','南亚','绘画','重要',
    '帕哈里《旋律花环》组画之一，克利夫兰艺术博物馆藏（2001.111）。','约1750年',
    '宫廷男女执驯鹰；帕哈里以猎鹰著称；此名亦为印度古典音乐的一种调式，画面对应该调式的听感。','shri-raga-mewar,musical-mode','cma-2001-111')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")