# -*- coding: utf-8 -*-
"""Cycle164：中世纪/文艺复兴圣咏手稿 6 条。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1952-88","Cleveland Museum of Art — Title Page of Abbot Berno's Tonarius, c. 1030, acc. 1952.88",
  "https://openaccess-api.clevelandart.org/api/artworks/1952.88","2026-11-24 API HTTP 200；羊皮纸墨、蛋彩与金 21.5×15.3cm；德国赖兴瑙修道院11世纪；说明含调式集为规范礼仪圣咏的音乐手册、献给科隆大主教皮尔格林"),
 ("cma-1933-446","Cleveland Museum of Art — Bifolium Excised from a Carolingian Gradual, c. 830-60, acc. 1933.446",
  "https://openaccess-api.clevelandart.org/api/artworks/1933.446","2026-11-24 API HTTP 200；紫色羊皮纸金银墨 29×10cm；德国或法国东北部9世纪；说明含歌咏集、强调字母、其他叶存柏林与特里尔"),
 ("cma-1950-391","Cleveland Museum of Art — Bifolio from a Gradual, c. 1300, acc. 1950.391",
  "https://openaccess-api.clevelandart.org/api/artworks/1950.391","2026-11-24 API HTTP 200；羊皮纸墨、蛋彩与金 55.7×37.9cm；意大利锡耶纳(?)；说明含诸圣节弥撒入祭咏 Gaudeamus omnes in Domino"),
 ("cma-1985-60","Cleveland Museum of Art — Bifolium from an Antiphonary, c. 1320-40, acc. 1985.60",
  "https://openaccess-api.clevelandart.org/api/artworks/1985.60","2026-11-24 API HTTP 200；羊皮纸 51×37.7cm；意大利博洛尼亚；署名圣多米尼克首席彩饰师；说明含多明我会修道院用书"),
 ("cma-1930-661","Cleveland Museum of Art — Antiphonary, c. 1470-80, acc. 1930.661",
  "https://openaccess-api.clevelandart.org/api/artworks/1930.661","2026-11-24 API HTTP 200；羊皮纸 抄本55.9×43.2×10.2cm；意大利锡耶纳；署名杰罗拉莫·达·克雷莫纳；说明称图饰出自其追随者；含复活节首晨祷应答"),
 ("cma-1921-140","Cleveland Museum of Art — Gradual, c. 1520, acc. 1921.140",
  "https://openaccess-api.clevelandart.org/api/artworks/1921.140","2026-11-24 API HTTP 200；羊皮纸与木封面 抄本51.1×35.6×8.9cm；意大利维罗纳；署名杰罗拉莫·代·利布里(1474—1555)；说明称彩饰出自其圈子里的彩饰师"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('cma-berno-tonarius','贝尔诺《调式集》献词页（赖兴瑙，约1030）','作品','music-medieval','中世纪','欧洲','手稿','重要',
  '赖兴瑙院长贝尔诺《调式集》的献词页，克利夫兰艺术博物馆藏（1952.88）。','约1030年',
  '羊皮纸墨、蛋彩与金，尺寸21.5×15.3厘米；该馆称调式集是用来规范礼仪圣咏的音乐手册，由赖兴瑙院长贝尔诺（1008—1048在任）所撰，献给科隆大主教皮尔格林（1021—1036在任），其名字见于本叶底部。',
  'gregorian-chant,medieval-music','cma-1952-88'),
 ('cma-carolingian-gradual','加洛林歌咏集对开页（约830—60）','作品','music-medieval','中世纪','欧洲','手稿','重要',
  '加洛林时期紫色羊皮纸歌咏集对开页，克利夫兰艺术博物馆藏（1933.446）。','约830—60年',
  '紫色羊皮纸金银墨，尺寸29×10厘米；该馆称这是弥撒中所唱圣咏的歌咏集（cantatorium或gradual），同书其他叶存于柏林与特里尔；无装饰首字母而用推入页边的强调字母。',
  'gregorian-chant,medieval-music','cma-1933-446'),
 ('cma-gradual-gaudeamus','格拉杜尔对开页：诸圣节入祭咏（约1300）','作品','music-medieval','中世纪','欧洲','手稿','重要',
  '约1300年的格拉杜尔对开页，含诸圣节弥撒入祭咏，克利夫兰艺术博物馆藏（1950.391）。','约1300年',
  '羊皮纸墨、蛋彩与金，尺寸55.7×37.9厘米；产地该馆写意大利锡耶纳（带问号）；大号装饰首字母G引出 Gaudeamus omnes in Domino，是11月1日诸圣节弥撒的入祭咏；反面为乐谱与文字。',
  'gregorian-chant,music-notation','cma-1950-391'),
 ('cma-bologna-antiphonary','博洛尼亚安提芳那对开页：圣多米尼克布道（约1320—40）','作品','music-medieval','中世纪','欧洲','手稿','重要',
  '博洛尼亚彩饰师所作安提芳那对开页，克利夫兰艺术博物馆藏（1985.60）。','约1320—40年',
  '羊皮纸墨、蛋彩与金，尺寸51×37.7厘米；署名圣多米尼克首席彩饰师；该馆称首字母M中的圣多米尼克像表明它曾属多明我会修道院的抄本；该工坊专为艾米利亚地区的富裕宗教机构制作大型抄本。',
  'gregorian-chant,medieval-music','cma-1985-60'),
 ('cma-siena-antiphonary','锡耶纳《安提芳那》（约1470—80）','作品','music-renaissance','15—16世纪','欧洲','手稿','重要',
  '锡耶纳《安提芳那》抄本，署名杰罗拉莫·达·克雷莫纳，克利夫兰艺术博物馆藏（1930.661）。','约1470—80年',
  '羊皮纸墨、蛋彩与金，抄本55.9×43.2×10.2厘米；该馆称首字母A中的复活基督出自杰罗拉莫的直接追随者之手，使用大师的设计；安提芳那通常分多卷，用于教士团体咏唱日课；所示圣咏为复活节第一晨祷应答。',
  'renaissance-music,gregorian-chant','cma-1930-661'),
 ('cma-verona-gradual','维罗纳《格拉杜尔》（约1520）','作品','music-renaissance','15—16世纪','欧洲','手稿','重要',
  '维罗纳圈子的格拉杜尔抄本，署名杰罗拉莫·代·利布里，克利夫兰艺术博物馆藏（1921.140）。','约1520年',
  '羊皮纸墨、蛋彩与金，木封面，抄本51.1×35.6×8.9厘米；该馆称格拉杜尔是弥撒所用的主要合唱用书，常分多卷；本卷似为一套中仅存的一册；彩饰出自杰罗拉莫·代·利布里圈子里的彩饰师。',
  'renaissance-music,gregorian-chant','cma-1921-140'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
txt="\n".join(lines)
T=[t for t in T if "'%s'"%t[0] not in txt]
if T:
    close=max(i for i,l in enumerate(lines) if l.strip()=="]")
    lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
    io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
