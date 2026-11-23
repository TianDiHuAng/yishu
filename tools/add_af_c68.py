# -*- coding: utf-8 -*-
"""Cycle68：非洲再补 4 条（Vili 象牙雕、阿散蒂金刀鞘、约鲁巴门廊柱、Ifá 项链）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

NEWS=[("cma-1969-138","Cleveland Museum of Art — Carving (ivory tusk), Kongo/Vili, c. 1900, acc. 1969.138",
  "https://openaccess-api.clevelandart.org/api/artworks/1969.138","2026-11-23 API HTTP 200；象牙 17.8cm；说明含欧洲客户与自我再现"),
 ("cma-1935-312","Cleveland Museum of Art — Knife-sheath tip (sika boha), Asante, 1800s, acc. 1935.312",
  "https://openaccess-api.clevelandart.org/api/artworks/1935.312","2026-11-23 API HTTP 200；金 8.7cm；说明含 kra 生命之力与 repoussé 技法"),
 ("cma-1969-55","Cleveland Museum of Art — Veranda Post (Òpó), Yorùbá (probably Ekiti), early–mid 1900s, acc. 1969.55",
  "https://openaccess-api.clevelandart.org/api/artworks/1969.55","2026-11-23 API HTTP 200；木等 106.6cm；说明含权力分配主题"),
 ("cma-1995-23","Cleveland Museum of Art — Ifá diviner's necklace (òdìgbà Ifá), Yorùbá, 1900s, acc. 1995.23",
  "https://openaccess-api.clevelandart.org/api/artworks/1995.23","2026-11-23 API HTTP 200；布、玻璃珠等 49.5cm；说明含 òrún 与护身小袋")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

T=[('vili-ivory-tusk','维利象牙雕刻（殖民期纪念品）','作品','art-africa','19—20世纪','非洲','雕塑','重要',
    '刚果／维利雕刻者所作小象牙雕，克利夫兰艺术博物馆藏（1969.138）。','约1900年',
    '为欧洲客户而作的「纪念品」，却也在其中选择性地再现刚果人的衣着——自本地腰布到欧洲呢帽。','kongo-nkisi-nkondi,african-art','cma-1969-138'),
   ('asante-knife-sheath','阿散蒂金刀鞘尖（sika boha）','作品','art-africa','19世纪','非洲','综合','重要',
    '阿散蒂金匠行会所制金鞘尖，克利夫兰艺术博物馆藏（1935.312）。','1800年代',
    '金鞘包覆国王仪式用刀（sikay）的铁刃；金在阿坎诸国象征生命之力 kra，是太阳在世间的对应物。','asante-goldweight,asante-soul-disc','cma-1935-312'),
   ('yoruba-veranda-post','约鲁巴门廊柱（Òpó）','作品','art-africa','20世纪','非洲','雕塑','重要',
    '尼日利亚埃基蒂州（推定）约鲁巴宫殿雕柱，克利夫兰艺术博物馆藏（1969.55）。','1900年代初至中期',
    '宫廷由数进院落组成，围以具象雕柱；骑马武士与跪姿女性为埃基蒂常见主题，象征约鲁巴社会的权力分配。','yoruba-gelede-masks,yoruba-ifa-necklace','cma-1969-55'),
   ('yoruba-ifa-necklace','约鲁巴 Ifá 占卜者项链（òdìgbà Ifá）','作品','art-africa','20世纪','非洲','综合','重要',
    '约鲁巴占卜者随身项链，克利夫兰艺术博物馆藏（1995.23）。','1900年代',
    '彩玻璃珠为占卜增辉并标示占卜者的高地位；如同国王，其权威源自彼岸 òrún；小袋内缝入护身之物。','yoruba-veranda-post,yoruba-gelede-masks','cma-1995-23')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")