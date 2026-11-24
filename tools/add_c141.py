# -*- coding: utf-8 -*-
"""Cycle141：希腊陶器 4 条（黑绘狄俄尼索斯双耳瓶、西西弗斯画师钟形杯、雅典双耳瓶与韦奇伍德仿作、红绘斯塔姆诺斯）。查重通过。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o340722","Victoria and Albert Museum — Attic black-figure amphora, late 6th c. BCE, O340722",
  "https://api.vam.ac.uk/v2/object/O340722","2026-11-24 API HTTP 200；红陶黑绘 26.4×16.5cm；说明含狄俄尼索斯/西勒诺斯与迈那得"),
 ("vam-o340727","Victoria and Albert Museum — 'Sisyphos Painter' bell-krater, Apulia, ca. 440 BCE, O340727",
  "https://api.vam.ac.uk/v2/object/O340727","2026-11-24 API HTTP 200；红绘陶钟形杯 31.8×34.3cm；说明含双管吹奏与舞者"),
 ("vam-o77713","Victoria and Albert Museum — Attic amphora (Wedgwood admired), ca. 450–440 BCE, O77713",
  "https://api.vam.ac.uk/v2/object/O77713","2026-11-24 API HTTP 200；黑地橙绘陶 34.29×17.78cm；说明含18世纪英国收藏与韦奇伍德仿制"),
 ("vam-o340729","Victoria and Albert Museum — Attic red-figure stamnos, ca. 450 BCE, O340729",
  "https://api.vam.ac.uk/v2/object/O340729","2026-11-24 API HTTP 200；红绘陶 26.4×28.9cm；说明含狄俄尼索斯与迈那得/西勒诺斯"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('attic-bf-amphora-dionysus','雅典黑绘双耳瓶（狄俄尼索斯）','作品','art-ancient','公元前6世纪','希腊','陶瓷','核心',
  '雅典黑绘双耳瓶，维多利亚与艾伯特博物馆藏（O340722）。','公元前6世纪末',
  '红陶「黑绘」加刻线与白泥绘；一面狄俄尼索斯、一面西勒诺斯，皆伴一迈那得；颈侧三棕叶纹以曲茎相连。（该记录无 summary）','greek-art,kouros-torso','vam-o340722'),
 ('sisyphos-bell-krater','「西西弗斯画师」钟形杯（阿普利亚）','作品','art-ancient','公元前5世纪','希腊','陶瓷','核心',
  '红绘钟形杯，维多利亚与艾伯特博物馆藏（O340727）。','约公元前440年',
  '阿提卡希腊画师「西西弗斯画师」在意大利所作；A：蓄须者吹双管、二青年戴编篮帽起舞；B：三立青年；下有回纹带。（该记录无 summary）','greek-art,attic-bf-amphora-dionysus','vam-o340727'),
 ('attic-amphora-wedgwood','雅典双耳瓶（韦奇伍德仰慕之例）','作品','art-ancient','公元前5世纪','希腊','陶瓷','重要',
  '黑地橙绘雅典双耳瓶，维多利亚与艾伯特博物馆藏（O77713）。','约公元前450—440年',
  '双耳储物瓶，原盛酒或油；黑地橙绘男女像；此类希腊瓶在18世纪晚期英国备受推崇，常陈于私人图书室与专设古物廊；斯塔福德郡陶工韦奇伍德（1730—1795）曾仿制。','greek-art,sisyphos-bell-krater','vam-o77713'),
 ('attic-stamnos-dionysus','雅典红绘斯塔姆诺斯','作品','art-ancient','公元前5世纪','希腊','陶瓷','核心',
  '红绘斯塔姆诺斯，维多利亚与艾伯特博物馆藏（O340729）。','约公元前450年',
  '红绘（黑地留白）斯塔姆诺斯；A：狄俄尼索斯居中、二迈那得左右；B：一迈那得与二西勒诺斯。（该记录无 summary）','attic-bf-amphora-dionysus,greek-art','vam-o340729'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")