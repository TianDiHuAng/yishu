# -*- coding: utf-8 -*-
"""Cycle135：伊斯兰 4 条（米纳伊杯、萨法维罂粟织物、萨法维《五宝》故事、萨珊马形饮器）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1917-977","Cleveland Museum of Art — Mina'i beaker with seated princes, Kashan, 1180–1220, acc. 1917.977",
  "https://openaccess-api.clevelandart.org/api/artworks/1917.977","2026-11-24 API HTTP 200；熔块胎釉上彩 13.3×12.3cm；说明含首个真彩瓷与书像式场景"),
 ("cma-1926-22","Cleveland Museum of Art — Safavid textile with poppies on golden ground, 1600–1750, acc. 1926.22",
  "https://openaccess-api.clevelandart.org/api/artworks/1926.22","2026-11-24 API HTTP 200；丝与金线斜纹纬浮印花 85.7×71.1cm；说明含印伊织物贸易"),
 ("cma-1947-500-b","Cleveland Museum of Art — Khamsa of Nizami: Khusrau and Shirin (verso), Shiraz, 1540–70, acc. 1947.500.b",
  "https://openaccess-api.clevelandart.org/api/artworks/1947.500.b","2026-11-24 API HTTP 200；纸本不透明水彩金 29.6×16.2cm；说明含夜景、石榴与tanbur"),
 ("cma-1964-41","Cleveland Museum of Art — Sasanian horse-shaped drinking vessel, 200–325 CE, acc. 1964.41",
  "https://openaccess-api.clevelandart.org/api/artworks/1964.41","2026-11-24 API HTTP 200；银局部鎏金 12×10.8×32.7cm；说明含尼萨马与无权杖环像"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('minai-beaker-princes','米纳伊坐王子高足杯','作品','art-islamic','12—13世纪','西亚·中亚','陶瓷','核心',
  '卡尚米纳伊釉上彩高足杯，克利夫兰艺术博物馆藏（1917.977）。','1180—1220年',
  'mina\u2019i 意为珐琅，为奢侈陶；以珐琅彩首次成真正多色瓷；蓝绿紫配锐黑红；人物场景常见，如列坐朝臣簇拥王者、狩猎放鹰。','minai-bowl-kashan,kashan-salting-mihrab','cma-1917-977'),
 ('safavid-poppy-textile','萨法维罂粟纹金地织物','作品','art-islamic','17—18世纪','西亚·中亚','织物','核心',
  '萨法维丝与金线织物，克利夫兰艺术博物馆藏（1926.22）。','1600—1750年',
  '印伊织物贸易兴盛，莫卧儿与萨法维宫廷皆赏两地产品；细腻人字纹托出成行罂粟，桃绿丝线以断纬相绞成花、表面光滑而轻。','ardabil-carpet,ottoman-silk-velvet','cma-1926-22'),
 ('safavid-khamsa-khusrau','《五宝》之《霍斯鲁与希琳》（萨法维）','作品','art-islamic','16世纪','西亚·中亚','绘画','核心',
  '设拉子《五宝》写本插图（背面），克利夫兰艺术博物馆藏（1947.500.b）。','1540—1570年',
  '尼扎米《五宝》含萨珊王霍斯鲁·帕尔维兹（590—628）与亚美尼亚公主希琳之恋；夜色以变暗的银点星；希琳奉无花果石榴（喻丰产），右下乐人弹长颈有品tanbur。','shiraz-frontispiece,panj-ganj-page','cma-1947-500-b'),
 ('sasanian-horse-vessel','萨珊马形饮器','作品','art-islamic','公元3—4世纪','西亚·中亚','金属器','核心',
  '萨珊银局部鎏金马形饮器，克利夫兰艺术博物馆藏（1964.41）。','200—325年',
  '马为古伊朗钟爱题材、育马兴盛；此健硕牡马源出阿契美尼德王朝皇家圣种尼萨马；萨珊马具繁丽却无马镫；马静卧如近东骆驼待人骑；肩部圆章内为持权杖环之王像。','sasanian-hunting-dish,luristan-ibex-standard','cma-1964-41'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")