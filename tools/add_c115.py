# -*- coding: utf-8 -*-
"""Cycle115：伊斯兰金属器 4 条（大马士革盖钵、呼罗珊执壶、Qa’itbay 盆、Zayn al-Din 桶）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o76198","Victoria and Albert Museum — Lidded bowl, Damascus, 1500–1550, O76198",
  "https://api.vam.ac.uk/v2/object/O76198","2026-11-24 API HTTP 200；黄铜嵌银 高6.0 径14.6cm；说明含意家族纹章与香料容器"),
 ("vam-o76859","Victoria and Albert Museum — Ewer, Khurasan, ca. 1200–1250, O76859",
  "https://api.vam.ac.uk/v2/object/O76859","2026-11-24 API HTTP 200；铜片嵌铜银 高38cm；说明含九宽九窄棱与狮纹"),
 ("vam-o84518","Victoria and Albert Museum — Basin of Sultan Qa’itbay, Egypt, 1468–1496, O84518",
  "https://api.vam.ac.uk/v2/object/O84518","2026-11-24 API HTTP 200；锤揲黄铜嵌饰 高15.4 径40.6cm；说明含 Qa’itbay 赞助"),
 ("vam-o83886","Victoria and Albert Museum — Bucket signed Zayn al-Din, ca. 1475–1500, O83886",
  "https://api.vam.ac.uk/v2/object/O83886","2026-11-24 API HTTP 200；黄铜旋切贴银 高13.5 径27.5cm；说明含 Zayn al-Din 署名"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('damascus-lidded-bowl','大马士革嵌银盖钵','作品','art-islamic','16世纪','西亚·中亚','金属器','重要',
  '大马士革黄铜嵌银盖钵，维多利亚与艾伯特博物馆藏（O76198）。','1500—1550年',
  '浅盖钵、陡壁、平贴合盖；錾刻嵌银与黑料；细密缠枝、盾形圆章；平盖或为量盛香料之器；带未识意大利家族纹章。','khurasan-ewer,qaitbay-basin','vam-o76198'),
 ('khurasan-ewer','呼罗珊嵌金银执壶','作品','art-islamic','13世纪','西亚·中亚','金属器','核心',
  '呼罗珊铜片嵌铜银执壶，维多利亚与艾伯特博物馆藏（O76859）。','约1200—1250年',
  '束腰足圈承九宽九窄棱身、间以细凸棱；肩部圆凸；平肩中央八角玫瑰饰接长颈与长流；饰结绳纹、为匿名主人祈福铭、颈流蹲狮。','mamluk-inlaid-basin,damascus-lidded-bowl','vam-o76859'),
 ('qaitbay-basin','卡伊特贝盆（马穆鲁克）','作品','art-islamic','15世纪','西亚·中亚','金属器','核心',
  '埃及锤揲黄铜嵌饰盆，维多利亚与艾伯特博物馆藏（O84518）。','1468—1496年',
  '深壁大盆，锤揲、錾刻与嵌饰；苏丹 Qa’itbay 治下艺作勃兴，多因其亲自赞助；宗教建筑及其陈设为大宗。','mamluk-inlaid-basin,mamluk-mosque-lamp','vam-o84518'),
 ('zayn-al-din-bucket','扎因丁署名铜桶','作品','art-islamic','15世纪','西亚·中亚','金属器','重要',
  '黄铜旋切贴银铜桶，维多利亚与艾伯特博物馆藏（O83886）。','约1475—1500年',
  '带提手，通体錾刻花卉并部分贴银以增贵；提手凸缘内侧有阿拉伯署名 Zayn al-Din，其署名亦见于数件同类器。','damascus-lidded-bowl,qaitbay-basin','vam-o83886'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")