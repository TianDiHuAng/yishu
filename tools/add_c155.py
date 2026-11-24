# -*- coding: utf-8 -*-
"""Cycle155：巴洛克 4 条（伦勃朗作坊像 / 克劳德·洛兰 / 普桑 / 哈尔斯）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1950-252","Cleveland Museum of Art — Rembrandt van Rijn, A Bearded Man Wearing a Hat (Portrait of a Man), c. 1655–60, acc. 1950.252",
  "https://openaccess-api.clevelandart.org/api/artworks/1950.252","2026-11-24 API HTTP 200；布面油画 84.5×69.2cm；题款Rembrandt 16[?]；说明含斯宾诺莎旧说已重新考虑、可能为作坊制品"),
 ("cma-1962-151","Cleveland Museum of Art — Claude Lorrain, Rest on the Flight into Egypt, early 1640s, acc. 1962.151",
  "https://openaccess-api.clevelandart.org/api/artworks/1962.151","2026-11-24 API HTTP 200；布面油画 208×152.5cm；说明含理想风景、圣家族与天使献果"),
 ("cma-1981-18","Cleveland Museum of Art — Nicolas Poussin, The Holy Family on the Steps, 1648, acc. 1981.18",
  "https://openaccess-api.clevelandart.org/api/artworks/1981.18","2026-11-24 API HTTP 200；布面油画 73.3×105.8cm；说明含苹果、圆规象征与几何构图"),
 ("cma-1999-173","Cleveland Museum of Art — Frans Hals, Portrait of Tieleman Roosterman, 1634, acc. 1999.173",
  "https://openaccess-api.clevelandart.org/api/artworks/1999.173","2026-11-24 API HTTP 200；布面油画 117×87cm；题款ÆTAT SVÆ 36 / AN° 1634；说明含哈勒姆亚麻丝绸商、可见笔触"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('rembrandt-bearded-man-hat','伦勃朗（作坊？）《戴帽的有胡子男子》（约1655—60）','作品','art-baroque','17世纪','荷兰','绘画','重要',
  '题为伦勃朗的男子像布面油画，克利夫兰艺术博物馆藏（1950.252），归属有疑。','约1655—60年',
  '该馆说明：此画曾被视为斯宾诺莎像或犹太学生像，因证据不足这些说法已被重新考虑；披风与帽子画得宽而薄，该馆认为很可能是作坊制品，人物的沉思相对流于表面；右肩上方有题款「Rembrandt 16[?]」。',
  'rembrandt,baroque','cma-1950-252'),
 ('claude-rest-flight-egypt','克劳德·洛兰《逃往埃及途中的休息》（1640年代初）','作品','art-baroque','17世纪','法国','绘画','重要',
  '克劳德·洛兰理想风景布面油画，克利夫兰艺术博物馆藏（1962.151）。','1640年代初',
  '该馆称克劳德是近代早期最有影响的风景画家之一、「理想风景」的大师：以茂盛枝叶与宁静气氛暗示理想化的想象往昔，意在造出比自然本身更美更和谐的景色；前景中圣家族在树荫坡上休息，跪着的天使向圣婴献果；此类风景受欧洲富有藏家欢迎，是他们逃离都市喧嚣的宁静去处。',
  'baroque,rococo','cma-1962-151'),
 ('poussin-holy-family-steps','普桑《台阶上的圣家族》（1648）','作品','art-baroque','17世纪','法国','绘画','重要',
  '普桑布面油画，克利夫兰艺术博物馆藏（1981.18）。','1648年',
  '该馆说明：看似简单的构图是对圣家族在人类救赎中作用的复杂沉思；中央玛利亚向世人呈现圣婴，左侧伊丽莎白前倾预示其死，圣若翰献苹果象征人类堕落，右侧约瑟夫持圆规，既是木匠职业标志也象征天父；画家有条不紊地经营构图，以清晰原色、简洁形体与几何组织表达圣家族的核心地位。',
  'baroque,lippi-holy-family-tondo','cma-1981-18'),
 ('hals-tieleman-roosterman','哈尔斯《蒂勒曼·罗斯特曼像》（1634）','作品','art-baroque','17世纪','荷兰','绘画','重要',
  '哈尔斯布面肖像，克利夫兰艺术博物馆藏（1999.173）。','1634年',
  '该馆说明：罗斯特曼是哈勒姆极富有的亚麻与丝绸商，画像时36岁；与许多荷兰同行不同，哈尔斯偏好强烈可见的笔触以传达坐像者的生气；其姿态自信，服饰端庄而奢华，袖饰镶边与纽扣，腰间缠丝带花结，黑衣与宽亚麻领、花边袖口相映；右上方题「ÆTAT SVÆ 36 / AN° 1634」。',
  'baroque,rembrandt','cma-1999-173'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")
