# -*- coding: utf-8 -*-
"""Cycle17：新增 2 条建筑类条目（哥特式建筑、罗马式建筑），归入 art-medieval，medium=建筑。
来源结构：内容来源（已核验 Wikipedia 专页）+ 身份确认（Wikidata）+ 关联风格页。
诚实处理：Wikidata 只确认实体身份与名称，不提供年代；年代类断言仍标待核实。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","catalog.py")
s=io.open(P,encoding="utf-8").read()
anchor='\n]\n\ndef entries():'
assert anchor in s
ROWS='''
# ==== Cycle17 新增：建筑类（A 类矩阵缺口，2 来源/条） ====
("gothic-architecture","哥特式建筑","风格","art-medieval","中世纪晚期","西欧","建筑","重要",
 "中世纪晚期西欧以尖拱、肋拱、飞扶壁与大面积彩色玻璃为特征的建筑样式。","约12世纪后期—16世纪",
 "尖拱改变受力方式，肋拱与飞扶壁使墙体减薄、窗户得以扩大，彩色玻璃营造神秘光线；沙特尔大教堂为常被引用的实例。",
 "gothic,romanesque-architecture","enc-gothic-architecture,enc-gothic,wd-gothic-architecture"),
("romanesque-architecture","罗马式建筑","风格","art-medieval","中世纪盛期","西欧","建筑","重要",
 "11—12世纪西欧以厚墙、小窗、半圆拱与筒形拱为特征的建筑样式。","约11—12世纪",
 "半圆拱与厚重墙体承担荷载，门楣与柱头雕塑承担叙事功能；不同地区在材料与细部上各有差异。",
 "romanesque,gothic-architecture","enc-romanesque,enc-romanesque-architecture,wd-romanesque-architecture"),
'''
s=s.replace(anchor,ROWS+']\n\ndef entries():')
io.open(P,"w",encoding="utf-8").write(s)
print("catalog: 2 architecture entries added")