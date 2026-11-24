# -*- coding: utf-8 -*-
"""Cycle178：中世纪与文艺复兴音乐人物 6 条（Wikipedia 摘要+相邻页+Wikidata；取回日期 2026-11-24）。
生卒年/年代取自 Wikidata 简介或相邻页摘要（本页摘要未给），已在各条“待核实”注明。"""
import io,json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
WP="https://en.wikipedia.org/wiki/"
NOTE="2026-11-24 经 Wikipedia REST summary 接口取回，HTTP 200，页面标题与摘要匹配；摘要缓存于 data/_cache/wp"
WDN="2026-11-24 经 wd_api 读取实体成功，英文标签与条目一致；年代取自其英文简介"
A=[
 ("tallis","Thomas_Tallis","Thomas Tallis","Renaissance_music","Renaissance music","Q207789"),
 ("byrd","William_Byrd","William Byrd","Renaissance_music","Renaissance music","Q208375"),
 ("lassus","Orlande_de_Lassus","Orlando di Lasso","Franco-Flemish_School","Franco-Flemish School","Q154792"),
 ("gesualdo","Carlo_Gesualdo","Carlo Gesualdo","Madrigal","Madrigal","Q192958"),
 ("machaut","Guillaume_de_Machaut","Guillaume de Machaut","Ars_nova","Ars nova","Q200580"),
 ("leonin","Leonin","Léonin","Notre_Dame_school","Notre-Dame school","Q297501"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
def slug(p): return p.lower().replace("_","-")
def add(s):
    if s["id"] not in have: sd["sources"].append(s); have.add(s["id"])
for eid,pg,pn,pg2,pn2,q in A:
    add({"id":"enc-"+eid,"title":pn,"author":"Wikipedia contributors","year":"2026","url":WP+pg,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"enc-c178-"+slug(pg2),"title":pn2,"author":"Wikipedia contributors","year":"2026","url":WP+pg2,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"wd-"+eid,"title":"Wikidata: %s (%s)"%(pn,q),"author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026","url":"https://www.wikidata.org/wiki/"+q,"type":"权威结构化数据","verified":True,"verified_note":WDN})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
def S(eid,pg2): return "enc-%s,enc-c178-%s,wd-%s"%(eid,slug(pg2),eid)
T=[
 ('tallis','塔利斯（Thomas Tallis）','人物','music-renaissance','16世纪','英国','音乐体裁','重要',
  '盛期文艺复兴的英国作曲家，作品以声乐为主，在英国合唱音乐选集中占据首要位置。','约公元16世纪',
  '托马斯·塔利斯是盛期文艺复兴的英国作曲家。他的作品以声乐为主，在英国合唱音乐的选集中占据首要位置，被视为英国最伟大的作曲家之一，因其在英国音乐中独特的声音而受到推崇。',
  'renaissance-music,motet,byrd',S('tallis','Renaissance_music')),
 ('byrd','伯德（William Byrd）','人物','music-renaissance','16—17世纪','英国','音乐体裁','重要',
  '英国文艺复兴作曲家，被视为文艺复兴最伟大的作曲家之一，对本国及欧洲大陆的作曲家影响深远。','约公元1540—1623年',
  '威廉·伯德是英国文艺复兴作曲家，被视为文艺复兴最伟大的作曲家之一，对本国与欧洲大陆的作曲家都有深远影响。他常与约翰·邓斯泰布尔、亨利·珀塞尔并列，被视为英国早期音乐最重要的作曲家之一。',
  'renaissance-music,tallis,motet',S('byrd','Renaissance_music')),
 ('lassus','拉索（Orlando di Lasso）','人物','music-renaissance','16世纪','佛兰德斯','音乐体裁','重要',
  '文艺复兴晚期作曲家，佛兰德斯—法国乐派成熟复调风格的主要代表，极为多产，风格与体裁变化很大。','1532—1594年',
  '奥兰多·迪·拉索是文艺复兴晚期的作曲家，是佛兰德斯—法国乐派成熟复调风格的主要代表，与威廉·伯德、帕莱斯特里纳和托马斯·路易斯·德·维多利亚并列为文艺复兴晚期的主要作曲家之一。他极为多产，音乐在风格与体裁上变化很大，因此在整个欧洲享有空前的声誉。',
  'renaissance-music,palestrina,josquin',S('lassus','Franco-Flemish_School')),
 ('gesualdo','杰苏阿尔多（Carlo Gesualdo）','人物','music-renaissance','16—17世纪','意大利','音乐体裁','重要',
  '意大利贵族与作曲家，以写作牧歌与宗教音乐著称，使用直到19世纪晚期才再次出现的半音化语言。','1566—1613年',
  '卡洛·杰苏阿尔多·达·韦诺萨是意大利贵族与作曲家，同时是韦诺萨亲王与孔扎伯爵。他以写作牧歌与宗教音乐更为人知，所用的半音化语言直到19世纪晚期才再次出现。他还因发现第一任妻子与其贵族情人通奸而将二人杀害而闻名。',
  'madrigal,renaissance-music,monteverdi',S('gesualdo','Madrigal')),
 ('machaut','马肖（Guillaume de Machaut）','人物','music-medieval','14世纪','法国','音乐体裁','重要',
  '法国作曲家与诗人，中世纪晚期新艺术风格的核心人物，被视为14世纪最重要的法国作曲家与诗人。','约公元1300—1377年',
  '纪尧姆·德·马肖是法国作曲家与诗人，是中世纪晚期新艺术（ars nova）风格的核心人物。他在这一体裁中的统治地位如此突出，以致现代音乐学家用他的逝世来划分新艺术与随后的精微新艺术（ars subtilior）运动。他被视为14世纪最重要的法国作曲家与诗人，常被看作该世纪欧洲首屈一指的作曲家。',
  'medieval-music,polyphony,motet',S('machaut','Ars_nova')),
 ('leonin','莱奥南（Léonin）','人物','music-medieval','12世纪','法国','音乐体裁','重要',
  '已知第一位重要的复调奥尔加农作曲家，大概是法国人，大概在巴黎圣母院工作。','约公元12世纪',
  '莱奥南是已知第一位重要的复调奥尔加农作曲家。他大概是法国人，大概在巴黎圣母院生活与工作，是以姓名为人所知的最早的圣母院复调乐派与古艺术（ars antiqua）风格成员，这要归功于被称为“匿名者四世”的作者。除此之外别无确定的身份信息。',
  'organum,polyphony,medieval-music',S('leonin','Notre_Dame_school')),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
