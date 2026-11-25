# -*- coding: utf-8 -*-
"""Cycle191 探测：用 LC 主题词表(LCSH) suggest2 查音乐体裁/乐器/术语类百科同源条目的候选标目。只探测，不写入。原文存 tmp/lcsh_c191.json。"""
import json,os,sys,time,urllib.request,urllib.parse
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UA='YishuBot/1.0 (educational art-history knowledge base; contact: local-maintainer)'
API="https://id.loc.gov/authorities/subjects/suggest2?q=%s&searchtype=keyword&count=8"
C={
 'fugue':['Fugue'],'sonata':['Sonata'],'sonata-form':['Sonata form'],'symphony':['Symphony'],
 'symphonic-poem':['Symphonic poem'],'concerto':['Concerto'],'counterpoint':['Counterpoint'],
 'polyphony':['Polyphony'],'opera':['Opera'],'madrigal':['Madrigal'],'motet':['Motet'],
 'mass-music':['Masses'],'lied':['Songs (High voice) with piano','Lied'],'organum':['Organum'],
 'gregorian-chant':['Gregorian chants'],'musical-mode':['Musical intervals and scales','Modes (Music)'],
 'tonality':['Tonality'],'serialism':['Serialism (Music)','Twelve-tone system'],
 'minimalism-music':['Minimal music'],'impressionism-music':['Impressionism (Music)'],
 'pipa':['Pipa'],'guzheng':['Zheng'],'jingju':['Peking opera','Operas, Chinese'],
 'yayue':['Ya yue'],'regular-script':['Calligraphy, Chinese'],'cursive-script':['Calligraphy, Chinese'],
 'mannerism':['Mannerism (Art)'],'minimalism':['Minimal art'],'realism-art':['Realism in art'],
 'byzantine-art':['Art, Byzantine'],'venetian-school':['Painting, Venetian'],
 'beaux-arts-architecture':['Beaux-arts architecture','Eclecticism in architecture'],
}
def q(t):
    r=urllib.request.urlopen(urllib.request.Request(API%urllib.parse.quote(t),headers={'User-Agent':UA,'Accept':'application/json'}),timeout=40)
    d=json.loads(r.read().decode('utf-8','replace'))
    return [(h.get('aLabel',''),h.get('uri','').rsplit('/',1)[-1],h.get('vLabel','')) for h in d.get('hits',[])]
def main():
    out={}
    for eid,ts in C.items():
        out[eid]=[]
        for t in ts:
            try: out[eid]+=[(t,)+x for x in q(t)]
            except Exception as e: out[eid].append((t,'ERR',str(e)[:60],''))
            time.sleep(0.4)
        print(eid,'->',[(a,b) for _,a,b,_ in out[eid]][:4]); sys.stdout.flush()
    os.makedirs(os.path.join(ROOT,'tmp'),exist_ok=True)
    json.dump(out,open(os.path.join(ROOT,'tmp','lcsh_c191.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
if __name__=="__main__": main()
