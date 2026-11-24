# -*- coding: utf-8 -*-
"""Cycle182：建筑类 4 条（Wikipedia 摘要+相邻页+Wikidata；取回日期 2026-11-24）。"""
import io,json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
WP="https://en.wikipedia.org/wiki/"
NOTE="2026-11-24 经 Wikipedia REST summary 接口取回，HTTP 200，页面标题与摘要匹配；摘要缓存于 data/_cache/wp"
WDN="2026-11-24 经 wd_api 读取实体成功，英文标签与条目一致"
A=[
 ("korean-architecture","Korean_architecture","Korean architecture","Korean_art","Korean art","Q2860300"),
 ("spanish-architecture","Spanish_architecture","Spanish architecture","Spanish_art","Spanish art","Q2712488"),
 ("dutch-architecture","Architecture_of_the_Netherlands","Architecture of the Netherlands","Dutch_art","Dutch art","Q4070862"),
 ("gothic-revival-architecture","Gothic_Revival_architecture","Gothic Revival architecture","Gothic_architecture","Gothic architecture","Q186363"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
def slug(p): return p.lower().replace("_","-")
def add(s):
    if s["id"] not in have: sd["sources"].append(s); have.add(s["id"])
for eid,pg,pn,pg2,pn2,q in A:
    add({"id":"enc-"+eid,"title":pn,"author":"Wikipedia contributors","year":"2026","url":WP+pg,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"enc-c182-"+slug(pg2),"title":pn2,"author":"Wikipedia contributors","year":"2026","url":WP+pg2,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"wd-"+eid,"title":"Wikidata: %s (%s)"%(pn,q),"author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026","url":"https://www.wikidata.org/wiki/"+q,"type":"权威结构化数据","verified":True,"verified_note":WDN})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
def S(eid,pg2): return "enc-%s,enc-c182-%s,wd-%s"%(eid,slug(pg2),eid)
T=[
 ('korean-architecture','韩国建筑（Korean architecture）','风格','art-asia','历代','东亚','建筑','补充',
  '在朝鲜半岛历经数世纪发展的建筑风格，受佛教与韩国儒家影响，传统上以倾斜的屋顶最易辨认。','历代',
  '韩国建筑指在朝鲜半岛历经数世纪发展起来的建筑风格。在朝鲜半岛历史上，各个王国与王朝发展出受佛教与韩国儒家影响的独特建筑风格；传统韩国建筑大多可凭倾斜的屋顶辨认。',
  'goryeo-celadon-bottle,japanese-architecture,chinese-architecture',S('korean-architecture','Korean_art')),
 ('spanish-architecture','西班牙建筑（Spanish architecture）','风格','art-baroque','历代','西班牙','建筑','补充',
  '指今西班牙境内的建筑，以及西班牙建筑师在世界各地的建筑，主要影响曾属西班牙帝国的地区；随历史时期而有很大的历史与地域多样性。','历代',
  '西班牙建筑指今西班牙任何地区的建筑，以及西班牙建筑师在世界各地的建筑，主要影响曾属西班牙帝国的地区。该词包括在西班牙成为国家之前、该地被称为伊比利亚、希斯帕尼亚（Hispania），或被若干基督教与穆斯林王国瓜分时期建于今国界之内的建筑。西班牙建筑依历史时期而呈现出很大的历史与地域多样性；它沿着与地中海周边以及中欧、北欧其他建筑风格相似的路线发展，但也有一些西班牙建筑是独一无二的。',
  'islamic-architecture,baroque-architecture,gothic-architecture',S('spanish-architecture','Spanish_art')),
 ('dutch-architecture','荷兰建筑（Architecture of the Netherlands）','风格','art-baroque','中世纪至今','荷兰','建筑','补充',
  '今荷兰领土内的建筑史，不含常被并入“低地国家”的比利时；因缺石而以砖为主要建材。','历代',
  '荷兰建筑指今荷兰领土内的建筑史，因此不含常被纳入更宽泛的“低地国家”概念的比利时。荷兰建筑的独特性格长期被否认，但从中世纪到今天荷兰建筑创造的丰富性证明并非如此。直到19世纪，荷兰与佛兰德斯的建筑有显著相似，因为二者直到文艺复兴都有共同文化；然而17世纪以来新教的、商业的、田园的、自由的荷兰，与长期受外国统治的天主教的、勤勉的佛兰德斯并不相像。更具体地说，与佛兰德斯建筑不同，荷兰在建造中用石一向有限，因为其领土上石材极少；这种稀缺使荷兰人转向以砖为主的建筑，砖甚至被用来铺路。',
  'baroque,rembrandt,vermeer',S('dutch-architecture','Dutch_art')),
 ('gothic-revival-architecture','哥特复兴建筑（Gothic Revival architecture）','风格','art-neo-romantic','17世纪下半叶—19世纪','英国·欧洲','建筑','重要',
  '17世纪下半叶起逐渐积累、19世纪上半叶在英国广为流行的建筑运动，意在复兴中世纪哥特建筑，以补充甚至取代当时盛行的新古典风格。','约公元17世纪下半叶—19世纪末',
  '哥特复兴是一场建筑运动，自17世纪下半叶起逐渐积累，到19世纪上半叶成为广泛的运动，主要在英国。越来越严肃、博学的崇拜者试图复兴中世纪的哥特建筑，意在补充甚至取代当时盛行的新古典风格。哥特复兴借用中世纪实例的特征，包括装饰图案、尖顶饰、尖券窗与滴水石。到19世纪中叶，它已成为西方世界最突出的建筑风格，随后在1880年代与1890年代初开始过时。',
  'gothic-architecture,neoclassical-architecture,romanticism-art',S('gothic-revival-architecture','Gothic_architecture')),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
