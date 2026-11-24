# -*- coding: utf-8 -*-
"""Cycle179 overlay：巴洛克音乐人物 5 条（只转述 Wikipedia 摘要，不补写作品）。"""
import json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
LD=os.path.join(ROOT,"data","l2")
def W(eid,sec,diag,srcs,note):
    json.dump({"id":eid,"level":"L2","sections":sec,"svg":render_svg(diag,eid),"sources":srcs,
               "needs_verification":True,"pending_notes":note},
              open(os.path.join(LD,eid+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    print("wrote",eid)
NOSRC="本条目事实仅来自 Wikipedia 摘要（2026-11-24 取回）及同源的 Wikidata，来源独立性有限，整条标记待核实。"
def YR(y): return "年代（%s）摘要未给出，取自 Wikidata 简介，需另取权威来源核实。"%y
def INF(): return "生卒年摘要与 Wikidata 简介均未给出；条目 when 写“约公元17—18世纪”，是据摘要将其归为巴洛克作曲家、并参照巴洛克音乐页（约1600—1750）推算的世纪范围，不是其生卒年的断言，需另取来源核实。"
def S(era,feat,who,tech,rel,pic,todo):
    return {"时代背景":era,"风格特征":feat,"代表人物与作品":who,"技法或形式分析":tech,"与前后风格的关系和争论":rel,"一图":pic,"待核实":"（1）"+NOSRC+todo}

W("purcell",S(
 "摘要称，珀塞尔是巴洛克中期的英国作曲家与管风琴家。",
 "摘要称，他极为多产。",
 "摘要列出的作品：一百多首歌曲、悲剧歌剧《狄多与埃涅阿斯》，以及为莎士比亚《仲夏夜之梦》改编版《仙后》所写的剧乐。摘要没有给出各作品的年份，本条目不补写。",
 "摘要没有给出具体的技法或形式，只按体裁罗列：歌曲、歌剧、剧乐。",
 "摘要没有谈到他与同时代作曲家的比较或争论。另一条摘要（伯德）称他与邓斯泰布尔、伯德并列为英国早期音乐最重要的作曲家之一，那是伯德条目摘要的说法，不是本条的。",
 "示意图以珀塞尔为中心，标示一百多首歌曲、歌剧《狄多与埃涅阿斯》、《仙后》剧乐三项。",
 "（2）"+YR("1659—1695年")+"（3）各作品年份，摘要未给出。"),
 {"nodes":[{"label":"一百多首歌曲","sub":"作品","kind":"muted"},{"label":"珀塞尔","sub":"巴洛克中期","kind":"accent"},{"label":"《狄多与埃涅阿斯》","sub":"悲剧歌剧","kind":"muted"},{"label":"《仙后》剧乐","sub":"仲夏夜之梦","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-purcell","enc-c179-baroque-music","wd-purcell"],"来源独立性有限（Wikipedia+Wikidata）；年代来自 Wikidata；作品年份未给出。")

W("lully",S(
 "摘要称，吕利大半生在路易十四的宫廷中工作，1661年成为法国臣民。",
 "摘要称，他被视为法国巴洛克音乐风格的大师，以歌剧最为知名。",
 "摘要列出他与莫里哀合作的喜剧芭蕾：《爱情医生》《乔治·唐丹》《浦尔索涅克先生》《普赛克》，以及他最知名的作品《贵人迷》。摘要没有给出各作品的年份，本条目不补写。",
 "摘要称他是意大利出身的法国作曲家、舞者与器乐演奏家；没有给出具体的技法或形式，本条目不补写。",
 "摘要称，他与剧作家莫里哀是密友。相邻的法国歌剧页称，外国出身的作曲家在法国歌剧传统中扮演了角色，吕利列在其中。库内相关条目可参见歌剧与蒙特威尔第，但摘要没有把他们联系起来。",
 "示意图以吕利为中心，标示路易十四宫廷、与莫里哀合作的喜剧芭蕾、法国巴洛克歌剧三项。",
 "（2）"+YR("1632—1687年")+"（3）各作品年份，摘要未给出；（4）“大师”属摘要转述的评价；（5）本条目首稿曾误写出摘要中没有的作品名，已在入库前更正为摘要原文所列。"),
 {"nodes":[{"label":"路易十四宫廷","sub":"大半生","kind":"muted"},{"label":"吕利","sub":"法国巴洛克","kind":"accent"},{"label":"歌剧","sub":"最知名","kind":"muted"},{"label":"与莫里哀合作","sub":"喜剧芭蕾","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-lully","enc-c179-french-opera","wd-lully"],"来源独立性有限（Wikipedia+Wikidata）；年代来自 Wikidata；作品年份未给出。")

W("scarlatti-domenico",S(
 "摘要称，他按年代主要被归为巴洛克作曲家，但其音乐对古典风格的发展有影响。",
 "摘要称，他和父亲亚历山德罗·斯卡拉蒂一样，用多种音乐形式创作，今天主要以555首键盘奏鸣曲闻名。",
 "摘要点名的是555首键盘奏鸣曲，没有列出具体曲名，本条目不补写。他一生大部分时间效力于葡萄牙与西班牙王室。库内相关条目可参见奏鸣曲。",
 "摘要没有给出键盘奏鸣曲的具体形式，本条目不补写。",
 "摘要称，他按年代属巴洛克，音乐却影响了古典风格的发展，位于两个时期之间；影响的具体表现，摘要未给出。",
 "示意图以斯卡拉蒂为中心，标示巴洛克、555首键盘奏鸣曲、影响古典风格三项。",
 "（2）"+INF()+"（3）具体曲目，摘要未给出；（4）Wikipedia 页面标题为 Domenico Scarlatti，库内 id 为 scarlatti-domenico，以区别于其父亚历山德罗。"),
 {"nodes":[{"label":"巴洛克","sub":"按年代","kind":"muted"},{"label":"斯卡拉蒂","sub":"意大利","kind":"accent"},{"label":"555首键盘奏鸣曲","sub":"今日所知","kind":"muted"},{"label":"影响古典风格","sub":"发展","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-scarlatti-domenico","enc-c179-baroque-music","wd-scarlatti-domenico"],"来源独立性有限（Wikipedia+Wikidata）；生卒年均未给出，when 为推算；曲目未给出。")

W("corelli",S(
 "摘要称，科雷利是巴洛克中期的意大利作曲家、乐师与小提琴家。",
 "摘要称，他的音乐是现代奏鸣曲与协奏曲体裁发展的关键，对确立小提琴的首要地位也至关重要。",
 "摘要没有列出具体作品名，本条目不补写。库内相关条目可参见奏鸣曲、协奏曲与维瓦尔第，但摘要没有提到他们。",
 "摘要称，他的音乐标志着现代调性与功能和声的第一次融合。可对照大小调体系条目，但该条摘要没有提到他。",
 "摘要把他置于奏鸣曲、协奏曲与调性发展的源头一侧。“关键”“第一次融合”是摘要的叙述，本条目不作独立判断。",
 "示意图以科雷利为中心，标示现代奏鸣曲与协奏曲、小提琴的首要地位、调性与功能和声三项。",
 "（2）"+YR("1653—1713年")+"（3）具体作品，摘要未给出；（4）“第一次融合”属摘要的概括，本条目未核验。"),
 {"nodes":[{"label":"奏鸣曲与协奏曲","sub":"现代体裁","kind":"muted"},{"label":"科雷利","sub":"巴洛克中期","kind":"accent"},{"label":"小提琴首要地位","sub":"确立","kind":"muted"},{"label":"调性与功能和声","sub":"首次融合","kind":"muted"}],
  "arrows":[{"from":1,"to":0},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-corelli","enc-c179-baroque-music","wd-corelli"],"来源独立性有限（Wikipedia+Wikidata）；年代来自 Wikidata；作品未给出。")

W("telemann",S(
 "摘要称，泰勒曼是德国巴洛克作曲家与多乐器演奏家。",
 "摘要称，至少就现存作品而言，他是历史上最多产的作曲家之一。",
 "摘要没有列出具体作品名，本条目不补写。摘要称，同时代人认为他是当时德国主要的作曲家之一。库内相关条目可参见巴赫。",
 "摘要没有给出具体的技法或形式，本条目不补写。",
 "摘要称，同时代人把他与好友巴赫、也与他私交的亨德尔相提并论且评价颇高；巴赫曾让泰勒曼做自己儿子卡尔·菲利普·埃马努埃尔的教父，并以其名为子取名。“最多产”与“评价颇高”都是摘要的叙述，本条目不作独立判断。",
 "示意图以泰勒曼为中心，标示最多产作曲家之一、与巴赫是好友、与亨德尔相识三项。",
 "（2）"+INF()+"（3）具体作品，摘要未给出；（4）“最多产”限定为“至少就现存作品而言”，本条目沿用此限定。"),
 {"nodes":[{"label":"巴赫","sub":"好友","kind":"muted"},{"label":"泰勒曼","sub":"德国巴洛克","kind":"accent"},{"label":"亨德尔","sub":"私交","kind":"muted"},{"label":"最多产之一","sub":"就现存作品","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":2,"to":1},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-telemann","enc-c179-baroque-music","wd-telemann"],"来源独立性有限（Wikipedia+Wikidata）；生卒年均未给出，when 为推算；作品未给出。")
