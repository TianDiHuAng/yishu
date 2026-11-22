# -*- coding: utf-8 -*-
"""Cycle3 B1新增4条（记谱法/调式/小提琴/钢琴），依据 Outline of music 空白维度。"""
import io, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","catalog.py")
s=io.open(P,encoding="utf-8").read()
anchor='\n]\n\ndef entries():'
assert anchor in s
ROWS='''
# ==== Cycle3 B1新增：Outline of music 空白维度（记谱法/调式/西方乐器） ====
("music-notation","记谱法","术语","glossary-tools","历代","全球","音乐体裁","重要",
 "以符号系统记录音乐音高、节奏与演奏指示的方法。","历代",
 "记谱法使音乐得以跨时空保存与传播，是复调与大型体裁发展的技术前提；西方五线谱与中国古代工尺谱等体系各有传统。","gregorian-chant,polyphony","enc-music-notation,enc-staff-notation"),
("musical-mode","调式","术语","glossary-tools","历代","全球","音乐体裁","重要",
 "音阶中音高之间的组织关系及主音优先性的体系。","历代",
 "调式决定旋律的音高素材与色彩；欧洲中世纪教会调式、大小调体系与世界各地民歌调式各有规则。","tonality,gregorian-chant","enc-mode,enc-church-modes"),
("violin","小提琴","术语","glossary-tools","17世纪—今","欧洲","音乐体裁","补充",
 "西方弦乐器家族的高音弓弦乐器，四弦定弦并广泛用于独奏、室内乐与管弦乐。","约公元17世纪定型—至今",
 "小提琴在巴洛克时期成为重要独奏与合奏乐器，古典与浪漫时期协奏曲与奏鸣曲文献丰富。","baroque-music,symphony","enc-violin,enc-baroque-music"),
("piano","钢琴","术语","glossary-tools","18世纪—今","欧洲","音乐体裁","补充",
 "以琴槌击弦发声的键盘乐器，音域宽广、可同时演奏多声部。","约公元18世纪定型—至今",
 "钢琴在古典与浪漫时期成为作曲与演奏的核心乐器，奏鸣曲、练习曲与艺术歌曲均以其为主要载体。","sonata,chopin","enc-piano,enc-classical-period-music"),
'''
s=s.replace(anchor,ROWS+']\n\ndef entries():')
io.open(P,"w",encoding="utf-8").write(s)
print("added 4 B1 entries")
