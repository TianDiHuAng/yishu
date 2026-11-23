# -*- coding: utf-8 -*-
"""Cycle96 修正：清理重名重复，改为 4 条唯一条目
（hei-tiki 改用 1969 号 id；去掉与既有 1963.554 重复的 asmat；补 Wahaika 短棍）。
"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg

T=[
 ('maori-hei-tiki-1969','毛利绿玉颈坠（hei-tiki，1969号）','作品','art-oceania','19世纪','大洋洲','雕塑','核心',
  '毛利绿玉颈坠，克利夫兰艺术博物馆藏（1969.107）。','1800年代',
  '首领世袭并承载 mana；此坠为连接生者与前欧祖先的传家宝；或表现 Hine-te-Iwaiwa，生育守护者。','maori-wakahuia,oceania-art','cma-1969-107'),
 ('maori-wakahuia','毛利 Wakahuia 宝盒','作品','art-oceania','19世纪','大洋洲','雕塑','核心',
  '毛利木雕鲍鱼壳宝盒，克利夫兰艺术博物馆藏（1961.405）。','1800年代',
  '浅浮雕螺旋与两端小人像；盛首领饰物；因首级与颈部为 tapu，故悬于屋梁；库克1769—70所见即此类。','maori-hei-tiki-1969,oceania-art','cma-1961-405'),
 ('maori-wahaika-club','毛利 Wahaika 短棍','作品','art-oceania','19世纪','大洋洲','雕塑','重要',
  '毛利木制短棍，克利夫兰艺术博物馆藏（1964.455）。','1800年代中期',
  '佩于腰带，用于近身格斗；早期无饰石制，后骨木制装饰渐繁；侧附小人像或表武器之 mana，柄端人面表战斗的攻击性。','maori-hei-tiki-1969,oceania-art','cma-1964-455'),
 ('tami-bowl','塔米群岛木碗','作品','art-oceania','19世纪','大洋洲','综合','重要',
  '塔米群岛彩绘木碗，克利夫兰艺术博物馆藏（1965.322）。','1800年代',
  '以石斧、竹刀、树熊牙与猪/鹤鸵/狗骨为工具；用杜鹃木，刻纹深浅不一，多施石墨并抛光；花纹为家族所有。','maori-wakahuia,oceania-art','cma-1965-322'),
]

# 1) 替换 catalog 末尾的有问题块
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
start=2846
assert lines[start].startswith("('maori-hei-tiki'"), lines[start][:40]
block=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
lines[start:close]=block
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog block replaced with 4 clean tuples")

# 2) 补 source cma-1964-455
sp=os.path.join(ROOT,"data","sources.json"); sd=json.load(open(sp,encoding="utf-8"))
have={s["id"] for s in sd["sources"]}
if "cma-1964-455" not in have:
    sd["sources"].append({"id":"cma-1964-455",
        "title":"Cleveland Museum of Art — Short Club (Wahaika), Māori, mid-19th c., acc. 1964.455",
        "author":"Cleveland Museum of Art（开放数据 API）","year":"2026",
        "url":"https://openaccess-api.clevelandart.org/api/artworks/1964.455",
        "type":"权威机构藏品记录","verified":True,
        "verified_note":"2026-11-23 API HTTP 200；木 35.6cm；说明含腰带佩挂与 mana 小人像"})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

# 3) 覆盖层
LD=os.path.join(ROOT,"data","l2")
def W(eid,sec,diag,srcs,note):
    json.dump({"id":eid,"level":"L2","sections":sec,"svg":render_svg(diag,eid),"sources":srcs,
               "needs_verification":True,"pending_notes":note},
              open(os.path.join(LD,eid+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("wrote",eid)

W("maori-hei-tiki-1969",{
 "时代背景":"该馆说明，在毛利人中，**首领是世袭的**，并被赋予 **mana**（权力与威望）；mana 可以**寄托并世代相传于与其相关的艺术品中**。本件为19世纪绿玉颈坠。",
 "风格特征":"该馆指出，**hei-tiki** 正是这类**受珍视、承载 mana 的传家宝**——它们把生者与**岛屿前欧洲时代的祖先**连接起来。它可能表现 **Hine-te-Iwaiwa**，一位传说中的女祖先：她是**毛利女性气质的典范**，也是**生育的守护者**。",
 "代表人物与作品":"作者未署名。相关条目见 Wakahuia 宝盒与大洋洲艺术。本件为克利夫兰艺术博物馆藏品（1969.107）。",
 "技法或形式分析":"材质为**绿玉（pounamu，或为软玉）**，整体16.9 × 10.2厘米（据该馆藏品记录）。该馆对石种用疑问号（nephrite?），本条目亦不确断具体玉种。",
 "与前后风格的关系和争论":"本条目据该馆说明把「mana 的传递」作为核心：坠饰的价值不只在其形，而在它**储存并传递社会身份**。这使一件小型佩饰成为**世系与权威的载体**。",
 "一图":"示意图以世袭 mana、前欧祖先连接与 Hine-te-Iwaiwa 三者关系标示本坠。",
 "待核实":"（1）事实来自单一机构（CMA），整条标记待核实；（2）玉种该馆用 nephrite?，未定；（3）本坠的具体递藏谱系未取得；（4）「可能表现 Hine-te-Iwaiwa」为推测。",
},{"nodes":[{"label":"世袭 mana","sub":"权力·威望","kind":"muted"},{"label":"hei-tiki","sub":"16.9cm","kind":"accent"},
  {"label":"连接祖先","sub":"前欧时代","kind":"muted"},{"label":"Hine-te-Iwaiwa","sub":"生育守护","kind":"muted"}],
 "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"hei-tiki：mana、祖先与女祖神"},["cma-1969-107"],
 "单一机构（CMA）来源；玉种未定；递藏谱系未取得。")

W("maori-wahaika-club",{
 "时代背景":"该馆说明，**wahaika** 佩于腰带，毛利人用于**近身格斗**。本件为19世纪中期木制短棍。",
 "风格特征":"该馆指出一个**材质演变**：早期**无饰**的短棍以**石**制；后来的**骨与木**制短棍则装饰**日益复杂的雕刻图案**。",
 "代表人物与作品":"作者未署名。相关条目见 hei-tiki 与大洋洲艺术。本件为克利夫兰艺术博物馆藏品（1964.455）。",
 "技法或形式分析":"材质为**木**，整体长35.6厘米（据该馆藏品记录）。该馆给出两处**图像—语义**说明：**紧贴于棍侧的小人像**很可能表现**武器的超自然力（mana）**；而**握柄末端的人面**表达**战斗的攻击性**。",
 "与前后风格的关系和争论":"本条目据该馆说明把兵器视为**承载 mana 的物**：一件格斗武器的力量，部分来自其雕刻所象征的超自然属性，而不只是物理形制。本条目只陈述该馆的解释。",
 "一图":"示意图以腰带佩挂、mana 小人像与柄端攻击性人面三者关系标示本棍。",
 "待核实":"（1）事实来自单一机构（CMA），整条标记待核实；（2）「很可能表现 mana」为推测；（3）本棍所属部族与所有者未记录；（4）石制早期型与木制的年代关系未细化。",
},{"nodes":[{"label":"腰带佩挂","sub":"近身格斗","kind":"muted"},{"label":"Wahaika","sub":"35.6cm","kind":"accent"},
  {"label":"侧附小人像","sub":"mana?","kind":"muted"},{"label":"柄端人面","sub":"攻击性","kind":"muted"}],
 "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"Wahaika：佩挂、mana 与攻击性"},["cma-1964-455"],
 "单一机构（CMA）来源；mana 为推测；所有者未记录。")
print("overlays done")