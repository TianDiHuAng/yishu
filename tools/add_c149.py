# -*- coding: utf-8 -*-
"""Cycle149：北美平原原住民 4 条（Lakota 彩绘皮衬衫 / 摇篮 / Cheyenne 珠饰毯条 / Lakota 储物袋）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1984-1046","Cleveland Museum of Art — Hide Shirt, Lakota Sioux, c. 1890, acc. 1984.1046",
  "https://openaccess-api.clevelandart.org/api/artworks/1984.1046","2026-11-24 API HTTP 200；皮、颜料、玻璃珠、人发 97.8×150cm；说明含酋长特权、战功人发、保留地时期"),
 ("cma-1984-1047","Cleveland Museum of Art — Cradle or Baby Carrier, Lakota (Sioux), c. 1900, acc. 1984.1047",
  "https://openaccess-api.clevelandart.org/api/artworks/1984.1047","2026-11-24 API HTTP 200；鞣皮、棉布、玻璃珠、金属珠、铜铃、筋线 24.1×25.4×85.7cm；说明含精神福佑与触敌之勇"),
 ("cma-1927-260","Cleveland Museum of Art — Blanket Strip, Tsitsistas (Cheyenne), c. 1900, acc. 1927.260",
  "https://openaccess-api.clevelandart.org/api/artworks/1927.260","2026-11-24 API HTTP 200；鞣皮、玻璃珠、黄色贸易布、铜珠、筋线 182.9×13cm；说明含十字圆圈图案与黑麋鹿引语"),
 ("cma-1937-850","Cleveland Museum of Art — Storage Bag, Lakota (Sioux), late 1800s, acc. 1937.850",
  "https://openaccess-api.clevelandart.org/api/artworks/1937.850","2026-11-24 API HTTP 200；鞣皮、玻璃珠、染马毛、锡锥、筋线 高38.8cm；说明含 possible bag 与帐内枕用"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('lakota-hide-shirt','拉科塔彩绘皮衬衫（约1890）','作品','art-americas','19世纪','北美洲','综合','重要',
  '大平原拉科塔（苏族）皮、颜料、玻璃珠与人发制成的衬衫，克利夫兰艺术博物馆藏（1984.1046）。','约1890年',
  '传统上只有拉科塔首席酋长有权穿彩绘衬衫，是以牺牲与勇敢赢得、失职即失去的荣誉；此件作于保留地时期，已成战争老兵的特权；人发束每束代表一次战功，多半由家人捐出。',
  'hopi-canteen-katsina,navajo-chief-blanket-rug','cma-1984-1046'),
 ('lakota-cradle','拉科塔珠饰摇篮（约1900）','作品','art-americas','19—20世纪','北美洲','综合','重要',
  '大平原拉科塔鞣皮与玻璃珠制婴儿背袋，克利夫兰艺术博物馆藏（1984.1047）。','约1900年',
  '平原各族重视华美的刺绣或珠饰摇篮：既赐婴儿以精神福佑，也给家庭与制作者（通常为女性亲属）带来声望；制作摇篮被视同「触敌」之勇；此件为抱在臂中，另有木架可靠放。',
  'lakota-hide-shirt,navajo-biilee-dress','cma-1984-1047'),
 ('cheyenne-blanket-strip','夏安珠饰毯条（约1900）','作品','art-americas','19—20世纪','北美洲','综合','重要',
  '大平原夏安（Tsitsistas）鞣皮、玻璃珠、黄色贸易布与铜珠的毯条，克利夫兰艺术博物馆藏（1927.260）。','约1900年',
  '兽皮袍常以刺绣或珠饰条装点，后来也缝在替代袍子的毯上；此条的圆中十字象征世界、四方与神圣中心；该馆引用奥格拉拉拉科塔圣者黑麋鹿1932年的话说明圆的世界观。',
  'lakota-hide-shirt,navajo-chief-blanket-rug','cma-1927-260'),
 ('lakota-storage-bag','拉科塔储物袋（19世纪末）','作品','art-americas','19世纪','北美洲','综合','重要',
  '大平原拉科塔鞣皮、玻璃珠、染马毛与锡锥制成的储物袋，克利夫兰艺术博物馆藏（1937.850）。','1800年代末',
  '长方软皮袋，早期白人商人称之为「possible bag」（什么都装得下）；在帐内存放私物并兼作枕头，迁徙时挂在马鞍侧面，装饰随之展示。',
  'lakota-cradle,hopi-canteen-katsina','cma-1937-850'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")
