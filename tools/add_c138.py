# -*- coding: utf-8 -*-
"""Cycle138：中国瓷器 4 条（明青花婴戏碗、斗彩高足杯、康熙青花罐、纹章瓷杯）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o176456","Victoria and Albert Museum — Ming blue-and-white bowl, Jingdezhen, 1450–1464, O176456",
  "https://api.vam.ac.uk/v2/object/O176456","2026-11-24 API HTTP 200；瓷 径22.1 高12.2cm；说明含婴戏与多子寓意"),
 ("vam-o168503","Victoria and Albert Museum — Doucai stemcup, Jingdezhen, 1465–1487, O168503",
  "https://api.vam.ac.uk/v2/object/O168503","2026-11-24 API HTTP 200；青花加釉上彩 高7.62cm；说明含斗彩二次烧与六字款"),
 ("vam-o77998","Victoria and Albert Museum — Kangxi blue-and-white jar and lid, Jingdezhen, 1662–1722, O77998",
  "https://api.vam.ac.uk/v2/object/O77998","2026-11-24 API HTTP 200；青花瓷 高23 径20cm；说明含ginger jar与青花源流"),
 ("vam-o185338","Victoria and Albert Museum — Armorial porcelain cup, Jingdezhen, ca. 1755–60, O185338",
  "https://api.vam.ac.uk/v2/object/O185338","2026-11-24 API HTTP 200；软质瓷釉上彩描金 高7.9 径8.6cm；说明含「Le Grand」纹章（记录无 summary）"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('ming-jingdezhen-bowl-1450','明青花婴戏碗','作品','art-ceramics','15世纪','中国','陶瓷','核心',
  '景德镇明青花碗，维多利亚与艾伯特博物馆藏（O176456）。','1450—1464年',
  '厚胎白瓷深锥形直足碗；釉下钴蓝绘婴戏园景、足饰回纹；婴戏为明清瓷常见题材，寄多子与家族兴旺之愿；据御窑出土瓷片定于明1450—1464。','yuan-lion-jar,chenghua-doucai-cup','vam-o176456'),
 ('doucai-stemcup-1465','斗彩高足杯','作品','art-ceramics','15世纪','中国','陶瓷','核心',
  '景德镇斗彩高足杯，维多利亚与艾伯特博物馆藏（O168503）。','1465—1487年',
  '釉下青花勾轮廓、再填釉上彩，需二次烧成——即「斗彩」（contrasting colours）；外壁绘两枝大叶果实与两对鸟；足内青花六字款；明代尤盛。','chenghua-doucai-cup,ming-jingdezhen-bowl-1450','vam-o168503'),
 ('kangxi-jar-lid-qing','康熙青花盖罐','作品','art-ceramics','17—18世纪','中国','陶瓷','重要',
  '景德镇康熙青花罐带盖，维多利亚与艾伯特博物馆藏（O77998）。','1662—1722年',
  '球腹青花绘人物场景；盖沿卷云纹、盖上蹲一鳞甲兽；西方称ginger jar（多因盛姜进口），中国则盛物或陈设；釉下青花14世纪起流行。','yuan-lion-jar,ming-jingdezhen-bowl-1450','vam-o77998'),
 ('armorial-porcelain-cup','纹章瓷杯（Le Grand）','作品','art-ceramics','18世纪','中国','陶瓷','重要',
  '景德镇软质纹章瓷杯，维多利亚与艾伯特博物馆藏（O185338）。','约1755—1760年',
  '软质瓷钟形无柄杯；釉上彩与描金；一面绘带盔、冠饰与羽饰之盾徽，绶带书「Le Grand」，装饰或为法国式；口沿饰贝壳边。','kangxi-jar-lid-qing,ming-jingdezhen-bowl-1450','vam-o185338'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")