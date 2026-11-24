# -*- coding: utf-8 -*-
"""Cycle118：东南亚 4 条（Hevajra、帕輿钩、伽楼多楣饰、Baphuon 跪像）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-2011-143","Cleveland Museum of Art — Hevajra, Angkor, c. 1200, acc. 2011.143",
  "https://openaccess-api.clevelandart.org/api/artworks/2011.143","2026-11-24 API HTTP 200；青铜 46×23.9cm；说明含八面十六臂与 Jayavarman VII"),
 ("cma-1982-12","Cleveland Museum of Art — Palanquin Hook, Cambodia, 1175–1230, acc. 1982.12",
  "https://openaccess-api.clevelandart.org/api/artworks/1982.12","2026-11-24 API HTTP 200；青铜 17.4cm；说明含伽楼多面与輿制"),
 ("cma-1967-37","Cleveland Museum of Art — Lintel with Garuda, Cambodia, 875–925, acc. 1967.37",
  "https://openaccess-api.clevelandart.org/api/artworks/1967.37","2026-11-24 API HTTP 200；砂岩 52.6×118.1cm；说明含毗湿奴坐骑与蛇尾"),
 ("cma-1978-8","Cleveland Museum of Art — Kneeling Male Figure, Baphuon period, 1010–80, acc. 1978.8",
  "https://openaccess-api.clevelandart.org/api/artworks/1978.8","2026-11-24 API HTTP 200；青铜 43.2cm；说明含第三只眼与银嵌五官"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('hevajra-buddhist','喜金刚像（Hevajra）','作品','art-asia','13世纪','东南亚','雕塑','核心',
  '吴哥青铜喜金刚像，克利夫兰艺术博物馆藏（2011.143）。','约1200年',
  '阇耶跋摩七世重 Hevajra 灌顶仪式，都城东门立巨型舞姿石像；八面十六臂四腿，左持印度诸神象（财/死/日/月/火/风/水/地），右持动物。','khmer-naga-buddha,champa-planetary-deity-dongduong','cma-2011-143'),
 ('palanquin-hook-angkor','吴哥帕輿钩','作品','art-asia','12—13世纪','东南亚','金属器','重要',
  '吴哥青铜帕輿钩，克利夫兰艺术博物馆藏（1982.12）。','1175—1230年',
  '王室/僧侣出行乘輿；青铜件铸形繁复并鎏金；钩末端为伽楼多面（鹰喙/程式化翼羽），顶空承接木杠。','khmer-naga-buddha,hevajra-buddhist','cma-1982-12'),
 ('garuda-lintel-khmer','伽楼多楣饰','作品','art-asia','9世纪末—10世纪初','东南亚','雕塑','核心',
  '柬埔寨砂岩石楣，克利夫兰艺术博物馆藏（1967.37）。','875—925年',
  '伽楼多（半人半鹰、毗湿奴坐骑）；喙鼻，翼作繁叶状；中拱枝蔓生女性与珠宝，终为眼镜蛇首；其为蛇之天敌，故按蛇尾。','khmer-naga-buddha,palanquin-hook-angkor','cma-1967-37'),
 ('baphuon-kneeling-figure','Baphuon 期跪像','作品','art-asia','11世纪','东南亚','雕塑','重要',
  '吴哥 Baphuon 期青铜跪像，克利夫兰艺术博物馆藏（1978.8）。','1010—1080年',
  '额上第三眼示认同湿婆；跪姿举双手示崇拜；低腰带下裳为 Baphuon 期典型；眼/眉/须/髯原嵌银。','hevajra-buddhist,palanquin-hook-angkor','cma-1978-8'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")