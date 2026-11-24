# -*- coding: utf-8 -*-
"""Cycle144：浮世绘 4 条（歌麿摺物、国贞剧场后台、广重隅田雪、北斋富岳三十六景）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o71806","Victoria and Albert Museum — Utamaro, Rolling up a Blind for Plum Blossom Viewing, late 1790s, O71806",
  "https://api.vam.ac.uk/v2/object/O71806","2026-11-24 API HTTP 200；木版彩印摺物；说明含琴后少女表情与江户游乐"),
 ("vam-o71692","Victoria and Albert Museum — Kunisada, Dressing Room Scenes at Dotonbori Theatres, early 1820s, O71692",
  "https://api.vam.ac.uk/v2/object/O71692","2026-11-24 API HTTP 200；木版 35.7×71.8cm；说明含大阪剧场与1821—22江户演员"),
 ("vam-o76529","Victoria and Albert Museum — Hiroshige, View of the Sumida River in the Snow, 1843–47, O76529",
  "https://api.vam.ac.uk/v2/object/O76529","2026-11-24 API HTTP 200；团扇绘 aiban 220×290mm；说明含atozuri后印与向岛渡口"),
 ("vam-o73124","Victoria and Albert Museum — Hokusai, Thirty-Six Views of Mount Fuji (Great Wave), ca. 1831, O73124",
  "https://api.vam.ac.uk/v2/object/O73124","2026-11-24 API HTTP 200；横大判蓝摺绘 24.8×35.8cm；说明含首套纯大判风景系列"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('utamaro-plum-blind','歌麿《卷帘赏梅》摺物','作品','art-asia','18世纪','东亚','版画','核心',
  '喜多川歌麿摺物版画，维多利亚与艾伯特博物馆藏（O71806）。','1790年代末',
  '摺物（私人订制彩印）；歌麿（1750—1806）早年佳作，线条精细写优雅女子；画面或本于某故事，却呈现江户两种游乐：赏梅等；尤重弹罢十三弦琴少女之神情。（记录无尺寸）','hiroshige-satta-sea,hokusai-36views','vam-o71806'),
 ('kunisada-dressing-room','国贞《道顿堀剧场后台》','作品','art-asia','19世纪','东亚','版画','核心',
  '歌川国贞三联画右幅，维多利亚与艾伯特博物馆藏（O71692）。','1820年代初',
  '绘大阪道顿堀角座与中座歌舞伎剧场内景；1821—22江户演员（皆男）赴大阪演出，国贞亲赴大阪作此售众；大阪剧场为较简朴两层建筑，异于江户。','hiroshige-sumida-snow,hiroshige-satta-sea','vam-o71692'),
 ('hiroshige-sumida-snow','广重《隅田川雪景》（团扇绘）','作品','art-asia','19世纪','东亚','版画','核心',
  '歌川广重团扇绘（uchiwa-e），维多利亚与艾伯特博物馆藏（O76529）。','1843—1847年',
  'aiban 团扇绘，atozuri 后印；色与套准仍佳；自北江户桥场渡口向岛一侧上望，对岸屋舍即标识；署名广重画。','hiroshige-satta-sea,kunisada-dressing-room','vam-o76529'),
 ('hokusai-36views','北斋《富岳三十六景》（巨浪）','作品','art-asia','19世纪','东亚','版画','核心',
  '葛饰北斋《富岳三十六景》之一，维多利亚与艾伯特博物馆藏（O73124）。','约1831年',
  '横大判「蓝摺绘（aizuri-e）」：巨浪覆舟、远景富士；北斋（1760—1849）为日本最著名画师；此系列为**首个纯以大判风景版画构成**的系列。','hiroshige-satta-sea,hokusai-red-fuji','vam-o73124'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")