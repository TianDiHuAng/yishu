# -*- coding: utf-8 -*-
"""Cycle178 overlay：中世纪与文艺复兴音乐人物 6 条（只转述 Wikipedia 摘要，不补写作品）。"""
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
NOWORK="摘要没有列出具体作品名，本条目不补写。"
def YR(y): return "年代（%s）摘要未给出，取自 Wikidata 简介，需另取权威来源核实。"%y
def S(era,feat,who,tech,rel,pic,todo):
    return {"时代背景":era,"风格特征":feat,"代表人物与作品":who,"技法或形式分析":tech,"与前后风格的关系和争论":rel,"一图":pic,"待核实":"（1）"+NOSRC+todo}

W("tallis",S(
 "摘要称，塔利斯是盛期文艺复兴的英国作曲家。",
 "摘要称，他的作品以声乐为主，在英国合唱音乐的选集中占据首要位置。",
 NOWORK+"相关条目可参见文艺复兴音乐、经文歌与伯德。",
 "摘要没有给出具体的技法或形式，本条目不补写。",
 "摘要称，他被视为英国最伟大的作曲家之一，因其在英国音乐中独特的声音而受到推崇。这是摘要转述的评价，本条目不作独立判断；摘要没有谈到他与伯德的关系。",
 "示意图以塔利斯为中心，标示盛期文艺复兴、声乐为主、英国合唱音乐三项。",
 "（2）生卒年，摘要与 Wikidata 简介（仅写“English composer”）均未给出；条目 when 写“约公元16世纪”，是据文艺复兴音乐页（15、16世纪）与“盛期文艺复兴”推算，不是对其生卒年的断言，需另取来源核实；（3）具体作品，摘要未给出。"),
 {"nodes":[{"label":"盛期文艺复兴","sub":"英国","kind":"muted"},{"label":"塔利斯","sub":"作曲家","kind":"accent"},{"label":"声乐为主","sub":"作品","kind":"muted"},{"label":"英国合唱音乐","sub":"选集首位","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-tallis","enc-c178-renaissance-music","wd-tallis"],"来源独立性有限（Wikipedia+Wikidata）；生卒年均未给出，when 为推算；作品未给出。")

W("byrd",S(
 "摘要称，伯德是英国文艺复兴作曲家。",
 "摘要没有给出具体的风格特征，只说明他对本国与欧洲大陆的作曲家都有深远影响。",
 NOWORK+"相关条目可参见文艺复兴音乐、塔利斯与经文歌。",
 "摘要没有给出具体的技法或形式，本条目不补写。",
 "摘要称，他被视为文艺复兴最伟大的作曲家之一，常与约翰·邓斯泰布尔、亨利·珀塞尔并列为英国早期音乐最重要的作曲家之一。这是摘要转述的评价，本条目不作独立判断。",
 "示意图以伯德为中心，标示英国文艺复兴、影响本国与欧洲大陆、与邓斯泰布尔珀塞尔并列三项。",
 "（2）"+YR("约1540—1623年")+"（3）具体作品，摘要未给出；（4）“最伟大”属评价性表述。"),
 {"nodes":[{"label":"英国文艺复兴","sub":"作曲家","kind":"muted"},{"label":"伯德","sub":"深远影响","kind":"accent"},{"label":"本国与欧洲大陆","sub":"影响所及","kind":"muted"},{"label":"邓斯泰布尔珀塞尔","sub":"并列","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-byrd","enc-c178-renaissance-music","wd-byrd"],"来源独立性有限（Wikipedia+Wikidata）；年代来自 Wikidata；作品未给出。")

W("lassus",S(
 "摘要称，拉索是文艺复兴晚期的作曲家。",
 "摘要称，他是佛兰德斯—法国乐派成熟复调风格的主要代表；他极为多产，音乐在风格与体裁上变化很大。",
 NOWORK+"摘要称他与威廉·伯德、帕莱斯特里纳和托马斯·路易斯·德·维多利亚并列为文艺复兴晚期的主要作曲家之一。库内相关条目可参见帕莱斯特里纳、若斯坎与伯德。",
 "摘要没有给出具体的技法，只说明他的风格与体裁变化很大，这使他在整个欧洲享有空前的声誉。",
 "摘要称他属于佛兰德斯—法国乐派并代表其成熟阶段；这一乐派的概况可参见若斯坎条目。“空前的声誉”是摘要的说法，本条目不作独立判断。",
 "示意图以拉索为中心，标示佛兰德斯—法国乐派成熟复调、极为多产、与伯德帕莱斯特里纳维多利亚并列三项。",
 "（2）"+YR("1532—1594年")+"（3）具体作品，摘要未给出；（4）Wikipedia 页面标题为 Orlando di Lasso，Wikidata 标签为 Orlande de Lassus，是同一人的不同拼写，库内取 Lassus 作 id。"),
 {"nodes":[{"label":"佛兰德斯—法国乐派","sub":"成熟复调","kind":"muted"},{"label":"拉索","sub":"文艺复兴晚期","kind":"accent"},{"label":"极为多产","sub":"风格体裁多变","kind":"muted"},{"label":"伯德帕莱斯特里纳","sub":"并列","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-lassus","enc-c178-franco-flemish-school","wd-lassus"],"来源独立性有限（Wikipedia+Wikidata）；年代来自 Wikidata；作品未给出。")

W("gesualdo",S(
 "摘要称，杰苏阿尔多是意大利贵族与作曲家，同时是韦诺萨亲王与孔扎伯爵。相邻的牧歌页称，牧歌是文艺复兴与巴洛克早期（1580—1650）最典型的世俗声乐体裁。",
 "摘要称，他以写作牧歌与宗教音乐更为人知，所用的半音化语言直到19世纪晚期才再次出现。",
 NOWORK+"相关条目可参见牧歌与蒙特威尔第，但摘要没有把他们联系起来。",
 "摘要只说明他的语言是“半音化”的，没有给出具体的和声手法，本条目不补写。",
 "摘要称，他的半音化语言“直到19世纪晚期才再次出现”，这是摘要的概括，本条目不作独立判断。摘要另称，他因发现第一任妻子与其贵族情人通奸而将二人杀害，这是摘要陈述的生平事实，本条目只如实带过，不作渲染，也不据此评价其音乐。",
 "示意图以杰苏阿尔多为中心，标示牧歌、宗教音乐、半音化语言三项。",
 "（2）"+YR("1566—1613年")+"（3）具体作品，摘要未给出；（4）“半音化语言直到19世纪晚期才再次出现”与杀妻一事均来自摘要单一来源，需另取权威来源核实。"),
 {"nodes":[{"label":"牧歌","sub":"世俗声乐","kind":"muted"},{"label":"杰苏阿尔多","sub":"意大利贵族","kind":"accent"},{"label":"宗教音乐","sub":"也写作","kind":"muted"},{"label":"半音化语言","sub":"19世纪晚期再现","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":2,"to":1},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-gesualdo","enc-c178-madrigal","wd-gesualdo"],"来源独立性有限（Wikipedia+Wikidata）；年代来自 Wikidata；作品未给出；杀妻一事单一来源。")

W("machaut",S(
 "摘要称，马肖是中世纪晚期新艺术风格的核心人物。相邻的新艺术页称，新艺术指从《法韦尔传奇》准备期（1310年代）到马肖去世之间的时期。",
 "摘要没有给出具体的风格特征，只说明他在该体裁中的统治地位。",
 NOWORK+"摘要称他是法国作曲家与诗人，被视为14世纪最重要的法国作曲家与诗人，常被看作该世纪欧洲首屈一指的作曲家。",
 "摘要没有给出具体的技法或形式，本条目不补写。",
 "摘要称，他的统治地位如此突出，以致现代音乐学家用他的逝世来划分新艺术与随后的精微新艺术运动。库内相关条目可参见中世纪音乐与复调。“首屈一指”是摘要转述的评价。",
 "示意图以马肖为中心，标示新艺术、精微新艺术、作曲家与诗人三项。",
 "（2）"+YR("约1300—1377年")+"（3）具体作品，摘要未给出；（4）“14世纪首屈一指”属评价性表述。"),
 {"nodes":[{"label":"新艺术","sub":"中世纪晚期","kind":"muted"},{"label":"马肖","sub":"核心人物","kind":"accent"},{"label":"逝世为界","sub":"音乐学家划分","kind":"muted"},{"label":"精微新艺术","sub":"随后运动","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":2,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-machaut","enc-c178-ars-nova","wd-machaut"],"来源独立性有限（Wikipedia+Wikidata）；年代来自 Wikidata；作品未给出。")

W("leonin",S(
 "摘要称，莱奥南大概在巴黎圣母院生活与工作；相邻的圣母院乐派页称，该乐派指约1160至1250年在巴黎圣母院或其附近工作的作曲家群体及其音乐。",
 "摘要称，他是已知第一位重要的复调奥尔加农作曲家。",
 NOWORK+"摘要称，他是以姓名为人所知的最早的圣母院复调乐派与古艺术风格成员，这要归功于被称为“匿名者四世”的作者。库内相关条目可参见奥尔加农与复调。",
 "摘要没有给出具体的技法，只说明他写的是复调奥尔加农。可对照奥尔加农条目，但该条摘要没有提到他。",
 "摘要对他的身份十分谨慎：“大概是法国人”“大概在巴黎圣母院”，并说明除名字外别无确定的身份信息。他的名字是“Leoninus”及其拉丁指小形式“Leo”的法语对应。本条目照此保留不确定性。",
 "示意图以莱奥南为中心，标示复调奥尔加农、巴黎圣母院、匿名者四世三项。",
 "（2）生卒年，摘要未给出；Wikidata 简介只写“12世纪”，条目 when 写“约公元12世纪”，圣母院乐派页的约1160—1250年可作旁证，需另取来源核实；（3）具体作品，摘要未给出；（4）身份与地点均为“大概”，本条目不作确定表述。"),
 {"nodes":[{"label":"匿名者四世","sub":"记述者","kind":"muted"},{"label":"莱奥南","sub":"圣母院乐派","kind":"accent"},{"label":"复调奥尔加农","sub":"第一位重要作曲家","kind":"muted"},{"label":"巴黎圣母院","sub":"大概在此","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-leonin","enc-c178-notre-dame-school","wd-leonin"],"来源独立性有限（Wikipedia+Wikidata）；年代为Wikidata简介与相邻页旁证；作品未给出。")
