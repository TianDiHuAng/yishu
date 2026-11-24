# -*- coding: utf-8 -*-
"""Cycle143：伊斯兰釉砖 4 条（高尔砖板、伊朗米哈拉布、伊兹尼克立碑砖、伊斯法罕马赛克砖）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o82264","Victoria and Albert Museum — Tile panel from Gaur, 1450–1550, O82264",
  "https://api.vam.ac.uk/v2/object/O82264","2026-11-24 API HTTP 200；釉陶砖 82.5×45.5cm；说明含高尔废墟取出后任意拼合（记录无 summary）"),
 ("vam-o86037","Victoria and Albert Museum — Section of a mihrab, Iran, 1307, O86037",
  "https://api.vam.ac.uk/v2/object/O86037","2026-11-24 API HTTP 200；熔块胎钴蓝釉上彩描金 宽92cm；说明含浮雕阿拉伯铭（记录无 summary）"),
 ("vam-o85357","Victoria and Albert Museum — Iznik free-standing stele tile, 1560–1600, O85357",
  "https://api.vam.ac.uk/v2/object/O85357","2026-11-24 API HTTP 200；熔块胎釉下彩 42.2×29cm；说明含双面花与1550s配色"),
 ("vam-o1511742","Victoria and Albert Museum — Isfahan tile mosaic, ca. 1450–1500, O1511742",
  "https://api.vam.ac.uk/v2/object/O1511742","2026-11-24 API HTTP 200；裁形釉砖嵌灰泥 34.5×44.3cm；说明含莲纹蒙古传入与六色马赛克"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('gaur-tile-panel','高尔釉砖板（孟加拉）','作品','art-islamic','15—16世纪','南亚','陶瓷','核心',
  '孟加拉高尔废墟釉陶砖板，维多利亚与艾伯特博物馆藏（O82264）。','1450—1550年',
  '多色釉砖自高尔废墟取出后任意拼合，约拟屋宇正面；平砖与高浮雕砖相杂；陶地满施珐琅彩，主为蓝黄绿白。（该记录无 summary）','kutahya-tile-panel,iznik-stele-1560','vam-o82264'),
 ('iran-mihrab-1307','伊朗米哈拉布残段','作品','art-islamic','14世纪','西亚·中亚','陶瓷','核心',
  '伊朗熔块胎米哈拉布（祈祷龛）残段，维多利亚与艾伯特博物馆藏（O86037）。','1307年',
  '由二拱形砖与二三角砖组成；花卉纹与浮雕阿拉伯铭文，施蓝；同类平饰以褐色绘；通体描金与珐琅彩；据说取自某建筑（记录截断）。（该记录无 summary）','kashan-salting-mihrab,isfahan-tile-1450','vam-o86037'),
 ('iznik-stele-1560','伊兹尼克立碑砖','作品','art-islamic','16世纪','西亚·中亚','陶瓷','核心',
  '伊兹尼克熔块胎釉下彩立碑砖，维多利亚与艾伯特博物馆藏（O85357）。','1560—1600年',
  '罕见独立直立、双面饰的熔块胎板；白地施蓝绿红——1550—60年代伊兹尼克确立之配色；每面花卉合玫瑰/郁金香/梅或风信子，环中央……（记录截断）。','iznik-tile-panel-edirne,kutahya-tile-panel','vam-o85357'),
 ('isfahan-tile-1450','伊斯法罕马赛克砖（残）','作品','art-islamic','15世纪','西亚·中亚','陶瓷','核心',
  '伊斯法罕马赛克釉砖残段，维多利亚与艾伯特博物馆藏（O1511742）。','约1450—1500年',
  '以裁形釉砖嵌灰泥拼成图案；钴蓝地繁花；局部存浅蓝边；数块砖已脱落；纹含程式化莲——中国母题于1256—8年蒙古征服伊朗后在中东流行；每砖施六色之一。','kashan-salting-mihrab,iznik-stele-1560','vam-o1511742'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")