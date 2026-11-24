# -*- coding: utf-8 -*-
"""Cycle160：文艺复兴 4 条（安德烈亚·德尔·萨托 / 韦罗内塞 / 荷尔拜因 / 丢勒）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1937-577","Cleveland Museum of Art — Andrea del Sarto, The Sacrifice of Isaac, c. 1527, acc. 1937.577",
  "https://openaccess-api.clevelandart.org/api/artworks/1937.577","2026-11-24 API HTTP 200；木板油画 画心178×138cm；说明含未完成状态与制作方法、人物表情与古代雕塑和米开朗基罗的启发"),
 ("cma-1928-16","Cleveland Museum of Art — Paolo Veronese, Portrait of Agostino Barbarigo, after c. 1571, acc. 1928.16",
  "https://openaccess-api.clevelandart.org/api/artworks/1928.16","2026-11-24 API HTTP 200；布面油画 画心102.2×104.2cm；年代标注为after c. 1571；说明含勒班陀海战与手持箭矢、威尼斯军事肖像惯例"),
 ("cma-1971-166","Cleveland Museum of Art — Hans Holbein the Younger, Terminus, the Device of Erasmus, c. 1532, acc. 1971.166",
  "https://openaccess-api.clevelandart.org/api/artworks/1971.166","2026-11-24 API HTTP 200；木板油画 画心21.6×21.6cm；题款CONCEDO NVLLI与TERMINVS；说明含伊拉斯谟与界神忒耳弥努斯的合并"),
 ("cma-1926-211","Cleveland Museum of Art — Albrecht Durer, Melencolia I, 1514, acc. 1926.211",
  "https://openaccess-api.clevelandart.org/api/artworks/1926.211","2026-11-24 API HTTP 200；铜版雕刻 版痕23.8×18.9cm；说明含忧郁的拟人化形象、幻方总和34等象征物与光线表现"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('andrea-sacrifice-of-isaac','安德烈亚·德尔·萨托《以撒的献祭》（约1527）','作品','art-renaissance','16世纪','意大利·佛罗伦萨','油画','重要',
  '安德烈亚·德尔·萨托未完成的木板油画，克利夫兰艺术博物馆藏（1937.577）。','约1527年',
  '该馆说明：画面取自《创世记》，亚伯拉罕奉神命要杀死儿子以撒，举刀之际天使出现制止；作品的力量来自父子复杂的表情，合并悲痛、力量、顺从、恐惧与领悟，身体姿态受古代雕塑与米开朗基罗启发；此画未完成，因而显露他的工作方法：先把草图转到木板上，用绘出的线条加强粉笔线，再对整块木板罩上薄而带笔触的色彩薄层，使他可在作画时改动构图。',
  'high-renaissance,michelangelo','cma-1937-577'),
 ('veronese-barbarigo-portrait','韦罗内塞《阿戈斯蒂诺·巴巴里戈肖像》（1571年后）','作品','art-renaissance','16世纪','意大利·威尼斯','油画','重要',
  '韦罗内塞名下的威尼斯军事肖像，克利夫兰艺术博物馆藏（1928.16），年代标注为1571年后。','1571年后',
  '该馆说明：巴巴里戈是1571年10月7日勒班陀海战中威尼斯海军的副指挥，对抗奥斯曼帝国，战斗中被土耳其箭射死，肖像中他手持这支箭；16世纪威尼斯的军事肖像常让坐像者身着盔甲，姿势类似罗马皇帝，以与古代军队的勇武相联系；该馆记录的年代为after c. 1571，作者署为韦罗内塞。',
  'venetian-school,high-renaissance','cma-1928-16'),
 ('holbein-terminus-erasmus','荷尔拜因《伊拉斯谟的标记：界神忒耳弥努斯》（约1532）','作品','art-renaissance','16世纪','德国·英国·瑞士','油画','重要',
  '小荷尔拜因的小幅木板油画，克利夫兰艺术博物馆藏（1971.166）。','约1532年',
  '该馆说明：荷兰人文主义者伊拉斯谟（约1466—1536）承袭意大利文艺复兴精神，拥抱古希腊罗马文学并把其道德伦理信息纳入自己的著作；荷尔拜因在此把伊拉斯谟的面容与罗马界神忒耳弥努斯合并，后者曾违抗朱庇特而守住卡比托利欧山顶的位置；伊拉斯谟采用忒耳弥努斯与箴言concedo nulli（我不让于任何人）作为个人标记，象征虔诚与坚定；画上有题款CONCEDO NVLLI与TERMINVS。',
  'northern-renaissance,renaissance','cma-1971-166'),
 ('durer-melencolia-i','丢勒《忧郁 I》（1514）','作品','art-renaissance','16世纪','德国','版画','核心',
  '丢勒的铜版雕刻名作，克利夫兰艺术博物馆藏（1926.211）。','1514年',
  '该馆说明：这是丢勒雕版作品中的巅峰之作；忧郁或悲伤被视为与内省而富创造力的头脑相关，丢勒把它拟人化为一个不能动弹的有翼形象，无法使用散落四周的工具；总和各方向皆为34的幻方、消瘦的狗、沙漏与梯子，唤起时间、秩序、苦难、生与死；作品同时显示丢勒捕捉视觉感知的功力，光在透明沙漏、迸发的彗星、彩虹与几何石体上的表现各不相同。',
  'northern-renaissance,renaissance','cma-1926-211'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")
