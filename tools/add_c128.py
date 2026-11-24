# -*- coding: utf-8 -*-
"""Cycle128：日本小件 4 条（根付、刀镡、印笼、输出书桌盒）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o492598","Victoria and Albert Museum — Wood netsuke of a dancer, Japan, 18th c., O492598",
  "https://api.vam.ac.uk/v2/object/O492598","2026-11-24 API HTTP 200；木雕 3.18×5.08cm；说明含 himotoshi 与坠钮功能"),
 ("vam-o39087","Victoria and Albert Museum — Tsuba (sword guard), shakudo with cloisonné enamel, Japan, ca. 1800–1850, O39087",
  "https://api.vam.ac.uk/v2/object/O39087","2026-11-24 API HTTP 200；赤铜合金嵌珐琅 7.7×7.4cm；说明含护手演变与流派"),
 ("vam-o120429","Victoria and Albert Museum — Four-case inrō with autumn plants, Japan, 1600–1650, O120429",
  "https://api.vam.ac.uk/v2/object/O120429","2026-11-24 API HTTP 200；黑漆金莳绘梨地 9.0×5.3×3.1cm；说明含印章/药与时尚配饰"),
 ("vam-o77643","Victoria and Albert Museum — Export writing box, Nagasaki, 1800–1850, O77643",
  "https://api.vam.ac.uk/v2/object/O77643","2026-11-24 API HTTP 200；黑漆嵌螺钿 14.8×42.2×25.4cm；说明含仅外销与荷兰商人"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('netsuke-dancer','木雕舞者根付','作品','art-asia','18世纪','东亚','雕塑','核心',
  '日本木雕根付，维多利亚与艾伯特博物馆藏（O492598）。','18世纪',
  '根付为坠钮，男子以丝绳将袋/器悬于腰带；须小而不重、却有体积、无锐棱、坚固耐磨，尤须能系绳——本例有双孔（himotoshi）。','japanese-inro,tsuba-shakudo','vam-o492598'),
 ('tsuba-shakudo','刀镡（赤铜嵌珐琅）','作品','art-asia','19世纪','东亚','金属器','核心',
  '日本刀镡，维多利亚与艾伯特博物馆藏（O39087）。','约1800—1850年',
  '镡置于柄与刃之间护手；初为素铁圆盘，或镂或锤低浮雕；后多以铜合金做旧呈多色并嵌异色金属；遂成微型艺术，各流派自有风格。','netsuke-dancer,japanese-inro','vam-o39087'),
 ('inro-autumn-plants','四层印笼（秋草图）','作品','art-asia','17世纪','东亚','综合','核心',
  '日本四层印笼，维多利亚与艾伯特博物馆藏（O120429）。','1600—1650年',
  '饰秋草/菊/胡枝子；黑漆地金平莳绘与梨地；和服无袋故以丝绳＋根付悬印笼；原盛印章墨或药，后成昂贵却少实用的时尚配饰。','netsuke-dancer,japanese-inro','vam-o120429'),
 ('nagasaki-writing-box','长崎输出书桌盒','作品','art-asia','19世纪','东亚','综合','核心',
  '长崎输出黑漆螺钿书桌盒，维多利亚与艾伯特博物馆藏（O77643）。','1800—1850年',
  '盒开为书桌，斜面覆呢、下有抽屉、金属锁板（钥失）；黑漆嵌彩绘螺钿，饰枫枝鸟；此类盒日本不用、专为西销；17世纪后期荷兰商人独准在日贸易。','vandiem-lacquer-box,japanese-inro','vam-o77643'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")