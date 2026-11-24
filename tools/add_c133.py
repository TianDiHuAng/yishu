# -*- coding: utf-8 -*-
"""Cycle133：美洲 4 条（莫切海狮瓶、特奥蒂瓦坎壁画、萨波特克坐像、阿兹特克坐神）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-2014-375","Cleveland Museum of Art — Moche sea lion pup vessel, 200–850 CE, acc. 2014.375",
  "https://openaccess-api.clevelandart.org/api/artworks/2014.375","2026-11-24 API HTTP 200；陶与泥浆 19.7×15.5×16cm；说明含胃石与冥途传说"),
 ("cma-1963-252","Cleveland Museum of Art — Teotihuacán mural fragment, elite male & maguey, 500–550, acc. 1963.252",
  "https://openaccess-api.clevelandart.org/api/artworks/1963.252","2026-11-24 API HTTP 200；壁画残块 83.2×116.2cm；说明含口卷与龙舌兰刺"),
 ("cma-1954-857","Cleveland Museum of Art — Zapotec seated figure, 300 BCE–700 CE, acc. 1954.857",
  "https://openaccess-api.clevelandart.org/api/artworks/1954.857","2026-11-24 API HTTP 200；陶与泥浆 32.2×17.9×18.8cm；说明含历日象形13水/13燧刀"),
 ("cma-1990-136","Cleveland Museum of Art — Aztec seated deity (Macuilxochitl?), 1350–1519, acc. 1990.136",
  "https://openaccess-api.clevelandart.org/api/artworks/1990.136","2026-11-24 API HTTP 200；灰火山岩存红彩 37.5×20.3×24.8cm；说明含五花神与邻里小庙"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('moche-sealion-pup','莫切海狮幼崽瓶','作品','art-americas','公元3—9世纪','美洲','陶瓷','核心',
  '莫切陶与泥浆海狮瓶，克利夫兰艺术博物馆藏（2014.375）。','200—850年',
  '海狮常见于莫切艺术（肖形瓶或狩猎场景）；或因其胃中卵石而受珍视，今秘鲁民间医者视之为良药；殖民期传说海狮载亡者往海外岛，或可溯至莫切。','moche-bat-vessel,americas-art','cma-2014-375'),
 ('teotihuacan-mural-fragment','特奥蒂瓦坎壁画残块','作品','art-americas','公元6世纪','美洲','绘画','核心',
  '特奥蒂瓦坎风格湿壁画残块，克利夫兰艺术博物馆藏（1963.252）。','500—550年',
  '盛装贵男列队于富宅庭院墙；口卷示吟诵祈祷，一手泻花酒、一手携香袋；前后龙舌兰刺或喻献血与龙舌兰汁酒（pulque），刺插于束/地之上。','maya-palace-cylinder,americas-art','cma-1963-252'),
 ('zapotec-seated-figure','萨波特克坐像（陪俑）','作品','art-americas','公元前3—公元7世纪','美洲','雕塑','核心',
  '瓦哈卡萨波特克陶坐像，克利夫兰艺术博物馆藏（1954.857）。','约公元前300—公元700年',
  '萨波特克墓陶以华丽主瓮与较小陪俑成组；本俑或属近同组，另两件存墨西哥；身份（贵族/祖先/神）仍争；头冠与胸前象形为历日「13水」「13燧刀」。','moche-sealion-pup,americas-art','cma-1954-857'),
 ('aztec-seated-deity','阿兹特克坐神像（五花神？）','作品','art-americas','14—16世纪','美洲','雕塑','重要',
  '阿兹特克灰火山岩坐神像，克利夫兰艺术博物馆藏（1990.136）。','1350—1519年',
  '带缨头冠示青年坐男或为 Macuilxochitl（五花），司乐舞宴戏与性等诸乐；其祀在平民中流行；或为邻里小庙所作；石表或曾施灰泥重彩。','aztec-xochipilli-maize,aztec-feathered-serpent','cma-1990-136'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")