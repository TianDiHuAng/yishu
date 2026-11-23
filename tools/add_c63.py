# -*- coding: utf-8 -*-
"""Cycle63：新增 4 条北美原住民条目（纳瓦霍 2、霍皮 2）。北美由零覆盖起步。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1917-62","Cleveland Museum of Art — Hubbell Revival-Style Rug with Moki Stripes, Navajo, c. 1890–1910, acc. 1917.62",
  "https://openaccess-api.clevelandart.org/api/artworks/1917.62","2026-11-23 API HTTP 200；羊毛挂毯 194.8×138.4cm；说明含 Moki 纹来源不明与市场转向"),
 ("cma-1928-312","Cleveland Museum of Art — Hopi Kachina Dolls (watercolor by Fred Kabotie), c. 1920s, acc. 1928.312",
  "https://openaccess-api.clevelandart.org/api/artworks/1928.312","2026-11-23 API HTTP 200；纸本水彩 47.6×31.1cm；说明含 katsina 教喻与画家 Naqavoy’ma"),
 ("cma-1937-903","Cleveland Museum of Art — Fourth-Phase Chief Blanket Style Rug, Navajo, c. 1900, acc. 1937.903",
  "https://openaccess-api.clevelandart.org/api/artworks/1937.903","2026-11-23 API HTTP 200；羊毛挂毯 178.4×151.1cm；说明含「chief’s blanket」为误称与 Bosque Redondo"),
 ("cma-1937-708","Cleveland Museum of Art — Canteen with a Katsina-like Face, Hopi, 1890, acc. 1937.708",
  "https://openaccess-api.clevelandart.org/api/artworks/1937.708","2026-11-23 API HTTP 200；陶器施化妆土 21.5×24.5cm；说明含西班牙原型与游客市场")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('navajo-hubbell-rug','纳瓦霍 Hubbell 复兴风格地毯（Moki 条纹）','作品','art-americas','19—20世纪','北美洲','综合','重要',
    '纳瓦霍（Diné）女艺人所作羊毛挂毯，克利夫兰艺术博物馆藏（1917.62）。','约1890—1910年',
    '并置两种旧纹样：阶梯状菱形与 Moki 条纹；Moki 来源不明，或来自普韦布洛，或来自1540年入西南的西班牙人。','navajo-chief-blanket-rug,americas-art','cma-1917-62'),
   ('hopi-kachina-painting','霍皮 Katsina 偶人图（Fred Kabotie 绘）','作品','art-americas','20世纪','北美洲','绘画','重要',
    '霍皮画家 Fred Kabotie（Naqavoy’ma）纸本水彩，克利夫兰艺术博物馆藏（1928.312）。','约1920年代',
    '画中为象征 katsina 的偶人雕刻；此类雕刻赠予霍皮女孩，用以教其认识世界与自身位置。','hopi-canteen-katsina,americas-art','cma-1928-312'),
   ('navajo-chief-blanket-rug','纳瓦霍「酋长毯」样式地毯（第四期）','作品','art-americas','19—20世纪','北美洲','综合','重要',
    '仿 Diné 披肩毯样式的羊毛挂毯，克利夫兰艺术博物馆藏（1937.903）。','约1900年',
    '所谓 chief’s blanket 实为**误称**——Diné 并无酋长；1860年代 Bosque Redondo 囚禁后土著贸易网络崩解，织者转向外来收藏市场。','navajo-hubbell-rug,americas-art','cma-1937-903'),
   ('hopi-canteen-katsina','霍皮带 Katsina 面容水壶','作品','art-americas','19世纪','北美洲','综合','重要',
    '霍皮陶制大水壶，克利夫兰艺术博物馆藏（1937.708）。','1890年',
    '自1500年代起霍皮女性依西班牙原型制大肚水壶；晚期为迎合欧美游客而加饰，此面容为**想象性描绘**而非真实 Katsina。','hopi-kachina-painting,americas-art','cma-1937-708')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")