# -*- coding: utf-8 -*-
"""R20 守卫：覆盖层（data/l2/*.json）**不得**携带基础字段——基础字段的唯一真值是 tools/catalog.py。
若出现，说明有人又在覆盖层里改基础信息，会导致 catalog 与全站不一致（历史上的 when/overview 漂移即由此而来）。
返回码 1 表示违规。"""
import json,os,glob,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE=["title","kind","unit","era","region","medium","tier","def","when","overview"]
bad=[]
for p in sorted(glob.glob(os.path.join(ROOT,"data","l2","*.json"))):
    o=json.load(open(p,encoding="utf-8"))
    hit=[k for k in BASE if k in o]
    if hit: bad.append((os.path.basename(p),hit))
print("overlay_guard: 违规 %d 个文件%s"%(len(bad),(" → %s"%bad[:5]) if bad else ""))
sys.exit(1 if bad else 0)
