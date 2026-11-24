# -*- coding: utf-8 -*-
"""Cycle169：贝多芬相关美术作品 2 条（布德尔 / 克里胡贝尔）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1960-82","Cleveland Museum of Art — Emile Antoine Bourdelle, Head of Beethoven, 1891, acc. 1960.82",
  "https://openaccess-api.clevelandart.org/api/artworks/1960.82","2026-11-24 API HTTP 200；铜 整体59.2×42×52.1cm；左侧署名Bourdelle / Sculpt.，正面题贝多芬引语；说明含布德尔曾为罗丹助手、1888年起作贝多芬系列肖像、引语译文"),
 ("cma-1940-1132","Cleveland Museum of Art — Josef Kriehuber, Bust of Ludwig van Beethoven, 1827, acc. 1940.1132",
  "https://openaccess-api.clevelandart.org/api/artworks/1940.1132","2026-11-24 API HTTP 200；石版画 版痕16.7×17.1cm；印有贝多芬生于1770年12月16日波恩、卒于1827年3月26日维也纳、出版者Tobias Haslinger、石版印刷Trentsensky；馆方无说明文字"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('bourdelle-head-of-beethoven','布德尔《贝多芬头像》（1891）','作品','art-modern','19世纪','法国','雕塑','重要',
  '布德尔的贝多芬铜质头像，克利夫兰艺术博物馆藏（1960.82）。','1891年',
  '该馆说明：布德尔曾在巴黎美术学院学习并做过罗丹的助手，1888年起创作了一系列贝多芬雕塑肖像，用起伏有力的形体传达作曲家的创造精神；他在左下方题了贝多芬的一句话：“我的领域是空气；风起时，我的灵魂旋转。”',
  'beethoven,rodin','cma-1960-82'),
 ('kriehuber-bust-of-beethoven','克里胡贝尔《贝多芬胸像》（1827）','作品','art-neo-romantic','19世纪','奥地利','版画','补充',
  '克里胡贝尔的贝多芬石版画肖像，克利夫兰艺术博物馆藏（1940.1132）。','1827年',
  '该馆记录：这是克里胡贝尔1827年的石版画，版痕16.7×17.1厘米；画上印有贝多芬1770年12月16日生于波恩、1827年3月26日卒于维也纳的字样，以及出版者哈斯林格与印制者特伦森斯基的名字。馆方对此件没有附说明文字。',
  'beethoven,romantic-music','cma-1940-1132'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
txt="\n".join(lines)
T=[t for t in T if "'%s'"%t[0] not in txt]
if T:
    close=max(i for i,l in enumerate(lines) if l.strip()=="]")
    lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
    io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
