# -*- coding: utf-8 -*-
"""Cycle46：新增单元「伊斯兰艺术」+ 5 个条目（总览 1 + 器物 4）。
来源均为 CMA 藏品记录与策展说明（单机构 → needs_verification）。
"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

# ---------- 1. 来源 ----------
NEWS=[("cma-1944-485","Cleveland Museum of Art — The Wade Cup with Animated Script, Iran (Seljuq), 1200–1221, acc. 1944.485",
   "https://openaccess-api.clevelandart.org/api/artworks/1944.485","2026-11-23 API HTTP 200；黄铜嵌银、整体11.5cm/径16.1cm；说明含 animated script 与黄道十二宫"),
 ("cma-1962-23","Cleveland Museum of Art — Prayer Niche (Mihrab), Iran, Isfahan, Safavid style, acc. 1962.23",
   "https://openaccess-api.clevelandart.org/api/artworks/1962.23","2026-11-23 API HTTP 200；陶瓷马赛克、290.7×245.3cm；说明含朝向麦加的 qibla 墙与 thuluth 铭文"),
 ("cma-1995-17","Cleveland Museum of Art — Large Dish with Artichokes, Iznik, Ottoman, c. 1535–40, acc. 1995.17",
   "https://openaccess-api.clevelandart.org/api/artworks/1995.17","2026-11-23 API HTTP 200；fritware 釉下彩、径36.4cm；说明含意大利织物影响与苏莱曼时期"),
 ("cma-1959-249","Cleveland Museum of Art — Nishapur Figural Bowl, Iran, Samanid, 900s, acc. 1959.249",
   "https://openaccess-api.clevelandart.org/api/artworks/1959.249","2026-11-23 API HTTP 200；土陶釉下装饰、8×35.6cm；说明含萨珊金属器传统与狩猎母题")]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

# ---------- 2. 新增单元 ----------
p=os.path.join(ROOT,"tools","catalog.py"); s=io.open(p,encoding="utf-8").read()
if '"art-islamic"' not in s:
    anchor=' ("work-archives","作品档案"),\n])'
    assert anchor in s, "UNITS tail not found"
    s=s.replace(anchor,' ("art-islamic","伊斯兰艺术（西亚·中亚）"),\n ("work-archives","作品档案"),\n])')
    io.open(p,"w",encoding="utf-8").write(s)
    print("unit art-islamic added")

# ---------- 3. 条目 ----------
T=[('islamic-art','伊斯兰艺术','风格','art-islamic','7—19世纪','西亚·中亚','综合','核心',
    '以伊斯兰信仰与宫廷赞助为背景、跨越西亚中亚北非的视觉传统；本站以四件馆藏器物为具体节点。','7—19世纪（延伸至近代）',
    '书法铭文、阿拉伯式藤蔓与花卉母题、釉下彩与金属嵌饰是其常见语汇；不同地域与王朝各有取向。','wade-cup,mihrab-isfahan,iznik-dish-artichokes,nishapur-figural-bowl','cma-1944-485,cma-1962-23,cma-1995-17,cma-1959-249'),
   ('wade-cup','韦德杯（人物化铭文）','作品','art-islamic','13世纪','西亚·中亚','综合','重要',
    '伊朗塞尔柱时期黄铜嵌银杯，克利夫兰艺术博物馆藏（1944.485）；口沿铭文字母由人、兽、鸟形构成。','1200—1221年',
    '「人物化铭文（animated script）」的代表作；腹部分格内饰黄道十二宫小像。','islamic-art,nishapur-figural-bowl','cma-1944-485'),
   ('mihrab-isfahan','伊斯法罕祈祷龛','作品','art-islamic','16世纪','西亚·中亚','建筑','重要',
    '伊朗伊斯法罕萨法维风格祈祷龛，陶瓷马赛克，克利夫兰艺术博物馆藏（1962.23）。','约16世纪（该馆另记或为20世纪中期）',
    '位于清真寺朝向麦加的墙面上，周围以 thuluth 体铭刻《古兰经·光明章》，铭文为白釉、藤蔓为金与绿松石色。','islamic-art,iznik-dish-artichokes','cma-1962-23'),
   ('iznik-dish-artichokes','伊兹尼克洋蓟纹大盘','作品','art-islamic','16世纪','西亚·中亚','综合','重要',
    '奥斯曼伊兹尼克窑釉下彩大盘，克利夫兰艺术博物馆藏（1995.17）；中心为洋蓟、蔷薇与锯齿状 saz 叶。','约1535—40年',
    '伊兹尼克陶器以花卉母题著称，洋蓟纹可能取自输入奥斯曼宫廷的意大利高档织物。','islamic-art,mihrab-isfahan','cma-1995-17'),
   ('nishapur-figural-bowl','尼沙布尔人物纹碗','作品','art-islamic','10世纪','西亚·中亚','综合','重要',
    '伊朗尼沙布尔萨曼时期土陶釉下装饰碗，克利夫兰艺术博物馆藏（1959.249）。','900年代',
    '四个蓄须人物与兽鸟、带棱角文字环绕；中央骑马猎豹暗指萨珊式的皇家狩猎母题。','islamic-art,wade-cup','cma-1959-249')]
lines=s.split("\n") if False else io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
assert close is not None
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 5")