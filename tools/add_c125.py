# -*- coding: utf-8 -*-
"""Cycle125：4 条（伊卜克斯标顶、卢里斯坦轴杯、希腊罗马还愿浮雕、阿弥陀来迎图）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1992-246","Cleveland Museum of Art — Ibex standard finial, Luristan, c. 700–600 BCE, acc. 1992.246",
  "https://openaccess-api.clevelandart.org/api/artworks/1992.246","2026-11-24 API HTTP 200；青铜 13.5×9.7cm；说明含双羱羊与前腿成环"),
 ("cma-1930-729","Cleveland Museum of Art — Axel shaft cup, Luristan, c. 800–700 BCE, acc. 1930.729",
  "https://openaccess-api.clevelandart.org/api/artworks/1930.729","2026-11-24 API HTTP 200；铸青铜 径8.6cm；说明含亚述马具供应"),
 ("cma-1914-666","Cleveland Museum of Art — Double-sided votive relief, Ptolemaic Egypt, 305–30 BCE, acc. 1914.666",
  "https://openaccess-api.clevelandart.org/api/artworks/1914.666","2026-11-24 API HTTP 200；石灰岩 8.3×6.5cm；说明含习作/石片与范本"),
 ("cma-2025-138","Cleveland Museum of Art — Amida descent with 25 bodhisattvas, Nanbokuchō, acc. 2025.138",
  "https://openaccess-api.clevelandart.org/api/artworks/2025.138","2026-11-24 API HTTP 200；绢本切金 164.5×137.7cm；说明含观音持莲台"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('luristan-ibex-standard','卢里斯坦羱羊标顶','作品','art-ancient','公元前8—7世纪','西亚·中亚','金属器','重要',
  '伊朗卢里斯坦青铜标顶，克利夫兰艺术博物馆藏（1992.246）。','约公元前700—600年',
  '装饰管或为军徽；双抽象羱羊前腿延展成环（或曾插杆）；胸前横杆另托环；脊角/卷须/绞尾，后腿再汇一环；卢里斯坦为铁器时代半游牧金属业重镇。','luristan-master-cheekpiece,luristan-axel-cup','cma-1992-246'),
 ('luristan-axel-cup','卢里斯坦轴杯','作品','art-ancient','公元前9—8世纪','西亚·中亚','金属器','重要',
  '卢里斯坦铸青铜轴杯，克利夫兰艺术博物馆藏（1930.729）。','约公元前800—700年',
  '卢里斯坦少文字记录，所知皆由艺术品推得；为古养马业中心，以青铜马具/车具著称；曾向亚述帝国供马及配套硬件。','luristan-ibex-standard,shang-jia-vessel','cma-1930-729'),
 ('greco-roman-votive-relief','托勒密还愿浮雕（双面习作）','作品','art-ancient','托勒密时期','埃及','雕塑','重要',
  '埃及希腊罗马期石灰岩双面还愿浮雕，克利夫兰艺术博物馆藏（1914.666）。','公元前305—前30年',
  '习作（刻于石灰岩片/ostraca）与雕塑家模型让我们看见埃及艺术家如何工作；一面野犬首、另一面侧面人物，本身即杰作，或供临摹。','amenhotep-tomb-relief,canopic-jar-26','cma-1914-666'),
 ('amida-descent-painting','阿弥陀二十五菩萨来迎图','作品','art-asia','14世纪','东亚','绘画','核心',
  '日本南北朝绢本来迎图，克利夫兰艺术博物馆藏（2025.138）。','1300年代中期',
  '阿弥陀携25菩萨迎亡者往净土；多位菩萨奏乐以贺；观音跪持莲台供亡者乘归。','amida-shitennoji,japanese-art','cma-2025-138'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")