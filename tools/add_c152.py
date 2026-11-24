# -*- coding: utf-8 -*-
"""Cycle152：浪漫/新古典/写实 4 条（康斯太勃尔《布兰奇山池塘》/安格尔《安条克与斯特拉托尼斯》/米勒《田间归来》/柯罗《切尔瓦拉》）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1972-48","Cleveland Museum of Art — Branch Hill Pond, Hampstead, John Constable, 1828, acc. 1972.48",
  "https://openaccess-api.clevelandart.org/api/artworks/1972.48","2026-11-24 API HTTP 200；布面油画 画面60.6×78.1cm；说明含业余气象学家、1819-26租夏屋、乌云重于劳动者"),
 ("cma-1966-13","Cleveland Museum of Art — Antiochus and Stratonice, Jean-Auguste-Dominique Ingres, c. 1838, acc. 1966.13",
  "https://openaccess-api.clevelandart.org/api/artworks/1966.13","2026-11-24 API HTTP 200；亚麻布油画 画面48.1×63.9cm；说明含安条克病因、医生诊断、父亲让妻、1800年代颇受欢迎"),
 ("cma-1972-19","Cleveland Museum of Art — Return from the Fields, Jean-François Millet, c. 1846–47, acc. 1972.19",
  "https://openaccess-api.clevelandart.org/api/artworks/1972.19","2026-11-24 API HTTP 200；布面油画 画面46.2×37.8cm；说明含理想化农民生活、工业化与萧条、1848革命前怀旧；右下署 J. F. Millet"),
 ("cma-1963-91","Cleveland Museum of Art — La Cervara, the Roman Campagna, Jean Baptiste Camille Corot, c. 1830–31, acc. 1963.91",
  "https://openaccess-api.clevelandart.org/api/artworks/1963.91","2026-11-24 API HTTP 200；布面油画 画面97.6×135.8cm；说明含据写生与油画速写、1825-28居罗马、对角线构图、回想普桑古典风景"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('constable-branch-hill-pond','康斯太勃尔《汉普斯特德的布兰奇山池塘》（1828）','作品','art-neo-romantic','19世纪','欧洲','绘画','重要',
  '康斯太勃尔布面油画，汉普斯特德风景，克利夫兰艺术博物馆藏（1972.48）。','1828年',
  '康斯太勃尔是业余气象学家，最擅长精细观察云层、天气与自然光；他相信准确再现这些不断变化的因素，就能传达英国乡村的生机与壮丽；此画画于他1819—26年租住的汉普斯特德夏屋，重点放在深色雨云而非前景的劳动者，使其艰辛劳作的细节保持在悦目的远处。',
  'constable,turner-burning-parliament','cma-1972-48'),
 ('ingres-antiochus-stratonice','安格尔《安条克与斯特拉托尼斯》（约1838）','作品','art-neo-romantic','19世纪','欧洲','绘画','重要',
  '安格尔亚麻布油画，取材古代故事，克利夫兰艺术博物馆藏（1966.13）。','约1838年',
  '安条克患上神秘的病，卧床濒死；其父请来医生，医生发觉年轻女子斯特拉托尼斯一出现他的脉搏就加快，断定病因是激情，便向其父陈述；其父无私地把斯特拉托尼斯让给儿子；该题材既是爱情故事，又是父母之爱的典范，在1800年代很长时间内颇受欢迎。',
  'ingres,david-cupid-psyche','cma-1966-13'),
 ('millet-return-from-fields','米勒《田间归来》（约1846—47）','作品','art-neo-romantic','19世纪','欧洲','绘画','重要',
  '米勒布面油画，农民家庭题材，克利夫兰艺术博物馆藏（1972.19）。','约1846—1847年',
  '这是一幅对高尚农民生活的理想化描绘，作于法国剧烈工业化、经济萧条与农田荒弃之际；1840年代怀旧的农民场景特别受欢迎，与1848年革命中爆发的幻灭与紧张形成鲜明对比；画中家人的脸与形体模糊，使他们成为土地的象征而非个人。',
  'realism-art,courbet','cma-1972-19'),
 ('corot-la-cervara','柯罗《罗马平原的切尔瓦拉》（约1830—31）','作品','art-neo-romantic','19世纪','欧洲','绘画','重要',
  '柯罗布面大幅油画，罗马坎帕尼亚风景，克利夫兰艺术博物馆藏（1963.91）。','约1830—1831年',
  '此画依据户外所作的素描与油画速写完成；柯罗被意大利乡村之美吸引，1825至1828年住在罗马，常在罗马周边写生；画面结构严谨，形体沿一系列对角线向远处推进，是柯罗早期风格的特征，令人想起17世纪画家普桑的古典风景。',
  'constable,hackert-pozzuoli','cma-1963-91'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")
