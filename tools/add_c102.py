# -*- coding: utf-8 -*-
"""Cycle102：当代艺术 4 条（波洛克、罗斯科、沃霍尔、凯利）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1980-180","Cleveland Museum of Art — Jackson Pollock, Number 5, 1950, acc. 1980.180",
  "https://openaccess-api.clevelandart.org/api/artworks/1980.180","2026-11-23 API HTTP 200；布面油画 136.5×99.1cm；说明含滴洒法与满幅构图"),
 ("cma-1962-239","Cleveland Museum of Art — Mark Rothko, No. 2 (Red Maroons), 1962, acc. 1962.239",
  "https://openaccess-api.clevelandart.org/api/artworks/1962.239","2026-11-23 API HTTP 200；布面油画 200.7×205.7cm；说明含漂浮色域与基本情感"),
 ("cma-1997-246","Cleveland Museum of Art — Andy Warhol, Marilyn x 100, 1962, acc. 1997.246",
  "https://openaccess-api.clevelandart.org/api/artworks/1997.246","2026-11-23 API HTTP 200；丝网印与合成聚合物 205.7×567.7cm；说明含《尼亚加拉》剧照与批量复制"),
 ("cma-1964-142","Cleveland Museum of Art — Ellsworth Kelly, Red Blue, 1962, acc. 1964.142",
  "https://openaccess-api.clevelandart.org/api/artworks/1964.142","2026-11-23 API HTTP 200；布面油画 228.6×176.4cm；说明含两色两形关系与无笔触"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('pollock-number5','波洛克《第5号，1950》','作品','art-contemporary','20世纪','美国','绘画','核心',
  '波洛克布面油画，克利夫兰艺术博物馆藏（1980.180）。','1950年',
  '滴洒法：画布平铺，颜料自罐中甩出；线条网状覆盖全幅、无中心无方向，是艺术家动作与手势的直接记录。','modern-art,rothko-no2-red-maroons','cma-1980-180'),
 ('rothko-no2-red-maroons','罗斯科《第2号（红褐）》','作品','art-contemporary','20世纪','美国','绘画','核心',
  '罗斯科布面油画，克利夫兰艺术博物馆藏（1962.239）。','1962年',
  '成熟期漂浮色域；多层稀释颜料、有时以布擦湿面以求空灵；自称只表达基本情感（悲剧/狂喜/宿命）。','pollock-number5,warhol-marilyn-100','cma-1962-239'),
 ('warhol-marilyn-100','沃霍尔《玛丽莲×100》','作品','art-contemporary','20世纪','美国','绘画','核心',
  '沃霍尔丝网印布面，克利夫兰艺术博物馆藏（1997.246）。','1962年',
  '取材1953年《尼亚加拉》剧照；丝网印令艺术家之手缺席，叠于独特底画；探大众传媒/技术/波普/纯艺术之张力。','rothko-no2-red-maroons,kelly-red-blue','cma-1997-246'),
 ('kelly-red-blue','凯利《红蓝》','作品','art-contemporary','20世纪','美国','绘画','核心',
  '凯利布面油画，克利夫兰艺术博物馆藏（1964.142）。','1962年',
  '两色两形：蓝矩形边缘由画布决定（可测），红形则如呼吸浮动；无笔触却指向自然形态与感知方式。','warhol-marilyn-100,pollock-number5','cma-1964-142'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")