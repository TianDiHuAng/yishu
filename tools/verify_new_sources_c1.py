# -*- coding: utf-8 -*-
"""Cycle1 缺口修复：为新增中国艺术史条目联网核验来源，验证通过才加入 sources.json。"""
import json, os, re, ssl, time, urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
ctx=ssl.create_default_context()

CAND=[
 ("enc-bronze","Chinese bronze ware","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Chinese_bronze_ware","权威百科","bronze"),
 ("enc-shang-bronze","Chinese bronzes","Encyclopaedia Britannica","2026","https://www.britannica.com/art/Chinese-bronze-work","权威百科","bronze"),
 ("enc-yangshao","Yangshao culture","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Yangshao_culture","权威百科","Yangshao"),
 ("enc-painted-pottery","Painted pottery","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Painted_pottery","权威百科","pottery"),
 ("enc-chinese-jade","Chinese jade","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Chinese_jade","权威百科","jade"),
 ("enc-jade","Jade","Encyclopaedia Britannica","2026","https://www.britannica.com/science/jade","权威百科","jade"),
 ("enc-dunhuang","Dunhuang","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Dunhuang","权威百科","Dunhuang"),
 ("enc-chinese-buddhist-art","Chinese Buddhist art","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Chinese_Buddhist_art","权威百科","Buddhist"),
 ("enc-six-dynasties","Six Dynasties","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Six_Dynasties","权威百科","Six Dynasties"),
 ("enc-wei-jin-art","Art of the Six Dynasties","Wikipedia contributors","2026","https://en.wikipedia.org/wiki/Art_of_the_Six_Dynasties","权威百科","Six Dynasties"),
]
def verify(it):
    sid,title,author,year,url,typ,kw=it
    for i in range(3):
        try:
            req=urllib.request.Request(url,headers={"User-Agent":"Mozilla/5.0"})
            h=urllib.request.urlopen(req,timeout=30,context=ctx).read(600000).decode("utf-8","ignore")
            m=re.search(r"<title[^>]*>(.*?)</title>",h,re.I|re.S)
            tt=re.sub(r"<[^>]+>","",m.group(1)) if m else ""
            ok=kw.lower() in (tt+" "+h[:200000]).lower()
            return sid,ok,"HTTP200 <title>=%s kw=%s"%(tt[:45],kw)
        except Exception as e:
            last=e; time.sleep(1.3)
    return sid,False,"ERR %s %s"%(type(last).__name__,str(last)[:50])

def main():
    res={}
    with ThreadPoolExecutor(max_workers=5) as ex:
        futs={ex.submit(verify,it):it[0] for it in CAND}
        for f in as_completed(futs):
            try: sid,ok,note=f.result(); res[sid]=(ok,note)
            except Exception as e: res[futs[f]]=(False,str(e)[:60])
    p=os.path.join(D,"sources.json"); data=json.load(open(p,encoding="utf-8"))
    exist={s["id"] for s in data["sources"]}
    added=[]
    for it in CAND:
        sid,title,author,year,url,typ,kw=it
        ok,note=res.get(sid,(False,"未核验"))
        print(sid, "OK" if ok else "FAIL", note[:70])
        if ok and sid not in exist:
            data["sources"].append({"id":sid,"title":title,"author":author,"year":year,
                "url":url,"type":typ,"verified":True,"verified_note":note}); added.append(sid)
    json.dump(data,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
    print("added sources:",added)
if __name__=="__main__": main()
