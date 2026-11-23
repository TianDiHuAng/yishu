# -*- coding: utf-8 -*-
"""Cycle73：新增单元「陶瓷工艺」+ 4 条中国陶瓷（元青花、龙泉、定窑、钧窑）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1962-154","Cleveland Museum of Art — Jar with Lion-Head Handles, Jingdezhen (Yuan), 1300s, acc. 1962.154",
  "https://openaccess-api.clevelandart.org/api/artworks/1962.154","2026-11-23 API HTTP 200；釉下青花瓷 39.4×37.5cm；说明含伊朗钴料与伊儿汗母题"),
 ("cma-2020-188","Cleveland Museum of Art — Large Bowl with Molded Decoration, Longquan, 1300s–1400s, acc. 2020.188",
  "https://openaccess-api.clevelandart.org/api/artworks/2020.188","2026-11-23 API HTTP 200；瓷质石陶 15.1×42cm；说明含中东宴会用途"),
 ("cma-2020-186","Cleveland Museum of Art — Ding Ware Bowl of the Xing Type, Gongxian, 907–60, acc. 2020.186",
  "https://openaccess-api.clevelandart.org/api/artworks/2020.186","2026-11-23 API HTTP 200；白瓷象牙釉 4.7×18.5cm；说明含 Tea 色与釉色的关系"),
 ("cma-1957-33","Cleveland Museum of Art — Bulb Bowl, numbered Jun ware, early 1400s, acc. 1957.33",
  "https://openaccess-api.clevelandart.org/api/artworks/1957.33","2026-11-23 API HTTP 200；瓷质石陶 23.5×8cm；说明含数字款与蚯蚓走泥纹")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

p=os.path.join(ROOT,"tools","catalog.py"); s=io.open(p,encoding="utf-8").read()
if '"art-ceramics"' not in s:
    anchor=' ("work-archives","作品档案"),\n])'
    assert anchor in s
    s=s.replace(anchor,' ("art-ceramics","陶瓷工艺"),\n'+anchor)
    io.open(p,"w",encoding="utf-8").write(s); print("unit added")

T=[('yuan-blue-white-jar','元青花狮耳罐（景德镇）','作品','art-ceramics','14世纪','中国','综合','核心',
    '元 dynasty 景德镇釉下青花罐，克利夫兰艺术博物馆藏（1962.154）。','1300年代',
    '不晚于1330年代已生产，供宫廷与民间及外销；青花钴料自伊朗（很可能卡尚）进口。','longquan-export-bowl,ding-tea-bowl','cma-1962-154'),
   ('longquan-export-bowl','龙泉窑模印大碗','作品','art-ceramics','14—15世纪','中国','综合','重要',
    '龙泉窑青瓷大碗，克利夫兰艺术博物馆藏（2020.188）。','1300—1400年代',
    '瓣状壁如花开放、口沿具模印尖棱近金属器；釉厚且亮如玉；窑工已掌握烧造巨形器以供外销。','yuan-blue-white-jar,jun-numbered-bulb-bowl','cma-2020-188'),
   ('ding-tea-bowl','定窑「邢式」白瓷碗','作品','art-ceramics','10世纪','中国','综合','重要',
    '巩县窑（定窑系）象牙白釉碗，克利夫兰艺术博物馆藏（2020.186）。','907—960年',
    '此类碗用于饮茶，远销至萨马拉（今伊拉克）；唐人以红茶宜配淡青或白釉碗。','yuan-blue-white-jar,longquan-export-bowl','cma-2020-186'),
   ('jun-numbered-bulb-bowl','钧窑数字款钵','作品','art-ceramics','15世纪','中国','综合','重要',
    '钧台窑带数字款钵，克利夫兰艺术博物馆藏（1957.33）。','1400年代初',
    '底刻「二」字，数字标尺寸（一最大、十最小）；内壁蓝色乳光釉有「蚯蚓走泥纹」，外壁紫调来自铜呈色。','longquan-export-bowl,yuan-blue-white-jar','cma-1957-33')]
lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")