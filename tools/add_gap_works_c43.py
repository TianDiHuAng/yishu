# -*- coding: utf-8 -*-
"""Cycle43：补覆盖缺口 4 条（印度克什米尔立佛 / 马图拉栏楯柱 / 陈洪绶仿古册 / 赵孟頫河村渔乐）。
均为 CMA 单机构来源 → needs_verification，并在待核实首条写明。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1966-30","Cleveland Museum of Art — Standing Buddha, Kashmir, c. 900, acc. 1966.30",
   "https://openaccess-api.clevelandart.org/api/artworks/1966.30","2026-11-23 API HTTP 200；黄铜嵌银铜、整体98.1cm、座上藏文题记"),
 ("cma-1977-34","Cleveland Museum of Art — Corner Railing Pillar with Drinking Scenes, Mathura, 100s CE, acc. 1977.34",
   "https://openaccess-api.clevelandart.org/api/artworks/1977.34","2026-11-23 API HTTP 200；红砂岩 80×22.9×24cm"),
 ("cma-1979-27","Cleveland Museum of Art — Chen Hongshou, Paintings after Ancient Masters, 1598–1652, acc. 1979.27",
   "https://openaccess-api.clevelandart.org/api/artworks/1979.27","2026-11-23 API HTTP 200；双册二十二开、30.2×26.7cm"),
 ("cma-1978-66","Cleveland Museum of Art — Zhao Mengfu, River Village: Fisherman's Joy, c. 1302–3, acc. 1978.66",
   "https://openaccess-api.clevelandart.org/api/artworks/1978.66","2026-11-23 API HTTP 200；扇面裱为册页、28.6×30cm")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('indian-standing-buddha-kashmir','克什米尔立佛（克利夫兰藏）','作品','art-asia','9—10世纪','南亚','雕塑','重要',
    '克什米尔地区所作立佛铜像，克利夫兰艺术博物馆藏（1966.30）；座上藏文题记提到一位王室僧人。','约900年（座上题记涉及活动于约998—1026年的人物）',
    '以一足微离莲座暗示佛由超越境界进入人间，右手施无畏印；表面磨蚀显示其曾受灌顶等仪式供养。','buddhist-art-india,indian-art','cma-1966-30'),
   ('mathura-railing-pillar','马图拉栏楯柱（饮酒、药叉女与乐人）','作品','art-asia','2世纪','南亚','雕塑','重要',
    '贵霜期马图拉红砂岩栏楯柱，克利夫兰艺术博物馆藏（1977.34），雕饮酒歌舞的药叉女与乐人。','公元100年代',
    '柱身显示希腊罗马文化与犍陀罗风格对马图拉艺术的影响；基座另刻驼背女为肥硕药叉斟酒等场景。','indian-art,buddhist-art-india','cma-1977-34'),
   ('chen-hongshou-album','陈洪绶《仿古册》','作品','art-asia','16—17世纪','中国','绘画','重要',
    '明末陈洪绶双册二十二开，克利夫兰艺术博物馆藏（1979.27），含山水、人物与花卉。','1598—1652年',
    '晚年代表作，风格古拙而精炼；人物与山水被缩小呈现，如微型园林与案头供石，于小中见大。','ming-painting,china-painting-history','cma-1979-27'),
   ('zhao-mengfu-river-village','赵孟頫《河村渔乐》','作品','art-asia','14世纪','中国','绘画','重要',
    '赵孟頫青绿风格山水扇面（裱为册页），克利夫兰艺术博物馆藏（1978.66）。','约1302—03年',
    '融合南方平远水景与北方山水的尖峭树石特征，体现其在元代画坛的折中取向。','yuan-painting,china-painting-history','cma-1978-66')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
block=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
lines[close:close]=block
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")

E={}
E["indian-standing-buddha-kashmir"]={"sections":{
 "时代背景":"本像为克什米尔地区作品，克利夫兰艺术博物馆定年为约900年。据该馆说明，座上藏文题记称此像曾属于一位名为 Nagaraja 的王室僧人（藏文语境，活动约998—1026年）——这说明造像本身与其后世的持有者之间存在时间差，题记记录的是后来的归属而非制作年代。",
 "风格特征":"该馆说明描述其身形「修长而富运动感」：佛像一足稍稍离开莲花座，用以暗示其人性由超越境界进入我们这个世界；右手施无畏印，表示不必恐惧。雕像表面顺滑的磨蚀痕迹，被该馆解释为曾在克什米尔受过礼拜——仪式中以水等供物灌沐圣像。",
 "代表人物与作品":"相关条目见印度佛教艺术与印度艺术。本像属克什米尔造像系统；该馆说明指出，这类作品参与了佛教自印度向西藏的传播。作者姓名未见于记录，本条目不推定匠人。",
 "技法或形式分析":"材质为黄铜，嵌银与嵌铜（brass with silver and copper inlay），整体高98.1厘米，底座28.2厘米（据该馆藏品记录）。嵌银嵌铜用于表现眼部与衣饰细节，是克什米尔铜造像常见的做法；本条目只据该馆记录陈述本件材质，不推断工艺的普遍谱系。",
 "与前后风格的关系和争论":"该馆把本像放在「印度—西藏」佛教传播的脉络中说明，并强调其被礼拜的使用痕迹。关于克什米尔造像对西藏西部的影响程度、以及 Nagaraja 题记的具体释读，学界有专门讨论，本条目未取得可核验的两方材料，故不作判断。",
 "一图":"示意图以克什米尔造像、藏文题记与印度—西藏传播三者关系标示本像的位置。",
 "待核实":"（1）本条目全部事实来自单一机构（克利夫兰艺术博物馆）的藏品记录与说明，双源独立性未满足，整条标记待核实；（2）题记的完整释文与 Nagaraja 的身份考订未取得专门研究；（3）造像年代「约900年」与该馆说明中题记人物活动年代（约998—1026）的衔接关系，需依题记研究判定；（4）同类造像的比较谱系未写入。",
 },
 "diagram":{"nodes":[{"label":"克什米尔","sub":"约900年","kind":"accent"},{"label":"黄铜嵌银铜","sub":"98.1 cm","kind":"muted"},
   {"label":"藏文题记","sub":"Nagaraja","kind":"muted"},{"label":"印度→西藏","sub":"佛教传播","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":0,"to":2},{"from":1,"to":3}],"caption":"克什米尔立佛：材质、题记与传播脉络"},
 "sources":["cma-1966-30"]}

E["mathura-railing-pillar"]={"sections":{
 "时代背景":"本柱为贵霜期马图拉（Mathura）作品，克利夫兰艺术博物馆定年为公元100年代。马图拉是古代印度重要的造像中心；该馆说明把本柱放在希腊罗马文化与犍陀罗风格影响印度艺术的脉络中理解。",
 "风格特征":"柱身雕刻的女性形象「似乎处于醉意中」，奏乐起舞——这一题材被该馆称为「饮酒（bacchanalian）主题」在馬图拉艺术中的体现。基座另有两处场景：其一为驼背女子为肥硕的男性丰产神（yaksha）斟酒；其二「可能」表现马头药叉女吞食受害者的故事。",
 "代表人物与作品":"相关条目见印度艺术与印度佛教艺术。本柱为建筑构件（栏楯转角柱），说明其原本属于围绕圣地的围栏系统；作者未见于记录。",
 "技法或形式分析":"材质为红砂岩（red sandstone），整体80 × 22.9 × 24厘米（据该馆藏品记录）。作为转角柱，它需在两面同时承载叙事浮雕，因此构图被安排为分层与分段：上部为乐舞药叉女，基座为两处小场景。",
 "与前后风格的关系和争论":"该馆明确把本柱的「希腊罗马影响」与「犍陀罗风格、酒神主题对马图拉的影响」并列陈述，这正是印度艺术史中关于外来影响程度的长期议题；但本条目只转述该馆的判断，不就争议本身裁定。",
 "一图":"示意图以希腊罗马/犍陀罗影响、马图拉的酒神主题与栏楯构件功能三者关系标示本柱。",
 "待核实":"（1）本条目事实来自单一机构（克利夫兰艺术博物馆）藏品记录，整条标记待核实；（2）基座第二场景「马头药叉女」的解释该馆以 possibly/probably 措辞给出，属推测，本条目保留该措辞；（3）原属遗址与栏楯整体形制未取得来源；（4）贵霜期马图拉的年代框架未与专门研究核对。",
 },
 "diagram":{"nodes":[{"label":"希腊罗马·犍陀罗","sub":"外来影响","kind":"muted"},{"label":"马图拉","sub":"100年代","kind":"accent"},
   {"label":"酒神主题","sub":"药叉女乐舞","kind":"muted"},{"label":"栏楯转角柱","sub":"红砂岩","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"马图拉栏楯柱：外来影响与酒神主题"},
 "sources":["cma-1977-34"]}

E["chen-hongshou-album"]={"sections":{
 "时代背景":"本册为明末画家陈洪绶（1598—1652）所作双册，共二十二开，克利夫兰艺术博物馆藏（1979.27）。该馆把作品放在其晚年创作中论述；册中二十幅绘画含山水、人物与花卉，另有一开画女性——该馆指出，这一题材在他晚年其他册页中并不出现。",
 "风格特征":"该馆称其晚年作品是「奇特而古怪（peculiar and quirky）的艺术的精彩总结」：古拙（archaistic）而高度精炼，却不带浅薄或感伤。册中的人物与山水被缩小呈现，该馆以「微型中国园林」「精心挑选的小型案头供石或老根」作比，强调在小中见大的观看方式。",
 "代表人物与作品":"作者陈洪绶为明末画家。相关条目见明代绘画与中国绘画史。本册为双册（two albums）装，共二十二开，材质为绢本水墨或设色。",
 "技法或形式分析":"材质据该馆记录为「ink or ink and color on silk」（绢本水墨或设色），整体尺寸30.2 × 26.7厘米。册页形制决定了单开的尺幅有限，因此人物与景物被压缩为小幅构图；该馆正是从这一形制出发解释其「缩微」的视觉策略。",
 "与前后风格的关系和争论":"陈洪绶的「古拙」取径与明末复古风气相关，但该馆强调其精炼而不流于浅薄，这本身带有评价性。关于他在晚明画坛的位置、以及对其「古怪」风格的不同解读，学界有讨论，本条目未取得两方材料，故不裁定。",
 "一图":"示意图以晚明语境、古拙取径、册页形制与「小中见大」四者关系标示本册。",
 "待核实":"（1）本条目事实来自单一机构（克利夫兰艺术博物馆）藏品记录，整条标记待核实；（2）二十二开中二十幅为绘画的具体分册结构、以及各开内容清单未取得；（3）作者生卒1598—1652取自该馆记录，未以第二来源核对；（4）该馆的「archaistic」「quirky」等评价属一家之言，未与专门研究对照。",
 },
 "diagram":{"nodes":[{"label":"晚明","sub":"1598—1652","kind":"muted"},{"label":"陈洪绶","sub":"古拙·精炼","kind":"accent"},
   {"label":"双册二十二开","sub":"30.2×26.7","kind":"muted"},{"label":"小中见大","sub":"缩微策略","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":2,"to":3}],"caption":"陈洪绶《仿古册》：古拙取径与册页形制"},
 "sources":["cma-1979-27"]}

E["zhao-mengfu-river-village"]={"sections":{
 "时代背景":"据克利夫兰艺术博物馆说明，本幅作者赵孟頫为南方人，通晓文人诸艺（书法、鉴赏等）；他是被灭亡的南宋宗室，却在1286年被忽必烈征召至新都大都（今北京）的蒙古朝廷任职。本幅定年为约1302—03年，为扇面装裱成册页的青绿风格山水。",
 "风格特征":"该馆说明称，本幅把「南方特有的平远水景」与「北方山水传统的特征」结合起来——后者尤以尖峭的树木、枝干与粗面岩石为代表。这一「南北合」的取向，是理解赵孟頫山水面貌的关键。",
 "代表人物与作品":"作者赵孟頫；相关条目见元代绘画与中国绘画史。作品形制为扇面（fan painting）后裱为册页，材质为绢本设色。",
 "技法或形式分析":"材质与尺寸据该馆记录：扇面裱为册页，绢本设色（ink and color on silk），整体28.6 × 30厘米。青绿设色与尖峭树石的组合，在有限的扇面尺幅内同时容纳了平远与高峻两种空间感。",
 "与前后风格的关系和争论":"赵孟頫倡导「复古」，其仕元经历在南宋遗民语境中亦长期受到评说；该馆说明以「被征召」为中性的叙述，未对其政治选择作评价。关于「青绿」在元代的复兴与其个人的作用，学界有专门讨论，本条目未取得两方材料。",
 "一图":"示意图以南人身份、仕元经历、南北景融合与扇面形制四者关系标示本幅。",
 "待核实":"（1）本条目事实来自单一机构（克利夫兰艺术博物馆）藏品记录，整条标记待核实；（2）1286年应召的年份见于该馆说明，未以第二来源核对；（3）题跋、鉴藏印与流传经过未取得；（4）赵孟頫在画史评价中的争议（仕元问题、复古主张）未写入正文。",
 },
 "diagram":{"nodes":[{"label":"南人·宋宗室","sub":"身世","kind":"muted"},{"label":"赵孟頫","sub":"元代","kind":"accent"},
   {"label":"南北景合","sub":"青绿","kind":"muted"},{"label":"扇面册页","sub":"28.6×30","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"赵孟頫《河村渔乐》：身世、南北景与形制"},
 "sources":["cma-1978-66"]}

for eid,spec in E.items():
    svg=render_svg(spec["diagram"],eid)
    out={"id":eid,"level":"L2","sections":spec["sections"],"svg":svg,"sources":spec["sources"],
         "needs_verification":True,
         "pending_notes":"本条目事实仅取自单一机构（克利夫兰艺术博物馆）的藏品记录与策展说明，未获第二独立来源；断代、题记释读与评价性表述均待外部核对。详见待核实。"}
    json.dump(out,open(os.path.join(LD,eid+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("wrote",eid)