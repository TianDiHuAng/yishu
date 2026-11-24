# -*- coding: utf-8 -*-
"""Cycle139：日本武具 4 条（土井家胴丸、1859 甲胄、桃形兜、正宗铭刀）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o119925","Victoria and Albert Museum — Doi family domaru armour, Japan, ca. 1800, O119925",
  "https://api.vam.ac.uk/v2/object/O119925","2026-11-24 API HTTP 200；铁鎏金银铜等 高142cm；说明含胴丸与土井家纹"),
 ("vam-o75791","Victoria and Albert Museum — Suit of armour, signed Myochin Muneharu, 1859, O75791",
  "https://api.vam.ac.uk/v2/object/O75791","2026-11-24 API HTTP 200；铁面颊·金漆 高146cm 重61kg；说明含妙心家与镰仓摹作"),
 ("vam-o182770","Victoria and Albert Museum — Momonari kabuto helmet, Japan, 1700–1800, O182770",
  "https://api.vam.ac.uk/v2/object/O182770","2026-11-24 API HTTP 200；铁施漆 多尺寸；说明含桃形与日野式颈甲"),
 ("vam-o92843","Victoria and Albert Museum — Katana blade with Masamune attribution, Japan, 1300–1350, O92843",
  "https://api.vam.ac.uk/v2/object/O92843","2026-11-24 API HTTP 200；刀身 金象嵌正宗铭；说明含正宗为刀工之最"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('japanese-armour-1800','土井家胴丸甲胄','作品','art-asia','19世纪','东亚','综合','核心',
  '日本土井家胴丸甲胄，维多利亚与艾伯特博物馆藏（O119925）。','约1800年',
  '胴丸式约1400年始用：贴身一体式身甲、腿部防护更多、肩甲更小；盔前立等处车轮槌纹为土井家纹，该家为中阶武士。','japanese-armour-1859,kabuto-helmet-1700','vam-o119925'),
 ('japanese-armour-1859','妙心源道喜宗春作甲胄（1859）','作品','art-asia','19世纪','东亚','综合','核心',
  '1859年署名甲胄，维多利亚与艾伯特博物馆藏（O75791）。','1859年',
  '盔铭「妙心源道喜宗春，安政六年八月某日」即1859；为江户末期摹镰仓甲胄之佳作，然多加早期所无之饰；妙心家自16世纪有据、为武家制甲。','japanese-armour-1800,kabuto-helmet-1700','vam-o75791'),
 ('kabuto-helmet-1700','桃形兜（Momonari）','作品','art-asia','18世纪','东亚','综合','重要',
  '日本四板铁兜，维多利亚与艾伯特博物馆藏（O182770）。','1700—1800年',
  '四片赤褐色铁板成「桃形」，具纵向脊；近似「头形（Zunari）」式；配日野式紧贴颈甲（shikoro）；铁施漆。','japanese-armour-1859,japanese-armour-1800','vam-o182770'),
 ('japanese-sword-1300','正宗铭太刀刀身','作品','art-asia','14世纪','东亚','金属器','核心',
  '日本太刀刀身（金象嵌正宗铭），维多利亚与艾伯特博物馆藏（O92843）。','1300—1350年',
  '刀身带金象嵌铭，归于正宗（1264—1344）；正宗被视为日本刀史最伟大的刀工，其刀多短刀（tanto）、强而美、切割极利；许多归于其的技术进步……（记录截断）。','japanese-armour-1800,kabuto-helmet-1700','vam-o92843'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")