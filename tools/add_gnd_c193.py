# -*- coding: utf-8 -*-
"""Cycle193：《星月夜》《春之祭》补德国国家图书馆规范档(GND)作品记录来源。写入前经 lobid 按编号重取，核对标目、年代与作者，任一不符即中止。不改 when。"""
import json,os,urllib.request,time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));D=os.path.join(ROOT,"data")
TAG="（德国国家图书馆规范档作品记录对照，2026-11-25）"
M={
 'starry-night':('4209985-7','Sternennacht (The Museum of Modern Art, New York, NY)','1889','Gogh, Vincent van',
   'GND 作品记录为凡·高《星月夜》（纽约现代艺术博物馆藏），创作年代1889年，与本条目 when 一致。GND 另有同名的奥赛美术馆藏1888年作品（1271485265，即《罗讷河上的星夜》），是另一幅画，未采用。'),
 'rite-of-spring-work':('300158289','Le sacre du printemps','1910-1913','Stravinsky, Igor',
   'GND 作品记录为斯特拉文斯基《春之祭》，创作年代1910—1913年；本条目 when 1913年是首演年份，二者相容，未改 when。'),
}
def get(n):
    r=urllib.request.urlopen(urllib.request.Request('https://lobid.org/gnd/%s.json'%n,headers={'User-Agent':'YishuBot/1.0 (educational art-history knowledge base)'}),timeout=40)
    return json.loads(r.read().decode('utf-8'))
bad=[];rec={}
for eid,(n,name,date,who,_) in M.items():
    try:
        d=get(n);people=[c.get('label') for k in ('firstArtist','firstComposer','firstAuthor') for c in d.get(k,[])]
        ok=d.get('preferredName')==name and date in (d.get('dateOfProduction') or []) and who in people;rec[eid]=d
        msg='%s %s %s'%(d.get('preferredName'),d.get('dateOfProduction'),people)
    except Exception as e: ok=False;msg='ERR '+str(e)[:60]
    print(eid,'OK' if ok else 'MISMATCH '+msg)
    if not ok: bad.append(eid)
    time.sleep(0.5)
if bad: raise SystemExit('核对不通过，未写入: %s'%bad)
sp=os.path.join(D,"sources.json");sd=json.load(open(sp,encoding="utf-8"));have={s["id"] for s in sd["sources"]}
for eid,(n,name,date,who,_) in M.items():
    sid='gnd-'+n
    if sid not in have:
        sd["sources"].append({"id":sid,"title":"GND 作品规范记录 — %s"%name,"author":"Deutsche Nationalbibliothek（德国国家图书馆规范档 GND）",
          "year":"2026","url":"https://d-nb.info/gnd/"+n,"type":"国家图书馆作品规范记录（标目、作者、创作年代）","verified":True,
          "verified_note":"2026-11-25 经 lobid.org 按编号 %s 取回，核对标目“%s”、作者 %s、年代 %s"%(n,name,who,date)})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2);print("sources:",len(sd["sources"]))
for eid,(n,name,date,who,note) in M.items():
    sid='gnd-'+n;p=os.path.join(D,"l2",eid+".json");j=json.load(open(p,encoding="utf-8"))
    j.setdefault("sources",[])
    if sid not in j["sources"]: j["sources"].append(sid)
    sec=j.setdefault("sections",{});t=sec.get("待核实","")
    if TAG not in t: sec["待核实"]=t+TAG+note+"作品规范记录只能印证作品名称、作者与年代，不能印证风格解读与影响叙述。"
    json.dump(j,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("l2 updated",len(M))
