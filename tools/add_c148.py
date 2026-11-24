# -*- coding: utf-8 -*-
"""Cycle148：非洲艺术 4 条（Xhosa 烟斗 / 权杖 / Totem 2018 / 王室串珠吊坠）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-2010-199","Cleveland Museum of Art — Pipe, Xhosa-style maker(s), 1800s–1900s, acc. 2010.199",
  "https://openaccess-api.clevelandart.org/api/artworks/2010.199","2026-11-24 API HTTP 200；木、铜、玻璃珠、筋线、皮革 全长20.3cm；说明含母亲背负婴儿用长柄烟斗与祖先/生育关联"),
 ("cma-2010-205","Cleveland Museum of Art — Prestige Staff, Tsonga-style or Zulu-style maker, 1800s–1900s, acc. 2010.205",
  "https://openaccess-api.clevelandart.org/api/artworks/2010.205","2026-11-24 API HTTP 200；木 全长116.8cm；说明含牧牛者行路手杖与身份标示"),
 ("cma-2018-5","Cleveland Museum of Art — Totem 01/01-18 (Baga-Batcham-Alunga-Kota), 2018, acc. 2018.5",
  "https://openaccess-api.clevelandart.org/api/artworks/2018.5","2026-11-24 API HTTP 200；木、玻璃珠、线、胶、硅胶 188×53×38cm；说明含四种经典非洲面具/雕像形式的叠合与分类、商品化批评"),
 ("cma-2022-49-c","Cleveland Museum of Art — Royal ceremonial beadwork: pendant, Xhosa-style maker(s), 1800s, acc. 2022.49.c",
  "https://openaccess-api.clevelandart.org/api/artworks/2022.49.c","2026-11-24 API HTTP 200；玻璃珠、筋线、陶 22.9×7.3cm；说明含威尼斯/波希米亚进口珠、1770—1829年珠作货币"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('xhosa-beaded-pipe','科萨风格串珠烟斗（19—20世纪）','作品','art-africa','19—20世纪','非洲','综合','重要',
  '南非科萨风格木制长柄烟斗，饰铜、玻璃珠与皮革，克利夫兰艺术博物馆藏（2010.199）。','1800年代—1900年代',
  '长柄便于母亲背着婴儿时把烟引开；男子雕刻、女性制作者加串珠流苏，配色为科萨串珠的典型；流苏下悬一件微型围裙，暗示女主人身份。',
  'xhosa-beadwork-pendant,benin-plaque','cma-2010-199'),
 ('southern-african-prestige-staff','南部非洲权杖（楚松加或祖鲁风格）','作品','art-africa','19—20世纪','非洲','雕塑','重要',
  '南非楚松加或祖鲁风格的整木权杖，克利夫兰艺术博物馆藏（2010.205）。','1800年代—1900年代',
  '用途首先是实用：牧民随牛群迁徙时的行路伴侣；杖身之高标示持有者的地位或职能；球形杖头与螺旋段、链环几何纹显示工匠技艺。',
  'xhosa-beaded-pipe,benin-ancestral-head','cma-2010-205'),
 ('totem-01-01-18','《图腾 01/01-18》（巴加—巴查姆—阿伦加—科塔，2018）','作品','art-africa','21世纪','非洲','雕塑','重要',
  '喀麦隆当代艺术家以四种经典非洲面具与雕像形式叠合的木雕，克利夫兰艺术博物馆藏（2018.5）。','2018年',
  '科塔—马洪圭守护像坐于巴查姆 tsesah 面具之上，面具背后是本贝阿伦加社团面具，底座为巴加 d’mba 头饰；以叠合挑战分类、商品化与市场/博物馆的价值体系。',
  'benin-ancestral-head,southern-african-prestige-staff','cma-2018-5'),
 ('xhosa-beadwork-pendant','科萨王室礼仪串珠吊坠（19世纪）','作品','art-africa','19世纪','非洲','综合','重要',
  '南非东南开普地区科萨风格玻璃珠吊坠，克利夫兰艺术博物馆藏（2022.49.c）。','1800年代',
  '精英女性在节庆场合穿戴的串珠服饰，几乎全用进口威尼斯或波希米亚玻璃珠，是明确的地位象征；制作者选用色泽形状大小一致的上等珠。',
  'xhosa-beaded-pipe,benin-plaque','cma-2022-49-c'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")
