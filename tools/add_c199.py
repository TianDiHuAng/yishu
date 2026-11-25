# -*- coding: utf-8 -*-
"""Cycle199：扩大纲，音乐类新增 7 条（只转述 Wikipedia 摘要；取回 2026-11-25，缓存于 data/_cache/wp）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); sys.path.insert(0,os.path.join(ROOT,"tools"))
WP="https://en.wikipedia.org/wiki/"
NOTE="2026-11-25 经 Wikipedia REST summary 接口取回，HTTP 200，页面标题与摘要匹配；摘要缓存于 data/_cache/wp"
WDN="2026-11-25 由同一摘要接口返回的 wikibase_item 取得 QID，与页面标题对应"
A=[("string-quartet","String_quartet","String quartet","Q207338"),
 ("concerto","Concerto","Concerto","Q9748"),
 ("divertimento","Divertimento","Divertimento","Q647653"),
 ("bartok","Béla_Bartók","Béla Bartók","Q83326"),
 ("prokofiev","Sergei_Prokofiev","Sergei Prokofiev","Q49481"),
 ("electronic-music","Electronic_music","Electronic music","Q9778"),
 ("aleatoric-music","Aleatoric_music","Aleatoric music","Q623715")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for eid,pg,pn,q in A:
    for s in ({"id":"enc-"+eid,"title":pn,"author":"Wikipedia contributors","year":"2026","url":WP+pg,"type":"权威百科","verified":True,"verified_note":NOTE},
              {"id":"wd-"+eid,"title":"Wikidata: %s (%s)"%(pn,q),"author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026","url":"https://www.wikidata.org/wiki/"+q,"type":"权威结构化数据","verified":True,"verified_note":WDN}):
        if s["id"] not in have: sd["sources"].append(s); have.add(s["id"])
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
def S(e): return "enc-%s,wd-%s"%(e,e)
T=[
 ('string-quartet','弦乐四重奏（String quartet）','术语','music-classical','18世纪中叶—今','欧洲','音乐体裁','重要',
  '指一种音乐作品类型，也指演奏这类作品的四人组合：两把小提琴、一把中提琴、一把大提琴。','约公元18世纪中叶—今',
  '弦乐四重奏这一术语既指一种音乐作品类型，也指演奏四重奏的四人组合。自18世纪中叶起，许多作曲家创作弦乐四重奏。相应的乐团由两名小提琴手、一名中提琴手和一名大提琴手组成。',
  'haydn,beethoven,classical-period-music',S('string-quartet')),
 ('concerto','协奏曲（Concerto）','术语','music-baroque','巴洛克晚期—今','欧洲','音乐体裁','重要',
  '巴洛克晚期以来，多指为一名或多名独奏者与乐队（或其他乐团）而写的器乐作品；快—慢—快三乐章结构自18世纪初成为标准。','约公元18世纪初—今',
  '自巴洛克晚期以来，协奏曲大多被理解为一种器乐作品，为一名或多名独奏者而写，由乐队或其他乐团伴奏。典型的三乐章结构——慢乐章前后各有一个快乐章——自18世纪初成为标准。',
  'vivaldi,corelli,mozart',S('concerto')),
 ('divertimento','嬉游曲（Divertimento）','术语','music-classical','18世纪','欧洲','音乐体裁','补充',
  '一种音乐体裁，多数实例出自18世纪；情绪多轻快，通常为小型乐团而写，泛指多种世俗器乐作品。','约公元18世纪',
  '嬉游曲是一种音乐体裁，大多数实例出自18世纪。其情绪通常轻快，一般为小型乐团而写。该词用来描述为独奏者或室内乐团而写的多种世俗（非宗教）器乐作品。它通常是一种娱乐性音乐，但也可用于较严肃的体裁。1780年以后，该词一般指非正式或轻松的作品。',
  'mozart,haydn,classical-period-music',S('divertimento')),
 ('bartok','巴托克（Béla Bartók）','人物','music-modern','20世纪','匈牙利','音乐体裁','核心',
  '匈牙利作曲家、钢琴家与民族音乐学家（1881—1945），被视为20世纪最重要的作曲家之一，以采集与分析民间音乐著称。','1881—1945',
  '巴托克是匈牙利作曲家、钢琴家和民族音乐学家，被视为20世纪最重要的作曲家之一；他与李斯特被看作匈牙利最伟大的作曲家。代表作包括歌剧《蓝胡子城堡》、舞剧《神奇的满大人》、《为弦乐、打击乐与钢片琴而作的音乐》、《乐队协奏曲》和六首弦乐四重奏。他通过采集和分析研究民间音乐，成为比较音乐学（后称民族音乐学）的创始人之一。其作品常被描述为传统农民民间音乐与先锋音乐的结合。',
  '20th-century-classical,liszt,string-quartet',S('bartok')),
 ('prokofiev','普罗科菲耶夫（Sergei Prokofiev）','人物','music-modern','20世纪','俄国·苏联','音乐体裁','核心',
  '俄国作曲家、钢琴家与指挥家（1891—1953），后在苏联工作，被视为20世纪主要作曲家之一。','1891—1953',
  '普罗科菲耶夫是俄国作曲家、钢琴家和指挥家，后在苏联工作。作为多种音乐体裁中公认杰作的创作者，他被视为20世纪主要作曲家之一。广为流传的作品包括《三橘爱》中的进行曲、组曲《基热中尉》、舞剧《罗密欧与朱丽叶》（《骑士之舞》即出自此剧）和《彼得与狼》。在他从事的既有体裁中（不计少年习作），他完成了七部歌剧、七部交响曲、八部舞剧、五首钢琴协奏曲、两首小提琴协奏曲、一首大提琴协奏曲、一首大提琴与乐队的交响协奏曲和九首钢琴奏鸣曲。',
  '20th-century-classical,stravinsky,tchaikovsky',S('prokofiev')),
 ('electronic-music','电子音乐（Electronic music）','风格','music-modern','20世纪—今','全球','音乐体裁','重要',
  '泛指在创作中使用电子乐器、基于电路的音乐技术与软件或通用电子设备的一组音乐类型，包括纯电子与机电两类手段。','20世纪—今',
  '电子音乐泛指一组音乐类型，在创作中使用电子乐器、基于电路的音乐技术与软件，或通用电子设备。它包括用电子手段与机电手段制作的音乐。纯电子乐器完全依靠电路发声，例如电子振荡器、特雷门琴或合成器，无需先用机械方式产生声波再转为电信号。机电乐器则以琴弦或琴槌等机械部件产生声波，再由电磁拾音器、功率放大器和扬声器处理拾音器产生的电信号并转回声波，例如电传簧风琴（telharmonium）、哈蒙德风琴、电钢琴和电吉他。',
  '20th-century-classical,minimalism-music,aleatoric-music',S('electronic-music')),
 ('aleatoric-music','偶然音乐（Aleatoric music）','术语','music-modern','20世纪','欧美','音乐体裁','重要',
  '作品某些要素交由偶然决定，或作品实现的某些主要要素交由演奏者决定（或二者兼有）的音乐。','20世纪',
  '偶然音乐是指作品的某些要素交由偶然决定，或作品实现中的某些主要要素交由演奏者决定，或二者兼有的音乐。这一术语最常与偶然因素只涉及相对有限的若干可能性的做法相联系。',
  'serialism,20th-century-classical,electronic-music',S('aleatoric-music')),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
have_ids=io.open(p,encoding="utf-8").read()
T=[t for t in T if "('%s',"%t[0] not in have_ids and '("%s",'%t[0] not in have_ids]
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T),"sources",len(sd["sources"]))
