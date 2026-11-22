# -*- coding: utf-8 -*-
"""Cycle4: 应用 b5_remaining 中唯一已核验解决项（romanesque 地区差异）。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
items=[x for x in json.load(open(os.path.join(ROOT,"reports","b5_remaining_c4.json"),encoding="utf-8")) if x.get("resolved")]
# 来源已存在于 Cycle3（enc-romanesque 已核验），此URL即该来源，无需新增
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8"))
url=items[0]["source"]["url"]
src=next((s for s in sd["sources"] if s["url"]==url),None)
print("matching source:",src["id"] if src else "NONE")
if not src:
 sid="enc-romanesque-architecture"
 sd["sources"].append({"id":sid,"title":"Romanesque architecture","author":"Wikipedia contributors","year":"2026",
   "url":url,"type":"权威百科","verified":True,"verified_note":"B5-C4 HTTP200 命中厚墙/小窗/半圆拱/groin vault/regional"}); sid_use=sid
 json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
else: sid_use=src["id"]
# 更新 romanesque overlay
p=os.path.join(D,"l2","romanesque.json"); o=json.load(open(p,encoding="utf-8"))
if sid_use not in o["sources"]: o["sources"].append(sid_use)
o["sections"]["待核实"] += " 【已复核】厚墙小窗/半圆拱/十字拱的地区差异：第二来源 %s（%s），据该来源：%s"%(
 sid_use,url,items[0]["body_rewrite"])
json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("romanesque B5 applied")
