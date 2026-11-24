# -*- coding: utf-8 -*-
"""Cycle103：新古典/浪漫 4 条（透纳、大卫、哈克特、帕林克）。"""
import io,json,os,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
NEWS=[
 ("cma-1942-647","Cleveland Museum of Art — J.M.W. Turner, The Burning of the Houses of Lords and Commons, 1835, acc. 1942.647",
  "https://openaccess-api.clevelandart.org/api/artworks/1942.647","2026-11-23 API HTTP 200；布面油画 92×123.2cm；说明含1834年议会大火与夸大火势"),
 ("cma-1962-37","Cleveland Museum of Art — Jacques-Louis David, Cupid and Psyche, 1817, acc. 1962.37",
  "https://openaccess-api.clevelandart.org/api/artworks/1962.37","2026-11-23 API HTTP 200；布面油画 184.2×241.6cm；说明含 Moschus 诗与理想爱/肉体现实"),
 ("cma-1983-14","Cleveland Museum of Art — Philipp Hackert, View of the Gulf of Pozzuoli from Solfatara, 1803, acc. 1983.14",
  "https://openaccess-api.clevelandart.org/api/artworks/1983.14","2026-11-23 API HTTP 200；布面油画 119×166.5cm；说明含那不勒斯景观与德国浪漫的清晰造型"),
 ("cma-1937-575","Cleveland Museum of Art — Joseph Paelinck, Self-Portrait, c. 1812, acc. 1937.575",
  "https://openaccess-api.clevelandart.org/api/artworks/1937.575","2026-11-23 API HTTP 200；布面油画 89×69.3cm；说明含在大卫门下与罗马时期"),
]
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for sid,title,url,note in NEWS:
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":"Cleveland Museum of Art（开放数据 API）",
            "year":"2026","url":url,"type":"权威机构藏品记录","verified":True,"verified_note":note})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
T=[
 ('turner-burning-parliament','透纳《上议院与下议院焚毁》','作品','art-neo-romantic','19世纪','欧洲','绘画','核心',
  '透纳布面油画，克利夫兰艺术博物馆藏（1942.647）。','1835年',
  '记1834年10月16日伦敦议会大火；透纳夸大火势，以灾难表达人面对自然破坏力的无力；色块近于抽象。','turner,constable','cma-1942-647'),
 ('david-cupid-psyche','大卫《丘比特与普绪克》','作品','art-neo-romantic','19世纪','欧洲','绘画','核心',
  '大卫布面油画，克利夫兰艺术博物馆藏（1962.37）。','1817年',
  '以神话探讨理想之爱与肉体现实的冲突；丘比特被画成笨拙少年而非理想少年，取材 Moschus 的希腊诗。','neoclassicism,paelinck-self-portrait','cma-1962-37'),
 ('hackert-pozzuoli','哈克特《从索尔法塔拉望波佐利湾》','作品','art-neo-romantic','19世纪','欧洲','绘画','重要',
  '哈克特布面油画，克利夫兰艺术博物馆藏（1983.14）。','1803年',
  '18—19世纪画家云集那不勒斯写火山与古典废墟；细致描摹与极清晰的造型为德国浪漫绘画特征。','neoclassicism,turner-burning-parliament','cma-1983-14'),
 ('paelinck-self-portrait','帕林克《自画像》','作品','art-neo-romantic','19世纪','欧洲','绘画','重要',
  '帕林克布面油画，克利夫兰艺术博物馆藏（1937.575）。','约1812年',
  '比利时人，获资助赴巴黎从大卫学画，后赴罗马研究古物；着时髦 box-coat 与古式桌椅，见其质感描写功力。','david-cupid-psyche,neoclassicism','cma-1937-575'),
]
p=os.path.join(ROOT,"tools","catalog.py"); lines=io.open(p,encoding="utf-8").read().split("\n")
close=max(i for i,l in enumerate(lines) if l.strip()=="]")
lines[close:close]=["(%s),"%",\n ".join(repr(x) for x in t) for t in T]
io.open(p,"w",encoding="utf-8").write("\n".join(lines))
print("catalog appended 4")