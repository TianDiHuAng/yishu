# -*- coding: utf-8 -*-
"""Cycle157：当代艺术 4 条（劳森伯格 / 约翰斯 / 奥尔登堡 / 勒维特）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1966-333","Cleveland Museum of Art — Robert Rauschenberg, Gloria, 1956, acc. 1966.333",
  "https://openaccess-api.clevelandart.org/api/artworks/1966.333","2026-11-24 API HTTP 200；油彩、织物、订书钉、报纸、石墨等混合材料 170.5×163.4×4.5cm；说明含格洛丽亚·范德比尔特剪报与劳森伯格引语"),
 ("cma-1973-28","Cleveland Museum of Art — Jasper Johns, Reconstruction, 1959, acc. 1973.28",
  "https://openaccess-api.clevelandart.org/api/artworks/1973.28","2026-11-24 API HTTP 200；蜡画与拼贴 画布 155×111.7cm；背面题款Reconstruction/ J. Johns '59；说明含蜡画技法与标题解读"),
 ("cma-2004-88","Cleveland Museum of Art — Claes Oldenburg, Giant Toothpaste Tube, 1964, acc. 2004.88",
  "https://openaccess-api.clevelandart.org/api/artworks/2004.88","2026-11-24 API HTTP 200；乙烯基覆布填木棉、木、金属与铸塑料 64.8×167.6×43.2cm；说明为对奥尔登堡的总体介绍"),
 ("cma-2008-144","Cleveland Museum of Art — Sol LeWitt, Wall Drawing #4, 1969, acc. 2008.144",
  "https://openaccess-api.clevelandart.org/api/artworks/2008.144","2026-11-24 API HTTP 200；黑铅笔直接画于墙 304.7×304.7cm；说明含证书与指示的所有权制度、本版本由工作室人员与博物馆人员完成"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('rauschenberg-gloria','劳森伯格《格洛丽亚》（1956）','作品','art-contemporary','20世纪','美国','综合材料绘画','重要',
  '劳森伯格把报纸剪报、照片与颜料并置的综合材料作品，克利夫兰艺术博物馆藏（1966.333）。','1956年',
  '该馆说明：此作是劳森伯格把现成印刷物与抽象绘画结合的构图的典型；他把报纸剪报（多张为纽约社交名媛格洛丽亚·范德比尔特）、一张照片、印刷纸板与几处颜料并置，摒弃了艺术材料的传统等级，模糊了日常生活与艺术的界线；该馆引他的话：一双袜子并不比木头、钉子、松节油、油彩与织物更不适合用来作画。',
  'contemporary-art,pollock-number5,dada','cma-1966-333'),
 ('johns-reconstruction','约翰斯《重建》（1959）','作品','art-contemporary','20世纪','美国','绘画','重要',
  '约翰斯的蜡画与拼贴作品，克利夫兰艺术博物馆藏（1973.28）。','1959年',
  '该馆说明：蜡画技法把颜料悬浮在加热的蜡中，上画后很快干燥，因此艺术家的手势与笔触、滴痕清晰可见；约翰斯还在画面上加了一块折入的画布，形成三段式构图；标题暗示画只在观者心中才有意义，观者依据艺术家提供的基本标记与材料词汇来「重建」作品；画布背面题「Reconstruction/ J. Johns \'59」。',
  'contemporary-art,rauschenberg-gloria,abstract-expressionism','cma-1973-28'),
 ('oldenburg-giant-toothpaste-tube','奥尔登堡《巨型牙膏管》（1964）','作品','art-contemporary','20世纪','美国','雕塑','重要',
  '奥尔登堡把日用品放大为软雕塑的作品，克利夫兰艺术博物馆藏（2004.88）。','1964年',
  '该馆对奥尔登堡的总体介绍：他在1960年代因参与纽约反主流文化人物的集体表演「偶发艺术」与艺术影片而知名；同十年后期，他从无处不在的消费文化取材，用出人意料的材料把寻常物件做成巨大尺寸的雕塑，把平庸的家居之物提升为艺术品，使最日常的题材显得陌生，如同初次相遇；该作为乙烯基覆布填木棉，配木、金属与铸塑料部件。',
  'pop-art,contemporary-art','cma-2004-88'),
 ('lewitt-wall-drawing-4','勒维特《墙绘 #4》（1969）','作品','art-contemporary','20世纪','美国','观念艺术','重要',
  '勒维特直接画在墙上的观念艺术作品，克利夫兰艺术博物馆藏（2008.144），现存为一个执行版本。','1969年',
  '该馆说明：勒维特是观念艺术家，1960年代末至1970年代初开始直接在墙上作画，以创作不受纸张约束的作品；他设计了一套所有权制度：买家获得一份证书与一份带指示的绘制稿，任何其他绘制者都可据以施作，从而把作品向绘制者的诠释敞开；该馆这一版本由勒维特工作室代表与博物馆安装人员合作完成；黑铅笔直接画于墙，整体304.7×304.7厘米。',
  'conceptual-art,minimalism','cma-2008-144'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")
