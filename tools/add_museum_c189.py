# -*- coding: utf-8 -*-
"""Cycle189：给4件作品条目追加收藏机构官方藏品页来源。写入前逐条取回页面核对关键字段，任一不符即中止。"""
import json,os,re,html,urllib.request,time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)));D=os.path.join(ROOT,"data")
TAG="（收藏机构藏品页对照，2026-11-24）"
M={
 'mona-lisa':('mus-louvre-joconde','https://collections.louvre.fr/ark:/53355/cl010062370','Musée du Louvre（卢浮宫藏品数据库）',
   'Louvre Collections — Portrait de Lisa Gherardini, dit La Joconde ou Monna Lisa',['La Joconde','1503 / 1519'],
   '卢浮宫藏品记录年代为1503/1519年，与本条目 when 一致。'),
 'birth-of-venus-work':('mus-uffizi-venus','https://www.uffizi.it/en/artworks/birth-of-venus','Gallerie degli Uffizi（乌菲兹美术馆官网）',
   'Uffizi Galleries — Birth of Venus, Sandro Botticelli',['Birth of Venus','1485 ca.'],
   '乌菲兹官网年代为约1485年，与本条目 when 一致。'),
 'sistine-ceiling-work':('mus-vatican-volta','https://www.museivaticani.va/content/museivaticani/en/collezioni/musei/cappella-sistina/volta.html','Musei Vaticani（梵蒂冈博物馆官网）',
   'Musei Vaticani — Sistine Chapel, Ceiling',['8 May 1508','31 October 1512'],
   '梵蒂冈博物馆称1508年5月8日签约、1512年10月31日前完成，与本条目 when 一致。'),
 'guernica-work':('mus-reinasofia-guernica','https://www.museoreinasofia.es/en/collection/artwork/guernica-0','Museo Nacional Centro de Arte Reina Sofía（索菲亚王后国家艺术中心官网）',
   'Museo Reina Sofía — Guernica, Pablo Picasso (DE00050)',['Picasso, Pablo','1937','DE00050'],
   '索菲亚王后艺术中心记录为1937年（5月1日—6月4日，巴黎），布面油画，登记号 DE00050，与本条目 when 一致。'),
}
def txt(u):
    r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':'Mozilla/5.0 YishuBot/1.0'}),timeout=40)
    h=r.read().decode('utf-8','replace')
    return re.sub(r'\s+',' ',html.unescape(re.sub(r'<[^>]+>',' ',re.sub(r'(?s)<(script|style).*?</\1>','',h))))
bad=[]
for eid,(sid,url,auth,title,keys,_) in M.items():
    try: t=txt(url); miss=[k for k in keys if k not in t]
    except Exception as e: miss=['ERR '+str(e)[:60]]
    print(eid,'OK' if not miss else 'MISS %s'%miss)
    if miss: bad.append(eid)
    time.sleep(0.8)
if bad: raise SystemExit('核对不通过，未写入: %s'%bad)
sp=os.path.join(D,"sources.json");sd=json.load(open(sp,encoding="utf-8"));have={s["id"] for s in sd["sources"]}
for eid,(sid,url,auth,title,keys,note) in M.items():
    if sid not in have:
        sd["sources"].append({"id":sid,"title":title,"author":auth,"year":"2026","url":url,"type":"收藏机构官方藏品记录（作品名称、作者、年代）","verified":True,
          "verified_note":"2026-11-24 取回该页面，核对到：%s"%"、".join(keys)})
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2);print("sources:",len(sd["sources"]))
for eid,(sid,url,auth,title,keys,note) in M.items():
    p=os.path.join(D,"l2",eid+".json");j=json.load(open(p,encoding="utf-8"))
    if sid not in j["sources"]: j["sources"].append(sid)
    t=j["sections"].get("待核实","")
    if TAG not in t: j["sections"]["待核实"]=t+TAG+note+"藏品页只能印证作品名称、作者与年代，不能印证风格解读与影响叙述。"
    json.dump(j,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("l2 updated",len(M))
