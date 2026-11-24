# -*- coding: utf-8 -*-
"""Cycle184：给12个核心风格条目追加盖蒂 AAT 来源（独立机构词表），并在“待核实”记录与库内表述的异同。
不改 when、不改正文，只追加来源与待核实说明。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
AAT="https://vocab.getty.edu/aat/"
TAG="（AAT 对照，2026-11-24）"
# 条目id -> (AAT编号, AAT标签, 对照说明)
M={
 'impressionism':('300021503','Impressionist (style)','AAT 定义：19世纪西方艺术运动，发展于法国，拒绝传统学院教学，尝试用色彩物理学的科学来精确表现色彩、色调与光；以小笔触纯色、户外作画捕捉一天中转瞬即逝的时刻、客观描绘当代生活为特征。与本条目一致，未发现冲突。'),
 'baroque':('300021147','Baroque','AAT 定义：约1590至1750年西欧与美洲的建筑、视觉艺术、装饰艺术、音乐与文学的风格与时期；以均衡与整体为特征，常强调壮观场面与情感内容，倾向明暗对比、实与虚对比、强对角线与曲线。与本条目的差异：AAT 起点为约1590年（本条目 when 为约1600年），差约10年；AAT 范围含西欧与美洲及多门类，比本条目“17世纪兴起于欧洲”更宽。两者是不同来源的断代与范围口径，本条目不裁决，保持原 when。'),
 'cubism':('300021495','Cubist','AAT 定义：国际艺术运动，起源归于布拉克与毕加索，约1908年，分阶段发展，持续到1920年代初；以强调画面平面性、拒绝传统再现方法、通过同时呈现多个侧面使物体解体为特征。与本条目基本一致（本条目约1908—1920年）。'),
 'surrealism':('300021512','Surrealist','AAT 定义：主要以巴黎为中心的国际知识运动，自1920年代到1940年代末，吸收象征主义的某些审美实验与达达的态度，强调通过融合现实与本能、潜意识和梦境，探索经验的极限，以创造绝对现实。与本条目的差异：AAT 终点约1940年代末，本条目 when 为约1924—1966年，终点差约20年；AAT 以巴黎为中心，本条目地域写“欧洲”。两者口径不同，本条目不裁决，保持原 when。'),
 'expressionism':('300021502','Expressionist (style)','AAT 定义：国际性的艺术、文学、音乐、舞蹈与戏剧风格，兴盛于1905至1920年，尤其在德国；以抛弃传统写实与比例标准、转而表现艺术家情感、造成线条、色彩与形式的变形为特征。与本条目的差异：AAT 终点为1920年（本条目 when 约1905—1930年），差约10年；AAT 范围含多门类。本条目不裁决，保持原 when。'),
 'romanticism-art':('300056557','romanticism (form of expression)','AAT 定义：视觉艺术、文学、戏剧与音乐中强调情感、戏剧性或异域的取向。该词条跨门类、定义较宽泛，不含具体年代与地域，因此只能印证本条目“强调情感”的基本含义，不能印证 when（约1800—1850年）与地域。'),
 'renaissance':('300021140','Renaissance','AAT 定义：始于14世纪晚期的意大利、传遍欧洲、在16世纪达到顶点的知识运动、风格与文化；风格以对古罗马与古希腊的艺术、建筑、文学与理想的有意参照为特征。与本条目基本一致；AAT 起点为14世纪晚期，本条目 when 约1400—1600年，口径略有出入但相容。'),
 'rococo':('300021155','Rococo','AAT 定义：主要指装饰艺术的时期，约1700年出现于法国路易十五宫廷，在欧洲占主导，直到18世纪晚期被古典复兴取代；以奢华、不对称、优雅、欢快与淡雅色调为特征，与巴洛克较重的形式和较暗的色彩形成对照。与本条目的差异：AAT 起点约1700年（本条目 when 约1715—1770年），差约15年。本条目不裁决，保持原 when。'),
 'dada':('300021500','Dada','AAT 定义：欧洲的艺术与文学运动，对西方文明的矫饰的反叛，1916年始于苏黎世，是对第一次世界大战的反应；主张运用反讽、虚无主义、反传统、荒诞，强调偶然在诗歌、表演与艺术作品创作中的重要性，作品通常是被改造用于视觉艺术创作的寻常物品。与本条目一致，未发现冲突。'),
 'post-impressionism':('300021508','Post-Impressionist','AAT 定义：存在于19世纪晚期到20世纪初的西方艺术运动，该术语由评论家罗杰·弗莱、克莱夫·贝尔等人创造，指年代上继印象派之后、又有别于新印象派的艺术；特征是迥然不同、高度个人化的艺术风格。与本条目基本相容；AAT 强调该词是批评家后设的归类。'),
 'futurism':('300021374','Futurist','AAT 定义：以意大利为中心的文学与艺术运动，强调速度、动力、能量并拒绝过去，始于1909年马里内蒂的写作；未来主义也在俄国发展，带有更革命、更政治的内涵；绘画上，到1912年前依赖分色技法，之后采纳立体主义的同时视角与变形平面。与本条目一致（起点1909年）；本条目 when 终点为1944年，AAT 摘录未给出终点。'),
 'bauhaus':('300021432','Bauhaus','AAT 定义：德国的艺术、设计与建筑学校，1919至1925年在魏玛、1925至1932年在德绍、1932至1933年在柏林；同时训练学生的美术与工艺，生产适于大批量生产、采用简单几何形式的物品与建筑设计。与本条目一致（1919—1933年）。'),
}
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for eid,(num,label,_) in M.items():
    sid="aat-"+num
    if sid not in have:
        sd["sources"].append({"id":sid,"title":"Getty AAT — %s, %s"%(label,num),"author":"J. Paul Getty Trust（Art & Architecture Thesaurus，开放词表）","year":"2026","url":AAT+num,"type":"权威机构词表（术语定义）","verified":True,
            "verified_note":"2026-11-24 经 vocab.getty.edu SPARQL 接口取回该术语的英文定义（scopeNote），编号与标签匹配"})
        have.add(sid)
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
# 追加到条目：L2 覆盖文件的 sources 与“待核实”
for eid,(num,label,note) in M.items():
    p=os.path.join(D,"l2",eid+".json")
    j=json.load(open(p,encoding="utf-8"))
    sid="aat-"+num
    if sid not in j["sources"]: j["sources"].append(sid)
    t=j["sections"].get("待核实","")
    if TAG not in t: j["sections"]["待核实"]=t+TAG+note
    json.dump(j,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("l2 updated",len(M))
