# -*- coding: utf-8 -*-
"""Cycle52：新增 5 条。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1975-168","Cleveland Museum of Art — Pair of Masks (Gẹ̀lẹ̀dẹ́), Yorùbá, c. 1945–50, acc. 1975.168",
  "https://openaccess-api.clevelandart.org/api/artworks/1975.168","2026-11-23 API HTTP 200；木与颜料；两件高77.7/86cm；说明含 Ìyá Nlá 与 Duga 名声"),
 ("cma-1990-22","Cleveland Museum of Art — Memorial head (nsodie), Akan style, late 1600s–early 1700s, acc. 1990.22",
  "https://openaccess-api.clevelandart.org/api/artworks/1990.22","2026-11-23 API HTTP 200；赤陶 19.1×13.6×15.5cm；作者记为 unknown female ceramicist"),
 ("cma-1946-226","Cleveland Museum of Art — Mantle, Paracas (Cavernas) style, c. 300 BCE–200 CE, acc. 1946.226",
  "https://openaccess-api.clevelandart.org/api/artworks/1946.226","2026-11-23 API HTTP 200；驼科纤维平织加刺绣 154.9×292.1cm"),
 ("cma-1952-233","Cleveland Museum of Art — Backrest of a Litter, Chimú, 1185–1275 (radiocarbon), acc. 1952.233",
  "https://openaccess-api.clevelandart.org/api/artworks/1952.233","2026-11-23 API HTTP 200；木、金合金、颜料、贝壳镶嵌 60.4×95cm"),
 ("cma-2025-180","Cleveland Museum of Art — Celadon Cup with Molded Lotus Petal Design, Goryeo, 1100s–1200s, acc. 2025.180",
  "https://openaccess-api.clevelandart.org/api/artworks/2025.180","2026-11-23 API HTTP 200；青瓷 高11cm 口径10.7cm；说明含随葬组合")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('yoruba-gelede-masks','约鲁巴 Gelede 成对面具','作品','art-africa','20世纪','非洲','雕塑','重要',
    '尼日利亚约鲁巴人 Gelede 社的成对面具，克利夫兰艺术博物馆藏（1975.168）。','约1945—50年',
    '由男性在年度化装游行中佩戴，敬奉「大母」Ìyá Nlá；面具塑「美丽少女」，头巾上栖鳄鱼，尾节可摆动。','asante-memorial-head,african-art','cma-1975-168'),
   ('asante-memorial-head','阿散蒂纪念头像（nsodie）','作品','art-africa','17—18世纪','非洲','雕塑','重要',
    '加纳阿坎（Asante）风格的赤陶纪念头像，克利夫兰艺术博物馆藏（1990.22）。','约17世纪末—18世纪初',
    '王室在世时委托女性艺人依记忆塑像，逝后置于圣林；理想化的贵人形貌与个人细节并存。','yoruba-gelede-masks,african-art','cma-1990-22'),
   ('paracas-mantle','帕拉卡斯披巾','作品','art-americas','公元前3—公元2世纪','美洲','综合','重要',
    '秘鲁南岸帕拉卡斯（Cavernas）风格驼科纤维披巾，克利夫兰艺术博物馆藏（1946.226）。','约公元前300—公元200年',
    '竖穴墓中以多层织物裹尸并随葬器物；干燥环境保存了大量织物；双头鸟纹以红蓝黄绿绣线构成。','chimu-litter-backrest,americas-art','cma-1946-226'),
   ('chimu-litter-backrest','奇穆抬舆靠背','作品','art-americas','12—13世纪','美洲','综合','重要',
    '秘鲁北岸奇穆文化的抬舆靠背，克利夫兰艺术博物馆藏（1952.233）。','放射性碳测年 1185—1275（95.4%）',
    '抬舆由人力肩抬，是无畜力与车轮社会里尊者的交通方式；图中人物或为奇穆领主与四名官员。','paracas-mantle,americas-art','cma-1952-233'),
   ('goryeo-celadon-cup','高丽青瓷莲瓣纹盏','作品','art-asia','12世纪','东亚','综合','重要',
    '高丽王朝青瓷盏，克利夫兰艺术博物馆藏（2025.180）；模印莲瓣纹。','1100—1200年代',
    '日用青瓷是高丽墓葬中最常见的随葬品之一；以成套器物随葬被视为敬奉亡者、供其身后所需。','goryeo-celadon-bottle,kammavacha-manuscript','cma-2025-180')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 5")