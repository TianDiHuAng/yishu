# -*- coding: utf-8 -*-
"""Cycle18 修正：去掉 khmer-architecture 正文中来源未支撑的"19世纪后重新发现"表述，
改为不带年份的审慎表述，并把该点列入待核实。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
p=os.path.join(ROOT,"data","l2","khmer-architecture.json")
o=json.load(open(p,encoding="utf-8"))
old="其后随帝国衰落而中断，19世纪后被重新发现与研究。"
new="其后随帝国衰落而中断，建筑群在近现代被重新记录与研究（具体年代待核实）。"
sec=o["sections"]
assert old in sec["与前后风格的关系和争论"], "原文未匹配"
sec["与前后风格的关系和争论"]=sec["与前后风格的关系和争论"].replace(old,new)
add="（5）「近现代被重新记录与研究」的具体年代与研究者未在输入中给出，待补充第二来源（原稿曾写「19世纪后」，因来源未支撑已删去）。"
if "重新记录与研究" not in sec["待核实"]:
    sec["待核实"]=sec["待核实"]+" "+add
json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("patched khmer-architecture stance sentence")