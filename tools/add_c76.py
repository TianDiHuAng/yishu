# -*- coding: utf-8 -*-
"""Cycle76：日本陶瓷 4 条（伊万里酒瓶、伊万里大罐、志野水指、柿右卫门美人像）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1992-117","Cleveland Museum of Art — Sake Bottle, Arita/Imari style, mid–late 1600s, acc. 1992.117",
  "https://openaccess-api.clevelandart.org/api/artworks/1992.117","2026-11-23 API HTTP 200；釉下青花瓷 20cm 径10.2cm；说明含朝鲜陶工与高岭土发现"),
 ("cma-1964-266","Cleveland Museum of Art — Large Jar with Peonies, Orchids, Chrysanthemums, late 1600s, acc. 1964.266",
  "https://openaccess-api.clevelandart.org/api/artworks/1964.266","2026-11-23 API HTTP 200；伊万里釉下青花 高40.1cm 径30.5cm；说明含明亡与欧洲市场"),
 ("cma-1972.9","Cleveland Museum of Art — Water Container (Mizusashi) with Riverscape, Shino ware, acc. 1972.9",
  "https://openaccess-api.clevelandart.org/api/artworks/1972.9","2026-11-23 API HTTP 200；美浓志野石陶 径19.6cm 高18.4cm；说明含「绘志野」与茶人品味"),
 ("cma-1964-366","Cleveland Museum of Art — Standing Figure of a Beauty (Kakiemon), c. 1690, acc. 1964.366",
  "https://openaccess-api.clevelandart.org/api/artworks/1964.366","2026-11-23 API HTTP 200；釉上彩瓷 高38cm；说明含酒井田家族与柿右卫门之名")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('arita-sake-bottle','有田伊万里风格酒瓶','作品','art-asia','17世纪','日本','综合','重要',
    '有田（肥前）伊万里风格釉下青花酒瓶，克利夫兰艺术博物馆藏（1992.117）。','1600年代中—后期',
    '日本早期白瓷的出现与朝鲜陶工带来多室窑技术、并在日本发现高岭土直接相关。','imari-jar,kakiemon-beauty','cma-1992-117'),
   ('imari-jar','伊万里花木纹大罐','作品','art-asia','17世纪','日本','综合','重要',
    '伊万里釉下青花大罐，克利夫兰艺术博物馆藏（1964.266）。','1600年代末',
    '春牡丹、夏兰、秋菊同时开放于石间；纹样仿自输欧中国瓷器；明亡后中国外销中断，日本乘势供应欧洲市场。','arita-sake-bottle,shino-mizusashi','cma-1964-266'),
   ('shino-mizusashi','志野「绘」水指','作品','art-asia','16—17世纪','日本','综合','重要',
    '美浓志野石陶水指，克利夫兰艺术博物馆藏（1972.9），漆盖为近代配换。','1570年代末—1600年代初',
    '茶会备水之器；一面抽象纹样似芦苇小舟的水墨画，另一面为几何纹；形不规则、釉厚而莹。','imari-jar,kakiemon-beauty','cma-1972.9'),
   ('kakiemon-beauty','柿右卫门美人立像','作品','art-asia','17世纪','日本','综合','核心',
    '肥前柿右卫门釉上彩瓷美人像，克利夫兰艺术博物馆藏（1964.366）。','约1690年',
    '着层叠和服外罩「打挂」；原型或出自以游女为形的偶人；出酒井田家族，历代家长袭名柿右卫门。','arita-sake-bottle,imari-jar','cma-1964-366')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")