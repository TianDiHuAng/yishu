# -*- coding: utf-8 -*-
"""Cycle140：中世纪彩绘玻璃 4 条（女圣徒华盖、圣司提反、圣彼得布道、三王来拜）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o7327","Victoria and Albert Museum — Female saint under a canopy, England, 1325–1350, O7327",
  "https://api.vam.ac.uk/v2/object/O7327","2026-11-24 API HTTP 200；彩绘玻璃 1279×339mm；说明含华盖下女圣徒与Mary Magdalene?"),
 ("vam-o116900","Victoria and Albert Museum — St Stephen before the High Priest, Coutances, ca. 1230–1240, O116900",
  "https://api.vam.ac.uk/v2/object/O116900","2026-11-24 API HTTP 200；彩绘闪光玻璃 625×455mm；说明含库唐斯主教座堂回廊小堂"),
 ("vam-o8598","Victoria and Albert Museum — St Peter Preaching, Normandy, ca. 1525–1530, O8598",
  "https://api.vam.ac.uk/v2/object/O8598","2026-11-24 API HTTP 200；玻璃银黄 156.1×67.1cm；说明含Saint-Pierre-du-Chatel主保"),
 ("vam-o111371","Victoria and Albert Museum — Adoration of the Magi window, Guillaume de Marcillat, 1516, O111371",
  "https://api.vam.ac.uk/v2/object/O111371","2026-11-24 API HTTP 200；玻璃银黄 281×155.5cm；说明含Marcillat与法国技艺输出"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('female-saint-canopy-glass','华盖下女圣徒彩窗','作品','art-medieval','14世纪','欧洲','综合','核心',
  '英格兰彩绘玻璃板，维多利亚与艾伯特博物馆藏（O7327）。','1325—1350年',
  '女圣徒侧身向右、面作四分之三侧、双手合十祈祷；紫晕紫衣，白斗篷饰菱形纹与黑/银黄方边；立建筑华盖下，或为抹大拉的马利亚；单独圣徒居华盖下为中世纪彩窗/绘画/刺绣的典型题材。','stained-glass-donors-pair,st-stephen-glass-1230','vam-o7327'),
 ('st-stephen-glass-1230','圣司提反受审彩窗','作品','art-medieval','13世纪','欧洲','综合','核心',
  '诺曼底库唐斯彩绘玻璃板，维多利亚与艾伯特博物馆藏（O116900）。','约1230—1240年',
  '透明/彩色/闪光玻璃加绘；绘圣司提反立于犹太祭司长前；原属「圣司提反生平」大窗，置于库唐斯主教座堂回廊放射小堂之一；或示其以信仰辩护、驳亵渎之控。','female-saint-canopy-glass,st-peter-preaching-glass','vam-o116900'),
 ('st-peter-preaching-glass','圣彼得布道彩窗','作品','art-medieval','16世纪','欧洲','综合','核心',
  '诺曼底彩绘玻璃板，维多利亚与艾伯特博物馆藏（O8598）。','约1525—1530年',
  '圣彼得红袍蓝氅立讲坛布道；群众中一老者合手祈祷，示其已皈依；教堂常订制绘主保圣人生平的彩窗；Saint-Pierre-du-Chatel以圣彼得为主保，本板为其三幅之一。','st-stephen-glass-1230,female-saint-canopy-glass','vam-o8598'),
 ('adoration-magi-window-1516','三王来拜彩窗（马尔奇拉）','作品','art-medieval','16世纪','欧洲','综合','核心',
  '意大利三段式彩窗，维多利亚与艾伯特博物馆藏（O111371）。','1516年',
  '绘《马太福音》2:1—12 东方术士随星来拜；作者 Guillaume de Marcillat 生于法国，为罗马/佛罗伦萨/托斯卡纳教堂与世俗建筑首要彩窗师逾二十年（至1529），其作几遍科尔托纳与阿雷佐诸教堂，工坊授意大利学徒以法国彩窗之艺。','female-saint-canopy-glass,stained-glass-donors-pair','vam-o111371'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")