# -*- coding: utf-8 -*-
"""Cycle176：建筑类 6 条（Wikipedia 摘要+相邻页+Wikidata；取回日期 2026-11-24）。"""
import io,json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
WP="https://en.wikipedia.org/wiki/"
NOTE="2026-11-24 经 Wikipedia REST summary 接口取回，HTTP 200，页面标题与摘要匹配；摘要缓存于 data/_cache/wp"
WDN="2026-11-24 经 wd_api 读取实体成功，英文标签与条目一致"
WDN_MUGHAL="2026-11-24 经 wd_api 读取实体成功；英文标签与简介为 Mughal architecture，但中文标签错位为“潘契瑪哈勒（法泰赫普爾西克里）”，本项目只采英文标签"
A=[
 ("mughal-architecture","Mughal_architecture","Mughal architecture","Mughal_Empire","Mughal Empire","Q542261"),
 ("japanese-architecture","Japanese_architecture","Japanese architecture","Japanese_art","Japanese art","Q1422874"),
 ("indian-architecture","Indian_architecture","Architecture of India","Indian_art","Indian art","Q61050"),
 ("art-deco","Art_Deco","Art Deco","Modernism","Modernism","Q173782"),
 ("modern-architecture","Modern_architecture","Modern architecture","Modernism","Modernism","Q245188"),
 ("beaux-arts-architecture","Beaux-Arts_architecture","Beaux-Arts architecture","Eclecticism_in_architecture","Eclecticism in architecture","Q1268134"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
def add(s):
    if s["id"] not in have: sd["sources"].append(s); have.add(s["id"])
for eid,pg,pn,pg2,pn2,q in A:
    add({"id":"enc-"+eid,"title":pn,"author":"Wikipedia contributors","year":"2026","url":WP+pg,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"enc-c176-"+pg2.lower().replace("_","-"),"title":pn2,"author":"Wikipedia contributors","year":"2026","url":WP+pg2,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"wd-"+eid,"title":"Wikidata: %s (%s)"%(pn,q),"author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026","url":"https://www.wikidata.org/wiki/"+q,"type":"权威结构化数据","verified":True,"verified_note":WDN_MUGHAL if eid=="mughal-architecture" else WDN})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
def S(eid,pg2): return "enc-%s,enc-c176-%s,wd-%s"%(eid,pg2.lower().replace("_","-"),eid)
T=[
 ('mughal-architecture','莫卧儿建筑（Mughal architecture）','风格','art-asia','16—18世纪','南亚','建筑','重要',
  '16—18世纪在莫卧儿帝国发展起来的建筑风格，分布于南亚，主要在今印度、巴基斯坦、孟加拉国与阿富汗。','约公元16—18世纪',
  '莫卧儿建筑是16至18世纪在莫卧儿帝国发展的建筑风格，覆盖其不断变化的南亚疆域。它源自较早的印度—伊斯兰建筑，以及伊朗与中亚的建筑传统，尤其是帖木儿建筑；在阿克巴统治时期还进一步吸收并融合了更广泛的印度建筑的影响。莫卧儿建筑有统一的结构与特征：大型球根状穹顶、转角处的细长宣礼塔、巨大的厅堂、高大的拱顶门道与精致的装饰。实例主要见于今印度、巴基斯坦、孟加拉国与阿富汗。',
  'islamic-architecture,indian-art,mughal-alamgir-portrait',S('mughal-architecture','Mughal_Empire')),
 ('japanese-architecture','日本建筑（Japanese architecture）','风格','art-asia','历代','东亚','建筑','重要',
  '以木结构、略离地面抬高、瓦顶或茅草顶为典型特征的日本建筑，19世纪以来大量吸收西方、现代与后现代建筑。','历代',
  '日本建筑的典型特征是木结构、略微离地抬高、覆以瓦顶或茅草顶。传统上用拉门（隔扇）等隔断代替墙，使室内布局可随场合调整；人们通常坐在垫子上或直接坐在地上，椅子与高桌直到20世纪才广泛使用。但自19世纪以来，日本吸收了大量西方、现代与后现代建筑，如今是前沿建筑设计与技术的领先者。',
  'japanese-art,chinese-architecture,ukiyo-e',S('japanese-architecture','Japanese_art')),
 ('indian-architecture','印度建筑（Architecture of India）','风格','art-asia','历代','南亚','建筑','重要',
  '植根于印度历史、文化与宗教的建筑，包含印度教、耆那教、佛教、锡克教等风格，以及印度—伊斯兰、拉其普特、莫卧儿、南印度、印度—萨拉森等风格。','历代',
  '印度建筑植根于印度的历史、文化与宗教。在多种建筑风格与传统中，最广为人知的是依印度宗教与哲学建造的印度教、耆那教、佛教、锡克教风格，其中最普遍；印度—伊斯兰、拉其普特、莫卧儿、南印度与印度—萨拉森建筑也有突出的存在。',
  'indian-art,mughal-architecture,buddhist-art-india',S('indian-architecture','Indian_art')),
 ('art-deco','装饰艺术（Art Deco）','风格','art-modern','1910年代—1930年代初','欧洲·美洲','综合','重要',
  '1910年代一战前夕出现于巴黎、1920年代至1930年代初在国际上盛行的视觉艺术、建筑与产品设计风格。','约公元1910年代—1930年代初',
  '装饰艺术（Art Deco）是法语“装饰艺术”的简称，是一种视觉艺术、建筑与产品设计风格，1910年代第一次世界大战前夕出现于巴黎，在1920年代至1930年代初于国际上盛行，通过对从大型建筑到服装、时装、珠宝等小物件的外观与内部设计来体现。它影响了从摩天楼、电影院、桥梁，到远洋客轮、火车、汽车、卡车、公共汽车、家具与收音机、吸尘器等日常用品。',
  'bauhaus,modern-art,modern-architecture',S('art-deco','Modernism')),
 ('modern-architecture','现代建筑（Modern architecture）','风格','art-modern','20世纪','全球','建筑','重要',
  '20世纪突出的建筑运动与风格，介于更早的装饰艺术与后来的后现代之间，以新技术、功能主义、极简与拒绝装饰为基础。','约公元20世纪',
  '现代建筑又称现代主义建筑或现代运动，是20世纪突出的建筑运动与风格，介于更早的装饰艺术与后来的后现代运动之间。它以新颖的施工技术、功能主义原则、对极简的接纳，以及对装饰的拒斥为基础。',
  'bauhaus,art-deco,modern-art',S('modern-architecture','Modernism')),
 ('beaux-arts-architecture','学院派建筑（Beaux-Arts architecture）','风格','art-modern','19世纪30年代—19世纪末','欧洲·美洲','建筑','重要',
  '巴黎美术学院传授的学院派建筑风格，尤其盛行于1830年代至19世纪末，影响及于20世纪的欧美公共建筑。','约公元1830年代—1900年',
  '学院派建筑（Beaux-Arts）是巴黎美术学院传授的学院派建筑风格，尤其盛行于19世纪30年代至19世纪末。它以法国新古典主义的原则为基础，也吸收文艺复兴与巴洛克元素，并使用铁、玻璃以及后来的钢等现代材料。这一风格直到19世纪末乃至进入20世纪，对欧洲与美洲影响巨大，尤其用于机构与公共建筑。',
  'neoclassicism,baroque-architecture,renaissance-architecture',S('beaux-arts-architecture','Eclecticism_in_architecture')),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
