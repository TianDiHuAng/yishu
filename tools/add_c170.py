# -*- coding: utf-8 -*-
"""Cycle170：瓦格纳题材美术作品 3 条（雷东×2 / 方丹-拉图尔）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1925-21","Cleveland Museum of Art — Odilon Redon, Parsifal, 1892, acc. 1925.21",
  "https://openaccess-api.clevelandart.org/api/artworks/1925.21","2026-11-24 API HTTP 200；石版画 画面32.2×24.2cm；石上署名ODILON REDON；说明含雷东从瓦格纳音乐汲取灵感、帕西法尔为1882年歌剧主人公、暗沉色调与茫然凝视营造神秘感、拉尔夫·金为该馆捐赠的首件"),
 ("cma-1945-389","Cleveland Museum of Art — Odilon Redon, Brünnhilde in Twilight of the Gods, 1894, acc. 1945.389",
  "https://openaccess-api.clevelandart.org/api/artworks/1945.389","2026-11-24 API HTTP 200；石版画 画面38×29.2cm；说明含雷东对瓦格纳音乐的热情、布伦希尔德为《尼伯龙根的指环》终章主要角色、石版与素描相近、背景花朵以线勾勒、脸部以交叉排线"),
 ("cma-1916-1038","Cleveland Museum of Art — Henri Fantin-Latour, Tannhäuser, 1886, acc. 1916.1038",
  "https://openaccess-api.clevelandart.org/api/artworks/1916.1038","2026-11-24 API HTTP 200；布面油画 画心86.4×103.3cm；右下署名Fantin 86；说明含坐在左侧的唐豪瑟似未投入欢愉场面、独处阴影、瓦格纳歌剧围绕世俗与神圣之爱的冲突"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('redon-parsifal','雷东《帕西法尔》（1892）','作品','art-neo-romantic','19世纪','法国','版画','重要',
  '雷东以瓦格纳歌剧主人公为题的石版画，克利夫兰艺术博物馆藏（1925.21）。','1892年',
  '该馆说明：与当时许多艺术家一样，雷东从瓦格纳的音乐中汲取灵感，并在多种媒介中探索它；此画描绘帕西法尔，即瓦格纳1882年歌剧的主人公，那是一部围绕寻找圣杯的歌剧；暗沉的色调与帕西法尔茫然的凝视共同营造出神秘感。',
  'wagner,romantic-music,opera','cma-1925-21'),
 ('redon-brunnhilde','雷东《诸神的黄昏中的布伦希尔德》（1894）','作品','art-neo-romantic','19世纪','法国','版画','重要',
  '雷东以《尼伯龙根的指环》人物为题的石版画，克利夫兰艺术博物馆藏（1945.389）。','1894年',
  '该馆说明：此画显示雷东对瓦格纳音乐的热情；布伦希尔德是瓦格纳四部连套歌剧《尼伯龙根的指环》终章的主要角色；雷东在大量试验并掌握石版之后作此画，画面显出石版与素描相近，背景的花朵用线勾出轮廓，布伦希尔德的脸用交叉排线提亮，再把蜡笔侧过来，把她的头发与胸口加深。',
  'wagner,romantic-music,opera','cma-1945-389'),
 ('fantin-latour-tannhauser','方丹-拉图尔《唐豪瑟》（1886）','作品','art-neo-romantic','19世纪','法国','油画','重要',
  '方丹-拉图尔取材瓦格纳歌剧的油画，克利夫兰艺术博物馆藏（1916.1038）。','1886年',
  '该馆说明：坐在左侧的男子是唐豪瑟，他似乎没有完全投入这个欢愉的场面，在苍白的身体与淡雅的色调之间，只有他笼罩在阴影里；启发这幅画的瓦格纳歌剧，主题是世俗之爱与神圣之爱的冲突，这种紧张感体现在神情阴郁的唐豪瑟身上。',
  'wagner,romantic-music,opera','cma-1916-1038'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
txt="\n".join(lines)
T=[t for t in T if "'%s'"%t[0] not in txt]
if T:
    close=max(i for i,l in enumerate(lines) if l.strip()=="]")
    lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
    io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
