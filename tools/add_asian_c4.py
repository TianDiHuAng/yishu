# -*- coding: utf-8 -*-
"""Cycle4 B1新增：南亚/东南亚/东亚艺术 8条（History of painting 空白分支）。"""
import io, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","catalog.py")
s=io.open(P,encoding="utf-8").read()
anchor='\n]\n\ndef entries():'
assert anchor in s
s=s.replace(' ("glossary-tools","术语与辨疑"),\n]',
''' ("glossary-tools","术语与辨疑"),
 ("art-asia","亚洲艺术（南亚/东南亚/东亚）"),
]''')
ROWS='''
# ==== Cycle4 B1新增：History of painting 空白分支（南亚/东南亚/日本） ====
("indian-art","印度艺术","时期","art-asia","古代—近代","南亚","综合","重要",
 "印度次大陆的艺术传统，涵盖佛教、印度教与耆那教的宗教艺术及世俗绘画。","约公元前3世纪—公元19世纪",
 "印度艺术以雕塑与壁画见长，佛教艺术随丝路传播影响中亚与东亚，宗教图像具有象征与叙事功能。","buddhist-art-india,ajanta-caves","enc-indian-art,enc-history-painting"),
("buddhist-art-india","印度佛教艺术","风格","art-asia","古代—中世纪","南亚","雕塑,绘画","重要",
 "印度次大陆形成的佛教艺术传统，以佛像、石窟与壁画为核心。","约公元前3世纪—公元12世纪",
 "佛像雕刻在犍陀罗与马图拉等地发展，阿旃陀石窟壁画保存了杰出的佛教绘画遗存，并随佛教传播影响亚洲各地。","indian-art,ajanta-caves","enc-buddhist-art-india,enc-ajanta"),
("ajanta-caves","阿旃陀石窟","风格","art-asia","古代","南亚","绘画","补充",
 "印度马哈拉施特拉邦的佛教石窟群，以保存完好的古代壁画著称。","约公元前2世纪—公元6世纪",
 "阿旃陀石窟的壁画描绘佛本生故事与菩萨形象，色彩与线条展现了印度古代绘画的高度成就，是佛教艺术的重要遗存。","buddhist-art-india,indian-art","enc-ajanta,enc-buddhist-art-india"),
("khmer-art","高棉艺术","风格","art-asia","古代—中世纪","东南亚","建筑,雕塑","重要",
 "柬埔寨高棉帝国时期的艺术，以吴哥窟等印度教与佛教建筑闻名。","约公元9—15世纪",
 "高棉艺术以大规模寺庙建筑与浮雕叙事见长，吴哥建筑群体现印度教宇宙观与王权象征，是高棉文化的巅峰。","angkor,buddhist-art-india","enc-khmer-art,enc-angkor"),
("angkor","吴哥窟","风格","art-asia","中世纪","东南亚","建筑","补充",
 "柬埔寨吴哥地区的庞大寺庙建筑群，为高棉帝国的宗教与王权中心。","约公元9—15世纪",
 "吴哥建筑以层叠的塔庙与环绕的护城河象征印度教宇宙观，浮雕描绘史诗与王室场景，是世界最大的宗教建筑群之一。","khmer-art","enc-angkor,enc-khmer-art"),
("japanese-art","日本艺术","时期","art-asia","古代—近代","东亚","综合","重要",
 "日本列岛的艺术传统，涵盖佛教艺术、水墨画、浮世绘与装饰艺术。","约公元6世纪—19世纪",
 "日本艺术在吸收中国与韩国影响后形成独特风格，佛教造像、水墨画与浮世绘等门类成就突出，对近代西方艺术亦有影响。","ukiyo-e,zen-painting","enc-japanese-art,enc-ukiyo-e"),
("ukiyo-e","浮世绘","风格","art-asia","17—19世纪","日本","绘画","重要",
 "日本江户时代兴起的风俗画版画，题材包括美人、歌舞伎与风景。","约公元17—19世纪",
 "浮世绘以套色木版印刷与平面化构图见长，葛饰北斋与歌川广重等画家提升其艺术地位，19世纪传入欧洲后影响印象派与后印象派。","japanese-art,impressionism","enc-ukiyo-e,enc-japanese-art"),
("zen-painting","禅画","风格","art-asia","中世纪—近代","东亚","书法","补充",
 "东亚禅宗传统中的水墨绘画，强调简逸笔墨与顿悟精神。","约公元13—18世纪",
 "禅画以简练的笔触与留白传达禅意，与中国文人画传统相通，在日本禅宗寺院中发展为独立画风。","japanese-art,china-calligraphy-history","enc-zen-art,enc-japanese-art"),
'''
s=s.replace(anchor,ROWS+']\n\ndef entries():')
io.open(P,"w",encoding="utf-8").write(s)
print("added 8 Asian art entries")
