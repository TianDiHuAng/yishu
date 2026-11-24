# -*- coding: utf-8 -*-
"""Cycle175：音乐类 6 条（Wikipedia 摘要+相邻页+Wikidata；取回日期 2026-11-24）。"""
import io,json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
WP="https://en.wikipedia.org/wiki/"
NOTE="2026-11-24 经 Wikipedia REST summary 接口取回，HTTP 200，页面标题与摘要匹配；摘要缓存于 data/_cache/wp"
WDN="2026-11-24 经 wd_api 读取实体成功，英文标签与条目一致"
# (id, 页面, 显示名, 相邻页, 相邻显示名, QID)
A=[
 ("motet","Motet","Motet","Renaissance_music","Renaissance music","Q188285"),
 ("mass-music","Mass_(music)","Mass (music)","Medieval_music","Medieval music","Q217295"),
 ("concerto","Concerto","Concerto","Baroque_music","Baroque music","Q9748"),
 ("counterpoint","Counterpoint","Counterpoint","Polyphony","Polyphony","Q186393"),
 ("josquin","Josquin_des_Prez","Josquin des Prez","Franco-Flemish_School","Franco-Flemish School","Q143100"),
 ("hildegard","Hildegard_of_Bingen","Hildegard of Bingen","Gregorian_chant","Gregorian chant","Q70991"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
def add(s):
    if s["id"] not in have: sd["sources"].append(s); have.add(s["id"])
for eid,pg,pn,pg2,pn2,q in A:
    add({"id":"enc-"+eid,"title":pn,"author":"Wikipedia contributors","year":"2026","url":WP+pg,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"enc-c175-"+pg2.lower().replace("_","-"),"title":pn2,"author":"Wikipedia contributors","year":"2026","url":WP+pg2,"type":"权威百科","verified":True,"verified_note":NOTE})
    add({"id":"wd-"+eid,"title":"Wikidata: %s (%s)"%(pn,q),"author":"Wikimedia Foundation（Wikidata 社区维护）","year":"2026","url":"https://www.wikidata.org/wiki/"+q,"type":"权威结构化数据","verified":True,"verified_note":WDN})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
def S(eid,pg2): return "enc-%s,enc-c175-%s,wd-%s"%(eid,pg2.lower().replace("_","-"),eid)
T=[
 ('motet','经文歌（Motet）','术语','music-renaissance','13世纪—今','欧洲','音乐体裁','重要',
  '主要为声乐的多声部作品，形式与风格极为多样，从中世纪盛期延续至今，是文艺复兴音乐的主要复调体裁之一。','13世纪—今',
  '经文歌是西方古典音乐中主要为声乐的作品，形式与风格极为多样，从中世纪盛期延续至今，是文艺复兴音乐最突出的复调体裁之一。音乐学家玛格丽特·本特认为，“带歌词的多声部乐曲”足以作为13世纪至16世纪晚期乃至其后经文歌的准确定义。',
  'polyphony,renaissance-music,mass-music',S('motet','Renaissance_music')),
 ('mass-music','弥撒曲（Mass）','术语','music-medieval','中世纪—今','欧洲','音乐体裁','重要',
  '为西方基督教圣餐礼仪弥撒的文本谱曲的音乐体裁，通常由弥撒常规的五个乐章构成。','中世纪—今',
  '弥撒曲是为西方基督教圣餐礼仪“弥撒”的文本谱曲的音乐作品。通常是弥撒常规的五个乐章，但套曲可缩减，或扩充至包含部分或全部专有部分；其中的特例是安魂曲，因其引入咏的第一个词而得名。',
  'gregorian-chant,motet,medieval-music',S('mass-music','Medieval_music')),
 ('concerto','协奏曲（Concerto）','术语','music-baroque','巴洛克晚期—今','欧洲','音乐体裁','重要',
  '自巴洛克晚期以来多指为一件或多件独奏乐器与管弦乐队或其他乐队合作而写的器乐作品。','巴洛克晚期—今',
  '协奏曲自巴洛克晚期以来，多被理解为写给一位或多位独奏者、由管弦乐队或其他乐队伴奏的器乐作品。典型的三乐章结构——慢乐章前后各有一个快乐章——自18世纪初起成为标准。',
  'baroque-music,symphony,sonata-form',S('concerto','Baroque_music')),
 ('counterpoint','对位法（Counterpoint）','术语','music-renaissance','文艺复兴—今','欧洲','音乐体裁','核心',
  '两条或更多同时进行的旋律线之间的关系：和声上相互依赖，节奏与旋律轮廓上各自独立。','文艺复兴—今',
  '对位法是音乐理论中两条或更多同时进行的旋律线之间的关系：它们在和声上相互依赖，但在节奏与旋律轮廓上各自独立。该词源自拉丁语“点对点”，即“音对音”。对位法最常见于欧洲古典传统，在文艺复兴时期以及通行实践时期的大部分阶段，尤其是巴洛克时期，得到有力发展；西方教学中以“种”的体系讲授对位。',
  'polyphony,fugue,bach',S('counterpoint','Polyphony')),
 ('josquin','若斯坎·德普雷（Josquin des Prez）','人物','music-renaissance','15—16世纪','法国／佛兰德斯','音乐体裁','核心',
  '法国或法兰德斯—勃艮第乐派的文艺复兴作曲家，被视为文艺复兴最伟大的作曲家之一，作品以声乐为主。','15—16世纪',
  '若斯坎·德普雷是法国或佛兰德斯—法国乐派的文艺复兴作曲家，被视为文艺复兴最伟大的作曲家之一，是佛兰德斯—法国乐派的核心人物，对16世纪欧洲音乐影响深远。他发展出在各独立声部之间富于表现、常带模仿的复调风格，强调文字与音乐的关系，不再沿用早期文艺复兴冗长的单音节花腔，而偏好声部之间较短、反复的动机。他本人是歌手，作品以声乐为主，包括弥撒曲、经文歌与世俗尚松。',
  'motet,mass-music,palestrina',S('josquin','Franco-Flemish_School')),
 ('hildegard','宾根的希尔德加德（Hildegard of Bingen）','人物','music-medieval','中世纪盛期','德国','音乐体裁','重要',
  '中世纪盛期的德国本笃会女修道院长与博学者，是最知名的圣咏单声部作曲家之一。','中世纪盛期',
  '宾根的希尔德加德，号称“莱茵河的女先知”，是德国本笃会女修道院长与博学者，活跃于中世纪盛期，身兼医学作者、作曲家、哲学家、神秘主义者与异象者。她是最知名的圣咏单声部作曲家之一，也是现代录音最多的作曲家。一些学者认为她是德国科学博物学的奠基者。',
  'gregorian-chant,medieval-music,organum',S('hildegard','Gregorian_chant')),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
