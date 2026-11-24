# -*- coding: utf-8 -*-
"""Cycle150：印象派 4 条（莫奈《红头巾》/《普尔维尔的低潮》、莫里索《阅读》、雷诺阿《卖苹果的女人》）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1958-39","Cleveland Museum of Art — The Red Kerchief, Claude Monet, c. 1868–73, acc. 1958.39",
  "https://openaccess-api.clevelandart.org/api/artworks/1958.39","2026-11-24 API HTTP 200；布面油画 画面99×79.8cm；说明含卡米耶、阿尔让特伊、雪日、粗放笔触；题款：未署名"),
 ("cma-1947-196","Cleveland Museum of Art — Low Tide at Pourville, near Dieppe, 1882, Claude Monet, acc. 1947.196",
  "https://openaccess-api.clevelandart.org/api/artworks/1947.196","2026-11-24 API HTTP 200；布面油画 画面59.9×81.3cm；说明含诺曼底渔村普尔维尔、书信引文、1882年春住小旅馆；署名右下 82 Claude Monet"),
 ("cma-1950-89","Cleveland Museum of Art — Reading, Berthe Morisot, 1873, acc. 1950.89",
  "https://openaccess-api.clevelandart.org/api/artworks/1950.89","2026-11-24 API HTTP 200；布面油画 画面46×71.8cm；说明含姐姐埃德玛为模特、X光显示眼神被改、与马奈人物对比"),
 ("cma-1958-47","Cleveland Museum of Art — The Apple Seller, Pierre-Auguste Renoir, c. 1890, acc. 1958.47",
  "https://openaccess-api.clevelandart.org/api/artworks/1958.47","2026-11-24 API HTTP 200；布面油画 画面65.8×54.5cm；说明含妻子阿琳、侄子埃德蒙、埃索瓦；题款 a. renoir / 1864 与定年约1890并存，该馆未解释"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('monet-red-kerchief','莫奈《红头巾》（约1868—73）','作品','art-impression','19世纪','欧洲','绘画','重要',
  '莫奈布面油画，画他的第一任妻子卡米耶，克利夫兰艺术博物馆藏（1958.39）。','约1868—1873年',
  '雪日里卡米耶经过阿让特伊住宅的落地窗外；脸部以寥寥几笔快速涂抹，雪与树以粗放断续的纯白与纯绿笔触定形，技法大胆；该馆记录未署名。',
  'monet,impressionism','cma-1958-39'),
 ('monet-low-tide-pourville','莫奈《普尔维尔的低潮》（1882）','作品','art-impression','19世纪','欧洲','绘画','重要',
  '莫奈布面油画，诺曼底渔村普尔维尔海景，克利夫兰艺术博物馆藏（1947.196）。','1882年',
  '莫奈画过数幅普尔维尔，村里有木栈道、宽阔海滩与壮丽悬崖；据其书信，村子本身平平，但风景打动了他，海浪就拍在屋脚；1882年春他住在类似画中悬崖右下小屋的小旅馆。',
  'monet,pissarro-lock-pontoise','cma-1947-196'),
 ('morisot-reading','莫里索《阅读》（1873）','作品','art-impression','19世纪','欧洲','绘画','重要',
  '莫里索布面油画，以姐姐埃德玛为模特，克利夫兰艺术博物馆藏（1950.89）。','1873年',
  '女子坐在披肩上、视线落在书页，阳伞与扇子丢在草地；白裙映出户外的光影，花纹呼应草地野花；X光显示莫里索改过眼神，原本直视观者，近似马奈的人物处理；而她的人物多专注于事务或私下沉思。',
  'manet,impressionism','cma-1950-89'),
 ('renoir-apple-seller','雷诺阿《卖苹果的女人》（约1890）','作品','art-impression','19世纪','欧洲','绘画','重要',
  '雷诺阿布面油画，乡下女孩向画家之妻阿琳递苹果，克利夫兰艺术博物馆藏（1958.47）。','约1890年',
  '戴草帽的男孩可能是画家的侄子埃德蒙，戴发带的小女孩身份未明；柔和斑驳的阳光中，流畅笔触把人物连成一体，跃起的小狗添一点幽默与动势；该馆推测应完成于东法的埃索瓦。',
  'degas,impressionism','cma-1958-47'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")
