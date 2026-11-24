# -*- coding: utf-8 -*-
"""Cycle120：V&A 4 条（Van Diemen 漆盒、广州修伞匠外销画、屈塔希亚砖板、Harp-lute-guitar）。查重已过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o18899","Victoria and Albert Museum — The Van Diemen Box, Japan (Kyoto), 1636–1639, O18899",
  "https://api.vam.ac.uk/v2/object/O18899","2026-11-24 API HTTP 200；黑漆金银莳绘 48.3×36.7×16cm；说明含京都制作/出岛/范迪门妻铭"),
 ("vam-o85590","Victoria and Albert Museum — An Umbrella Mender, Guangzhou, ca. 1790, O85590",
  "https://api.vam.ac.uk/v2/object/O85590","2026-11-24 API HTTP 200；纸本水墨设色 36×46cm；说明含广州百业图一百幅之一"),
 ("vam-o103140","Victoria and Albert Museum — Kütahya tile panel, ca. 1660, O103140",
  "https://api.vam.ac.uk/v2/object/O103140","2026-11-24 API HTTP 200；熔块胎釉下彩 80块 192×256.5cm 重135kg；说明含壁龛花瓶一排"),
 ("vam-o58979","Victoria and Albert Museum — Harp-lute-guitar by Mr Harley, London, ca. 1810, O58979",
  "https://api.vam.ac.uk/v2/object/O58979","2026-11-24 API HTTP 200；金饰彩绘木弦颈乌木指板 长92cm；说明含威尔士亲王羽毛玫瑰"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('vandiem-lacquer-box','范迪门漆盒（外销莳绘）','作品','art-asia','17世纪','东亚','综合','核心',
  '日本京都制黑漆金银莳绘文书盒，维多利亚与艾伯特博物馆藏（O18899）。','1636—1639年',
  '盖面绘京都御所场景（天皇居高台、朝臣晋见、宫门与牛车）；盒盖内侧铭 Maria van Diemen（荷属东印度总督之妻）；京都特制经出岛由荷兰商船外销。','japanese-art,tami-bowl','vam-o18899'),
 ('canton-umbrella-mender','广州外销画《修伞匠》','作品','art-asia','18世纪','东亚','绘画','重要',
  '广州纸本水墨设色行商图，维多利亚与艾伯特博物馆藏（O85590）。','约1790年',
  '百幅「中国工匠与行业」组画之一；中景黑衣匠人坐于三脚架撑开的伞旁；为欧人了解中国而作。','china-trade-painting,japanese-art','vam-o85590'),
 ('kutahya-tile-panel','屈塔希亚釉砖板','作品','art-islamic','17世纪','西亚·中亚','陶瓷','核心',
  '土耳其屈塔希亚熔块胎釉砖板（80块），维多利亚与艾伯特博物馆藏（O103140）。','约1660年',
  '一排壁龛内各置花瓶；对称布局填满可用空间；1550s起伊兹尼克开创釉下彩墙砖板，为宫殿与清真寺墙面流行装饰。','iznik-tile-panel-edirne,islamic-art','vam-o103140'),
 ('harp-lute-guitar-va','哈普鲁特吉他（Harp-lute-guitar）','作品','music-instruments','19世纪初','欧洲','乐器','重要',
  '伦敦 Mr Harley 制哈普鲁特吉他，维多利亚与艾伯特博物馆藏（O58979）。','约1810年',
  '三器混成体；弦轴箱近鲁特式、低音加不按弦空弦；玫瑰孔为「威尔士亲王羽毛」纹或指夏洛特公主；Harley 于 Wych Street 仅以姓氏行商。','maler-lute,baffo-harpsichord','vam-o58979'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")