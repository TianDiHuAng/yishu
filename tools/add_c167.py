# -*- coding: utf-8 -*-
"""Cycle167：中国音乐相关藏品 5 条（听琴/弹琴画作、唐代竖琴俑、唐镜）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1983-85","Cleveland Museum of Art — Liu Songnian, Listening to the Qin (Zither), 1150-after 1225, acc. 1983.85",
  "https://openaccess-api.clevelandart.org/api/artworks/1983.85","2026-11-24 API HTTP 200；绢本墨与淡彩册页 23.8×24.6cm；南宋；题款劉松年；说明含伯牙与钟子期故事"),
 ("cma-1969-60","Cleveland Museum of Art — Wen Zhengming, Playing the Qin in a Secluded Valley, 1548, acc. 1969.60",
  "https://openaccess-api.clevelandart.org/api/artworks/1969.60","2026-11-24 API HTTP 200；纸本立轴墨与淡彩 132×50.5cm；明；题诗与款嘉靖戊申(1548)；说明含学者提出更近似陆治画法"),
 ("cma-1977-199","Cleveland Museum of Art — Tang Yin, Listening to the Qin, late 1400s-early 1500s, acc. 1977.199",
  "https://openaccess-api.clevelandart.org/api/artworks/1977.199","2026-11-24 API HTTP 200；绢本立轴墨与淡彩 画心35.8×29.1cm；明；说明含嵇康与《广陵散》传说"),
 ("cma-1931-450","Cleveland Museum of Art — Harpist, mid-700s, acc. 1931.450",
  "https://openaccess-api.clevelandart.org/api/artworks/1931.450","2026-11-24 API HTTP 200；釉陶 通高32.1cm；中国北方唐代；说明含唐墓俑与女乐师坐于圆台奏竖琴"),
 ("cma-1995-369","Cleveland Museum of Art — Lobed Mirror with a Tortoise Knob, Musician, and Phoenix, late 700s, acc. 1995.369",
  "https://openaccess-api.clevelandart.org/api/artworks/1995.369","2026-11-24 API HTTP 200；青铜 直径21.6cm；唐；有铭文；说明称图案含义不完全清楚、可能指侯晋与求仙"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('cma-liu-songnian-qin','刘松年《听琴图》（南宋册页）','作品','music-china','南宋','中国','音乐体裁','重要',
  '南宋刘松年的听琴册页，克利夫兰艺术博物馆藏（1983.85）。','约12—13世纪（1150—1225后）',
  '绢本墨与淡彩册页，画心23.8×24.6厘米，题款「劉松年」；该馆称画意追忆伯牙为知音钟子期弹七弦琴的故事；松荫清凉、香炉烟起与琴声相互映衬；方寸册页的形式以音乐为触动弹者与听者心灵的关键。',
  'guqin-instrument,song-painting','cma-1983-85'),
 ('cma-wen-zhengming-qin','文徵明《幽壑鸣琴》（1548）','作品','music-china','明代','中国','音乐体裁','重要',
  '文徵明1548年题诗的弹琴立轴，克利夫兰艺术博物馆藏（1969.60）。','1548年',
  '纸本立轴墨与淡彩，尺寸132×50.5厘米；题诗称以朱弦一曲小答松风太古之音，款署嘉靖戊申；该馆说明称此画有不同版本，学者认为岩石的扎实画法与立体的山势更像文徵明学生陆治（1496—1576）的特点。',
  'guqin-instrument,wen-zhengming-silk-poem,ming-painting','cma-1969-60'),
 ('cma-tang-yin-qin','唐寅《听琴图》（明代立轴）','作品','music-china','明代','中国','音乐体裁','重要',
  '明代唐寅的听琴立轴，克利夫兰艺术博物馆藏（1977.199）。','15世纪末—16世纪初',
  '绢本立轴墨与淡彩，画心35.8×29.1厘米；该馆称画意暗指嵇康（223—262）的一则传说：嵇康是三世纪一群特立独行的知识分子中的古琴家，所作《广陵散》幽怨得能唤来鬼魂；画中描绘一个扮成人形的鬼魂被另一鬼魂扶助从地下出来，其他鬼魂被月下茅屋中的琴师吸引。',
  'guqin-instrument,ming-painting','cma-1977-199'),
 ('cma-tang-harpist','唐代竖琴乐俑（8世纪中叶）','作品','music-china','唐代','中国','音乐体裁','重要',
  '唐代墓俑中的女乐师，克利夫兰艺术博物馆藏（1931.450）。','约8世纪中叶',
  '釉陶，通高32.1厘米；该馆称唐墓所置俑生动展现日常生活；这位女乐师坐在圆台上，竖琴（harp）斜靠在右大腿上演奏，发髻盘在额前，长而高腰的袍子垂到翘头鞋尖。',
  'china-music-history,tang-painting','cma-1931-450'),
 ('cma-tang-qin-mirror','唐代龟钮菱花镜：乐师与凤凰（8世纪晚期）','作品','music-china','唐代','中国','音乐体裁','重要',
  '唐代青铜镜，饰乐师与凤凰，克利夫兰艺术博物馆藏（1995.369）。','约8世纪晚期',
  '青铜，直径21.6厘米，有铭文；该馆称铭文说这是一对镜中的一面，以南方之金制成并置于玉匣，或暗示婚礼之赠；图案含义并不完全清楚，可能指道教仙人侯晋，他弹琴、懂鸟语、能依水中倒影预言；凤凰、水池与琴或都与求仙有关。',
  'guqin-instrument,china-music-history','cma-1995-369'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
txt="\n".join(lines)
T=[t for t in T if "'%s'"%t[0] not in txt]
if T:
    close=max(i for i,l in enumerate(lines) if l.strip()=="]")
    lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
    io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
