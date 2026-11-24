# -*- coding: utf-8 -*-
"""Cycle116：乐器 4 条（乌尔比诺 Citrin、Tielke 吉他、巴洛克双簧管、鲍伊 Koto）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("vam-o58649","Victoria and Albert Museum — Urbino Cittern, 1582, O58649",
  "https://api.vam.ac.uk/v2/object/O58649","2026-11-24 API HTTP 200；雕刻镶边松木枫木 长95cm；说明含金属弦拨奏与Il primo libro"),
 ("vam-o58931","Victoria and Albert Museum — Joachim Tielke guitar, Hamburg, 1693, O58931",
  "https://api.vam.ac.uk/v2/object/O58931","2026-11-24 API HTTP 200；玳瑁象牙锡镶木 长102cm；说明含丘比特与古典场景细木镶嵌"),
 ("vam-o58639","Victoria and Albert Museum — Baroque oboe, Holland, ca. 1700, O58639",
  "https://api.vam.ac.uk/v2/object/O58639","2026-11-24 API HTTP 200；黄杨银键象牙箍 577mm；说明含奏乐场景雕与hautbois"),
 ("vam-o1784498","Victoria and Albert Museum — Koto used by David Bowie on 'Heroes', ca. 1977, O1784498",
  "https://api.vam.ac.uk/v2/object/O1784498","2026-11-24 API HTTP 200；模塑塑料 13弦 含原盒与说明书；说明含 Moss Garden"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Victoria and Albert Museum（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('urbino-cittern','乌尔比诺 Citrin（1582）','作品','music-instruments','16世纪','欧洲','乐器','核心',
  '乌尔比诺 Citrin，维多利亚与艾伯特博物馆藏（O58649）。','1582年',
  '金属弦金属品、拨片扫弦，旋律多在上弦；枫木微拱背、松木微拱面，末端有「梳」托弦；1574年 Vitale 出版后流行意/中欧。','baffo-harpsichord,maler-lute','vam-o58649'),
 ('tielke-guitar','蒂尔克吉他（汉堡，1693）','作品','music-instruments','17世纪','欧洲','乐器','核心',
  'Joachim Tielke 制吉他，维多利亚与艾伯特博物馆藏（O58931）。','1693年',
  '拱背五宽肋，玳瑁/象牙/锡细木镶嵌花卉、丘比特与带铭古典场景；面板黑檀象牙锡梯纹镶边并花卉镶嵌。','stradivari-violin,baffo-harpsichord','vam-o58931'),
 ('baroque-oboe-holland','荷兰巴洛克双簧管（约1700）','作品','music-instruments','17—18世纪','欧洲','乐器','重要',
  '荷兰黄杨双簧管，维多利亚与艾伯特博物馆藏（O58639）。','约1700年',
  '三节黄杨、象牙箍银键；节上低浮雕月桂/莨苕；喇叭口雕两奏乐场景（小提琴起舞与四乐师）；名称源于法语hautbois，由中世纪肖姆管演变。','northumberland-bagpipe,baffo-harpsichord','vam-o58639'),
 ('bowie-koto-heroes','鲍伊《Heroes》用古筝（koto）','作品','music-instruments','20世纪','东亚','乐器','核心',
  '大卫·鲍伊《Heroes》专辑「Moss Garden」所用玩具古筝，维多利亚与艾伯特博物馆藏（O1784498）。','约1977年',
  '模塑塑料13弦玩具筝，附原纸盒与说明书；棕塑木纹面板、两端织物；为流行音乐借用东方乐器的物证。','guzheng,japanese-art','vam-o1784498'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")