# -*- coding: utf-8 -*-
"""Cycle44：新增 4 条浮世绘「同作品·双机构」条目。
《两国花火》《唐崎夜雨》（广重）、《源宗于朝臣》《柿本人麻吕》（北斋）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[
 ("cma-1940-986","Cleveland Museum of Art — Hiroshige, Fireworks at Ryōgoku, 1858, acc. 1940.986",
  "https://openaccess-api.clevelandart.org/api/artworks/1940.986","2026-11-23 API HTTP 200；sheet 33.7×22cm；说明含1850年代赞助放焰火背景"),
 ("vam-o420241","Victoria and Albert Museum — Ryōgoku Fireworks (Ryōgoku hanabi), O420241",
  "https://collections.vam.ac.uk/item/O420241/","2026-11-23 V&A API HTTP 200；题名含系列《江户名所百景》，36.2×24.8cm；该馆未记年代"),
 ("cma-1985-312","Cleveland Museum of Art — Hiroshige, Night Rain at Karasaki, c. 1835, acc. 1985.312",
  "https://openaccess-api.clevelandart.org/api/artworks/1985.312","2026-11-23 API HTTP 200；24.4×36.8cm；说明含唐崎松与和歌英译（Matthi Forrer 译）"),
 ("vam-o423295","Victoria and Albert Museum — Night Rain at Karasaki (Karasaki yau), O423295",
  "https://collections.vam.ac.uk/item/O423295/","2026-11-23 V&A API HTTP 200；题名含系列《近江八景》，22.9×35.6cm"),
 ("cma-1985-327","Cleveland Museum of Art — Hokusai, Poem by Minamoto no Muneyuki, 1835–36, acc. 1985.327",
  "https://openaccess-api.clevelandart.org/api/artworks/1985.327","2026-11-23 API HTTP 200；24.2×35.3cm；说明含系列构思与和歌英译"),
 ("vam-o422853","Victoria and Albert Museum — Poem by Minamoto no Muneyuki Ason, O422853",
  "https://collections.vam.ac.uk/item/O422853/","2026-11-23 V&A API HTTP 200；题名含系列《百人一首乳母绘解》，24.92×37.3cm"),
 ("cma-1930-190","Cleveland Museum of Art — Hokusai, Poem by Kakinomoto no Hitomaro, 1835–36, acc. 1930.190",
  "https://openaccess-api.clevelandart.org/api/artworks/1930.190","2026-11-23 API HTTP 200；25.8×37.8cm；说明含人麻吕生卒与和歌英译"),
 ("vam-o424258","Victoria and Albert Museum — Poem by Kakinomoto no Hitomaro, O424258",
  "https://collections.vam.ac.uk/item/O424258/","2026-11-23 V&A API HTTP 200；题名含系列《百人一首》，35.6×24.1cm（方向与 CMA 记录相反）"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":("Cleveland Museum of Art（开放数据 API）" if sid.startswith("cma") else "Victoria and Albert Museum（V&A API v2）"),
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('hiroshige-ryogoku-fireworks','《两国花火》（广重）','作品','art-asia','19世纪','日本','绘画','重要',
    '歌川广重《江户名所百景》之一，绘两国桥上空的焰火；CMA（1940.986）与 V&A（O420241）各藏印本。','1858年',
    '以近半幅画面描绘夜空与焰火，河岸茶屋与游船赞助的烟火在1850年代的江户吸引大量人群围观。','ukiyo-e,japanese-art','cma-1940-986,vam-o420241'),
   ('hiroshige-karasaki-night-rain','《唐崎夜雨》（广重）','作品','art-asia','19世纪','日本','绘画','重要',
    '歌川广重《近江八景》之一，绘琵琶湖畔唐崎松与夜雨；CMA（1985.312）与 V&A（O423295）各藏印本。','约1835年',
    '唐崎松为湖畔名胜，枝干以竹架支撑、下护神社；画面题咏和歌，将雨声与松名连在一起。','ukiyo-e,japanese-art','cma-1985-312,vam-o423295'),
   ('hokusai-muneyuki-poem','《源宗于朝臣》（北斋）','作品','art-asia','19世纪','日本','绘画','重要',
    '葛饰北斋《百人一首乳母绘解》之一；CMA（1985.327）与 V&A（O422853）各藏印本。','1835—36年',
    '系列以「乳母误解和歌」的视角作图，刻意错解典故，造成诗与画之间被视为滑稽的错位。','ukiyo-e,japanese-art,hokusai-red-fuji','cma-1985-327,vam-o422853'),
   ('hokusai-hitomaro-poem','《柿本人麻吕》（北斋）','作品','art-asia','19世纪','日本','绘画','重要',
    '葛饰北斋《百人一首乳母绘解》之一，取柿本人麻吕（约660—739）和歌；CMA（1930.190）与 V&A（O424258）各藏印本。','1835—36年',
    '画面与「长夜独眠」的和歌相配，属该系列以错解制造反差的典型手法。','ukiyo-e,japanese-art,hokusai-red-fuji','cma-1930-190,vam-o424258')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")

E={}
E["hiroshige-ryogoku-fireworks"]={"sections":{
 "时代背景":"两国桥横跨隅田川，连接江户（今东京）两岸热闹的街区，是广重版画中反复出现的题材（据克利夫兰艺术博物馆说明）。该馆指出，1850年代河岸的料理店与其他商家经常赞助焰火表演，这类表演吸引大量人群——桥上、岸边、茶屋与租用的游船上都挤满观者。",
 "风格特征":"该馆说明称，广重在此把**近一半画面**留给闪耀焰火的夜空。这一构图安排使「看火」这件事本身成为主体：桥、人群与水面退为陪衬，夜色与火光构成画面的主调。",
 "代表人物与作品":"作者歌川广重（1797—1858）。相关条目见浮世绘与日本艺术。英国维多利亚与艾尔伯特博物馆藏有同图印本，题名《两国花火（Ryōgoku hanabi）》，属《江户名所百景》，纸本，高36.2厘米、宽24.8厘米；该馆记录未给出年代。",
 "技法或形式分析":"克利夫兰记录本幅为纸本，sheet 尺寸33.7 × 22厘米。两馆尺寸略有差异（33.7×22 对 36.2×24.8），说明二者是不同印本，具体裁切与修边情况本条目未取得记录。",
 "与前后风格的关系和争论":"广重对同一座桥与同一片河面的反复处理，构成其江户名所系列的主线之一；焰火题材把商业赞助、城市娱乐与版画的销售结合起来，是该系列面向城市读者的直接证据。",
 "一图":"示意图以两国桥、焰火赞助与两馆藏本三者关系标示本作品。",
 "待核实":"（1）两馆藏本版次关系未判定，尺寸差异原因（裁切或印次）缺记录；（2）V&A 记录未给年代，「1858年」仅据 CMA 一家；（3）作者生卒1797—1858取自 CMA 创作者记录；（4）焰火赞助的具体商家名与场次该馆未列出。",
 },
 "diagram":{"nodes":[{"label":"两国桥","sub":"隅田川","kind":"muted"},{"label":"焰火·1858","sub":"近半幅夜空","kind":"accent"},
   {"label":"商家赞助","sub":"1850年代","kind":"muted"},{"label":"CMA / V&A","sub":"各藏印本","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":2,"to":1},{"from":1,"to":3}],"caption":"《两国花火》：桥、焰火与两馆藏本"},
 "sources":["cma-1940-986","vam-o420241"]}

E["hiroshige-karasaki-night-rain"]={"sections":{
 "时代背景":"唐崎松是琵琶湖畔的著名胜景，其枝干以竹架支撑，树下护有一座神社（据克利夫兰艺术博物馆说明）。本幅属广重的《近江八景》系列，该馆定年为约1835年。",
 "风格特征":"画面以夜雨为题，把松、湖畔与雨丝组织在同一视域中；该馆说明强调松树在景观与信仰两方面的地位。八景这一母题源自中国潇湘八景，在日本被反复移植到近江（琵琶湖）等地的实景上。",
 "代表人物与作品":"作者歌川广重。相关条目见浮世绘与日本艺术。英国维多利亚与艾尔伯特博物馆藏有同图印本，题名《唐崎夜雨（Karasaki yau）》，属《近江八景》，纸本，高22.9厘米、宽35.6厘米；该馆记录未给年代。",
 "技法或形式分析":"克利夫兰记录本幅24.4 × 36.8厘米；V&A 记录22.9 × 35.6厘米，二者为不同印本。画上题咏和歌，该馆附有英译（署名 Matthi Forrer 译），大意是：傍晚的雨中、渐近的晚风里，唐崎的松树因而得名。译文原为分行诗体，本条目只摘其意，不整段迻录。",
 "与前后风格的关系和争论":"把名胜与和歌并置，是八景类版画的常规做法；雨景在广重笔下反复出现（另见《庄野 白雨》），两幅的雨法不同：一为山间急雨，一为湖上夜雨。",
 "一图":"示意图以近江八景母题、唐崎松与两馆藏本三者关系标示本作品。",
 "待核实":"（1）V&A 记录未给年代，「约1835年」仅据 CMA；（2）和歌英译由该馆署名 Matthi Forrer，本条目未核原书；（3）两馆印本差异未判定；（4）唐崎松的社殿沿革该馆仅一句带过，未展开。",
 },
 "diagram":{"nodes":[{"label":"近江八景","sub":"母题来源","kind":"muted"},{"label":"唐崎夜雨","sub":"c.1835","kind":"accent"},
   {"label":"唐崎松·竹架","sub":"湖畔名所","kind":"muted"},{"label":"CMA / V&A","sub":"各藏印本","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"《唐崎夜雨》：八景母题与名所"},
 "sources":["cma-1985-312","vam-o423295"]}

E["hokusai-muneyuki-poem"]={"sections":{
 "时代背景":"该馆说明指出，北斋设计《百人一首乳母绘解》系列时，采取「一位困惑的乳母试图图解古典和歌、却错失其中微妙典故」的视角。这一设定并非失误，而是有意的设计。",
 "风格特征":"由于乳母「误解」和歌，画面与诗句之间形成当时读者会视为**滑稽的错位**（该馆用 comical disconnect）。也就是说，图像不是诗句的忠实插图，而是对误读的表演。",
 "代表人物与作品":"作者葛饰北斋（1760—1849）。本幅取源宗于朝臣的和歌。相关条目见浮世绘、日本艺术与《凯风快晴》。英国维多利亚与艾尔伯特博物馆藏有同图印本，题名《源宗于朝臣》，属《百人一首乳母绘解》，纸本，高24.92厘米、宽37.3厘米。",
 "技法或形式分析":"克利夫兰记录本幅24.2 × 35.3厘米；V&A 记录24.92 × 37.3厘米，属不同印本。该馆附有和歌英译，大意诉山中冬日的孤寂：草木枯萎、访客稀少，两皆断绝。译文原为分行诗体，本条目只述其意，不整段迻录。",
 "与前后风格的关系和争论":"以「误读」为结构原则的系列在浮世绘中并不多见；它与同一时期以典故精确取胜的做法相反，把错解本身做成卖点，可视为对古典教养的一种戏仿。",
 "一图":"示意图以百人一首母题、乳母误读的构思与两馆藏本三者关系标示本作品。",
 "待核实":"（1）V&A 记录未给年代，「1835—36年」仅据 CMA；（2）和歌原文与英译的分行情形本条目未迻录，仅存其意；（3）「滑稽错位」是该馆的解释，未与日本学界研究对照；（4）该系列总幅数与该图在系列中的序号未取得。",
 },
 "diagram":{"nodes":[{"label":"百人一首","sub":"母题","kind":"muted"},{"label":"乳母误读","sub":"结构原则","kind":"accent"},
   {"label":"诗画错位","sub":"滑稽","kind":"muted"},{"label":"CMA / V&A","sub":"各藏印本","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":1,"to":3}],"caption":"《源宗于朝臣》：误读结构与诗画错位"},
 "sources":["cma-1985-327","vam-o422853"]}

E["hokusai-hitomaro-poem"]={"sections":{
 "时代背景":"该馆说明指出，北斋此系列以「困惑的乳母图解古典和歌」为设定，图像与诗句之间常出现有意的错位。本幅取柿本人麻吕（约660—739，据该馆说明）的和歌。",
 "风格特征":"与《源宗于朝臣》同属一个系列，画面服务于「误读」的结构：和歌写长夜独眠的漫长，图像则以可见的物象把「长」具体化，二者之间的对不上正是趣味所在。",
 "代表人物与作品":"作者葛饰北斋。相关条目见浮世绘、日本艺术与《凯风快晴》。英国维多利亚与艾尔伯特博物馆藏有同图印本，题名《柿本人麻吕》，纸本；该馆记录的尺寸为高35.6厘米、宽24.1厘米，与 CMA 记录（25.8×37.8）方向相反，属不同印本或著录方向差异。",
 "技法或形式分析":"克利夫兰记录本幅25.8 × 37.8厘米。该馆附有和歌英译，大意以「山鸟的长尾」比喻漫长秋夜，写独眠之苦；译文原为分行诗体，本条目只述其意，不整段迻录。",
 "与前后风格的关系和争论":"同一系列内两幅（本幅与《源宗于朝臣》）显示了北斋处理古典和歌的一致策略：把文本的权威交给「不可靠的图解者」，让错读成为画面的一部分。",
 "一图":"示意图以百人一首母题、人麻吕和歌与两馆藏本三者关系标示本作品。",
 "待核实":"（1）V&A 记录未给年代且尺寸方向与 CMA 相反，二者关系需目验判定；（2）「1835—36年」仅据 CMA；（3）人麻吕生卒约660—739取自该馆说明，未以第二来源核对；（4）和歌原文未迻录。",
 },
 "diagram":{"nodes":[{"label":"人麻吕和歌","sub":"约660—739","kind":"muted"},{"label":"乳母绘解","sub":"1835—36","kind":"accent"},
   {"label":"长夜独眠","sub":"图像具体化","kind":"muted"},{"label":"CMA / V&A","sub":"尺寸方向相反","kind":"muted"}],
  "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":2,"to":3}],"caption":"《柿本人麻吕》：和歌、误读与藏本差异"},
 "sources":["cma-1930-190","vam-o424258"]}

for eid,spec in E.items():
    svg=render_svg(spec["diagram"],eid)
    json.dump({"id":eid,"level":"L2","sections":spec["sections"],"svg":svg,"sources":spec["sources"]},
              open(os.path.join(LD,eid+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("wrote",eid)