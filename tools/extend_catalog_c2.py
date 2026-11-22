# -*- coding: utf-8 -*-
"""Cycle2: 追加比较/导读/辨析类条目到 catalog.py（B4读者问题缺口，§4 上限11条）。"""
import io, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","catalog.py")
s=io.open(P,encoding="utf-8").read()
anchor='\n]\n\ndef entries():'
assert anchor in s, "anchor not found"
# 新单元
s=s.replace(' ("music-china","中国音乐史"),\n])',
''' ("music-china","中国音乐史"),
 ("overview-guide","导读与学科方法"),
 ("comparative","比较视野"),
 ("glossary-tools","术语与辨疑"),
])''')
# 新条目（id,title,kind,unit,era,region,medium,tier,def,when,overview,related,sources）
ROWS='''
# ==== Cycle2 新增：B4读者问题缺口（导读/比较/术语） ====
("what-is-art-history","什么是艺术史","术语","overview-guide","学科方法","全球","综合","核心",
 "研究视觉艺术的历史发展、风格演变与社会文化语境的学科。","历代",
 "艺术史区别于艺术鉴赏与艺术批评，关注作品在历史脉络中的位置、风格承变与生产条件。","art-criticism-note,reading-path","enc-art-history,enc-art-criticism"),
("what-is-music-history","什么是音乐史","术语","overview-guide","学科方法","全球","音乐体裁","核心",
 "研究音乐的历史发展、体裁演变与风格变迁的学科。","历代",
 "音乐史区别于乐理与音乐学，按时代与体裁梳理作曲实践、形式技法与接受语境。","musicology-note,reading-path","enc-musicology,enc-medieval-music"),
("reading-path","零基础阅读路径","术语","overview-guide","学科方法","全球","综合","重要",
 "本知识库推荐的入门到深入的学习顺序。","历代",
 "建议按学科导论→通史单元→核心流派→代表人物与作品的顺序阅读，先建立框架再深入细节。","what-is-art-history,what-is-music-history","enc-art-history,enc-musicology"),
("art-criticism-note","艺术史与艺术批评的区分","术语","overview-guide","学科方法","全球","综合","补充",
 "艺术史重历史脉络与事实考证，艺术批评重价值判断与阐释。","历代",
 "二者视角不同：前者追问作品为何产生、如何演变，后者评价作品优劣与意义。","what-is-art-history","enc-art-history,enc-art-criticism"),
("musicology-note","音乐史与音乐学的区分","术语","overview-guide","学科方法","全球","音乐体裁","补充",
 "音乐史按时代叙述音乐变迁，音乐学以更广的方法研究音乐现象。","历代",
 "音乐史侧重时间线索与体裁沿革，音乐学包含历史音乐学、民族音乐学、音乐理论等分支。","what-is-music-history","enc-musicology,enc-music-history"),
("baroque-crossmedia","巴洛克：艺术与音乐的共通美学","风格","comparative","17—18世纪","欧洲","综合","重要",
 "比较巴洛克艺术与巴洛克音乐在动势、戏剧性与对比手法上的共通追求。","约17—18世纪",
 "视觉艺术以明暗对照与对角线构图制造动势，音乐以力度对比、通奏低音与大型声乐体裁强化戏剧性。","baroque,baroque-music","enc-baroque-art,enc-baroque-music"),
("romantic-crossmedia","浪漫主义：绘画与音乐两种媒介","风格","comparative","19世纪","欧洲","综合","重要",
 "比较浪漫主义在绘画与音乐中的题材选择、情感表达与形式突破。","约19世纪",
 "绘画偏重戏剧性题材与色彩表现，音乐偏重情感张力、民族性与和声复杂化，共享对个体情感的强调。","romanticism-art,romantic-music","enc-romantic-art,enc-romantic-music"),
("renaissance-crossmedia","文艺复兴：美术与音乐的同期性","风格","comparative","14—16世纪","欧洲","综合","重要",
 "比较视觉艺术与音乐在文艺复兴时期的时间重合与人文主义共同背景。","约14—16世纪",
 "两个领域同受人文主义影响，艺术复兴古典形式，音乐发展复调与世俗体裁，但具体断代略有错位。","renaissance,renaissance-music","enc-renaissance,enc-renaissance-music"),
("impression-crossmedia","印象主义：光与色的跨媒介追求","风格","comparative","19末—20世纪初","欧洲","综合","重要",
 "比较印象派绘画与印象主义音乐在氛围、色彩与音色上的共同追求。","约1870—1920年",
 "绘画以松散笔触与光色瞬间记录印象，音乐以色彩性和声与精致配器营造氛围，均弱化传统结构。","impressionism,impressionism-music","enc-impressionism,enc-impressionist-music"),
("modern-to-contemporary","从现代到当代的分期衔接","时期","glossary-tools","20世纪","欧美","综合","重要",
 "梳理现代艺术与当代艺术之间的断代争议与过渡。","约1950—1970年",
 "现代艺术下限与当代艺术上限的划分无统一标准，抽象表现主义、波普与观念艺术构成过渡环节。","modern-art,contemporary-art","enc-modern-contemporary,enc-postmodern"),
'''
s=s.replace(anchor, ROWS+']\n\ndef entries():')
io.open(P,"w",encoding="utf-8").write(s)
print("catalog extended with Cycle2 rows")
