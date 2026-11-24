# -*- coding: utf-8 -*-
"""Cycle162：巴洛克 3 条（鲁本斯 / 委拉斯开兹 / 哈尔斯）。来源 CMA。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1947-207","Cleveland Museum of Art — Peter Paul Rubens, Portrait of Isabella Brant, c. 1620-25, acc. 1947.207",
  "https://openaccess-api.clevelandart.org/api/artworks/1947.207","2026-11-24 API HTTP 200；木板油画 画心53×46cm；说明含伊莎贝拉·勃兰特为鲁本斯第一任妻子、暖色调与笔触"),
 ("cma-1965-15","Cleveland Museum of Art — Diego Velazquez, Portrait of the Jester Calabazas, c. 1631-32, acc. 1965.15",
  "https://openaccess-api.clevelandart.org/api/artworks/1965.15","2026-11-24 API HTTP 200；布面油画 画心175×106cm；说明含西班牙宫廷弄臣卡拉巴萨斯与全身宫廷肖像格式"),
 ("cma-1948-137","Cleveland Museum of Art — Frans Hals, Portrait of a Woman, probably Aeltje Dircksdr. Pater, 1638, acc. 1948.137",
  "https://openaccess-api.clevelandart.org/api/artworks/1948.137","2026-11-24 API HTTP 200；布面油画 画心66.5×52.3cm；题款AETAT SUAE 41 / ANNO 1638；说明含湿中湿技法与暂定的画中人身份"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('rubens-isabella-brant','鲁本斯《伊莎贝拉·勃兰特肖像》（约1620—25）','作品','art-baroque','17世纪','佛兰德斯','油画','重要',
  '鲁本斯为第一任妻子所作的木板肖像，克利夫兰艺术博物馆藏（1947.207）。','约1620—25年',
  '该馆说明：伊莎贝拉·勃兰特是鲁本斯的第一任妻子，他以多种方式画过她很多次，她在35岁时去世；这幅亲密的肖像至少作于她去世前五年，以温暖的色调、丰润的笔触与生动的表情，显示画家与模特之间的亲近关系；她也是该馆另一件鲁本斯作品中一位宁芙的模特。',
  'baroque,rubens','cma-1947-207'),
 ('velazquez-jester-calabazas','委拉斯开兹《弄臣卡拉巴萨斯肖像》（约1631—32）','作品','art-baroque','17世纪','西班牙','油画','重要',
  '委拉斯开兹为西班牙宫廷弄臣所作的全身肖像，克利夫兰艺术博物馆藏（1965.15）。','约1631—32年',
  '该馆说明：卡拉巴萨斯是西班牙国王菲利普四世宫廷中的弄臣，有身体与智力上的残障，画家强调这一状态而不是试图掩盖；西班牙宫廷珍视并宠爱有残障的人，而委拉斯开兹改变了他们在肖像中的描绘方式；这件作品用正式的全身宫廷肖像格式，来呈现在当时通常被视为边缘的一类人，并深刻地赋予他人性。',
  'baroque,velazquez','cma-1965-15'),
 ('hals-woman-aeltje-pater','哈尔斯《女子肖像（或为阿尔切·迪尔克斯多赫特·帕特尔）》（1638）','作品','art-baroque','17世纪','荷兰','油画','重要',
  '哈尔斯1638年题年的女子肖像，克利夫兰艺术博物馆藏（1948.137）。','1638年',
  '该馆说明：哈尔斯的肖像常有大胆而参差的笔触，这幅显示他试验湿中湿技法，即不待下层干透就接续加上颜料层，发际线处混合的笔触暗示了一根根头发；画中人被暂定为阿尔切·迪尔克斯多赫特·帕特尔（1597—1678），即哈勒姆酿酒商兼市长扬·德·瓦埃尔（1594—1663）的妻子；题款称她画时41岁。',
  'baroque','cma-1948-137'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
txt="\n".join(lines)
T=[t for t in T if "'%s'"%t[0] not in txt]
if T:
    close=max(i for i,l in enumerate(lines) if l.strip()=="]")
    lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
    io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended",len(T))
