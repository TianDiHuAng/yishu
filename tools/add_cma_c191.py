# -*- coding: utf-8 -*-
"""Cycle191：给10个时期条目追加克利夫兰艺术博物馆(CMA)开放数据中一件代表馆藏的记录作来源。
写入前按 id 重新取回每件藏品，核对登记号与断代字段，任一不符即中止。只比对朝代/时期断代，不改 when、不改正文。"""
import json,os,urllib.request,time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));D=os.path.join(ROOT,"data")
TAG="（克利夫兰艺术博物馆馆藏对照，2026-11-25）"
API="https://openaccess-api.clevelandart.org/api/artworks/%d"
LIM="单件馆藏记录只能印证该时期的断代与存在此类作品，不能印证风格概括与影响叙述。"
M={
 'tang-painting':(148381,'1975.92','Tang dynasty (618-907)','CMA 断代唐代618—907年，与本条目 when 一致；代表作为约900年的《释迦三尊》绢画。'),
 'song-painting':(135836,'1959.348','Northern Song dynasty (960','CMA 断代北宋960—1127年（其馆藏另有南宋1127—1279年），与本条目 when 960—1279年相合；代表作为《溪山兰若图》，960—985年。'),
 'yuan-painting':(160133,'1997.91','Yuan dynasty (1271','CMA 断代元代1271—1368年，与本条目 when 一致；代表作为1347年《秋景鹑雀图》。'),
 'ming-painting':(138688,'1963.102','Ming dynasty (1368','CMA 断代明代1368—1644年，与本条目 when 一致；代表作为1542—1543年《赵孟頫写经换茶图》。'),
 'qing-painting':(137202,'1962.157','Qing dynasty (1644','CMA 断代清代写作1644—1911年，本条目 when 为1644—1912年（以宣统退位计）；止年差一年属计法不同，未改 when。代表作为1690年《仿古山水册》。'),
 'six-dynasties-art':(151373,'1983.213','Six Dynasties period (220','CMA 断代六朝220—589年，与本条目 when 一致；代表作为约317—400年西王母纹铜镜。'),
 'shang-zhou-bronzes':(138689,'1963.103','Shang dynasty (c. 1600','CMA 断代商代约前1600—约前1046年、安阳期约前1250—前1046年，代表作为方卣；只印证了商代起点，周代下限前256年未经此来源印证。'),
 'egyptian-art':(130133,'1952.513','New Kingdom (1540','CMA 记录新王国约前1540—前1069年（第十八王朝阿蒙霍特普三世头像）；只落在本条目 when 约前3100—前30年之内，不能印证首尾年代。'),
 'angkor':(170075,'2012.294','Angkor','CMA 记录为柬埔寨吴哥、10世纪（湿婆信徒头像）；只落在本条目 when 约9—15世纪之内，不能印证首尾年代。'),
 'byzantine-art':(145192,'1970.36','Byzantine period','CMA 记录为君士坦丁堡、拜占庭时期、约1050年（游行十字架残件）；只落在本条目 when 约4—15世纪之内，不能印证首尾年代。'),
}
def get(i):
    r=urllib.request.urlopen(urllib.request.Request(API%i,headers={'User-Agent':'YishuBot/1.0 (educational art-history knowledge base)'}),timeout=40)
    return json.loads(r.read().decode('utf-8'))['data']
bad=[];rec={}
for eid,(i,acc,need,_) in M.items():
    try:
        a=get(i);c=' '.join(a.get('culture') or [])
        ok=a.get('accession_number')==acc and need in c
        rec[eid]=a
    except Exception as e: ok=False;c='ERR '+str(e)[:60]
    print(eid,'OK' if ok else 'MISMATCH '+c)
    if not ok: bad.append(eid)
    time.sleep(0.5)
if bad: raise SystemExit('核对不通过，未写入: %s'%bad)
sp=os.path.join(D,"sources.json");sd=json.load(open(sp,encoding="utf-8"));have={s["id"] for s in sd["sources"]}
for eid,(i,acc,need,_) in M.items():
    a=rec[eid];sid='cma-'+acc.replace('.','-')
    if sid not in have:
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
