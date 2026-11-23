# -*- coding: utf-8 -*-
"""Cycle53：新增 5 条（纳斯卡人首纹碗、朝鲜朝蜀葵杯、朝鲜朝婚礼袍、占婆行星神、占婆飞天托架）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-2009-435","Cleveland Museum of Art — Bowl with Trophy Heads, Nasca, c. 100–650 CE, acc. 2009.435",
  "https://openaccess-api.clevelandart.org/api/artworks/2009.435","2026-11-23 API HTTP 200；陶器施化妆土 10.2×10.2cm；说明含薄壁与较高烧成温度"),
 ("cma-1969-85","Cleveland Museum of Art — Hollyhock-shaped Cup, Joseon, 1400s, acc. 1969.85",
  "https://openaccess-api.clevelandart.org/api/artworks/1969.85","2026-11-23 API HTTP 200；瓷器 高3.6cm；说明含官窑限量生产与宫廷宴仪"),
 ("cma-1918-552","Cleveland Museum of Art — Bridal Robe (Hwarot), Joseon, late 1800s, acc. 1918.552",
  "https://openaccess-api.clevelandart.org/api/artworks/1918.552","2026-11-23 API HTTP 200；丝缎地平绣 114.3×174cm；说明含修补与纸质衬边"),
 ("cma-1935-147","Cleveland Museum of Art — Enthroned planetary deity, Champa, 850–75, acc. 1935.147",
  "https://openaccess-api.clevelandart.org/api/artworks/1935.147","2026-11-23 API HTTP 200；砂岩 86.5×37.5cm；说明含九曜护法与开光星象"),
 ("cma-1990-34","Cleveland Museum of Art — Apsara Bracket, Champa, 900s, acc. 1990.34",
  "https://openaccess-api.clevelandart.org/api/artworks/1990.34","2026-11-23 API HTTP 200；砂岩 55.9×53.3cm；说明含建筑构件功能")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('nazca-trophy-head-bowl','纳斯卡人首纹碗','作品','art-americas','2—7世纪','美洲','综合','重要',
    '秘鲁南岸纳斯卡文化的陶碗，克利夫兰艺术博物馆藏（2009.435）；外壁重复人首（trophy head）母题。','约100—650年',
    '器壁薄、烧成温度高于更早时期；暖色化妆土多样；人首母题同时指向战争与丰产。','paracas-mantle,americas-art','cma-2009-435'),
   ('joseon-hollyhock-cup','朝鲜朝蜀葵形杯','作品','art-asia','15世纪','东亚','综合','重要',
    '朝鲜王朝官窑所制蜀葵形瓷杯，克利夫兰艺术博物馆藏（1969.85）。','1400年代',
    '口沿作蜀葵花瓣形；蜀葵向阳，寓忠君；据王室档案用于国王赐酒的国宴与接待明使的茶礼。','joseon-hwarot-robe,goryeo-celadon-cup','cma-1969-85'),
   ('joseon-hwarot-robe','朝鲜朝婚礼袍（hwarot）','作品','art-asia','19世纪','东亚','综合','重要',
    '朝鲜王朝新娘礼服，克利夫兰艺术博物馆藏（1918.552）；丝缎地彩绣吉祥纹。','1800年代末',
    '蝶寓婚姻幸福、凤寓多子、莲与白鹤寓长寿；大量修补与拼补反映新儒学崇尚俭约，并显示其为可共享传承的公共资源。','joseon-hollyhock-cup','cma-1918-552'),
   ('champa-planetary-deity','占婆行星神坐像','作品','art-asia','9世纪','东南亚','雕塑','重要',
    '越南中部占婆东阳寺的砂岩行星神像，克利夫兰艺术博物馆藏（1935.147）。','850—875年',
    '为护持佛寺的九曜之一；左手短剑、髭须与蹙眉示其忿怒护法身份；坐姿为「王者安逸」。','champa-apsara-bracket','cma-1935-147'),
   ('champa-apsara-bracket','占婆飞天托架','作品','art-asia','10世纪','东南亚','雕塑','重要',
    '越南占婆的砂岩飞天构件，克利夫兰艺术博物馆藏（1990.34）。','900年代',
    '天人盛装、层叠冠与重耳饰，捧莲蕾献供；原为栏楯端头或天花托架的建筑装饰。','champa-planetary-deity','cma-1990-34')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 5")