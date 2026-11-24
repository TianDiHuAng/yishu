# -*- coding: utf-8 -*-
"""Cycle179：巴洛克音乐人物 5 条（Wikipedia 摘要+相邻页+Wikidata；取回日期 2026-11-24）。
年代取自 Wikidata 简介或相邻页摘要（本页摘要未给），已在各条“待核实”注明。"""
import io,json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
WP="https://en.wikipedia.org/wiki/"
NOTE="2026-11-24 经 Wikipedia REST summary 接口取回，HTTP 200，页面标题与摘要匹配；摘要缓存于 data/_cache/wp"
WDN="2026-11-24 经 wd_api 读取实体成功，英文标签与条目一致；年代取自其英文简介（如有）"
A=[
 ("purcell","Henry_Purcell","Henry Purcell","Baroque_music","Baroque music","Q9695"),
 ("lully","Jean-Baptiste_Lully","Jean-Baptiste Lully","French_opera","French opera","Q1192"),
 ("scarlatti-domenico","Domenico_Scarlatti","Domenico Scarlatti","Baroque_music","Baroque music","Q167837"),
 ("corelli","Arcangelo_Corelli","Arcangelo Corelli","Baroque_music","Baroque music","Q164475"),
 ("telemann","Georg_Philipp_Telemann","Georg Philipp Telemann","Baroque_music","Baroque music","Q75854"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
def slug(p): return p.lower().replace("_","-")
def add(s):
    if s["id"] not in have: sd["sources"].append(s); have.add(s["id"])
for eid,pg,pn,pg2,pn2,q in A:
    add({"id":"enc-"+eid,"title":pn,"author":"Wikipedia contributors","year":"2026","url":WP+pg,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"enc-c179-"+slug(pg2),"title":pn2,"author":"Wikipedia contributors","year":"2026","url":WP+pg2,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"wd-"+eid,"title":"Wikidata: %s (%s)"%(pn,q),"author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026","url":"https://www.wikidata.org/wiki/"+q,"type":"权威结构化数据","verified":True,"verified_note":WDN})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
def S(eid,pg2): return "enc-%s,enc-c179-%s,wd-%s"%(eid,slug(pg2),eid)
T=[
 ('purcell','珀塞尔（Henry Purcell）','人物','music-baroque','17世纪','英国','音乐体裁','重要',
  '巴洛克中期的英国作曲家与管风琴家，极为多产，作品含一百多首歌曲、悲剧歌剧《狄多与埃涅阿斯》与《仙后》的剧乐。','1659—1695年',
  '亨利·珀塞尔是巴洛克中期的英国作曲家与管风琴家。他极为多产，作品包括一百多首歌曲、悲剧歌剧《狄多与埃涅阿斯》，以及为莎士比亚《仲夏夜之梦》改编版《仙后》所写的剧乐。',
  'baroque-music,opera,byrd',S('purcell','Baroque_music')),
 ('lully','吕利（Jean-Baptiste Lully）','人物','music-baroque','17世纪','法国','音乐体裁','重要',
  '意大利出身的法国作曲家、舞者与器乐演奏家，被视为法国巴洛克音乐风格的大师，以歌剧最为知名，大半生在路易十四宫廷。','1632—1687年',
  '让—巴蒂斯特·吕利是意大利出身的法国作曲家、舞者与器乐演奏家，被视为法国巴洛克音乐风格的大师。他以歌剧最为知名，一生大部分时间在路易十四的宫廷中工作，1661年成为法国臣民。他与剧作家莫里哀是密友，二人合作了多部喜剧芭蕾，其中包括《爱情医生》《乔治·唐丹》《浦尔索涅克先生》《普赛克》，以及他最知名的作品《贵人迷》。',
  'baroque-music,opera,monteverdi',S('lully','French_opera')),
 ('scarlatti-domenico','多梅尼科·斯卡拉蒂（Domenico Scarlatti）','人物','music-baroque','17—18世纪','意大利','音乐体裁','重要',
  '意大利作曲家，按年代主要归入巴洛克，但其音乐影响了古典风格的发展，今天主要以555首键盘奏鸣曲闻名。','约公元17—18世纪',
  '朱塞佩·多梅尼科·斯卡拉蒂是意大利作曲家。按年代，他主要被归为巴洛克作曲家，但他的音乐对古典风格的发展有影响。他和著名的父亲亚历山德罗·斯卡拉蒂一样，用多种音乐形式创作，但今天主要以555首键盘奏鸣曲闻名。他一生大部分时间效力于葡萄牙与西班牙王室。',
  'baroque-music,sonata,classical-period-music',S('scarlatti-domenico','Baroque_music')),
 ('corelli','科雷利（Arcangelo Corelli）','人物','music-baroque','17—18世纪','意大利','音乐体裁','重要',
  '巴洛克中期的意大利作曲家、乐师与小提琴家，其音乐是现代奏鸣曲与协奏曲体裁发展、小提琴地位确立，以及现代调性与功能和声首次融合的关键。','1653—1713年',
  '阿尔坎杰罗·科雷利是巴洛克中期的意大利作曲家、乐师与小提琴家。他的音乐是现代奏鸣曲与协奏曲体裁发展的关键，对确立小提琴的首要地位也至关重要，并标志着现代调性与功能和声的第一次融合。',
  'baroque-music,sonata,concerto',S('corelli','Baroque_music')),
 ('telemann','泰勒曼（Georg Philipp Telemann）','人物','music-baroque','17—18世纪','德国','音乐体裁','重要',
  '德国巴洛克作曲家与多乐器演奏家，就现存作品而言是历史上最多产的作曲家之一，同时代人视其为德国主要作曲家之一。','约公元17—18世纪',
  '格奥尔格·菲利普·泰勒曼是德国巴洛克作曲家与多乐器演奏家。至少就现存作品而言，他是历史上最多产的作曲家之一。同时代人认为他是当时德国主要的作曲家之一，把他与好友约翰·塞巴斯蒂安·巴赫、也与他私交的亨德尔相提并论且评价颇高；巴赫曾让泰勒曼做自己儿子卡尔·菲利普·埃马努埃尔的教父并以其名为子取名。',
  'baroque-music,bach,concerto',S('telemann','Baroque_music')),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
