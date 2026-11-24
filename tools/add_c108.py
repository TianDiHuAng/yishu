# -*- coding: utf-8 -*-
"""Cycle108：V&A 4 条（广重《萨埵海》、北斋花鸟、马穆鲁克错金银铜盆、伊兹尼克釉砖板）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o78132","Victoria and Albert Museum — Utagawa Hiroshige, The Sea off Satta in Suruga Province, 1858, O78132",
  "https://api.vam.ac.uk/v2/object/O78132","2026-11-24 API HTTP 200；纸本锦绘 38×25.5cm；说明含大浪与富士"),
 ("vam-o71685","Victoria and Albert Museum — Katsushika Hokusai, Kingfisher, Irises and Wild Pinks, ca. 1834, O71685",
  "https://api.vam.ac.uk/v2/object/O71685","2026-11-24 API HTTP 200；彩印木版 22.9×16.5cm；说明含花鸟画与中判"),
 ("vam-o83883","Victoria and Albert Museum — Mamluk brass basin inlaid with gold and silver, Egypt, ca. 1250–1350, O83883",
  "https://api.vam.ac.uk/v2/object/O83883","2026-11-24 API HTTP 200；错金银铜盆 高18.5 径42.5cm；说明含苏卢斯体铭与月神圆章"),
 ("vam-o86971","Victoria and Albert Museum — Iznik tile panel, 1570–1574, O86971",
  "https://api.vam.ac.uk/v2/object/O86971","2026-11-24 API HTTP 200；釉下彩熔块胎 62×102cm；说明含埃迪尔内宫殿"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('hiroshige-satta-sea','广重《骏河萨埵海》','作品','art-asia','19世纪','东亚','版画','核心',
  '歌川广重木版锦绘，维多利亚与艾伯特博物馆藏（O78132）。','1858年',
  '竖大判锦绘；前景巨浪如冠，远景富士；由画师、雕版师、印工依出版商指令分工而成。','hiroshige-shono,hokusai-kingfisher-print','vam-o78132'),
 ('hokusai-kingfisher-print','北斋《翠鸟·鸢尾·石竹》','作品','art-asia','19世纪','东亚','版画','核心',
  '葛饰北斋彩印木版花鸟画，维多利亚与艾伯特博物馆藏（O71685）。','约1834年',
  '花鸟画（kacho-ga）；中判尺寸，静态花鸟配汉诗/和歌，可见中国影响；翠鸟似向花下河水俯冲。','hokusai-red-fuji,hiroshige-satta-sea','vam-o71685'),
 ('mamluk-inlaid-basin','马穆鲁克错金银铜盆','作品','art-islamic','13—14世纪','西亚·中亚','金属器','核心',
  '埃及错金银铜盆，维多利亚与艾伯特博物馆藏（O83883）。','约1250—1350年',
  '锤揲铜胎错金银；外壁苏卢斯体铭文衬缠枝；内壁圆章交替骑者与月神；底心交错纹与坐姿王者。','mamluk-mosque-lamp,islamic-art','vam-o83883'),
 ('iznik-tile-panel-edirne','伊兹尼克釉砖板（埃迪尔内）','作品','art-islamic','16世纪','西亚·中亚','陶瓷','核心',
  '奥斯曼六块釉砖板，维多利亚与艾伯特博物馆藏（O86971）。','1570—1574年',
  '釉下彩熔块胎；为一龛形板的顶部；或装饰伊斯坦布尔西北埃迪尔内皇宫，中央龛内白地缠枝花卉。','minai-bowl-kashan,islamic-art','vam-o86971'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")