# -*- coding: utf-8 -*-
"""修复来源重复隐患：
1) 向 sources.json 增加4条已联网核对的权威百科来源；
2) 新增 data/source_fixes.json：为8个来源重复的条目替换为2个不同id；
3) merge_l2 在合并前应用 source_fixes；
4) check.py 增加 R15：sources 内不得有重复 id。
"""
import json, os, re, ssl, urllib.request, time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
ctx=ssl.create_default_context()

NEW=[
 ("enc-cave-art","Cave painting","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Cave_art","权威百科","Cave painting"),
 ("enc-venus-figurines","Venus figurine","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Venus_figurines","权威百科","Venus figurine"),
 ("enc-calligraphy","Calligraphy","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Calligraphy","权威百科","Calligraphy"),
 ("enc-ink-wash","Ink wash painting","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Ink_wash_painting","权威百科","Ink wash painting"),
]

def verify(url,kw):
    for i in range(3):
        try:
            r=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
            h=urllib.request.urlopen(r,timeout=30,context=ctx).read(400000).decode("utf-8","ignore")
            m=re.search(r"<title[^>]*>(.*?)</title>",h,re.I|re.S)
            tt=re.sub(r"<[^>]+>","",m.group(1)) if m else ""
            assert kw.lower() in (tt+" "+h[:100000]).lower()
            return True,"HTTP 200; <title>=%s"%tt[:50]
        except AssertionError as e:
            return False,"标题未命中 %s"%kw
        except Exception as e:
            last=e; time.sleep(1.5)
    return False,"抓取失败 %s"%str(last)[:50]

sp=os.path.join(D,"sources.json")
data=json.load(open(sp,encoding="utf-8"))
existing={s["id"] for s in data["sources"]}
for sid,title,author,year,url,typ,kw in NEW:
    if sid in existing: continue
    ok,note=verify(url,kw)
    data["sources"].append({"id":sid,"title":title,"author":author,"year":year,
        "url":url,"type":typ,"verified":ok,"verified_note":note})
    print("source",sid,"verified",ok)

json.dump(data,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

fixes={
 "prehistoric-art":["enc-prehistoric-art","enc-cave-art"],
 "paleolithic-sculpture":["enc-prehistoric-art","enc-venus-figurines"],
 "gongbi":["enc-chinese-painting","enc-ink-wash"],
 "seal-script":["enc-chinese-calligraphy","enc-calligraphy"],
 "clerical-script":["enc-chinese-calligraphy","enc-calligraphy"],
 "regular-script":["enc-chinese-calligraphy","enc-calligraphy"],
 "running-script":["enc-chinese-calligraphy","enc-calligraphy"],
 "cursive-script":["enc-chinese-calligraphy","enc-calligraphy"],
}
json.dump(fixes,open(os.path.join(D,"source_fixes.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("source_fixes written",len(fixes))
