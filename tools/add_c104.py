# -*- coding: utf-8 -*-
"""Cycle104：印象/后印象 4 条（梵高×3 异媒介 + 毕沙罗）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1947-209","Cleveland Museum of Art — Vincent van Gogh, The Large Plane Trees (Road Menders at Saint-Rémy), 1889, acc. 1947.209",
  "https://openaccess-api.clevelandart.org/api/artworks/1947.209","2026-11-23 API HTTP 200；布面油画 73.4×91.8cm；说明含圣雷米疗养院与致提奥书信"),
 ("cma-1948-303","Cleveland Museum of Art — Vincent van Gogh, Dr. Gachet, 1890, acc. 1948.303",
  "https://openaccess-api.clevelandart.org/api/artworks/1948.303","2026-11-23 API HTTP 200；蚀刻与干刻 18.1×15.2cm；说明含梵高唯一蚀刻版与皮萨罗推荐"),
 ("cma-1990-7","Cleveland Museum of Art — Camille Pissarro, The Lock at Pontoise, 1872, acc. 1990.7",
  "https://openaccess-api.clevelandart.org/api/artworks/1990.7","2026-11-23 API HTTP 200；布面油画 53×83cm；说明含户外快速写生与碎笔触"),
 ("cma-1958-30","Cleveland Museum of Art — Vincent van Gogh, Landscape with Wheelbarrow, 1883, acc. 1958.30",
  "https://openaccess-api.clevelandart.org/api/artworks/1958.30","2026-11-23 API HTTP 200；水彩与不透明水彩 24.9×35.7cm；说明含德伦特荒原与致提奥书信"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('van-gogh-plane-trees','梵高《大悬铃木（圣雷米修路工）》','作品','art-impression','19世纪','欧洲','绘画','核心',
  '梵高布面油画，克利夫兰艺术博物馆藏（1947.209）。','1889年',
  '圣雷米疗养院时期；医生准其户外写生以缓解抑郁；致提奥信中描述村中巨木与修路景象。','post-impressionism,van-gogh-dr-gachet','cma-1947-209'),
 ('van-gogh-dr-gachet','梵高《加歇医生》（蚀刻）','作品','art-impression','19世纪','欧洲','版画','核心',
  '梵高蚀刻与干刻版画，克利夫兰艺术博物馆藏（1948.303）。','1890年',
  '去世前两个月作，是梵高**唯一**的蚀刻作品；经毕沙罗推荐投加歇医生，医生赠铜版并助其手压印制。','van-gogh-plane-trees,post-impressionism','cma-1948-303'),
 ('pissarro-lock-pontoise','毕沙罗《蓬图瓦兹水闸》','作品','art-impression','19世纪','欧洲','绘画','核心',
  '毕沙罗布面油画，克利夫兰艺术博物馆藏（1990.7）。','1872年',
  '印象派户外快速写生的开创者之一；急流与阴天以纯色碎笔触写成，或不打草稿一次完成。','impressionism,monet','cma-1990-7'),
 ('van-gogh-drenthe-wheelbarrow','梵高《德伦特风景（手推车）》','作品','art-impression','19世纪','欧洲','绘画','重要',
  '梵高水彩与不透明水彩画，克利夫兰艺术博物馆藏（1958.30）。','1883年',
  '1883年离海牙赴德伦特荒原；以钢绿与冷蓝的有限色盘写「广袤平原没入无限」，天光泛淡紫。','van-gogh-plane-trees,post-impressionism','cma-1958-30'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")