# -*- coding: utf-8 -*-
"""Cycle174 overlay：建筑类 6 条（Wikipedia 摘要+相邻页+Wikidata；只转述摘要，不补写）。"""
import json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
LD=os.path.join(ROOT,"data","l2")
def W(eid,sec,diag,srcs,note):
    json.dump({"id":eid,"level":"L2","sections":sec,"svg":render_svg(diag,eid),"sources":srcs,
               "needs_verification":True,"pending_notes":note},
              open(os.path.join(LD,eid+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("wrote",eid)
NOSRC="本条目事实仅来自 Wikipedia 摘要（2026-11-24 取回）及同源的 Wikidata 标签，来源独立性有限，整条标记待核实。"
NOWHO="摘要没有列举建筑师与具体建筑，本条目不补写；需另取专著或博物馆来源后再增补。"
def S(era,feat,who,tech,rel,pic,todo):
    return {"时代背景":era,"风格特征":feat,"代表人物与作品":who,"技法或形式分析":tech,"与前后风格的关系和争论":rel,"一图":pic,"待核实":"（1）"+NOSRC+todo}

W("renaissance-architecture",S(
 "摘要称，文艺复兴建筑是约15世纪初到16世纪初、欧洲各地区的建筑。",
 "摘要称，它体现出对古希腊、古罗马思想与物质文化某些元素的自觉复兴与发展。",
 NOWHO+"相关条目可参见文艺复兴。",
 "摘要没有给出具体的结构或装饰手法。可知的只有它对古希腊罗马元素的复兴与发展。",
 "摘要称，风格上它承接哥特建筑，又被巴洛克建筑与新古典主义建筑接替。",
 "示意图以文艺复兴建筑为中心，标示承接哥特建筑、复兴古代元素、被巴洛克接替三项。",
 "（2）各地区的差异与分期，摘要仅说“不同地区”，未展开；（3）具体建筑师与建筑，摘要未给出。"),
 {"nodes":[{"label":"哥特建筑","sub":"此前","kind":"muted"},{"label":"文艺复兴建筑","sub":"15—16世纪初","kind":"accent"},{"label":"古代希腊罗马","sub":"复兴元素","kind":"muted"},{"label":"巴洛克建筑","sub":"此后","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":2,"to":1},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-renaissance-architecture","enc-c174-classical-architecture","wd-renaissance-architecture"],"来源独立性有限（Wikipedia+Wikidata）；分期差异与名作未给出。")

W("baroque-architecture",S(
 "摘要称，巴洛克建筑出现于16世纪末的意大利，并逐渐传遍欧洲。盛期巴洛克为1625—1675年，晚期为1675—1750年；约1730年更繁复的变体洛可可在中欧兴起。",
 "摘要称，这是一种高度装饰性、戏剧化的风格。",
 NOWHO+"相关条目可参见巴洛克与洛可可。",
 "摘要对形式的描述只有“高度装饰性、戏剧化”，以及它意在激发惊叹、敬畏。盛期巴洛克用于意大利、西班牙、葡萄牙、法国、巴伐利亚与奥地利的教堂和宫殿；晚期远及俄国、奥斯曼帝国与西葡的拉美殖民地。",
 "摘要称，它最初由天主教会、尤其是耶稣会引入，用新的建筑激发惊叹与敬畏，以对抗宗教改革与新教教会。约1730年出现的洛可可是更繁复的变体。",
 "示意图以巴洛克建筑为中心，标示天主教会与耶稣会引入、盛期与晚期、洛可可变体三项。",
 "（2）与宗教改革对抗的说法是摘要对其起因的概括，未展开论证；（3）具体建筑师与建筑，摘要未给出。"),
 {"nodes":[{"label":"天主教会","sub":"耶稣会引入","kind":"muted"},{"label":"巴洛克建筑","sub":"16世纪末起","kind":"accent"},{"label":"盛期与晚期","sub":"1625—1750","kind":"muted"},{"label":"洛可可","sub":"约1730变体","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-baroque-architecture","enc-c174-baroque","wd-baroque-architecture"],"来源独立性有限（Wikipedia+Wikidata）；名作与建筑师未给出。")

W("neoclassical-architecture",S(
 "摘要称，新古典主义建筑产生于始于18世纪中叶意大利、法国与德国的新古典主义运动。",
 "摘要称，它又称古典复兴建筑，意在剥去晚期巴洛克的过度装饰，回到更纯粹、更完整、更正统的古典风格，并使之适应现代用途。",
 NOWHO+"相关条目可参见新古典主义。",
 "摘要没有给出具体手法，只说明它的目标是回到更纯粹的古典风格并适应现代用途。",
 "摘要称，此前欧洲大部分地区两个世纪的主流风格是文艺复兴与巴洛克建筑，二者已是对古罗马古典建筑与古希腊建筑的部分复兴；新古典主义则要剥去晚期巴洛克的过度装饰。摘要称它成为西方最突出的建筑风格之一。",
 "示意图以新古典主义建筑为中心，标示此前的文艺复兴与巴洛克、回到古典风格、适应现代用途三项。",
 "（2）摘要说明了它与文艺复兴、巴洛克同样回望古典，但“更纯粹”的判断是摘要的概括；（3）具体建筑师与建筑，摘要未给出。"),
 {"nodes":[{"label":"文艺复兴与巴洛克","sub":"部分复兴古典","kind":"muted"},{"label":"新古典主义建筑","sub":"18世纪中叶起","kind":"accent"},{"label":"剥去晚期巴洛克装饰","sub":"意图","kind":"muted"},{"label":"更纯粹的古典","sub":"适应现代","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-neoclassical-architecture","enc-c174-neoclassicism","wd-neoclassical-architecture"],"来源独立性有限（Wikipedia+Wikidata）；名作与建筑师未给出。")

W("byzantine-architecture",S(
 "摘要称，拜占庭帝国的建筑通常从公元330年算起，当年君士坦丁大帝在拜占庭建立新的罗马首都，即后来的君士坦丁堡；下限是1453年帝国灭亡。",
 "摘要称，风格继续以拱、拱顶和穹顶为基础，常为大尺度。",
 NOWHO+"相关条目可参见拜占庭艺术。",
 "摘要称，金底墙面镶嵌画成为最宏伟建筑的标准装饰，湿壁画则是较廉价的替代。可知的结构要素是拱、拱顶与穹顶。",
 "摘要称，起初拜占庭与罗马帝国之间没有明确界线，早期拜占庭建筑在风格与结构上与晚期罗马建筑难以区分。",
 "示意图以拜占庭建筑为中心，标示晚期罗马建筑、拱顶与穹顶、金底镶嵌画三项。",
 "（2）摘要没有说明早期拜占庭与晚期罗马建筑何时开始分化；（3）具体建筑师与建筑，摘要未给出。"),
 {"nodes":[{"label":"晚期罗马建筑","sub":"难以区分","kind":"muted"},{"label":"拜占庭建筑","sub":"330—1453","kind":"accent"},{"label":"拱、拱顶、穹顶","sub":"常大尺度","kind":"muted"},{"label":"金底镶嵌画","sub":"标准装饰","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-byzantine-architecture","enc-c174-byzantine-empire","wd-byzantine-architecture"],"来源独立性有限（Wikipedia+Wikidata）；名作与分化时间未给出。")

W("chinese-architecture",S(
 "摘要称，中国建筑在中国历经千年发展，自早期古代出现以来，其结构原则大体不变。",
 "摘要称，主要变化在于多样的装饰细节，结构原则大体不变。",
 NOWHO+"相关条目可参见吴哥窟与高棉建筑，但摘要并未提到它们，两者关系本条目不作判断。",
 "摘要没有给出具体构件或做法。可知的是：结构原则长期稳定，变化集中在装饰细节。",
 "摘要称，自唐代起，中国建筑对日本、朝鲜、越南、蒙古等邻近东亚国家的建筑风格产生重大影响，对马来西亚、新加坡、印度尼西亚、斯里兰卡、泰国、老挝、柬埔寨、菲律宾等东南亚与南亚国家也有较小影响。",
 "示意图以中国建筑为中心，标示结构原则大体不变、装饰细节多样、影响东亚与东南亚三项。",
 "（2）本条目暂挂在“中国绘画史”单元下，因库内尚无中国建筑专属单元；（3）具体建筑类型与实例（宫殿、园林、木构等），摘要未给出；（4）摘要所称对东南亚、南亚的影响，本条目未核验。"),
 {"nodes":[{"label":"结构原则","sub":"大体不变","kind":"muted"},{"label":"中国建筑","sub":"历经千年","kind":"accent"},{"label":"装饰细节","sub":"主要变化","kind":"muted"},{"label":"影响东亚","sub":"自唐代起","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-chinese-architecture","enc-c174-chinese-art","wd-chinese-architecture"],"来源独立性有限（Wikipedia+Wikidata）；类型、实例、分期未给出。")

W("islamic-architecture",S(
 "摘要称，伊斯兰建筑涵盖从伊斯兰早期历史到今天的建筑风格；伊斯兰世界历史上西起西非与欧洲，东至东亚。",
 "摘要称，各地区的伊斯兰建筑风格有共通之处。",
 NOWHO+"相关条目可参见伊斯兰艺术、伊斯法罕祈祷龛与伊兹尼克花卉纹砖。",
 "摘要没有列出具体的形式要素。可知的是：风格既含世俗也含宗教建筑，且各地因本地材料与技术而不同。",
 "摘要称，随时间推移，各地区因本地材料与技术、地方王朝与赞助人、不同的艺术生产中心，有时还因不同的宗教派别，形成各自的风格。",
 "示意图以伊斯兰建筑为中心，标示世俗与宗教建筑、共通之处、各地区风格三项。",
 "（2）“共通之处”具体指什么，摘要未说明；（3）具体建筑师与建筑，摘要未给出。"),
 {"nodes":[{"label":"世俗与宗教","sub":"两类建筑","kind":"muted"},{"label":"伊斯兰建筑","sub":"早期至今","kind":"accent"},{"label":"共通之处","sub":"各地共享","kind":"muted"},{"label":"各地区风格","sub":"材料王朝等","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"据 Wikipedia 摘要"},
 ["enc-islamic-architecture","enc-c174-islamic-art","wd-islamic-architecture"],"来源独立性有限（Wikipedia+Wikidata）；共通要素与名作未给出。")
