# -*- coding: utf-8 -*-
"""Cycle79：中国绘画 4 条（巨然、牧溪龙、杜堇林逋、景泰菩萨十地）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1959-348","Cleveland Museum of Art — Juran, Buddhist Retreat by Stream and Mountains, 960–85, acc. 1959.348",
  "https://openaccess-api.clevelandart.org/api/artworks/1959.348","2026-11-23 API HTTP 200；绢本水墨立轴 184.5×56.1cm；说明含江南画派与南唐降宋"),
 ("cma-1958-427-1","Cleveland Museum of Art — Muqi Fachang, Dragon, c. 1250–79, acc. 1958.427.1",
  "https://openaccess-api.clevelandart.org/api/artworks/1958.427.1","2026-11-23 API HTTP 200；绢本水墨立轴 125.2×57.2cm；说明含阴阳对屏与禅寺语境"),
 ("cma-1954-582","Cleveland Museum of Art — Du Jin, The Poet Lin Bu Wandering in the Moonlight, late 1400s, acc. 1954.582",
  "https://openaccess-api.clevelandart.org/api/artworks/1954.582","2026-11-23 API HTTP 200；纸本设色立轴 156.4×72.4cm；说明含林逋生平与杜堇真迹之罕"),
 ("cma-1973-70-1","Cleveland Museum of Art — Bodhisattvas of the Ten Stages, 1454, acc. 1973.70.1",
  "https://openaccess-api.clevelandart.org/api/artworks/1973.70.1","2026-11-23 API HTTP 200；绢本设色立轴 140.8×79.3cm；说明含景泰五年金字题记与水陆法会")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('juran-buddhist-retreat','巨然《溪山兰若》','作品','art-china-painting','10世纪','中国','绘画','核心',
    '僧巨然绢本水墨立轴，克利夫兰艺术博物馆藏（1959.348）。','960—985年',
    '巨然与董源共开江南山水一派，以湿墨写平远雾景；其北迁开封后的面貌可见「北宋院体」式主峰。','zhao-mengfu-river-village,muqi-dragon','cma-1959-348'),
   ('muqi-dragon','牧溪《龙》（与《虎》对屏）','作品','art-china-painting','13世纪','中国','绘画','核心',
    '牧溪（法常）绢本水墨《龙》，克利夫兰艺术博物馆藏（1958.427.1），与《虎》成对。','约1250—1279年',
    '龙虎应阴阳互补之义；龙在层层波浪云气中探首，虎为近景强调体量；原为禅寺对屏，或夹护观音像。','juran-buddhist-retreat,ten-stages-bodhisattvas','cma-1958-427-1'),
   ('du-jin-lin-bu','杜堇《林逋行吟图》','作品','art-china-painting','15世纪','中国','绘画','核心',
    '杜堇纸本设色立轴，克利夫兰艺术博物馆藏（1954.582）。','1400年代末',
    '画北宋隐士林逋（967—1028）月下看梅；林逋以梅为妻、以鹤为子；杜堇署款真迹存世稀少，此为其一。','juran-buddhist-retreat,zhao-mengfu-river-village','cma-1954-582'),
   ('ten-stages-bodhisattvas','《菩萨十地》立轴（景泰五年）','作品','art-china-painting','15世纪','中国','绘画','核心',
    '明景泰五年绢本设色立轴，克利夫兰艺术博物馆藏（1973.70.1）。','1454年',
    '绘菩萨十地趋向佛果；与该馆另一轴同属水陆法会所用组画；右上钤玺并有金字题记，左下墨书记「奉旨所制」。','muqi-dragon,juran-buddhist-retreat','cma-1973-70-1')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")