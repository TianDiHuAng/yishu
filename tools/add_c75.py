# -*- coding: utf-8 -*-
"""Cycle75：中国陶瓷再补 4 条（磁州窑玩具俑、过渡期方瓶、康熙瓣瓶、北宋磁州瓶）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1957-56","Cleveland Museum of Art — Lady Holding a Vase, Cizhou ware, 1100s–1200s, acc. 1957.56",
  "https://openaccess-api.clevelandart.org/api/artworks/1957.56","2026-11-23 API HTTP 200；石陶化妆土 19.7×9.5cm；说明含玩具用途与釉上彩先行"),
 ("cma-2018-293","Cleveland Museum of Art — Transitional Blue-and-White Square Bottle, 1628–1722, acc. 2018.293",
  "https://openaccess-api.clevelandart.org/api/artworks/2018.293","2026-11-23 API HTTP 200；釉下青花瓷 高31.1cm；说明含欧洲杜松子酒瓶形与失去宫廷订单"),
 ("cma-2020-174","Cleveland Museum of Art — Lobed vase, underglaze cobalt blue, Kangxi, 1661–1722, acc. 2020.174",
  "https://openaccess-api.clevelandart.org/api/artworks/2020.174","2026-11-23 API HTTP 200；釉下青花瓷 20.4×12.2cm；说明含与博纳尔画作的关联"),
 ("cma-1948-226","Cleveland Museum of Art — Vase with Floral Scrolls, Cizhou, 900s–1000s, acc. 1948.226",
  "https://openaccess-api.clevelandart.org/api/artworks/1948.226","2026-11-23 API HTTP 200；釉石陶刻花嵌白 高41.3cm；说明含化妆土与胎色对比")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('cizhou-toy-figurine','磁州窑持瓶女俑（玩具）','作品','art-ceramics','12—13世纪','中国','雕塑','重要',
    '磁州窑模制彩绘女俑，克利夫兰艺术博物馆藏（1957.56）。','1100—1200年代',
    '持长颈花瓶（浇花用）；磁州窑不供御用，只做日用器与陶俑，后者被认为作**玩具**。','cizhou-floral-vase,ding-duck-bowl','cma-1957-56'),
   ('transitional-square-bottle','过渡期青花方瓶','作品','art-ceramics','17世纪','中国','综合','重要',
    '景德镇釉下青花方瓶，克利夫兰艺术博物馆藏（2018.293）。','1628—1722年',
    '器形源自**欧洲杜松子酒瓶**；纹样为豹、麒麟、马等异兽；属明末清初「过渡期」，窑场失去宫廷订单后转向新客源。','kangxi-lobed-vase,yuan-blue-white-jar','cma-2018-293'),
   ('kangxi-lobed-vase','康熙青花瓣瓶','作品','art-ceramics','17—18世纪','中国','综合','核心',
    '康熙朝景德镇釉下青花瓣瓶，克利夫兰艺术博物馆藏（2020.174）。','1661—1722年',
    '青花绘画性在康熙朝达最高；画工技艺可比专业画家；蓝彩迎合士人、宫廷与海外市场。','transitional-square-bottle,chenghua-doucai-cup','cma-2020-174'),
   ('cizhou-floral-vase','北宋磁州窑花卉纹瓶','作品','art-ceramics','10—11世纪','中国','综合','重要',
    '北宋磁州窑刻花嵌白瓶，克利夫兰艺术博物馆藏（1948.226）。','900—1000年代',
    '磁州窑以化妆土、粗放纹样与色差见长；此瓶以刻划与嵌白取得韵律感；烧成后化妆土呈象牙色、露胎呈肉桂褐。','cizhou-toy-figurine,jun-numbered-bulb-bowl','cma-1948-226')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")