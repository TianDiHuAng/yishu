# -*- coding: utf-8 -*-
"""Cycle99：东南亚 4 条（高棉那伽座佛、堕罗钵底佛首、蒲甘坐佛、占婆九曜神）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1963-263","Cleveland Museum of Art — Naga-Enthroned Buddha, Angkor, 1100s, acc. 1963.263",
  "https://openaccess-api.clevelandart.org/api/artworks/1963.263","2026-11-23 API HTTP 200；青铜存鎏金 58.4×28cm；说明含阇耶跋摩七世与慈悲/智慧"),
 ("cma-1969-56","Cleveland Museum of Art — Bust of Buddha, Dvaravati, c. 700, acc. 1969.56",
  "https://openaccess-api.clevelandart.org/api/artworks/1969.56","2026-11-23 API HTTP 200；石灰岩 60.6×34.3cm；说明含印度元素与孟族面容"),
 ("cma-2011-149","Cleveland Museum of Art — Seated Buddha, Burma (Pagan), 1100s, acc. 2011.149",
  "https://openaccess-api.clevelandart.org/api/artworks/2011.149","2026-11-23 API HTTP 200；木胎黑漆鎏金 100×62×30cm；说明含触地印与蒲甘"),
 ("cma-1935-147","Cleveland Museum of Art — Enthroned Planetary Deity, Champa, 850–75, acc. 1935.147",
  "https://openaccess-api.clevelandart.org/api/artworks/1935.147","2026-11-23 API HTTP 200；砂岩 86.5×37.5cm；说明含九曜护法与 kirtimukha"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('khmer-naga-buddha','高棉那伽座佛','作品','art-asia','12世纪','东南亚','雕塑','核心',
  '吴哥期青铜鎏金那伽座佛，克利夫兰艺术博物馆藏（1963.263）。','12世纪',
  '阇耶跋摩七世以「那伽座佛」自比，象征慈悲（Lokeshvara）与智慧（Prajnaparamita）所生之觉悟者。','dvaravati-buddha-bust,burmese-seated-buddha','cma-1963-263'),
 ('dvaravati-buddha-bust','堕罗钵底佛首','作品','art-asia','7—9世纪','东南亚','雕塑','核心',
  '泰国中部堕罗钵底风格石灰岩佛首，克利夫兰艺术博物馆藏（1969.56）。','约公元700年',
  '长耳、肉髻、螺发等图像元素源自印度；孟族赋予面部独特表现：锐利双眼与程式化丰厚卷唇。','khmer-naga-buddha,buddhist-art-india','cma-1969-56'),
 ('burmese-seated-buddha','蒲甘坐佛','作品','art-asia','12世纪','东南亚','雕塑','核心',
  '缅甸蒲甘风格木胎黑漆鎏金坐佛，克利夫兰艺术博物馆藏（2011.149）。','12世纪',
  '结跏趺坐禅定，右手触地印请大地为证；双层莲座示超验；整木雕成、黑漆鎏金，同类大件极罕。','dvaravati-buddha-bust,khmer-naga-buddha','cma-2011-149'),
 ('champa-planetary-deity-dongduong','占婆九曜神像（同阳寺）','作品','art-asia','9世纪','东南亚','雕塑','核心',
  '越南占婆砂岩九曜神像，克利夫兰艺术博物馆藏（1935.147）。','公元850—875年',
  '九曜之一、护寺之神；短匕首、须与蹙眉示猛护；王者安逸坐姿与宝冠示天界之王；座上 kirtimukha 示创造力。','khmer-naga-buddha,dvaravati-buddha-bust','cma-1935-147'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")