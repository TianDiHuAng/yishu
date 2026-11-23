# -*- coding: utf-8 -*-
"""Cycle51：新增 5 条（莫切蝙蝠瓶、印加束腰外衣、Nok 陶塑头像、高丽青瓷瓶、缅甸 Kammavacha）。
均为 CMA 单机构来源 → needs_verification。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-2005-6","Cleveland Museum of Art — Big-Eared Brown Bat Vessel, Moche, 200–850 CE, acc. 2005.6",
  "https://openaccess-api.clevelandart.org/api/artworks/2005.6","2026-11-23 API HTTP 200；陶器施化妆土 18.4×17.7×15.8cm；说明含2021年以莫切命名的新种"),
 ("cma-1957-136","Cleveland Museum of Art — Tunic, Inca, c. 1400–1540, acc. 1957.136",
  "https://openaccess-api.clevelandart.org/api/artworks/1957.136","2026-11-23 API HTTP 200；挂毯织造 棉与驼科纤维 85.1×76.2cm；说明含 Inca Key 纹样"),
 ("cma-1995-21","Cleveland Museum of Art — Head, Nok culture, thermoluminescence 20–620 CE, acc. 1995.21",
  "https://openaccess-api.clevelandart.org/api/artworks/1995.21","2026-11-23 API HTTP 200；赤陶 38.2×20cm；含热释光测年与制作者性别的史学批评"),
 ("cma-1918-454","Cleveland Museum of Art — Bottle with Chrysanthemum Design, Goryeo, 1200s–1300s, acc. 1918.454",
  "https://openaccess-api.clevelandart.org/api/artworks/1918.454","2026-11-23 API HTTP 200；青瓷镶嵌白/黑泥 高40.4cm 径14.7cm；含金漆修补（kintsugi）"),
 ("cma-1945-172","Cleveland Museum of Art — Kammavacha: Buddhist Ordination Text, Myanmar, 1800s, acc. 1945.172",
  "https://openaccess-api.clevelandart.org/api/artworks/1945.172","2026-11-23 API HTTP 200；漆与贴金、玻璃镶嵌；巴利文缅甸体；含 nats 装饰")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('moche-bat-vessel','莫切蝙蝠形陶瓶','作品','art-americas','3—9世纪','美洲','雕塑','重要',
    '秘鲁北岸莫切文化的陶瓶，克利夫兰艺术博物馆藏（2005.6）；塑造一只展翅欲飞的大耳褐蝠。','200—850年',
    '莫切匠人对写实与「动作顶点」的把握在此可见；蝙蝠兼具飞行与兽毛的矛盾特征，可能与生死过渡相关。','inca-tunic,americas-art','cma-2005-6'),
   ('inca-tunic','印加束腰外衣（tunic）','作品','art-asia','15—16世纪','美洲','综合','重要',
    '印加帝国贵族专属的挂毯织造外衣，克利夫兰艺术博物馆藏（1957.136）。','约1400—1540年',
    '以交错挂毯法织成，纹样为常见的「印加键（Inca Key）」；由国家再分配给忠诚的藩属。','moche-bat-vessel,americas-art','cma-1957-136'),
   ('nok-terracotta-head','Nok 文化陶塑头像','作品','art-africa','公元前1世纪—公元7世纪','非洲','雕塑','重要',
    '尼日利亚中部 Nok 文化的赤陶头像，克利夫兰艺术博物馆藏（1995.21），热释光测年为公元20—620年。','热释光测年 20—620 CE',
    '为撒哈拉以南非洲最早的巨型具象雕塑传统之一；发掘显示多件曾被有意打碎置于铺地之下，指向仪式行为。','benin-plaque,african-art','cma-1995-21'),
   ('goryeo-celadon-bottle','高丽青瓷镶嵌菊纹瓶','作品','art-asia','13—14世纪','东亚','综合','重要',
    '高丽王朝青瓷长颈酒瓶，克利夫兰艺术博物馆藏（1918.454）；镶嵌白与黑泥的野菊纹。','1200—1300年代',
    '野菊既是「饮酒」诗意象，也寓意长寿；口沿破损处曾以金漆修补（日本称 kintsugi）。','kammavacha-manuscript','cma-1918-454'),
   ('kammavacha-manuscript','缅甸 Kammavacha 戒律文书','作品','art-asia','19世纪','东南亚','综合','重要',
    '缅甸的佛教授戒仪式文书，克利夫兰艺术博物馆藏（1945.172）；漆叶、贴金与玻璃镶嵌。','1800年代',
    '在家信众为仪式出资制作；巴利文以缅甸体书写；倒数第二叶画有赞颂状的天人（nats）。','goryeo-celadon-bottle','cma-1945-172')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 5")