# -*- coding: utf-8 -*-
"""Cycle47：新增 3 单元（非洲/美洲/大洋洲）+ 6 件作品条目。
材料来源为 CMA 藏品记录与策展说明；其中贝宁两件涉及殖民攫取、阿兹特克羽蛇被该馆记为可能伪作，均如实写出。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1999-1","Cleveland Museum of Art — Plaque, Benin Kingdom, 1500s–1600s, acc. 1999.1",
  "https://openaccess-api.clevelandart.org/api/artworks/1999.1","2026-11-23 API HTTP 200；铜合金 45.7×38.1cm；说明含1897年英军取走与1898年入不列颠博物馆"),
 ("cma-1938-6","Cleveland Museum of Art — Ancestral Commemorative Head, Benin Kingdom, acc. 1938.6",
  "https://openaccess-api.clevelandart.org/api/artworks/1938.6","2026-11-23 API HTTP 200；铜合金与铁 29.9×21.6×20.4cm；说明含祭祖功能与今日陈列的对比"),
 ("cma-1967-29","Cleveland Museum of Art — Front Face of a Stela, El Perú-Waka', Maya, 692 CE, acc. 1967.29",
  "https://openaccess-api.clevelandart.org/api/artworks/1967.29","2026-11-23 API HTTP 200；石灰岩 274.4×182.3cm；说明含 k'atun 纪年与统治者身份"),
 ("cma-1941-46","Cleveland Museum of Art — Feathered Serpent (Quetzalcoatl), Aztec, acc. 1941.46",
  "https://openaccess-api.clevelandart.org/api/artworks/1941.46","2026-11-23 API HTTP 200；石材 27.7×20.1×22cm；说明明确讨论真伪存疑"),
 ("cma-1954-147","Cleveland Museum of Art — Pendant (Hei-tiki), Maori, 1800s, acc. 1954.147",
  "https://openaccess-api.clevelandart.org/api/artworks/1954.147","2026-11-23 API HTTP 200；软玉 11.2×5.5cm；说明含 mana 与 Hine-te-Iwaiwa"),
 ("cma-1963-554","Cleveland Museum of Art — War Shield, Asmat, c. 1940, acc. 1963.554",
  "https://openaccess-api.clevelandart.org/api/artworks/1963.554","2026-11-23 API HTTP 200；彩绘木 176.5×60.3×7cm；说明含猎首宴与红树根取材")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

p=os.path.join(ROOT,"tools","catalog.py"); s=io.open(p,encoding="utf-8").read()
for unit_id,unit_name,after in [("art-africa","非洲艺术（撒哈拉以南）","art-islamic"),("art-americas","美洲原住民与前哥伦布艺术","art-africa"),("art-oceania","太平洋艺术（大洋洲）","art-americas")]:
    if '"%s"'%unit_id not in s:
        anchor=' ("work-archives","作品档案"),\n])'
        assert anchor in s
        s=s.replace(anchor,' ("%s","%s"),\n'%(unit_id,unit_name)+anchor)
io.open(p,"w",encoding="utf-8").write(s)
print("units added")

T=[('benin-plaque','贝宁宫庭铜牌（两名侍从扶王）','作品','art-africa','15—16世纪','非洲','综合','重要',
    '尼日利亚贝宁王国Ẹdo族王室铸造行会所作铜合金牌饰，克利夫兰艺术博物馆藏（1999.1）。','1500—1600年代',
    '构图以等级安排大小：王者居中且形体更大；两名侍从自两侧扶持被重礼服饰压住的王。','benin-ancestral-head,islamic-art','cma-1999-1'),
   ('benin-ancestral-head','贝宁祖灵纪念头像（uhunmwun-elao）','作品','art-africa','16世纪','非洲','雕塑','重要',
    '贝宁王国Ẹdo族王室铸造行会所作铜合金与铁头像，克利夫兰艺术博物馆藏（1938.6）。','约16世纪中或17世纪初',
    '新王为先王设祭坛时所铸；珊瑚珠层叠于颈，面部理想化，厚铸的头部原承象牙。','benin-plaque,islamic-art','cma-1938-6'),
   ('maya-el-peru-stela','埃尔佩鲁石碑正面（瓦卡）','作品','art-americas','7世纪','美洲','雕塑','重要',
    '危地马拉佩滕省埃尔佩鲁（El Perú-Waka’）玛雅古典期石灰岩石碑，克利夫兰艺术博物馆藏（1967.29）。','692年',
    '刻一位女性统治者，纪念二十年周期 k’atun 的通过；头饰用绿咬鹃羽毛、佩饰可能为玉，或曾掌军政。','aztec-feathered-serpent','cma-1967-29'),
   ('aztec-feathered-serpent','阿兹特克羽蛇（克察尔科亚特尔）','作品','art-americas','15—16世纪','美洲','雕塑','重要',
    '中墨西哥阿兹特克风格石雕，克利夫兰艺术博物馆藏（1941.46）；该馆明确讨论其真伪存疑。','1325—1521年（或为近代）',
    '盘绕躯体呈胸肌、膝与臀的隆起，状若人披蛇装；面具与真实阿兹特克蛇像惯例不合。','maya-el-peru-stela','cma-1941-46'),
   ('maori-hei-tiki','毛利吊坠（hei-tiki）','作品','art-oceania','19世纪','大洋洲','雕塑','重要',
    '新西兰毛利人软玉吊坠，克利夫兰艺术博物馆藏（1954.147）。','1800年代',
    '为承载 mana（威望与灵力）的祖传之物，连接生者与前欧洲时代的祖先；或指传说女性始祖 Hine-te-Iwaiwa。','asmat-war-shield','cma-1954-147'),
   ('asmat-war-shield','阿斯马特战盾','作品','art-oceania','20世纪','大洋洲','综合','重要',
    '伊里安查亚阿斯马特人所制彩绘木盾，克利夫兰艺术博物馆藏（1963.554）。','约1940年',
    '以红树板根雕成，白（石灰）、红（赭石）、黑（炭）三色；蹲踞祖先与食果动物纹样，以果喻人头。','maori-hei-tiki','cma-1963-554')]
lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 6")