# -*- coding: utf-8 -*-
"""Cycle137：现代/当代 4 条（马蒂斯室内、德加舞者饰带、鲁奥秋末、坎农纪念木刻组画）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1952-153","Cleveland Museum of Art — Henri Matisse, Interior with an Etruscan Vase, 1940, acc. 1952.153",
  "https://openaccess-api.clevelandart.org/api/artworks/1952.153","2026-11-24 API HTTP 200；布面油画 73.7×108cm；说明含尼斯Régina旅馆与二战"),
 ("cma-1946-83","Cleveland Museum of Art — Edgar Degas, Frieze of Dancers, c. 1895, acc. 1946.83",
  "https://openaccess-api.clevelandart.org/api/artworks/1946.83","2026-11-24 API HTTP 200；布面油画 70×200.5cm；说明含四视角与迈布里奇"),
 ("cma-1964-161","Cleveland Museum of Art — Georges Rouault, End of Autumn No. 4, 1952, acc. 1964.161",
  "https://openaccess-api.clevelandart.org/api/artworks/1964.161","2026-11-24 API HTTP 200；布面油画 75×105.4cm；说明含信仰与彩窗训练"),
 ("cma-2025-5","Cleveland Museum of Art — T. C. Cannon, Memorial Woodcut Suite, c. 1978, acc. 2025.5",
  "https://openaccess-api.clevelandart.org/api/artworks/2025.5","2026-11-24 API HTTP 200；五幅彩印木刻；说明含Kiowa-Caddo与流行美学"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('matisse-interior-etruscan','马蒂斯《有伊特鲁里亚瓶的室内》','作品','art-contemporary','20世纪','欧洲','绘画','核心',
  '马蒂斯布面油画，克利夫兰艺术博物馆藏（1952.153）。','1940年',
  '女子坐桌旁看书与散果；绿盆栽、红纹帘、橙古瓶构成绚丽；作于尼斯Régina旅馆画室，二战爆发后约半年；艺术给其内心平衡以抗乱世。','fauvism,modern-art','cma-1952-153'),
 ('degas-frieze-dancers','德加《舞者饰带》','作品','art-contemporary','19世纪','欧洲','绘画','核心',
  '德加布面油画，克利夫兰艺术博物馆藏（1946.83）。','约1895年',
  '或为同一舞者四视角；设定模糊、色如薄缕、颜料流淌；前景圆圈以拇指按出；六尺画布上如此大胆，时人当惊；多视角或受迈布里奇摄影启发。','degas,modern-art','cma-1946-83'),
 ('rouault-end-autumn','鲁奥《秋末·第4号》','作品','art-contemporary','20世纪','欧洲','绘画','核心',
  '鲁奥布面油画，克利夫兰艺术博物馆藏（1964.161）。','1952年',
  '常归表现主义与野兽派，却以基督教信仰为艺核；此秋景作于卒前六年；旷野人物与辉光天色，或联「逃往埃及」；宝石般色块以粗黑线框，映其早年彩窗训练。','fauvism,modern-art','cma-1964-161'),
 ('cannon-memorial-woodcut','坎农《纪念木刻组画》','作品','art-contemporary','20世纪','美洲','版画','核心',
  'T. C. Cannon 五幅彩印木刻组画，克利夫兰艺术博物馆藏（2025.5）。','约1978年',
  '坎农为 Kiowa-Caddo 原住民画家；原住民肖像以明亮色盘与波普美学并糅传统与当代；每幅据其主要油画；整组呈现其对原住民身份之复杂探索。','modern-art,americas-art','cma-2025-5'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")