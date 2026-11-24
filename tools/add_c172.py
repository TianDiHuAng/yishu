# -*- coding: utf-8 -*-
"""Cycle172：美术基础技法术语 6 条（盖蒂 AAT 定义；单来源，待核实）。"""
import io,json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
AAT="https://vocab.getty.edu/aat/"
NEWS=[
 ("aat-300067391","Getty AAT — contrapposto, 300067391","300067391"),
 ("aat-300053417","Getty AAT — foreshortening, 300053417","300053417"),
 ("aat-300053368","Getty AAT — impasto, 300053368","300053368"),
 ("aat-300458811","Getty AAT — glaze (painting), 300458811","300458811"),
 ("aat-300053386","Getty AAT — grisaille, 300053386","300053386"),
 ("aat-300056506","Getty AAT — trompe-l'oeil, 300056506","300056506"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,num in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"J. Paul Getty Trust（Art & Architecture Thesaurus，开放词表）",
            "year":"2026","url":AAT+num,"type":"权威机构词表（术语定义）","verified":True,
            "verified_note":"2026-11-24 经 vocab.getty.edu SPARQL 接口取回该术语的英文定义（scopeNote），编号与标签匹配；定义原文存档于 tmp/aat_batch2.json"})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
U="glossary-tools"
T=[
 ('contrapposto','对立式平衡（Contrapposto）','术语',U,'历代','欧洲','雕塑','重要',
  '人物静立时重心移到一条腿上，姿态平衡而不对称的站姿。','历代',
  '对立式平衡指人物静立、重心落在一条腿上的站姿：姿态平衡但不对称，髋、肩、头朝不同方向转动或倾斜。','classical-crossmedia,high-renaissance','aat-300067391'),
 ('foreshortening','透视缩短（Foreshortening）','术语',U,'历代','欧洲','绘画','重要',
  '在图像再现中缩减物体或人物的某些尺度，以表示其向画面深处后退。','历代',
  '透视缩短是在图像中缩减物体或人物的某些尺度，以显示其退向画面空间深处。','linear-perspective,early-renaissance','aat-300053417'),
 ('impasto','厚涂（Impasto）','术语',U,'历代','全球','绘画','重要',
  '把颜料以厚而不透明的块面涂上画面，通常用蘸饱颜料的画笔或调色刀。','历代',
  '厚涂指把颜料以厚而不透明的块面涂在画面上，通常用蘸足颜料的画笔或调色刀。','oil-painting,rembrandt','aat-300053368'),
 ('glaze','罩染（Glaze）','术语',U,'历代','欧洲','绘画','重要',
  '加在画面上、用以改变色调的一层透明到半透明的薄色膜。','历代',
  '在绘画中，罩染是加在画面上的一层透明至半透明的薄色膜，用来改变色调。','oil-painting,sfumato','aat-300458811'),
 ('grisaille','灰色画（Grisaille）','术语',U,'历代','欧洲','绘画','重要',
  '用单色（通常是灰色调）画出形象的画法。','历代',
  '灰色画指以单色（通常是灰色调）画出形象，可见于绘画、彩绘玻璃、珐琅以及陶瓷等器物。','chiaroscuro,stained-glass-donors-pair','aat-300053386'),
 ('trompe-loeil','错视画（Trompe-l\'oeil）','术语',U,'历代','欧洲','绘画','重要',
  '法语意为“骗过眼睛”，指逼真到足以使观者误以为所画对象是真实的图像。','历代',
  '错视画是逼真到可能使观者误以为所绘物体、场景、质感或视点是真实的图像，通常指西方的二维艺术或浅浮雕。','linear-perspective,renaissance','aat-300056506'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
