# -*- coding: utf-8 -*-
"""Cycle86：古埃及/近东 4 条（古迪亚、明内弗、阿蒙霍特普墓浮雕、纳芙蒂蒂 talatat）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1963-154","Cleveland Museum of Art — Statue of Gudea, Neo-Sumerian, c. 2144–2124 BCE, acc. 1963.154",
  "https://openaccess-api.clevelandart.org/api/artworks/1963.154","2026-11-23 API HTTP 200；闪长岩 126×55×36cm；说明含30余尊古迪亚像与2400余条铭文"),
 ("cma-1948-420","Cleveland Museum of Art — Striding Statue of Minnefer, Old Kingdom, c. 2377–2311 BCE, acc. 1948.420",
  "https://openaccess-api.clevelandart.org/api/artworks/1948.420","2026-11-23 API HTTP 200；彩绘石灰岩 53.8×14.4×23.4cm；说明含 serdab 与 ka"),
 ("cma-1963-100","Cleveland Museum of Art — Tomb Relief of Amenhotep and Family, New Kingdom, c. 1279–1257 BCE, acc. 1963.100",
  "https://openaccess-api.clevelandart.org/api/artworks/1963.100","2026-11-23 API HTTP 200；石灰岩存彩 128×119.5cm；说明含1913—14发掘与四城分藏"),
 ("cma-1959-188","Cleveland Museum of Art — Talatat: Portrait of Nefertiti, Karnak, c. 1353–1347 BCE, acc. 1959.188",
  "https://openaccess-api.clevelandart.org/api/artworks/1959.188","2026-11-23 API HTTP 200；彩绘砂岩 22×22.7cm；说明含阿顿神庙拆解与王后形象频度"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('gudea-statue','古迪亚雕像（新苏美尔）','作品','art-ancient','公元前22世纪','西亚·中亚','雕塑','核心',
  '拉伽什统治者古迪亚雕像，克利夫兰艺术博物馆藏（1963.154）。','约前2144—2124年',
  '双手交握的姿势见于30余尊古迪亚像；该馆记已辨识2400余条关于其统治的铭文。','shang-zhou-bronzes,egyptian-art','cma-1963-154'),
 ('minnefer-statue','明内弗行进像','作品','art-ancient','公元前24世纪','埃及','雕塑','核心',
  '古王国第五王朝彩绘石灰岩雕像，克利夫兰艺术博物馆藏（1948.420）。','约前2377—2311年',
  '出土于吉萨马斯塔巴密封雕像室（serdab）；仪式后作为亡者替身，享用供品以维系 ka。','gudea-statue,egyptian-art','cma-1948-420'),
 ('amenhotep-tomb-relief','阿蒙霍特普医生墓浮雕','作品','art-ancient','公元前13世纪','埃及','雕塑','重要',
  '拉美西斯二世时期阿西尤特墓室浮雕，克利夫兰艺术博物馆藏（1963.100）。','约前1279—1257年',
  '医生率家人举手祈祷；1913—14年发掘后分藏四城，紧邻右半在苏黎世。','gudea-statue,minnefer-statue','cma-1963-100'),
 ('nefertiti-talatat','纳芙蒂蒂 Talatat 浮雕','作品','art-ancient','公元前14世纪','埃及','雕塑','核心',
  '卡纳克阿顿神庙彩绘砂岩浮雕块，克利夫兰艺术博物馆藏（1959.188）。','约前1353—1347年',
  '阿肯那顿短命宗教改革时期作品；王后形象频度远超国王；神庙后被拆作阿蒙神庙基填。','minnefer-statue,egyptian-art','cma-1959-188'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")