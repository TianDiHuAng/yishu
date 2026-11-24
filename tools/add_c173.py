# -*- coding: utf-8 -*-
"""Cycle173：美术基础术语 6 条（盖蒂 AAT 定义；单来源，待核实）。"""
import io,json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
AAT="https://vocab.getty.edu/aat/"
NEWS=[
 ("aat-300015638","Getty AAT — still lifes, 300015638","300015638"),
 ("aat-300178234","Getty AAT — triptychs, 300178234","300178234"),
 ("aat-300075940","Getty AAT — altarpieces, 300075940","300075940"),
 ("aat-300053373","Getty AAT — scumbling, 300053373","300053373"),
 ("aat-300343524","Getty AAT — tenebrism, 300343524","300343524"),
 ("aat-300189805","Getty AAT — pentimenti, 300189805","300189805"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,num in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"J. Paul Getty Trust（Art & Architecture Thesaurus，开放词表）",
            "year":"2026","url":AAT+num,"type":"权威机构词表（术语定义）","verified":True,
            "verified_note":"2026-11-24 经 vocab.getty.edu SPARQL 接口取回该术语的英文定义（scopeNote），编号与标签匹配；定义原文存档于 tmp/aat_batch3.json、tmp/aat_batch3b.json"})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
U="glossary-tools"
T=[
 ('still-life','静物画（Still life）','术语',U,'历代','欧洲','绘画','重要',
  '以无生命物体为描绘重点的图像，常见为水果、花卉、器皿等摆放在桌上的对象。','历代',
  '静物画是以无生命物体为描绘重点的图像，常见题材有水果、花卉、器皿和餐具，也可含头骨、蜡烛、沙漏等，通常摆放在桌上。','oil-painting,baroque','aat-300015638'),
 ('triptych','三联画（Triptych）','术语',U,'历代','欧洲','绘画','重要',
  '由三块相连的板组成或装在三块相连板上的画或雕刻，常为外侧两翼可折向中央的形式。','历代',
  '三联画是由三块相连的板组成、或装在三块相连的板上的画或雕刻，外侧两翼常可折向中央，是祭坛画的常见形式。','altarpiece,gothic','aat-300178234'),
 ('altarpiece','祭坛画（Altarpiece）','术语',U,'历代','欧洲','绘画','重要',
  '基督教教堂中带图像的绘制或雕刻物，通常有框，置于祭坛后部或挂在祭坛后的墙上。','历代',
  '祭坛画指基督教教堂里绘制或雕刻的带图像的物件，通常有框，立在祭坛后部或挂在祭坛后的墙上，主题多为宗教人物，常含叙事或教诲场景，也可含教堂的赞助人。','triptych,early-christian-art','aat-300075940'),
 ('scumbling','擦涂法（Scumbling）','术语',U,'历代','欧洲','绘画','重要',
  '用近乎干的笔把不透明或半透明的颜色涂在画面上，使形象不那么清晰或鲜亮的技法。','历代',
  '擦涂法是用近乎干的画笔，把一层不透明或半透明的颜色涂到画面上，使形象变得不那么清晰或鲜亮。','glaze,sfumato','aat-300053373'),
 ('tenebrism','暗调法（Tenebrism）','术语',U,'历代','欧洲','绘画','重要',
  '在画面中强调阴影、黑暗或夜景效果的技法，阴影常使画中人物变得模糊。','历代',
  '暗调法是在画中强调阴影、黑暗或夜景效果的技法；这样的处理通常会使画中的人物变得模糊不清。','chiaroscuro,caravaggio','aat-300343524'),
 ('pentimenti','悔改痕迹（Pentimenti）','术语',U,'历代','欧洲','绘画','重要',
  '画家改变主意的物证，被覆盖过的部分重新显露出来。','历代',
  '悔改痕迹是画家中途改变构思的物证，表现为画面中曾被涂盖的部分重新显露出来。','oil-painting,fresco','aat-300189805'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
