# -*- coding: utf-8 -*-
"""Cycle182 overlay：建筑类 4 条（只转述 Wikipedia 摘要，不补写）。"""
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
NOSRC="本条目事实仅来自 Wikipedia 摘要（2026-11-24 取回）及同源的 Wikidata 标签，来源独立性有限，整条标记待核实。"
NOWHO="摘要没有列举建筑师与具体建筑，本条目不补写；需另取专著或博物馆来源后再增补。"
def S(era,feat,who,tech,rel,pic,todo):
    return {"时代背景":era,"风格特征":feat,"代表人物与作品":who,"技法或形式分析":tech,"与前后风格的关系和争论":rel,"一图":pic,"待核实":"（1）"+NOSRC+todo}

W("korean-architecture",S(
 "摘要称，韩国建筑是在朝鲜半岛历经数世纪发展起来的建筑风格。摘要没有给出起讫年代，本条目不限定。",
 "摘要称，传统韩国建筑大多可凭倾斜的屋顶辨认。",
 NOWHO+"库内相关条目可参见高丽青瓷，但摘要没有提到。",
 "摘要对形式的描述只有一项：倾斜的屋顶。本条目不补写其他构造做法。",
 "摘要称，朝鲜半岛历史上各个王国与王朝发展出独特的建筑风格，受佛教与韩国儒家影响。摘要没有谈到它与中国、日本建筑的关系，库内互链是本项目所加，本条目不作比较。",
 "示意图以韩国建筑为中心，标示佛教影响、韩国儒家影响、倾斜屋顶三项。",
 "（2）本条目内容很薄，因为所依摘要只有两句，本条目没有为凑篇幅而补写；（3）各王国与王朝的建筑差异、具体建筑，摘要未给出；（4）“独特的风格”是摘要的概括，本条目未核验。"),
 {"nodes":[{"label":"佛教","sub":"影响","kind":"muted"},{"label":"韩国建筑","sub":"数世纪发展","kind":"accent"},{"label":"韩国儒家","sub":"影响","kind":"muted"},{"label":"倾斜的屋顶","sub":"最易辨认","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":2,"to":1},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-korean-architecture","enc-c182-korean-art","wd-korean-architecture"],"来源独立性有限（Wikipedia+Wikidata）；内容薄，摘要仅两句。")

W("spanish-architecture",S(
 "摘要称，西班牙建筑包括西班牙成为国家之前、该地被称为伊比利亚、希斯帕尼亚（Hispania），或被若干基督教与穆斯林王国瓜分时期，建于今国界之内的建筑。",
 "摘要称，西班牙建筑依历史时期而呈现出很大的历史与地域多样性。",
 NOWHO+"相关条目可参见伊斯兰建筑、巴洛克建筑与哥特式建筑，但摘要没有把它们联系起来，库内互链是本项目所加。",
 "摘要没有给出具体的形式要素，本条目不补写。",
 "摘要称，它沿着与地中海周边以及中欧、北欧其他建筑风格相似的路线发展，但也有一些西班牙建筑是独一无二的。摘要对“独一无二”没有举例。",
 "示意图以西班牙建筑为中心，标示今西班牙境内、西班牙建筑师在世界各地、历史与地域多样性三项。",
 "（2）摘要把范围界定得很宽：既包括今西班牙境内，也包括西班牙建筑师在世界各地的建筑，主要影响曾属西班牙帝国的地区，本条目照录，不作收窄；（3）各历史时期的风格与具体建筑，摘要未给出；（4）本条目挂在“巴洛克”单元只是权宜，因库内没有欧洲建筑通史单元，并不表示它属于巴洛克时期。"),
 {"nodes":[{"label":"今西班牙境内","sub":"含建国前","kind":"muted"},{"label":"西班牙建筑","sub":"历史地域多样","kind":"accent"},{"label":"世界各地","sub":"西班牙建筑师","kind":"muted"},{"label":"曾属帝国地区","sub":"主要影响","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":2,"to":1},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-spanish-architecture","enc-c182-spanish-art","wd-spanish-architecture"],"来源独立性有限（Wikipedia+Wikidata）；各时期风格与名作未给出；单元归属为权宜。")

W("dutch-architecture",S(
 "摘要称，荷兰建筑指今荷兰领土内的建筑史，从中世纪到今天；因此不含常被纳入更宽泛的“低地国家”概念的比利时。",
 "摘要称，由于领土上石材极少，荷兰在建造中用石一向有限，转向以砖为主的建筑，砖甚至被用来铺路。",
 NOWHO+"相关条目可参见巴洛克、伦勃朗与维米尔，但摘要没有提到他们，库内互链是本项目所加。",
 "摘要给出的形式信息只有材料：以砖为主、石材有限。本条目不补写具体的砖构做法或建筑类型。",
 "摘要称，直到19世纪，荷兰与佛兰德斯的建筑有显著相似，因为二者直到文艺复兴都有共同文化；但17世纪以来，新教的、商业的、田园的、自由的荷兰，与长期受外国统治的天主教的、勤勉的佛兰德斯并不相像。摘要另称，荷兰建筑的独特性格长期被否认，而中世纪至今的丰富创造证明并非如此。以上都是摘要的叙述，本条目不作独立判断。",
 "示意图以荷兰建筑为中心，标示与佛兰德斯的共同文化、石材稀缺、以砖为主三项。",
 "（2）“新教的、商业的、田园的、自由的”与“天主教的、勤勉的”是摘要的概括性对照，带有评价色彩，本条目未核验；（3）具体建筑与建筑师，摘要未给出；（4）本条目挂在“巴洛克”单元只是权宜，因库内没有欧洲建筑通史单元；（5）摘要未给出起讫年代，when 写“历代”。"),
 {"nodes":[{"label":"石材稀缺","sub":"领土上极少","kind":"muted"},{"label":"荷兰建筑","sub":"以砖为主","kind":"accent"},{"label":"佛兰德斯","sub":"文艺复兴前共同文化","kind":"muted"},{"label":"17世纪后分野","sub":"新教与天主教","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":2,"to":1},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-dutch-architecture","enc-c182-dutch-art","wd-dutch-architecture"],"来源独立性有限（Wikipedia+Wikidata）；名作与建筑师未给出；单元归属为权宜。")

W("gothic-revival-architecture",S(
 "摘要称，哥特复兴自17世纪下半叶起逐渐积累，到19世纪上半叶成为广泛的运动，主要在英国；19世纪中叶已成为西方世界最突出的建筑风格，随后在1880年代与1890年代初开始过时。",
 "摘要称，哥特复兴借用中世纪实例的特征，包括装饰图案、尖顶饰、尖券窗与滴水石。",
 NOWHO+"相关条目可参见哥特式建筑、新古典主义建筑与浪漫主义。",
 "摘要列出的借用特征共四项：装饰图案、尖顶饰、尖券窗、滴水石。摘要没有给出结构上的借用。",
 "摘要称，越来越严肃、博学的崇拜者试图复兴中世纪的哥特建筑，意在补充甚至取代当时盛行的新古典风格。可知它与新古典主义建筑形成对照，但摘要没有进一步展开两者的论争。“最突出”是摘要的叙述，本条目不作独立判断。",
 "示意图以哥特复兴建筑为中心，标示中世纪哥特建筑、新古典风格、19世纪中叶最突出三项。",
 "（2）摘要说它“主要在英国”，但又称其成为“西方世界”最突出的风格，二者的范围差异，摘要没有解释；（3）具体建筑与建筑师，摘要未给出；（4）“1880年代与1890年代初开始过时”是摘要的说法，when 写“约公元17世纪下半叶—19世纪末”是对该年代的概括。"),
 {"nodes":[{"label":"中世纪哥特建筑","sub":"被复兴","kind":"muted"},{"label":"哥特复兴","sub":"19世纪上半叶盛行","kind":"accent"},{"label":"新古典风格","sub":"意在补充或取代","kind":"muted"},{"label":"1880年代式微","sub":"开始过时","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-gothic-revival-architecture","enc-c182-gothic-architecture","wd-gothic-revival-architecture"],"来源独立性有限（Wikipedia+Wikidata）；名作与建筑师未给出。")
