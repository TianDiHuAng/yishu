# -*- coding: utf-8 -*-
"""Cycle151：大洋洲 4 条（新爱尔兰马兰根柱 / 拉帕努伊胸饰 Rei Miro / 埃莱马精灵板 / 阿贝拉姆山药面具）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1971-149","Cleveland Museum of Art — Malagan Memorial Festival Pole, New Ireland, 1800s, acc. 1971.149",
  "https://openaccess-api.clevelandart.org/api/artworks/1971.149","2026-11-24 API HTTP 200；彩绘木、海螺盖 高92.7cm；说明含马兰根葬礼筹备、宴飨、交换、雕刻展示后弃置或存放；无制作者"),
 ("cma-1961-406","Cleveland Museum of Art — Gorget (Rei Miro), Rapa Nui (Easter Island), 1800s, acc. 1961.406",
  "https://openaccess-api.clevelandart.org/api/artworks/1961.406","2026-11-24 API HTTP 200；木 30.8×69.8cm；说明含新月形、多为拉帕努伊贵族女性佩戴、尖端抽象形取代人头；来源记录 Howard Beasley、William Mathewson Milliken"),
 ("cma-1971-154","Cleveland Museum of Art — Spirit Board, Elema District, Papuan Gulf, before 1930, acc. 1971.154",
  "https://openaccess-api.clevelandart.org/api/artworks/1971.154","2026-11-24 API HTTP 200；彩绘木 高123.2cm；说明含陈于埃莱马男子屋、每块以所栖丛林精灵命名；说明原文有拼写错误 obejcts"),
 ("cma-1998-84","Cleveland Museum of Art — Yam Mask, Abelam People, Papua New Guinea, 1900s, acc. 1998.84",
  "https://openaccess-api.clevelandart.org/api/artworks/1998.84","2026-11-24 API HTTP 200；颜料、篮编 47.3×44.3×14.7cm；说明含阿贝拉姆男子比赛种巨大山药并以篮编面具装饰展示"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('malagan-memorial-pole','新爱尔兰马兰根纪念节庆柱（19世纪）','作品','art-oceania','19世纪','大洋洲','雕塑','重要',
  '新爱尔兰（美拉尼西亚）彩绘木柱，嵌海螺盖，克利夫兰艺术博物馆藏（1971.149）。','1800年代',
  '重要人物去世后，村民筹备盛大的马兰根（malagan）葬礼：集粮办宴，雇艺术家雕刻精美的雕像与面具，并邀邻近群体参加；仪式持续数日，有演说、舞蹈、音乐、宴飨与物品交换，以展示雕刻彩绘作品为高潮；宾客离去后，雕刻品被弃置，有时被收存。',
  'oceania-art,sepik-ancestral-figure','cma-1971-149'),
 ('rapa-nui-rei-miro','拉帕努伊（复活节岛）胸饰 Rei Miro（19世纪）','作品','art-oceania','19世纪','大洋洲','综合','重要',
  '拉帕努伊（复活节岛，波利尼西亚）木制新月形胸饰，克利夫兰艺术博物馆藏（1961.406）。','1800年代',
  'rei miro 意为「木制项链」，多由拉帕努伊的贵族女性佩戴；形制为优雅的新月形；本件两端尖头的抽象造型，取代了更典型的人头。',
  'oceania-art,maori-hei-tiki','cma-1961-406'),
 ('elema-spirit-board','埃莱马精灵板（1930年前）','作品','art-oceania','20世纪','大洋洲','雕塑','重要',
  '巴布亚新几内亚巴布亚湾埃莱马地区彩绘木板，克利夫兰艺术博物馆藏（1971.154）。','1930年前',
  '与其他神圣器物一样，精灵板陈列在埃莱马男子的房屋里；每一块都以栖于其中的丛林精灵命名。',
  'oceania-art,ambrym-grade-figure','cma-1971-154'),
 ('abelam-yam-mask','阿贝拉姆山药面具（20世纪）','作品','art-oceania','20世纪','大洋洲','综合','重要',
  '巴布亚新几内亚阿贝拉姆人以颜料绘饰的篮编面具，克利夫兰艺术博物馆藏（1998.84）。','1900年代',
  '阿贝拉姆男子比赛种植特别巨大的山药（长度可超过一米），并把它们装饰上篮编面具后展示。',
  'oceania-art,sepik-hook-figure','cma-1998-84'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")
