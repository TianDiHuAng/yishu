# -*- coding: utf-8 -*-
"""Cycle2 B6：新增1条近期动态条目（武王墩楚墓礼乐考古，双源=官方新闻+中国音乐史百科）。"""
import io, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","catalog.py")
s=io.open(P,encoding="utf-8").read()
anchor='\n]\n\ndef entries():'
assert anchor in s
ROWS='''
# ==== Cycle2 新增：B6近期动态（2025-12，官方来源） ====
("wuwangdu-chu-music-archaeology","武王墩楚墓礼乐考古新进展","时期","music-china","2025年","中国","音乐体裁","补充",
 "2025年厦门大学团队公布安徽淮南武王墩楚王大墓乐器整理成果，复原漆木瑟与笙竽类乐器并进行编钟测音。","2025年12月",
 "该成果为战国礼乐制度研究提供新材料，正式考古报告与测音数据尚待发表，本条仅据官方新闻与既有中国音乐史背景作审慎概述。","yayue,china-music-history","news-xiamen-wuwangdu,enc-chinese-music"),
'''
s=s.replace(anchor,ROWS+']\n\ndef entries():')
io.open(P,"w",encoding="utf-8").write(s)
print("B6 entry added")
