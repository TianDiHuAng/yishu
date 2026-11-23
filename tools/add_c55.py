# -*- coding: utf-8 -*-
"""Cycle55：新增 5 条（朝鲜朝白瓷四字罐、粉青刻花壶、刚果权贵帽、刚果十字架、泰东北窑果形罐）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1981-3","Cleveland Museum of Art — Jar with Four Auspicious Characters, Joseon, 1800s, acc. 1981.3",
  "https://openaccess-api.clevelandart.org/api/artworks/1981.3","2026-11-23 API HTTP 200；釉瓷 高19.4cm 径22.1cm；说明含1981年自东京古美术商购入与殖民期背景"),
 ("cma-1921-649","Cleveland Museum of Art — Wine Flask with Incised and Sgraffito Peony Design (Buncheong), 1500s, acc. 1921.649",
  "https://openaccess-api.clevelandart.org/api/artworks/1921.649","2026-11-23 API HTTP 200；粉青石陶 高22.6cm；说明含铁分高的粗炼土与高丽技法沿用"),
 ("cma-1997-180","Cleveland Museum of Art — Prestige Cap (mpu ngola), Kongo style, late 1800s–early 1900s, acc. 1997.180",
  "https://openaccess-api.clevelandart.org/api/artworks/1997.180","2026-11-23 API HTTP 200；拉菲草与豹爪 42×19.3×19cm；说明含1607年以来的记载与修复支架"),
 ("cma-2010-444","Cleveland Museum of Art — Crucifix, Kongo style, late 1800s–early 1900s, acc. 2010.444",
  "https://openaccess-api.clevelandart.org/api/artworks/2010.444","2026-11-23 API HTTP 200；铜合金、木、包钉、铁 44.7×22.2×3.2cm；说明含1491年改宗与 dikenga 符号"),
 ("cma-1983-156","Cleveland Museum of Art — Jar in the Shape of a Fruit, Khmer ware, 1100s, acc. 1983.156",
  "https://openaccess-api.clevelandart.org/api/artworks/1983.156","2026-11-23 API HTTP 200；施釉陶带褐化妆土 高24cm；说明含泰东北窑与果种待定")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('joseon-auspicious-jar','朝鲜朝白瓷四字纹罐','作品','art-asia','19世纪','东亚','综合','重要',
    '朝鲜王朝白瓷罐，克利夫兰艺术博物馆藏（1981.3）；四字吉语各置于花形开光内。','1800年代',
    '四字寓长寿、福、康宁、平安；此类罐常作寿礼与婚礼赠品；本件1981年购自东京古美术商。','joseon-buncheong-flask,joseon-hollyhock-cup','cma-1981-3'),
   ('joseon-buncheong-flask','朝鲜朝粉青刻花酒壶','作品','art-asia','16世纪','东亚','综合','重要',
    '朝鲜王朝粉青（buncheong）石陶酒壶，克利夫兰艺术博物馆藏（1921.649）。','1500年代',
    '粉青意为「粉绿」，因用铁分高的粗炼土而呈灰青釉；沿用高丽的白化妆土、镶嵌、印花与刻划技法。','joseon-auspicious-jar','cma-1921-649'),
   ('kongo-prestige-cap','刚果权贵帽（mpu ngola）','作品','art-africa','19—20世纪','非洲','综合','重要',
    '刚果风格拉菲草编帽，缘饰豹爪，克利夫兰艺术博物馆藏（1997.180）。','1800年代末—1900年代初',
    '此类编帽为高位男子所戴，豹爪以其「领地之主」的品性比拟佩戴者；纹样在刚果、维利、尤姆贝诸族共通。','kongo-crucifix,african-art','cma-1997-180'),
   ('kongo-crucifix','刚果十字架','作品','art-africa','19—20世纪','非洲','综合','重要',
    '刚果王国以木与金属制成的十字架，克利夫兰艺术博物馆藏（2010.444）。','1800年代末—1900年代初',
    '1491年国王改宗后天主教成为刚果国教；此像作于其后数世纪，基督结刚果式发辫；腰布上的 X 形纹指 dikenga。','kongo-prestige-cap,african-art','cma-2010-444'),
   ('khmer-thai-fruit-jar','泰东北窑果形罐','作品','art-asia','12世纪','东南亚','综合','重要',
    '柬埔寨／泰东北窑的施釉陶罐，克利夫兰艺术博物馆藏（1983.156）。','1100年代',
    '深褐釉、胎厚，盖沿下方刻波纹，盖上作卷曲果柄为钮；所拟果种难以判定，或为瓜类。','angkor,champa-apsara-bracket','cma-1983-156')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 5")