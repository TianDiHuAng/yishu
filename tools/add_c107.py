# -*- coding: utf-8 -*-
"""Cycle107：V&A 4 条（韩国民画虎鹊、马穆鲁克清真寺灯、卡尚米纳伊碗、日本印笼）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o22242","Victoria and Albert Museum — Tiger and Magpie (Hochakdo), Korea, 1850–1910, O22242",
  "https://api.vam.ac.uk/v2/object/O22242","2026-11-24 API HTTP 200；纸本水墨设色 装裱111×57.5cm；说明含虎辟邪/鹊报喜"),
 ("vam-o1768","Victoria and Albert Museum — Mosque lamp of Kafur al-Rumi, Egypt, 1342–1345, O1768",
  "https://api.vam.ac.uk/v2/object/O1768","2026-11-24 API HTTP 200；描金珐琅玻璃 高26cm；说明含马穆鲁克苏丹司库徽记"),
 ("vam-o85593","Victoria and Albert Museum — Mina'i Bowl, Kashan, 1180–1220, O85593",
  "https://api.vam.ac.uk/v2/object/O85593","2026-11-24 API HTTP 200；熔块胎釉上/釉下彩与描金 高9.0cm；说明含双骑手与金树"),
 ("vam-o76242","Victoria and Albert Museum — Inrō, Japan, 18th century, O76242",
  "https://api.vam.ac.uk/v2/object/O76242","2026-11-24 API HTTP 200；玳瑁·牙雕·裂纹蛋壳 高11.4cm；说明含印笼悬于腰带"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('tiger-magpie-hochakdo','韩国民画《虎鹊图》（Hochakdo）','作品','art-asia','19世纪','东亚','绘画','核心',
  '朝鲜纸本水墨设色《虎鹊图》，维多利亚与艾伯特博物馆藏（O22242）。','1850—1910年',
  '虎身朝右头转向左，望向左上松枝上两只喜鹊；虎为最强辟邪兽、鹊报喜；新年常悬于家门。','korean-celadon-bowl-lotus,japanese-art','vam-o22242'),
 ('mamluk-mosque-lamp','马穆鲁克清真寺灯（卡富尔·鲁米）','作品','art-islamic','14世纪','西亚·中亚','玻璃','核心',
  '玻璃描金珐琅清真寺灯，维多利亚与艾伯特博物馆藏（O1768）。','1342—1345年',
  '灰白无色玻璃，饰红白蓝珐琅；铭文与徽记为马穆鲁克苏丹萨利赫·伊斯玛仪之司库 Shibl al-Daula Kafur al-Rumi。','kashan-salting-mihrab,islamic-art','vam-o1768'),
 ('minai-bowl-kashan','卡尚米纳伊彩绘碗','作品','art-islamic','12—13世纪','西亚·中亚','陶瓷','核心',
  '卡尚熔块胎米纳伊碗，维多利亚与艾伯特博物馆藏（O85593）。','1180—1220年',
  '釉下与釉上彩并描金；碗心两骑手分居金树两侧，下方孔雀；内壁四组坐者与团花交替，若交谈之姿。','kashan-salting-mihrab,mamluk-mosque-lamp','vam-o85593'),
 ('japanese-inro','日本印笼（三层）','作品','art-asia','18世纪','东亚','综合','重要',
  '日本玳瑁与牙雕印笼，维多利亚与艾伯特博物馆藏（O76242）。','18世纪',
  '分层容器；和服无口袋，男子以丝绳与根付悬于腰带；原盛印章或药；一面持枪男子，一面倒挂猴捕蟹。','korean-celadon-bottle,japanese-art','vam-o76242'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")