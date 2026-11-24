# -*- coding: utf-8 -*-
"""Cycle163：乐器 5 条（提奥宾琴 / 月琴 / 乌德琴 / 坦布尔 / 手摇琴）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1918-368","Cleveland Museum of Art — Lute or Tiorbino, c. 1620, acc. 1918.368",
  "https://openaccess-api.clevelandart.org/api/artworks/1918.368","2026-11-24 API HTTP 200；木 全长100.7×27.7cm；馆方称意大利、约17世纪中叶制作、后经修补改动；说明含提奥宾琴比提奥波小、高八度"),
 ("cma-1918-382","Cleveland Museum of Art — Moon Lute (Yueqin), 1800s, acc. 1918.382",
  "https://openaccess-api.clevelandart.org/api/artworks/1918.382","2026-11-24 API HTTP 200；紫檀、梧桐木与羊肠弦 58.4×35.6cm；中国清代；说明含月琴名称由来与演奏法"),
 ("cma-1918-350","Cleveland Museum of Art — Oud, late 1800s-early 1900s, acc. 1918.350",
  "https://openaccess-api.clevelandart.org/api/artworks/1918.350","2026-11-24 API HTTP 200；木、羊肠弦与金属 81.3×33.7cm；西亚；题款 Work of Alexander, going to New York 1892"),
 ("cma-1918-347","Cleveland Museum of Art — Tanbur, late 1800s, acc. 1918.347",
  "https://openaccess-api.clevelandart.org/api/artworks/1918.347","2026-11-24 API HTTP 200；木、骨、珍珠母与金属丝 58.4×10.5cm；叙利亚或土耳其、奥斯曼时期；说明含三种文化特征与烧痕装饰"),
 ("cma-2020-422","Cleveland Museum of Art — Vielle a Roue (Hurdy-Gurdy), 1865-70, acc. 2020.422",
  "https://openaccess-api.clevelandart.org/api/artworks/2020.422","2026-11-24 API HTTP 200；木与珍珠母镶嵌；法国；署名雅克·德康特（1808—1884）；说明含摇柄轮擦弦与键盘变音"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('cma-tiorbino','提奥宾琴（意大利，约17世纪中叶）','作品','music-instruments','17世纪','欧洲','乐器','重要',
  '长颈鲁特琴类的小型提奥宾琴，克利夫兰艺术博物馆藏（1918.368）。','约17世纪中叶',
  '该馆称其为意大利制、约17世纪中叶，后经修补改动；长颈、形似提奥波而小得多、音高高八度；该馆称是现存最小的巴洛克提奥宾琴之一。',
  'maler-lute,baroque-music','cma-1918-368'),
 ('cma-yueqin','月琴（中国，清代）','作品','music-instruments','19世纪','东亚','乐器','重要',
  '清代月琴，克利夫兰艺术博物馆藏（1918.382）。','1800年代',
  '紫檀、梧桐木与羊肠弦；尺寸58.4×35.6厘米；因形似满月得名；用于民间乐队与京剧、地方戏并为歌唱伴奏；以指甲或拨片弹奏。',
  'pipa-instrument,opera','cma-1918-382'),
 ('cma-oud','乌德琴（西亚，19世纪末—20世纪初）','作品','music-instruments','19世纪','西亚·中亚','乐器','重要',
  '西亚乌德琴，克利夫兰艺术博物馆藏（1918.350）。','1800年代末—1900年代初',
  '木、羊肠弦与金属；尺寸81.3×33.7厘米；该馆称乌德属鲁特琴家族，梨形琴身、无品指板、琴头与琴颈成45至90度角；馆方记录有题款。',
  'maler-lute,ottoman-nay-flute','cma-1918-350'),
 ('cma-tanbur','坦布尔（叙利亚或土耳其，19世纪末）','作品','music-instruments','19世纪','西亚·中亚','乐器','重要',
  '奥斯曼时期长颈鲁特琴坦布尔，克利夫兰艺术博物馆藏（1918.347）。','1800年代末',
  '木、骨、珍珠母与金属丝；尺寸58.4×10.5厘米；采集于奥斯曼叙利亚；该馆称兼具叙利亚、土耳其与伊朗特征；梨形琴身饰烧痕与珍珠母嵌点。',
  'cma-oud,ottoman-nay-flute','cma-1918-347'),
 ('cma-hurdy-gurdy','手摇琴（法国，雅克·德康特，1865—70）','作品','music-instruments','19世纪','欧洲','乐器','重要',
  '法国手摇琴 vielle à roue，克利夫兰艺术博物馆藏（2020.422）。','1865—70年',
  '署名雅克·德康特（1808—1884）；木与珍珠母镶嵌；六弦，摇柄转轮擦弦，作用如琴弓；旋律由键盘推动小楔改变音高。',
  'maler-lute,stradivari-violin','cma-2020-422'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
txt="\n".join(lines)
T=[t for t in T if "'%s'"%t[0] not in txt]
if T:
    close=max(i for i,l in enumerate(lines) if l.strip()=="]")
    lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
    io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
