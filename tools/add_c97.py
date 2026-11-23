# -*- coding: utf-8 -*-
"""Cycle97：古代美洲 4 条（玛雅鹿形瓶、瓦里束腰衣、印加束腰衣1957、阿兹特克持玉米坐像）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1997-60","Cleveland Museum of Art — Deer Effigy Vessel, Maya, 250–600 CE, acc. 1997.60",
  "https://openaccess-api.clevelandart.org/api/artworks/1997.60","2026-11-23 API HTTP 200；陶 22.8×24.7×18cm；说明含还原烧成与金星/海螺/蛙"),
 ("cma-1949-12","Cleveland Museum of Art — Tunic with Profile Animal and Human Heads, Wari, c. 700–1100, acc. 1949.12",
  "https://openaccess-api.clevelandart.org/api/artworks/1949.12","2026-11-23 API HTTP 200；驼毛棉挂毯 97.8×99.1cm；说明含横向经线与影响印加"),
 ("cma-1957-136","Cleveland Museum of Art — Inca Tunic, c. 1400–1540, acc. 1957.136",
  "https://openaccess-api.clevelandart.org/api/artworks/1957.136","2026-11-23 API HTTP 200；挂毯棉与驼毛 85.1×76.2cm；说明含 Aclla 织女与国家再分配"),
 ("cma-1949-555","Cleveland Museum of Art — Seated Male Carrying Maize, Aztec, 1325–1521, acc. 1949.555",
  "https://openaccess-api.clevelandart.org/api/artworks/1949.555","2026-11-23 API HTTP 200；石与颜料 31.1×24.1×30.5cm；说明含花与玉米的象征"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('maya-deer-vessel','玛雅鹿形陶瓶','作品','art-americas','公元3—7世纪','美洲','雕塑','核心',
  '玛雅黑陶鹿形瓶，克利夫兰艺术博物馆藏（1997.60）。','公元250—600年',
  '还原气氛烧成的黑陶；鹿常为狩猎或献祭对象；金星纹与海螺示死亡，蹄下蛙蟾关乎农事丰产（鸣声报雨）。','moche-bat-vessel,americas-art','cma-1997-60'),
 ('wari-tunic','瓦里束腰外衣','作品','art-americas','公元8—12世纪','美洲','综合','核心',
  '瓦里文化驼毛棉挂毯束腰衣，克利夫兰艺术博物馆藏（1949.12）。','约700—1100年',
  '两长幅折肩缝合；经线横向（异于常态），似影响后期印加束腰衣；纹样为人与兽（鹿或蝠）侧首交替。','inca-tunic,paracas-mantle','cma-1949-12'),
 ('inca-tunic-1957','印加束腰外衣（1957号）','作品','art-americas','15—16世纪','美洲','综合','核心',
  '印加挂毯束腰外衣，克利夫兰艺术博物馆藏（1957.136）。','约1400—1540年',
  '细密挂毯为贵族特权；由贵族妇女、职业织工与 Aclla（选女）织造，由国家再分配为赏赐；纹样为「印加之钥」。','inca-tunic,wari-tunic','cma-1957-136'),
 ('aztec-xochipilli-maize','阿兹特克持玉米坐像','作品','art-americas','14—16世纪','美洲','雕塑','重要',
  '阿兹特克石雕坐像，克利夫兰艺术博物馆藏（1949.555）。','1325—1521年',
  '或为 Macuilxochitl 或 Xochipilli，司美、艺术与嬉戏舞蹈；手持花锥；背负玉米棒或喻其创造力。','aztec-feathered-serpent,americas-art','cma-1949-555'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")