# -*- coding: utf-8 -*-
"""Cycle6 B4作品档案：新增5条代表作档案条目（每条≥2已核验来源）。"""
import io, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","catalog.py")
s=io.open(P,encoding="utf-8").read()
anchor='\n]\n\ndef entries():'
assert anchor in s
s=s.replace(' ("art-asia","亚洲艺术（南亚/东南亚/东亚）"),\n]',
''' ("art-asia","亚洲艺术（南亚/东南亚/东亚）"),
 ("work-archives","作品档案"),
]''')
ROWS='''
# ==== Cycle6 B4新增：作品档案（B4爱好者问题，均有≥2核验来源） ====
("starry-night","《星月夜》","作品","work-archives","19世纪","欧美","绘画","重要",
 "文森特·梵高创作的油画，现藏纽约现代艺术博物馆（MoMA）。","1889年",
 "此画为梵高在圣雷米疗养院期间所作，以漩涡状笔触与强烈色彩描绘夜空，是后印象派的代表作之一。","van-gogh,post-impressionism","enc-starry-night,enc-moma"),
("birth-of-venus-work","《维纳斯的诞生》","作品","work-archives","15世纪","意大利","绘画","重要",
 "桑德罗·波提切利的蛋彩画，现藏佛罗伦萨乌菲齐美术馆。","约公元1485年",
 "作品描绘维纳斯自海浪中诞生的场景，以流畅线条与明丽色彩著称，体现文艺复兴早期的人文主义趣味。","botticelli,early-renaissance","enc-birth-venus,enc-uffizi"),
("sistine-ceiling-work","西斯廷礼拜堂天顶画","作品","work-archives","16世纪","意大利","绘画","重要",
 "米开朗基罗为梵蒂冈西斯廷礼拜堂绘制的天顶壁画。","约公元1508—1512年",
 "天顶画以《创世纪》场景为核心，塑造了极具体量感的人物形象，是盛期文艺复兴雕塑式绘画的杰作。","michelangelo,high-renaissance","enc-sistine-ceiling,enc-michelangelo"),
("guernica-work","《格尔尼卡》","作品","work-archives","20世纪","西班牙","绘画","重要",
 "巴勃罗·毕加索的黑白灰油画，回应1937年格尔尼卡轰炸。","1937年",
 "作品以变形与拼贴化的图像控诉战争暴力，成为20世纪最具政治性的艺术作品之一，现藏马德里索菲亚王后艺术中心。","picasso,cubism","enc-guernica,enc-picasso"),
("rite-of-spring-work","《春之祭》","作品","work-archives","20世纪","俄国/法国","音乐体裁","重要",
 "伊戈尔·斯特拉文斯基的芭蕾舞剧，1913年在巴黎首演引发轰动。","1913年",
 "作品以强烈节奏与不协和音响描绘史前祭祀场景，首演时的争议成为现代音乐史上的著名事件。","stravinsky,20th-century-classical","enc-rite-spring,enc-stravinsky"),
'''
s=s.replace(anchor,ROWS+']\n\ndef entries():')
io.open(P,"w",encoding="utf-8").write(s)
print("added 5 work-archive entries")
