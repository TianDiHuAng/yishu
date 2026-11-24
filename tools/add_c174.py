# -*- coding: utf-8 -*-
"""Cycle174：联网恢复后补建筑类 6 条（Wikipedia REST 摘要 + 相邻页 + Wikidata；取回日期 2026-11-24）。"""
import io,json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
WP="https://en.wikipedia.org/wiki/"
NOTE="2026-11-24 经 Wikipedia REST summary 接口取回，HTTP 200，页面标题与摘要匹配；摘要缓存于 data/_cache/wp"
WDN="2026-11-24 经 wd_api 读取实体成功，英文标签与条目一致"
# (id, 页面标题, 显示名, 相邻页, 相邻显示名, QID, wd标签)
A=[
 ("renaissance-architecture","Renaissance_architecture","Renaissance architecture","Classical_architecture","Classical architecture","Q236122"),
 ("baroque-architecture","Baroque_architecture","Baroque architecture","Baroque","Baroque","Q840829"),
 ("neoclassical-architecture","Neoclassical_architecture","Neoclassical architecture","Neoclassicism","Neoclassicism","Q54111"),
 ("byzantine-architecture","Byzantine_architecture","Byzantine architecture","Byzantine_Empire","Byzantine Empire","Q47591"),
 ("chinese-architecture","Chinese_architecture","Chinese architecture","Chinese_art","Chinese art","Q957904"),
 ("islamic-architecture","Islamic_architecture","Islamic architecture","Islamic_art","Islamic art","Q212940"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
def add(s):
    if s["id"] not in have: sd["sources"].append(s); have.add(s["id"])
for eid,pg,pn,pg2,pn2,q in A:
    add({"id":"enc-"+eid,"title":pn,"author":"Wikipedia contributors","year":"2026","url":WP+pg,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"enc-c174-"+pg2.lower().replace("_","-"),"title":pn2,"author":"Wikipedia contributors","year":"2026","url":WP+pg2,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"wd-"+eid,"title":"Wikidata: %s (%s)"%(pn,q),"author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026","url":"https://www.wikidata.org/wiki/"+q,"type":"权威结构化数据","verified":True,"verified_note":WDN})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
def S(eid,pg2): return "enc-%s,enc-c174-%s,wd-%s"%(eid,pg2.lower().replace("_","-"),eid)
T=[
 ('renaissance-architecture','文艺复兴建筑（Renaissance architecture）','风格','art-renaissance','15世纪初—16世纪初','欧洲','建筑','重要',
  '约15世纪初至16世纪初欧洲的建筑风格，有意复兴并发展古希腊罗马的思想与物质文化元素。','15世纪初—16世纪初',
  '文艺复兴建筑指约15世纪初到16世纪初欧洲各地区的建筑，自觉复兴并发展古希腊、古罗马思想与物质文化的某些元素；风格上承接哥特建筑，后被巴洛克建筑与新古典主义建筑接替。',
  'renaissance,gothic-architecture,baroque-architecture',S('renaissance-architecture','Classical_architecture')),
 ('baroque-architecture','巴洛克建筑（Baroque architecture）','风格','art-baroque','16世纪末—18世纪中叶','欧洲','建筑','重要',
  '16世纪末起源于意大利的高度装饰性、戏剧化的建筑风格，后传遍欧洲。','16世纪末—18世纪中叶',
  '巴洛克建筑是16世纪末出现于意大利的高度装饰性、戏剧化的风格，后逐渐传遍欧洲。它最初由天主教会尤其是耶稣会引入，用以对抗宗教改革。盛期巴洛克（1625—1675）见于意、西、葡、法、巴伐利亚与奥地利的教堂和宫殿，晚期（1675—1750）远及俄国、奥斯曼帝国与拉美殖民地；约1730年更繁复的变体洛可可在中欧兴起。',
  'baroque,rococo,renaissance-architecture',S('baroque-architecture','Baroque')),
 ('neoclassical-architecture','新古典主义建筑（Neoclassical architecture）','风格','art-neo-romantic','18世纪中叶—19世纪','欧洲','建筑','重要',
  '18世纪中叶起于意、法、德的古典复兴建筑风格，意在剥去晚期巴洛克的过度装饰。','18世纪中叶起',
  '新古典主义建筑又称古典复兴建筑，由始于18世纪中叶意大利、法国与德国的新古典主义运动产生，成为西方最突出的建筑风格之一。此前欧洲大部分地区两个世纪的主流风格是文艺复兴与巴洛克建筑，二者已是对古罗马古典建筑的部分复兴；新古典主义则意在剥去晚期巴洛克的过度装饰，回到更纯粹、更完整、更正统的古典风格，并使之适应现代用途。',
  'neoclassicism,baroque-architecture,renaissance-architecture',S('neoclassical-architecture','Neoclassicism')),
 ('byzantine-architecture','拜占庭建筑（Byzantine architecture）','风格','art-medieval','公元330—1453年','东罗马','建筑','重要',
  '拜占庭帝国的建筑，通常从公元330年君士坦丁建新都起算，至1453年帝国灭亡。','公元330—1453年',
  '拜占庭帝国的建筑通常从公元330年君士坦丁大帝在拜占庭建立新的罗马首都（后称君士坦丁堡）起算，直到1453年帝国灭亡。起初拜占庭与罗马帝国之间并无明确界线，早期拜占庭建筑在风格与结构上与晚期罗马建筑难以区分。其风格继续以拱、拱顶和穹顶为基础，常为大尺度；金底墙面镶嵌画成为最宏伟建筑的标准装饰，湿壁画则是较廉价的替代。',
  'byzantine-art,fresco,romanesque-architecture',S('byzantine-architecture','Byzantine_Empire')),
 ('chinese-architecture','中国建筑（Chinese architecture）','风格','art-china-painting','历代','中国','建筑','重要',
  '在中国历经千年发展的建筑风格体系，对整个东亚建筑产生影响。','历代',
  '中国建筑是在中国历经千年发展而成的建筑风格，并影响了整个东亚的建筑。自早期古代出现以来，其结构原则大体不变，主要变化在于多样的装饰细节。自唐代起，中国建筑对日本、朝鲜、越南、蒙古等邻近东亚国家的建筑风格产生重大影响，对东南亚与南亚部分国家也有较小影响。',
  'angkor,khmer-architecture,china-painting-history',S('chinese-architecture','Chinese_art')),
 ('islamic-architecture','伊斯兰建筑（Islamic architecture）','风格','art-islamic','7世纪至今','西亚·中亚','建筑','重要',
  '与伊斯兰文明相关的建筑风格，涵盖世俗与宗教建筑，从伊斯兰早期历史延续至今。','7世纪至今',
  '伊斯兰建筑包括与伊斯兰文明相关的建筑风格，涵盖从伊斯兰早期历史到今天的世俗与宗教建筑。伊斯兰世界地域广阔，历史上西起西非与欧洲、东至东亚。各地区的伊斯兰建筑风格有共通之处，但随时间推移，因本地材料与技术、地方王朝与赞助人、不同的艺术生产中心，有时还因宗教派别不同，形成各自的风格。',
  'islamic-art,mihrab-isfahan,iznik-tile-spandrel',S('islamic-architecture','Islamic_art')),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
