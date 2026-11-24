# -*- coding: utf-8 -*-
"""Cycle171：美术基础技法术语 6 条（来源：盖蒂 AAT 词表定义；单来源，待核实）。"""
import io,json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
AAT="https://vocab.getty.edu/aat/"
NEWS=[
 ("aat-300053357","Getty AAT — fresco painting (technique), 300053357","300053357"),
 ("aat-300056348","Getty AAT — linear perspective (technique), 300056348","300056348"),
 ("aat-300053414","Getty AAT — chiaroscuro, 300053414","300053414"),
 ("aat-300015062","Getty AAT — tempera, 300015062","300015062"),
 ("aat-300178684","Getty AAT — oil painting (technique), 300178684","300178684"),
 ("aat-300053421","Getty AAT — sfumato, 300053421","300053421"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,num in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"J. Paul Getty Trust（Art & Architecture Thesaurus，开放词表）",
            "year":"2026","url":AAT+num,"type":"权威机构词表（术语定义）","verified":True,
            "verified_note":"2026-11-24 经 vocab.getty.edu SPARQL 接口取回该术语的英文定义（scopeNote），编号与标签匹配；定义原文存档于 tmp/aat_terms.json"})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
U="glossary-tools"
T=[
 ('fresco','湿壁画（Fresco）','术语',U,'历代','全球','绘画','重要',
  '把颜料调水后刷在湿的或半干的石灰灰泥上的壁画技法。','历代',
  '湿壁画是一种壁画技法：干颜料先与水研磨，再刷到湿的或半干的石灰灰泥上。','early-renaissance,high-renaissance','aat-300053357'),
 ('linear-perspective','线性透视（Linear perspective）','术语',U,'历代','欧洲','绘画','重要',
  '正交线向一个或多个灭点汇聚的透视体系。','历代',
  '线性透视是正交线向一个或多个灭点汇聚的体系；在西方艺术中常指意大利文艺复兴发展出的一点透视。','early-renaissance,renaissance','aat-300056348'),
 ('chiaroscuro','明暗对照法（Chiaroscuro）','术语',U,'历代','欧洲','绘画','重要',
  '在画面内对比明与暗的技法，形体主要由明暗区域的交接而非锐利轮廓线来确定。','历代',
  '明暗对照法以明暗对比塑造形体，形体多由亮部与暗部的交接来确定，而不靠清晰的轮廓线。','caravaggio,rembrandt,leonardo','aat-300053414'),
 ('tempera','蛋彩（Tempera）','术语',U,'历代','全球','绘画','重要',
  '由油脂成分与水成分乳化而成的颜料，标准做法用蛋黄加水。','历代',
  '蛋彩是油脂与水的乳化颜料；标准乳剂常用蛋黄与水，也有用全蛋、亚麻籽油、酪蛋白胶、树胶或蜡的变体。','early-renaissance,oil-painting','aat-300015062'),
 ('oil-painting','油画技法（Oil painting）','术语',U,'历代','欧洲','绘画','重要',
  '用悬浮于植物干性油中的颜料作画的技艺。','历代',
  '油画是用悬浮在植物干性油中的颜料创作；词表称其至少可追溯到欧洲中世纪，15世纪已广泛用于架上绘画。','tempera,northern-renaissance','aat-300178684'),
 ('sfumato','晕涂法（Sfumato）','术语',U,'历代','欧洲','绘画','重要',
  '在油画中把一个色调融入另一个色调、做出柔和细腻过渡的效果，尤其见于透明罩染。','历代',
  '晕涂法指油画中让一种色调融入另一种色调，造出柔和细腻的过渡效果，尤其用于罩染。','oil-painting,leonardo,mona-lisa','aat-300053421'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
