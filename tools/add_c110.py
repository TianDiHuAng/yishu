# -*- coding: utf-8 -*-
"""Cycle110：中世纪 4 条（象牙基督受难像、巴黎象牙圣母子、利摩日福音书封、雪花石哀悼基督）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o72533","Victoria and Albert Museum — The Crucified Christ, Tuscany, 1290–1310, O72533",
  "https://api.vam.ac.uk/v2/object/O72533","2026-11-24 API HTTP 200；象牙存鎏金 15.3×6×5cm；说明含濒死面容与长发"),
 ("vam-o130510","Victoria and Albert Museum — The Virgin and Child, Paris, ca. 1240, O130510",
  "https://api.vam.ac.uk/v2/object/O130510","2026-11-24 API HTTP 200；象牙圆雕 高26cm；说明含最早法国立姿圣母子象牙"),
 ("vam-o120709","Victoria and Albert Museum — Gospel cover, Limoges, ca. 1200, O120709",
  "https://api.vam.ac.uk/v2/object/O120709","2026-11-24 API HTTP 200；铜鎏金錾胎珐琅 33.2×24.2cm；说明含基督庄严与四福音书作者"),
 ("vam-o94288","Victoria and Albert Museum — The Virgin with the Dead Christ, Netherlands, ca. 1430, O94288",
  "https://api.vam.ac.uk/v2/object/O94288","2026-11-24 API HTTP 200；雪花石 400×315mm；说明含虔敬像与新旧风格融合"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('ivory-crucified-christ','象牙基督受难像','作品','art-medieval','13世纪','欧洲','雕塑','核心',
  '托斯卡纳象牙存鎏金基督像，维多利亚与艾伯特博物馆藏（O72533）。','1290—1310年',
  '基督濒死：闭目、头偏一侧、微张口、左颊伤痕；长发分两缕垂肩；下颌底下有隐藏结构（记录处截断）。','ivory-virgin-child-paris,gothic','vam-o72533'),
 ('ivory-virgin-child-paris','巴黎象牙圣母子','作品','art-medieval','13世纪','欧洲','雕塑','核心',
  '巴黎象牙圆雕圣母子，维多利亚与艾伯特博物馆藏（O130510）。','约1240年',
  '圣母左臂托圣婴，圣婴右手祝福、左手持苹果；圆柱座残存鎏金铭文（天使问候）；最早法国立姿圣母子象牙之一。','ivory-crucified-christ,auvergne-virgin-majesty','vam-o130510'),
 ('limoges-gospel-cover','利摩日福音书封','作品','art-medieval','13世纪','欧洲','综合','核心',
  '利摩日錾胎珐琅铜鎏金福音书封，维多利亚与艾伯特博物馆藏（O120709）。','约1200年',
  '矩形，铜合金錾胎珐琅钉于橡木板；中为基督庄严坐虹、右手祝福左手持书；肩上有Α/Ω，四角为四福音书作者象征。','gothic-casket-panels,ivory-virgin-child-paris','vam-o120709'),
 ('alabaster-pieta','雪花石《哀悼基督》','作品','art-medieval','15世纪','欧洲','雕塑','核心',
  '尼德兰雪花石圣母抱亡基督像，维多利亚与艾伯特博物馆藏（O94288）。','约1430年',
  '圣母坐矮凳抱亡基督；左手扶其伸出的左臂、右手托其头；基督戴荆棘冠、可见枪伤；为虔敬而作。','ivory-crucified-christ,gothic','vam-o94288'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")