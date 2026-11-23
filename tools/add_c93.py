# -*- coding: utf-8 -*-
"""Cycle93：文艺复兴 4 条（Filippino Lippi tondo、Lotto 肖像、Buglioni 釉陶、Verrocchio 基督胸像）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1932-227","Cleveland Museum of Art — Filippino Lippi, Holy Family with Saints John the Baptist and Margaret, c. 1488–93, acc. 1932.227",
  "https://openaccess-api.clevelandart.org/api/artworks/1932.227","2026-11-23 API HTTP 200；木板蛋彩与油 直径153cm；说明含 Carafa 委托与古维纳斯改写为圣玛格丽特"),
 ("cma-1950-250","Cleveland Museum of Art — Lorenzo Lotto, Portrait of a Man, Possibly Girolamo Rosati, 1533–34, acc. 1950.250",
  "https://openaccess-api.clevelandart.org/api/artworks/1950.250","2026-11-23 API HTTP 200；布面油画 108.2×100.5cm；说明含手势之谜与三叶草/茉莉/玫瑰象征"),
 ("cma-1921-1180","Cleveland Museum of Art — Benedetto Buglioni, Virgin and Child Enthroned with Saints, c. 1510–20, acc. 1921.1180",
  "https://openaccess-api.clevelandart.org/api/artworks/1921.1180","2026-11-23 API HTTP 200；釉陶 174×96×27cm；说明含 della Robbia 推广釉陶与替代大理石"),
 ("cma-1921-956","Cleveland Museum of Art — Andrea del Verrocchio, Bust of Christ, c. 1470–1500, acc. 1921.956",
  "https://openaccess-api.clevelandart.org/api/artworks/1921.956","2026-11-23 API HTTP 200；彩绘陶与木 57.2×53.3×29.2cm；说明含工坊复制与分工"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('lippi-holy-family-tondo','利皮《圣家族与施洗约翰、圣玛格丽特》圆形画','作品','art-renaissance','15世纪','意大利','绘画','核心',
  'Filippino Lippi 木板蛋彩油圆形画，克利夫兰艺术博物馆藏（1932.227）。','约1488—1493年',
  '红衣主教 Carafa 委托；五个盛彩人物在圆形画幅中交叠；草图中古维纳斯像被改写为圣玛格丽特。','botticelli,early-renaissance','cma-1932-227'),
 ('lotto-portrait-man','洛托《男子肖像（或为罗萨蒂）》','作品','art-renaissance','16世纪','意大利','绘画','核心',
  'Lorenzo Lotto 布面油画，克利夫兰艺术博物馆藏（1950.250）。','1533—1534年',
  '手势之谜；桌上三叶草寓丰饶/婚姻、茉莉与玫瑰寓纯洁与爱；「被打断的瞬间」是洛托的自然主义特征。','renaissance,high-renaissance','cma-1950-250'),
 ('buglioni-glazed-terracotta','布利奥尼《圣母圣婴与二圣》釉陶','作品','art-renaissance','16世纪','意大利','雕塑','重要',
  'Benedetto Buglioni 釉陶祭坛，克利夫兰艺术博物馆藏（1921.1180）。','约1510—1520年',
  '三圣与圣母着色对比亮蓝底，半圆天空现三天使首；釉陶洁白耐久，在幽暗教堂中醒目，由 della Robbia 推广以替代大理石。','donatello,early-renaissance','cma-1921-1180'),
 ('verrocchio-christ-bust','韦罗基奥《基督胸像》','作品','art-renaissance','15世纪','意大利','雕塑','核心',
  'Andrea del Verrocchio 彩绘陶与木胸像，克利夫兰艺术博物馆藏（1921.956）。','约1470—1500年',
  '仿 Orsanmichele《基督与圣多马》青铜像；陶比青铜大理石价廉；躯干由助手、面容与头发由韦罗基奥本人完成。','leonardo,donatello','cma-1921-956'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")