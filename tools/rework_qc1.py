# -*- coding: utf-8 -*-
"""Cycle1 质量闸：返工 early-christian-art（移除来源无支撑的「鱼与牧羊人」裸断言，修正不实待核实措辞）。"""
import json, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"data","l2","early-christian-art.json")
o=json.load(open(P,encoding="utf-8"))
s=o["sections"]
s["overview"]="早期基督教艺术见于地下墓室壁画与巴西利卡教堂，后者成为礼拜建筑的基本形制；早期图像中的寓意性表现待来源核实。"
s["风格特征"]="所引来源页可支撑的内容为巴西利卡（basilica）作为礼拜建筑形制，以及地下墓室壁画这一形态。关于「鱼」「牧羊人」等寓意图像的中文表述，在所引英文来源页无逐字对应，列入待核实，不作为本条既定特征。"
s["技法或形式分析"]="在空间与建筑层面，来源可支撑的内容为地下墓室壁画与巴西利卡教堂两类形态。图像层面的具体寓意母题（如鱼、牧羊人）在所引来源页无逐字对应，待第二来源核实。"
s["一图"]="示意图展示巴西利卡礼拜建筑形制与地下墓室壁画两类形态的关系。"
s["待核实"]="（1）原L1种子的精确年代「约公元2—6世纪」在所引来源页无逐字支撑，此处不再声称「来源给出」，该区间待第二来源核实；（2）「鱼」「牧羊人」等寓意图像在所引英文来源页无逐字对应，待补中文或专著来源；（3）具体墓室、教堂名称、作品年份与收藏地未在输入中提及，待补充。"
o["overview"]=s["overview"]
json.dump(o,open(P,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("early-christian-art reworked")
