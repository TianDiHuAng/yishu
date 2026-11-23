# -*- coding: utf-8 -*-
"""Cycle92：两河/波斯早期 4 条。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1970-61","Cleveland Museum of Art — Bull Calf Polemount, Sumerian, c. 2700 BCE, acc. 1970.61",
  "https://openaccess-api.clevelandart.org/api/artworks/1970.61","2026-11-23 API HTTP 200；玄武岩 7.7×5.1×13.1cm；说明含镶嵌丢失与极少数幸存的祭祀像"),
 ("cma-1943-279","Cleveland Museum of Art — Guardsman relief from Palace of Xerxes, Persepolis, 486–465 BCE, acc. 1943.279",
  "https://openaccess-api.clevelandart.org/api/artworks/1943.279","2026-11-23 API HTTP 200；灰石灰岩 53×43.6cm；说明含波斯波利斯西楼梯与希罗多德"),
 ("cma-1961-33","Cleveland Museum of Art — Master of Animals Cheekpiece, Luristan, c. 700 BCE, acc. 1961.33",
  "https://openaccess-api.clevelandart.org/api/artworks/1961.33","2026-11-23 API HTTP 200；铸造刻线青铜 14.9×21.3cm；说明含动物主人母题与马具"),
 ("cma-1962-150","Cleveland Museum of Art — Sasanian hunting dish of Hormizd II/III, 400–600 CE, acc. 1962.150",
  "https://openaccess-api.clevelandart.org/api/artworks/1962.150","2026-11-23 API HTTP 200；鎏金银盘 4.6×20.8cm；说明含王冠辨识与后世纪念作"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('sumer-bull-polemount','苏美尔牛犊杆头饰','作品','art-ancient','公元前27世纪','西亚·中亚','雕塑','核心',
  '苏美尔玄武岩小牛像，克利夫兰艺术博物馆藏（1970.61）。','约公元前2700年',
  '原为神庙崇拜物；眼、额部三角与绳索纹曾嵌异色石或骨，镶嵌已失。','gudea-statue,egyptian-art','cma-1970-61'),
 ('xerxes-guard-relief','薛西斯宫卫兵浮雕残块','作品','art-ancient','公元前5世纪','西亚·中亚','雕塑','核心',
  '波斯波利斯宫殿灰石灰岩浮雕，克利夫兰艺术博物馆藏（1943.279）。','公元前486—前465年',
  '或出自宫殿西阶梯；希罗多德记希腊以民主对君主制击败薛西斯。','greek-art,roman-art','cma-1943-279'),
 ('luristan-master-cheekpiece','卢里斯坦「动物主人」马颊饰','作品','art-ancient','公元前8—前7世纪','西亚·中亚','综合','重要',
  '伊朗卢里斯坦铸造刻线青铜马具，克利夫兰艺术博物馆藏（1961.33）。','约公元前700年',
  '有角男子抓双翼兽前腿，翼兽踩兔；环供连接马衔，另一片颊饰已失。','gudea-statue,shang-zhou-bronzes','cma-1961-33'),
 ('sasanian-hunting-dish','萨珊狩猎纹银盘','作品','art-ancient','公元5—6世纪','西亚·中亚','综合','重要',
  '萨珊鎏金银盘，克利夫兰艺术博物馆藏（1962.150）。','公元400—600年',
  '以王冠识为霍尔米兹德二世，但风格提示或为后世同理之名君主的纪念作。','islamic-art,roman-art','cma-1962-150'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")