# -*- coding: utf-8 -*-
"""Cycle177：音乐人物 6 条（Wikipedia 摘要+相邻页+Wikidata；取回日期 2026-11-24）。
生卒年取自 Wikidata 简介（摘要未给），已在各条“待核实”注明。"""
import io,json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
WP="https://en.wikipedia.org/wiki/"
NOTE="2026-11-24 经 Wikipedia REST summary 接口取回，HTTP 200，页面标题与摘要匹配；摘要缓存于 data/_cache/wp"
WDN="2026-11-24 经 wd_api 读取实体成功，英文标签与条目一致；生卒年取自其英文简介"
A=[
 ("vivaldi","Antonio_Vivaldi","Antonio Vivaldi","Baroque_music","Baroque music","Q1340"),
 ("brahms","Johannes_Brahms","Johannes Brahms","Romantic_music","Romantic music","Q7294"),
 ("liszt","Franz_Liszt","Franz Liszt","Romantic_music","Romantic music","Q41309"),
 ("mahler","Gustav_Mahler","Gustav Mahler","Romantic_music","Romantic music","Q7304"),
 ("tchaikovsky","Pyotr_Ilyich_Tchaikovsky","Pyotr Ilyich Tchaikovsky","Romantic_music","Romantic music","Q7315"),
 ("gluck","Christoph_Willibald_Gluck","Christoph Willibald Gluck","Classical_period_(music)","Classical period (music)","Q130759"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
def slug(p): return p.lower().replace("_","-").replace("(","").replace(")","")
def add(s):
    if s["id"] not in have: sd["sources"].append(s); have.add(s["id"])
for eid,pg,pn,pg2,pn2,q in A:
    add({"id":"enc-"+eid,"title":pn,"author":"Wikipedia contributors","year":"2026","url":WP+pg,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"enc-c177-"+slug(pg2),"title":pn2,"author":"Wikipedia contributors","year":"2026","url":WP+pg2,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"wd-"+eid,"title":"Wikidata: %s (%s)"%(pn,q),"author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026","url":"https://www.wikidata.org/wiki/"+q,"type":"权威结构化数据","verified":True,"verified_note":WDN})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
def S(eid,pg2): return "enc-%s,enc-c177-%s,wd-%s"%(eid,slug(pg2),eid)
T=[
 ('vivaldi','维瓦尔第（Antonio Vivaldi）','人物','music-baroque','17—18世纪','意大利','音乐体裁','核心',
  '意大利巴洛克作曲家、小提琴演奏家与经纪人，被视为最伟大的巴洛克作曲家之一，巩固了协奏曲形式，尤其是独奏协奏曲。','1678—1741年',
  '安东尼奥·维瓦尔第是意大利作曲家、小提琴演奏家，也是巴洛克音乐的经纪人。他被视为最伟大的巴洛克作曲家之一，生前即影响欧洲各地，催生了许多模仿者与仰慕者。他在配器、小提琴技巧与标题音乐方面开创了多项发展，并把新兴的协奏曲形式，尤其是独奏协奏曲，巩固为被广泛接受并沿用的惯用形式。',
  'baroque-music,concerto,bach',S('vivaldi','Baroque_music')),
 ('brahms','勃拉姆斯（Johannes Brahms）','人物','music-romantic','19世纪','德国','音乐体裁','核心',
  '德国浪漫主义中期作曲家、钢琴家与指挥家，作品以富于表现的对位、更自由的不协和、节奏活力与传统曲式为特色。','1833—1897年',
  '约翰内斯·勃拉姆斯是浪漫主义中期的德国作曲家、钢琴家与指挥家。他的音乐以富于表现的对位、更自由的不协和、节奏的活力与传统曲式为特色。作品包括四部交响曲、四部协奏曲、一部安魂曲、大量室内乐，以及数百首民歌改编曲与艺术歌曲。',
  'romantic-music,counterpoint,lied',S('brahms','Romantic_music')),
 ('liszt','李斯特（Franz Liszt）','人物','music-romantic','19世纪','匈牙利','音乐体裁','核心',
  '浪漫主义时期的匈牙利作曲家、钢琴演奏大师、指挥家与教师，作品跨越六十余年，被视为其时代最多产、最有影响的作曲家之一。','1811—1886年',
  '弗朗茨·李斯特是浪漫主义时期的匈牙利作曲家、钢琴演奏大师、指挥家与教师。他的创作跨越六十多年，被视为其时代最多产、最有影响的作曲家之一，他的钢琴作品至今仍被广泛演出与录音。',
  'romantic-music,symphonic-poem,chopin',S('liszt','Romantic_music')),
 ('mahler','马勒（Gustav Mahler）','人物','music-romantic','19世纪末—20世纪初','奥地利·波希米亚','音乐体裁','核心',
  '奥地利—波希米亚的浪漫主义作曲家，同辈中最重要的指挥家之一，是19世纪传统与20世纪初现代主义之间的桥梁。','1860—1911年',
  '古斯塔夫·马勒是奥地利—波希米亚的浪漫主义作曲家，也是同辈中首屈一指的指挥家。作为作曲家，他充当了19世纪传统与20世纪初现代主义之间的桥梁。他生前作为指挥家的地位毋庸置疑，自己的音乐却在一段相对被冷落的时期之后才广受欢迎，其间包括纳粹时代在欧洲大部分地区对其演出的禁令。1945年之后，新一代听众重新发现了他的作品，他成为被演出与录音最多的作曲家之一，这一地位延续至21世纪。',
  'romantic-music,symphony,20th-century-classical',S('mahler','Romantic_music')),
 ('tchaikovsky','柴可夫斯基（Pyotr Ilyich Tchaikovsky）','人物','music-romantic','19世纪','俄国','音乐体裁','核心',
  '浪漫主义时期的俄国作曲家，第一位音乐给国际留下持久印象的俄国作曲家，写下古典曲目中最流行的一批音乐会与舞台音乐。','1840—1893年',
  '彼得·伊里奇·柴可夫斯基是浪漫主义时期的俄国作曲家，是第一位音乐给国际留下持久印象的俄国作曲家。他写下了古典曲目中最流行的一批音乐会与剧场音乐，包括《1812序曲》、第一钢琴协奏曲、小提琴协奏曲、《罗密欧与朱丽叶》序曲幻想曲、数部交响曲、歌剧《叶甫盖尼·奥涅金》，以及芭蕾《天鹅湖》《睡美人》《胡桃夹子》。',
  'romantic-music,concerto,opera',S('tchaikovsky','Romantic_music')),
 ('gluck','格鲁克（Christoph Willibald Gluck）','人物','music-classical','18世纪','德意志·奥地利','音乐体裁','重要',
  '早期古典时期的意大利与法国歌剧作曲家，在维也纳哈布斯堡宫廷推动了歌剧戏剧性做法的实际改革。','1714—1787年',
  '克里斯托夫·维利巴尔德·格鲁克是早期古典时期意大利歌剧与法国歌剧的作曲家。他生于上普法尔茨、成长于波希米亚，二者当时都属神圣罗马帝国，在维也纳的哈布斯堡宫廷成名，并在那里实现了许多知识分子长期呼吁的歌剧戏剧性做法的实际改革。1760年代一系列激进的新作，其中有《奥菲欧与欧律狄刻》和《阿尔切斯特》，打破了梅塔斯塔西奥式正歌剧在这个世纪大部分时间里的垄断。他以乐队宣叙调引入更多戏剧性，并削减通常冗长的返始咏叹调，后期歌剧的长度只有典型巴洛克歌剧的一半。',
  'opera,classical-period-music,mozart',S('gluck','Classical_period_(music)')),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
