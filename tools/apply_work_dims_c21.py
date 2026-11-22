# -*- coding: utf-8 -*-
"""Cycle21d：把 Wikidata 的尺寸/藏品编号/材质写入 5 个作品条目的"待核实"节，
标注【已复核·Wikidata】并明示"该数据为单一结构化来源，正文暂不引用"（遵守双源规则）。"""
import json,os,re
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LD=os.path.join(ROOT,"data","l2")
d=json.load(open(os.path.join(ROOT,"reports","work_dims_c21.json"),encoding="utf-8"))
def fmt(v): 
    try: return ("%.1f"%float(str(v).lstrip("+"))).rstrip("0").rstrip(".")
    except Exception: return str(v)
n=0
for eid,rec in d.items():
    if not rec["height_P2048"] or not rec["width_P2049"]: continue
    p=os.path.join(LD,eid+".json")
    if not os.path.exists(p): print("skip(no overlay)",eid); continue
    o=json.load(open(p,encoding="utf-8"))
    h=fmt(rec["height_P2048"][0]); w=fmt(rec["width_P2049"][0])
    mat="、".join(rec["material_P186"][:2]); inv="、".join(rec["inventory_P217"][:2])
    line="【已复核·Wikidata】尺寸/材质/藏品号：%s × %s cm；材质 %s；藏品编号 %s（来源 https://www.wikidata.org/wiki/%s）。"%(h,w,mat or "未列",inv or "未列",rec["qid"])
    line+=" 说明：该组数据目前**仅有一个结构化来源**（Wikidata），未达双源互证标准，故只登记于此、**不写入正文**。"
    pend=o["sections"]["待核实"]
    if "【已复核·Wikidata】尺寸" not in pend:
        o["sections"]["待核实"]=pend+" "+line
        json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1); n+=1
        print(eid,"->",h,"x",w,"cm |",mat,"|",inv)
print("updated",n)