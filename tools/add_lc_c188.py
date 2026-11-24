# -*- coding: utf-8 -*-
"""Cycle188：给31个作曲家人物条目追加美国国会图书馆(LC)名称权威来源。
先用 suggest2 列出候选，选定主标目（排除无年代重复记录与作品级记录）；再逐条取回权威记录核对标签；只比对姓名与生卒年；不改 when、不改正文。"""
import json,os,urllib.request,time
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
LC="https://id.loc.gov/authorities/names/"
TAG="（LC 名称权威对照，2026-11-24）"
UA='YishuBot/1.0 (educational art-history knowledge base; contact: local-maintainer)'
M={
 'palestrina':('n50051776','Palestrina, Giovanni Pierluigi da, 1525?-1594','LC 生年带问号，仅能印证大致年代。'),
 'bach':('n79021425','Bach, Johann Sebastian, 1685-1750',''),
 'monteverdi':('n79074370','Monteverdi, Claudio, 1567-1643',''),
 'haydn':('n79091193','Haydn, Joseph, 1732-1809',''),
 'mozart':('n80022788','Mozart, Wolfgang Amadeus, 1756-1791',''),
 'beethoven':('n79107741','Beethoven, Ludwig van, 1770-1827',''),
 'chopin':('n79127769','Chopin, Frédéric, 1810-1849',''),
 'wagner':('n79089831','Wagner, Richard, 1813-1883','LC 另有无年代的 n78055968，是同名重复标目，未采用。'),
 'schubert':('n50000561','Schubert, Franz, 1797-1828','LC 另有无年代的 n86107150，是同名重复标目，未采用。'),
 'stravinsky':('n79070061','Stravinsky, Igor, 1882-1971',''),
 'schoenberg':('n80032780','Schoenberg, Arnold, 1874-1951',''),
 'debussy':('n79132137','Debussy, Claude, 1862-1918',''),
 'josquin':('n80005115','Josquin, des Prez, -1521','LC 只给出卒年1521，无生年，仅能印证卒年。'),
 'hildegard':('n80118409','Hildegard, Saint, 1098-1179',''),
 'vivaldi':('n79021280','Vivaldi, Antonio, 1678-1741','LC 另有无年代的 nb2007021131，是同名重复标目，未采用。'),
 'brahms':('n79077221','Brahms, Johannes, 1833-1897',''),
 'liszt':('n79079048','Liszt, Franz, 1811-1886',''),
 'mahler':('n80067106','Mahler, Gustav, 1860-1911','LC 另有无年代的 n2009078687，是同名重复标目，未采用。'),
 'tchaikovsky':('n79072979','Tchaikovsky, Peter Ilich, 1840-1893',''),
 'gluck':('n79135399','Gluck, Christoph Willibald, Ritter von, 1714-1787',''),
 'tallis':('n50009548','Tallis, Thomas, approximately 1505-1585','LC 为约1505—1585年，本条目 when 只写到世纪，未改。'),
 'byrd':('n50032948','Byrd, William, 1539 or 1540-1623','LC 生年为1539或1540年，与本条目 when 的约1540年相容。'),
 'lassus':('n81037013','Lasso, Orlando di, 1532-1594','LC 以意大利语形式 Lasso 立目。'),
 'gesualdo':('n79110488','Gesualdo, Carlo, principe di Venosa, approximately 1560-1613','LC 生年为约1560年，本条目 when 为1566年，二者不一致；按 LC 只是"约"，不据此改 when，留待更多来源核实。'),
 'machaut':('n50018452','Guillaume, de Machaut, approximately 1300-1377','LC 以名而非姓立目（Guillaume, de Machaut）。'),
 'leonin':('n87807575','Léonin, active 12th century','LC 只给活动期12世纪，无生卒年。'),
 'purcell':('n79095298','Purcell, Henry, 1659-1695','LC 另有仅写缩写的 n85276381（Purcell, H.），是同名缩写标目，未采用。'),
 'lully':('n79072787','Lully, Jean-Baptiste, 1632-1687',''),
 'scarlatti-domenico':('n79070071','Scarlatti, Domenico, 1685-1757','本条目 when 只写"约公元17—18世纪"，LC 精确年份为1685—1757，二者相容；when 未改。'),
 'corelli':('n79059471','Corelli, Arcangelo, 1653-1713',''),
 'telemann':('n79117028','Telemann, Georg Philipp, 1681-1767','本条目 when 只写"约公元17—18世纪"，LC 精确年份为1681—1767，二者相容；when 未改。'),
}
def fetch_label(num):
    u=LC+num+'.json'
    r=urllib.request.urlopen(urllib.request.Request(u,headers={'User-Agent':UA,'Accept':'application/json'}),timeout=40)
    data=json.loads(r.read().decode('utf-8','replace'))
    for n in data:
        if n.get('@id','').endswith('/authorities/names/'+num):
            for key in ('http://www.loc.gov/mads/rdf/v1#authoritativeLabel','http://www.w3.org/2004/02/skos/core#prefLabel'):
                for v in n.get(key,[]):
                    if '@language' not in v:
                        return v.get('@value')
    return None
bad=[]
for eid,(num,label,_) in M.items():
    got=None
    try: got=fetch_label(num)
    except Exception as e: got='ERR '+str(e)[:60]
    ok=(got==label)
    print(eid,num,'OK' if ok else 'MISMATCH',got if not ok else '')
    if not ok: bad.append(eid)
    time.sleep(0.8)
if bad:
    raise SystemExit('标签不一致，未写入: %s'%bad)
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8")); have={s["id"] for s in sd["sources"]}
for eid,(num,label,_) in M.items():
    sid="lc-"+num
    if sid not in have:
        sd["sources"].append({"id":sid,"title":"Library of Congress Name Authority — %s, %s"%(label,num),"author":"Library of Congress（LC Name Authority File，开放权威档案）","year":"2026","url":LC+num,"type":"权威机构名称档案（人物姓名与生卒年）","verified":True,
            "verified_note":"2026-11-24 经 id.loc.gov 取回该权威记录，标签为「%s」，编号与标签匹配，生卒年已与库内条目对照"%label})
        have.add(sid)
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("sources:",len(sd["sources"]))
for eid,(num,label,note) in M.items():
    p=os.path.join(D,"l2",eid+".json")
    j=json.load(open(p,encoding="utf-8"))
    sid="lc-"+num
    if sid not in j["sources"]: j["sources"].append(sid)
    t=j["sections"].get("待核实","")
    if TAG not in t: j["sections"]["待核实"]=t+TAG+"LC 标目："+label+"。"+note+"LC 权威档案只能印证姓名与生卒年，不能印证风格归属或代表作。"
    json.dump(j,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("l2 updated",len(M))
