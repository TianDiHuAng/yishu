# -*- coding: utf-8 -*-
"""Cycle42：新增 3 个浮世绘作品条目——每项均为 CMA 与 V&A 同作品双机构。
《凯风快晴》（北斋）、《庄野 白雨》（广重）、《大桥安宅骤雨》（广重）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[
 ("cma-1930-189","Cleveland Museum of Art — Katsushika Hokusai, South Wind, Clear Sky (Red Fuji), early 1830s, acc. 1930.189",
  "https://openaccess-api.clevelandart.org/api/artworks/1930.189","2026-11-23 API HTTP 200；curators 说明含系列年代 1829–1833 与「赤富士」称谓"),
 ("cma-1948-306","Cleveland Museum of Art — Utagawa Hiroshige, Driving Rain at Shōno, 1833, acc. 1948.306",
  "https://openaccess-api.clevelandart.org/api/artworks/1948.306","2026-11-23 API HTTP 200；说明含三版三层灰、出版商 Takenouchi"),
 ("cma-1921-318","Cleveland Museum of Art — Utagawa Hiroshige, Sudden Shower over Shin-Ōhashi Bridge and Atake, 1857, acc. 1921.318",
  "https://openaccess-api.clevelandart.org/api/artworks/1921.318","2026-11-23 API HTTP 200；说明含 1855 震后重建、系列名"),
 ("vam-o129067","Victoria and Albert Museum — Hokusai, Clear Day with a Southern Breeze (Gaifū kaisei), O129067",
  "https://collections.vam.ac.uk/item/O129067/","2026-11-23 V&A API HTTP 200；题名含系列《富岳三十六景》，纸本 25.2 × 37.4 cm"),
 ("vam-o410702","Victoria and Albert Museum — Hiroshige, Shōno: Driving Rain (Shōno, hakuu), O410702",
  "https://collections.vam.ac.uk/item/O410702/","2026-11-23 V&A API HTTP 200；纸本 22.9 × 34.9 cm"),
 ("vam-o420904","Victoria and Albert Museum — Hiroshige, Sudden Shower over Shin-Ōhashi Bridge and Atake, O420904",
  "https://collections.vam.ac.uk/item/O420904/","2026-11-23 V&A API HTTP 200；纸本 14.13 × 9.04 cm（与大判尺寸不同，版次待核）"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"year":"2026","url":url,
            "author":("Cleveland Museum of Art（开放数据 API）" if sid.startswith("cma") else "Victoria and Albert Museum（V&A API v2）"),
            "type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('hokusai-red-fuji','《凯风快晴》（北斋）','作品','art-asia','19世纪','日本','绘画','重要',
    '葛饰北斋《富岳三十六景》之一，通称「赤富士」；克利夫兰艺术博物馆（1930.189）与维多利亚与艾尔伯特博物馆（O129067）各藏印本。','early 1830s（系列作于1829—1833年）',
    '以夏末秋初山体转红的时刻描绘富士山，是浮世绘风景版画中最广为人知的图像之一。','ukiyo-e,japanese-art','cma-1930-189,vam-o129067'),
   ('hiroshige-shono','《庄野 白雨》（广重）','作品','art-asia','19世纪','日本','绘画','重要',
    '歌川广重《东海道五十三次》中的雨景，CMA（1948.306）与 V&A（O410702）各藏印本。','1833年',
    '以三层灰版表现竹林的空间深度，并把出版商名与系列名题写在旅人的伞面上。','ukiyo-e,japanese-art','cma-1948-306,vam-o410702'),
   ('hiroshige-ohashi-atake','《大桥安宅骤雨》（广重）','作品','art-asia','19世纪','日本','绘画','重要',
    '歌川广重《名所江户百景》之一，绘隅田川大桥上突遇阵雨的行人；CMA（1921.318）与 V&A（O420904）各藏印本。','1857年',
    '出版于1855年大地震与大火后两年，画面焦点是雨中仓皇遮护的行人与远处安宅一带。','ukiyo-e,japanese-art','cma-1921-318,vam-o420904')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
block=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
lines[close:close]=block
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended")

E={}
E["hokusai-red-fuji"]={"sections":{
 "时代背景":"富士山是日本最高峰，出现在19世纪多数日本旅行文学中；该馆说明指出，当时的地图有时以富士形的图标标示其位置，并标注旅人可获得最佳观景处的地点。据克利夫兰艺术博物馆的策展说明，北斋在1829至1833年间创作了描绘富士山三十六景的系列版画，本幅即其中之一，常被称为「赤富士」。",
 "风格特征":"该馆说明称，画中所取时节为夏末秋初之间，此时山体呈现偏红的色调。系列以同一座山在不同天气、不同角度下的样貌为主题，本幅以晴日南风为题，山体轮廓清晰、色彩偏赤，与同系列其他作品的雪景、雨景形成对照。",
 "代表人物与作品":"作者为葛饰北斋（1760—1849，据该馆创作者记录）。相关条目见浮世绘与日本艺术。英国维多利亚与艾尔伯特博物馆藏有同一构图的印本，题名《晴日南风（Gaifū kaisei）》，属《富岳三十六景》，纸本，高25.2厘米、宽37.4厘米。",
 "技法或形式分析":"作品为木版画（多色摺）。据 V&A 藏品记录，其馆藏印本为纸本，尺寸25.2 × 37.4厘米；克利夫兰的记录把创作年代定为1830年代初，未在该馆说明中给出本幅尺寸，故本条目不以尺寸比较两馆藏本。",
 "与前后风格的关系和争论":"本幅属浮世绘风景版画一路，与同系列其他作品共同构成对富士山的系列化观看；「赤富士」这一通称即出自该馆说明。关于两馆藏本是否为同一版次、以及各自印造先后，本条目未取得可核验材料。",
 "一图":"示意图以系列（1829—1833）、赤富士母题、两馆藏本三者关系标示本作品的位置。",
 "待核实":"（1）两馆藏本的关系（同版次或不同印次）未获来源判定，暂并列而不合并；（2）克利夫兰记录未给尺寸，故尺寸仅据 V&A 一家；（3）作者生卒1760—1849取自 CMA 创作者记录，未以第二来源核对；（4）「赤富士」「夏末秋初」等表述均出自 CMA 策展说明，属单一机构的解释。",
 },
 "diagram":{"nodes":[{"label":"北斋","sub":"1760—1849","kind":"muted"},{"label":"富岳三十六景","sub":"1829—1833","kind":"accent"},
   {"label":"赤富士","sub":"夏末秋初","kind":"muted"},{"label":"CMA / V&A","sub":"各藏印本","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":2,"to":3}],"caption":"《凯风快晴》：系列、母题与两馆藏本"},
 "sources":["cma-1930-189","vam-o129067"]}

E["hiroshige-shono"]={"sections":{
 "时代背景":"歌川广重（1797—1858）为《东海道五十三次》所作。该馆说明指出，东海道是自京都通往江户（今东京）的道路，广重曾以这条路为题材创作过多种不同的系列；本幅属1833年的那一组。",
 "风格特征":"该馆说明称，这一构图把握了雨的气氛，以及雨对两组旅人造成的影响。背景竹林中以三层灰色暗示距离，使画面在平面版画中取得纵深。",
 "代表人物与作品":"相关条目见浮世绘与日本艺术。英国维多利亚与艾尔伯特博物馆藏有同图印本，题名《庄野 白雨（Shōno, hakuu）》，纸本，高22.9厘米、宽34.9厘米。日本方面的收藏与其它印本情况本条目未取得来源。",
 "技法或形式分析":"据该馆说明，此图需要三块版才能印出背景竹林所用的三层灰——这直接说明多版套色如何在有限色数下构造空间层次。同一说明还指出，出版商名「Takenouchi」与系列名的一部分被写在某位旅人的伞面上，使文字成为画面叙事的一部分。",
 "与前后风格的关系和争论":"把文字题写融入画面（伞面上的出版信息）是这批商业版画的生产痕迹，也是版本研究的重要线索；该馆说明以之作为辨识依据。广重对同一道路的反复处理，构成其风景版画的主要脉络之一。",
 "一图":"示意图以东海的五十三次系列、三版套色的灰阶层次与两馆藏本三者关系标示本作品。",
 "待核实":"（1）两馆藏本是否为同一版次未获判定；尺寸仅据 V&A（22.9 × 34.9 cm），CMA 未在说明中给出；（2）作者生卒1797—1858取自 CMA 创作者记录；（3）「庄野」作为宿场的地理与史料细节该馆仅简述，未展开；（4）伞面题字的完整释文未取得。",
 },
 "diagram":{"nodes":[{"label":"广重","sub":"1797—1858","kind":"muted"},{"label":"东海道五十三次","sub":"1833","kind":"accent"},
   {"label":"三版三层灰","sub":"空间深度","kind":"muted"},{"label":"CMA / V&A","sub":"各藏印本","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":2,"to":3}],"caption":"《庄野 白雨》：系列、套色层次与两馆藏本"},
 "sources":["cma-1948-306","vam-o410702"]}

E["hiroshige-ohashi-atake"]={"sections":{
 "时代背景":"该馆说明指出，本幅出版于1855年大地震与大火灾之后两年，描绘的是江户（今东京）隅田川上新近重建的大桥。画面远处的安宅一带，是当时的街区名。",
 "风格特征":"该馆说明把此图视为广重捕捉大气状况的能力的例证：突降的雨幕中，桥上行人相向而行，各自设法遮护自己。斜向的雨线与桥的横向结构相交，构成画面的主导动势。",
 "代表人物与作品":"作者为歌川广重，属《名所江户百景》系列。相关条目见浮世绘与日本艺术。英国维多利亚与艾尔伯特博物馆藏有同图印本，题名《大桥安宅骤雨（Ōhashi Atake no yūdachi）》，纸本，高14.13厘米、宽9.04厘米。",
 "技法或形式分析":"作品为木版画。两馆记录的尺寸差异明显：V&A 藏本14.13 × 9.04厘米，明显小于通常的大判尺寸；CMA 的说明未给出其藏本尺寸。本条目据实并列两馆记录，不推断何者为初印。",
 "与前后风格的关系和争论":"本幅常被作为广重雨景表现的代表之一；它与《庄野 白雨》同属雨景母题，但一为东海道系列的旅人，一为江户名胜的桥上行众。关于本图在后世欧洲的接受情况，本条目未取得可核验来源。",
 "一图":"示意图以1855年震后重建、名所江户百景系列、两馆藏本（含尺寸差异）三者关系标示本作品。",
 "待核实":"（1）V&A 藏本14.13 × 9.04厘米与大判尺寸差距较大，是否为不同版次、缩印或裁切，缺来源判定；（2）CMA 藏本尺寸未取得；（3）作者生卒1797—1858取自 CMA 创作者记录；（4）该图在欧洲的接受史（如后世画家的临摹）虽有通说，但本条目未取得可核验来源，故未写入正文。",
 },
 "diagram":{"nodes":[{"label":"1855 震后","sub":"桥重建","kind":"muted"},{"label":"名所江户百景","sub":"1857","kind":"accent"},
   {"label":"雨景母题","sub":"桥上行众","kind":"muted"},{"label":"尺寸差异","sub":"14.1×9.0","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":2,"to":3}],"caption":"《大桥安宅骤雨》：震后重建、系列与藏本差异"},
 "sources":["cma-1921-318","vam-o420904"]}

for eid,spec in E.items():
    svg=render_svg(spec["diagram"],eid)
    json.dump({"id":eid,"level":"L2","sections":spec["sections"],"svg":svg,"sources":spec["sources"]},
              open(os.path.join(LD,eid+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("wrote",eid)