# -*- coding: utf-8 -*-
"""Cycle156：现代艺术 4 条（蒙德里安×2 + 克利×2）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1967-215","Cleveland Museum of Art — Piet Mondrian, Composition with Red, Yellow, and Blue, 1927, acc. 1967.215",
  "https://openaccess-api.clevelandart.org/api/artworks/1967.215","2026-11-24 API HTTP 200；布面油画 49.5×49.5cm；题款P M '27；说明含网格、三原色与普世视觉语言"),
 ("cma-1971-220","Cleveland Museum of Art — Piet Mondrian, Field with Young Trees in the Foreground, c. 1907, acc. 1971.220",
  "https://openaccess-api.clevelandart.org/api/artworks/1971.220","2026-11-24 API HTTP 200；纸本油画裱板 65.7×72cm；说明含奥埃勒村、1907年夏、精神性追求"),
 ("cma-1961-50","Cleveland Museum of Art — Paul Klee, With the Dot, 1916, acc. 1961.50",
  "https://openaccess-api.clevelandart.org/api/artworks/1961.50","2026-11-24 API HTTP 200；钢笔墨 纸 12.4×14.5cm；说明含一战、齐柏林飞艇与1915年克利引语"),
 ("cma-1969-46","Cleveland Museum of Art — Paul Klee, Carnival in the Snow, 1923, acc. 1969.46",
  "https://openaccess-api.clevelandart.org/api/artworks/1969.46","2026-11-24 API HTTP 200；水彩 24×23.5cm；题款Karneval im Schnee（该馆记录截断）；说明含杂技演员、青骑士成员、先画后辨认的方法"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('mondrian-composition-rby-1927','蒙德里安《红、黄、蓝构图》（1927）','作品','art-modern','20世纪','荷兰','绘画','重要',
  '蒙德里安布面油画，克利夫兰艺术博物馆藏（1967.215）。','1927年',
  '该馆说明：1910年代蒙德里安的艺术由立体主义发展为以网格为基础的日益抽象的风格，完全放弃自然外观的再现，只用水平与垂直的矩形和红黄蓝三原色加黑白；他相信一战后的浩劫之下，这类抽象构图能以普世的视觉语言促成更和谐的社会；画面下方中央题「P M \'27」。',
  'modern-art,cubism','cma-1967-215'),
 ('mondrian-field-young-trees','蒙德里安《前景有幼树的田野》（约1907）','作品','art-modern','20世纪','荷兰','绘画','重要',
  '蒙德里安早期风景，纸本油画裱板，克利夫兰艺术博物馆藏（1971.220）。','约1907年',
  '该馆说明：画的是1907年夏蒙德里安居住的荷兰东部奥埃勒村周边的田野；暮色天空下树的剪影所造成的氛围，显示他对精神性的追求早于1916年开始画完全抽象的非具象构图；他受形而上学与哲学阅读引导，追求画中更高的精神现实，最终舍弃一切再现元素而走向纯粹几何抽象；弗兰克·斯特拉捐赠给该馆。',
  'mondrian-composition-rby-1927,post-impressionism','cma-1971-220'),
 ('klee-with-the-dot','克利《带着点》（1916）','作品','art-modern','20世纪','德国','素描','重要',
  '克利一战期间的钢笔墨画，克利夫兰艺术博物馆藏（1961.50）。','1916年',
  '该馆说明：画中悬浮的形象可能是圣者也可能是恶魔，俯视着包含齐柏林飞艇、断头的孩子、倒下的士兵与一个退缩（或攻击）的人物的场景；士兵头盔带把手，暗示机械化或非人化的战争机器；标题中的点（•）指圆形的飞艇，或克利画中常作不祥预兆的圆；该馆引克利1915年的话：世界越可怕，艺术越抽象；和平的世界产生写实的艺术。',
  'expressionism,modern-art','cma-1961-50'),
 ('klee-carnival-in-snow','克利《雪中狂欢节》（1923）','作品','art-modern','20世纪','德国','水彩','重要',
  '克利水彩，克利夫兰艺术博物馆藏（1969.46）。','1923年',
  '该馆说明：画中杂技演员与马戏小丑从复杂的形与色的图案中浮现，两个杂耍者共用一张脸和一个躯干；克利是慕尼黑青骑士团体成员，相信色与形本身即可承载情感、情绪与主观感受；他的方法是先不画主题，叠加有色形体，直到出现可辨认之物。',
  'klee-with-the-dot,expressionism,kandinsky','cma-1969-46'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")
