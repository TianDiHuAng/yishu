# -*- coding: utf-8 -*-
"""Cycle45：①新增《相模中原》（北斋，CMA 1940.997 + V&A O422861 双机构）；
②为已有《唐崎夜雨》补 V&A 第二份印本记录（O407359）作第三来源。
③记录「仙波堰」未建原因（CMA 无策展说明，内容不足）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,os.path.join(ROOT,"tools"))
from render_l2_svg import render_svg
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
NEWS=[("cma-1940-997","Cleveland Museum of Art — Hokusai, Nakahara in Sagami Province, ca. 1835, acc. 1940.997",
   "https://openaccess-api.clevelandart.org/api/artworks/1940.997","2026-11-23 API HTTP 200；sheet 25.1×37.8cm；说明含中原田野与东海道、神祠茅顶与石像"),
 ("vam-o422861","Victoria and Albert Museum — Nakahara in Sagami Province (Sōshū Nakahara), O422861",
   "https://collections.vam.ac.uk/item/O422861/","2026-11-23 V&A API HTTP 200；题名含系列《富岳三十六景》，38.5×25.5cm"),
 ("vam-o407359","Victoria and Albert Museum — Night Rain at Karasaki (Karasaki yau), O407359（同一构图另一印本）",
   "https://collections.vam.ac.uk/item/O407359/","2026-11-23 V&A API HTTP 200；与 O423295 同题同名，属另一份印本")]
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":("Cleveland Museum of Art（开放数据 API）" if sid.startswith("cma") else "Victoria and Albert Museum（V&A API v2）"),
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))

# ① 新条目
T=[('hokusai-nakahara-sagami','《相模中原》（北斋）','作品','art-asia','19世纪','日本','绘画','重要',
    '葛饰北斋《富岳三十六景》之一，自中原田野远望富士；CMA（1940.997）与 V&A（O422861）各藏印本。','约1835年',
    '前景为神祠茅草屋顶与溪畔石像，中景为中原田野，富士在远处；该地紧邻东海道主线。','ukiyo-e,japanese-art,hokusai-red-fuji','cma-1940-997,vam-o422861')]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=None
for i in range(len(lines)-1,-1,-1):
    if lines[i].strip()=="]": close=i; break
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 1")

svg=render_svg({"nodes":[{"label":"东海道","sub":"主线","kind":"muted"},{"label":"中原田野","sub":"中景","kind":"accent"},
  {"label":"富士","sub":"远景","kind":"muted"},{"label":"CMA / V&A","sub":"各藏印本","kind":"muted"}],
 "arrows":[{"from":0,"to":1},{"from":1,"to":2},{"from":2,"to":3}],"caption":"《相模中原》：田野、东海道与富士"}, "hokusai-nakahara-sagami")
over={"id":"hokusai-nakahara-sagami","level":"L2","svg":svg,"sources":["cma-1940-997","vam-o422861"],
 "sections":{
  "时代背景":"本幅属葛饰北斋《富岳三十六景》系列。该馆说明指出，中原一带的田野紧邻东海道——即沿东海岸连接江户与京都的主干道；画面正是自这片田野远望富士。",
  "风格特征":"该馆说明以三层交代画面：前景是神祠的茅草屋顶与溪畔的石像，中景是中原田野，富士山在远处。这一由近及远的分层，使「远望」成为构图的核心动作，而非把山当作孤立的主像。",
  "代表人物与作品":"作者葛饰北斋（1760—1849）。相关条目见浮世绘、日本艺术与《凯风快晴》。英国维多利亚与艾尔伯特博物馆藏有同图印本，题名《相模中原（Sōshū Nakahara）》，属《富岳三十六景》，38.5 × 25.5厘米。",
  "技法或形式分析":"克利夫兰记录本幅尺寸为 sheet 25.1 × 37.8厘米；V&A 记录38.5 × 25.5厘米（宽×高著录方式不同，横向尺寸略大），二者为不同印本。两馆记录均未提供版木或摺数信息。",
  "与前后风格的关系和争论":"该系列以同一座山在不同地点、不同天气下的观看为主题；本幅把山放在田野尽处，与《凯风快晴》把山推到画面中心的做法形成对照，可见系列内部的构图策略变化。",
  "一图":"示意图以东海道、中原田野与富士的距离关系标示本幅的构图层次。",
  "待核实":"（1）V&A 记录未给年代，「约1835年」仅据 CMA 一家；（2）两馆尺寸著录方向不同（25.1×37.8 对 38.5×25.5），差异原因待目验；（3）作者生卒1760—1849取自 CMA 创作者记录；（4）「紧邻东海道」的地理细节该馆仅一句带过，未展开。",
 }}
json.dump(over,open(os.path.join(LD,"hokusai-nakahara-sagami.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)

# ② 给《唐崎夜雨》补第三来源
kp=os.path.join(LD,"hiroshige-karasaki-night-rain.json"); ko=json.load(open(kp,encoding="utf-8"))
if "vam-o407359" not in ko["sources"]:
    ko["sources"].append("vam-o407359")
    ko["sections"]["待核实"]=ko["sections"]["待核实"].replace(
        "（3）两馆印本差异未判定。","（3）两馆印本差异未判定；V&A 另藏同题同构图的第二份印本（O407359），三份印本的先后与印次差异未判定。")
    json.dump(ko,open(kp,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print("karasaki: third source added")
print("done")