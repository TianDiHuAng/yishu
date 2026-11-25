# -*- coding: utf-8 -*-
"""Cycle192：古希腊、古罗马艺术补克利夫兰馆藏来源。复用 add_cma_c191 的核对与写入逻辑，写入前按 id 重取核对登记号与断代。"""
import json,os,urllib.request,time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));D=os.path.join(ROOT,"data")
TAG="（克利夫兰艺术博物馆馆藏对照，2026-11-25）"
API="https://openaccess-api.clevelandart.org/api/artworks/%d"
LIM="单件馆藏记录只能印证该时期的断代与存在此类作品，不能印证风格概括与影响叙述。"
M={
 'greek-art':(130360,'1953.125','Archaic period','CMA 记录为希腊古风时期、约前550年（青年立像躯干）；只落在本条目 when 约前900—前146年之内，不能印证首尾年代。'),
 'roman-art':(110232,'1928.856','Roman Empire','CMA 记录为意大利罗马、罗马帝国、约公元100—125年（石棺）；只落在本条目 when 约前509年—公元5世纪之内，不能印证首尾年代。'),
}
def get(i):
    r=urllib.request.urlopen(urllib.request.Request(API%i,headers={'User-Agent':'YishuBot/1.0 (educational art-history knowledge base)'}),timeout=40)
    return json.loads(r.read().decode('utf-8'))['data']
bad=[];rec={}
for eid,(i,acc,need,_) in M.items():
    try:
        a=get(i);c=' '.join(a.get('culture') or []);ok=a.get('accession_number')==acc and need in c;rec[eid]=a
    except Exception as e: ok=False;c='ERR '+str(e)[:60]
    print(eid,'OK' if ok else 'MISMATCH '+c)
    if not ok: bad.append(eid)
    time.sleep(0.5)
if bad: raise SystemExit('核对不通过，未写入: %s'%bad)
sp=os.path.join(D,"sources.json");sd=json.load(open(sp,encoding="utf-8"));have={s["id"] for s in sd["sources"]}
for eid,(i,acc,need,_) in M.items():
    a=rec[eid];sid='cma-'+acc.replace('.','-')
    if sid in have: print('reuse',sid); continue
    sd["sources"].append({"id":sid,"title":"Cleveland Museum of Art — %s (%s)"%(a['title'].strip(),acc),
      "author":"Cleveland Museum of Art（克利夫兰艺术博物馆开放数据）","year":"2026","url":a.get('url') or 'https://clevelandart.org/art/'+acc,
      "type":"收藏机构官方藏品记录（断代、年代、类别）","verified":True,
      "verified_note":"2026-11-25 经开放数据接口按 id %d 取回，核对登记号 %s 与断代：%s；年代 %s"%(i,acc,'；'.join(a.get('culture') or []),a.get('creation_date'))})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2);print("sources:",len(sd["sources"]))
for eid,(i,acc,need,note) in M.items():
    sid='cma-'+acc.replace('.','-')
    p=os.path.join(D,"l2",eid+".json");j=json.load(open(p,encoding="utf-8"))
    j.setdefault("sources",[])
    if sid not in j["sources"]: j["sources"].append(sid)
    sec=j.setdefault("sections",{});t=sec.get("待核实","")
    if TAG not in t: sec["待核实"]=t+TAG+note+LIM
    json.dump(j,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("l2 updated",len(M))
