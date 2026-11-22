# -*- coding: utf-8 -*-
"""第2批复检二轮：清理 cursive-script / donatello / romanesque 的残留无源说法。"""
import json, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LD=os.path.join(ROOT,"data","l2")
def load(e): return json.load(open(os.path.join(LD,e+".json"),encoding="utf-8"))
def save(e,o): json.dump(o,open(os.path.join(LD,e+".json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)

# cursive-script：人物节与一图去掉"狂草"断言
o=load("cursive-script")
o["sections"]["代表人物与作品"]="概述中点名张旭、怀素两位人物；来源页仅见其名录，未提供具体作品名称。相关条目中的行书、中国书法史为书体与史论条目，未附具体人物作品细节。"
o["sections"]["一图"]="示意图说明草书笔画高度简化、连绵奔放的特征，并连接相关书体条目。"
save("cursive-script",o)

# donatello：风格特征末句与一图去掉"解剖准确性"
o=load("donatello")
o["sections"]["风格特征"]="来源页记载多纳泰罗推动古典雕塑复兴，并以青铜《大卫》《圣乔治》等作品著称；“解剖准确性”这一术语在所引来源页无逐字对应，列入待核实。青铜《大卫》与《圣乔治》是概述点名的作品，体现其与古典雕塑复兴的关联。"
o["sections"]["一图"]="示意图以多纳泰罗为中心，连接青铜《大卫》与《圣乔治》，并标出古典雕塑复兴这一来源可支撑的取向。"
save("donatello",o)

# romanesque：时代背景/人物节/一图去掉1150与厚墙小窗/十字拱断言
o=load("romanesque")
o["when"]="约11—12世纪（中世纪盛期）"
o["sections"]["时代背景"]="罗马式艺术流行于中世纪盛期的西欧。定义给出的年代为11—12世纪；原L1种子的精确区间“约1000—1150年”在所引来源页无逐字对应，列入待核实。材料将厚重的石构教堂与门楣雕塑视为其标志。"
o["sections"]["代表人物与作品"]="材料未点名具体代表人物或作品。可作为代表对象的，是半圆拱（round-headed arches）与门楣（tympanum）、柱头（capital）雕塑等来源可支撑的建筑与雕塑特征；厚墙、小窗、十字拱等说法待第二来源核实。"
o["sections"]["一图"]="示意图用半圆拱与门楣、柱头雕塑概括罗马式艺术的建筑与雕塑特征。"
save("romanesque",o)
print("residual rework done for 3 entries")
