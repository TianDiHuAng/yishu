# -*- coding: utf-8 -*-
"""Cycle233 探测：为本次会话新增的风格/术语条目查 AAT（精确标签匹配），结果存 tmp/aat_c233.json，不写入数据。"""
import json,urllib.request,urllib.parse,time
EP='https://vocab.getty.edu/sparql.json'
def q(t):
    s='''select ?s ?l ?n where {?s a gvp:Concept; skos:inScheme aat: ; gvp:prefLabelGVP/xl:literalForm ?l . filter(lcase(str(?l))="%s") optional {?s skos:scopeNote/rdf:value ?n . filter(lang(?n)="en" || lang(?n)="")}} limit 6'''%t.lower()
    r=urllib.request.urlopen(urllib.request.Request(EP+'?query='+urllib.parse.quote(s),headers={'Accept':'application/sparql-results+json','User-Agent':'yishu/1.0'}),timeout=30)
    return [(b['s']['value'].rsplit('/',1)[-1],b['l']['value'],b.get('n',{}).get('value','')) for b in json.load(r)['results']['bindings']]
C={
 'pictorialism':['Pictorialism','Pictorialist'],'straight-photography':['straight photography'],'documentary-photography':['documentary photography','documentary photographs'],
 'brutalism':['Brutalist','New Brutalist'],'postmodern-architecture':['Postmodern','Post-Modern'],'ink-wash-painting':['ink wash painting','ink painting'],
 'literati-painting':['literati painting','Literati','wenrenhua'],'wu-school':['Wu School'],'four-wangs':['Four Wangs','Orthodox School'],
 'fortepiano':['fortepianos'],'viol':['viols','viola da gamba'],'guqin':['qins','guqins'],'bianzhong':['bianzhong'],'xiao':['xiaos','xiao'],'ruan':['ruans'],
 'galant-music':['galant'],'opera-seria':['opera seria'],'singspiel':['singspiele','singspiel'],'piano-sonata':['piano sonatas'],
 'chanson':['chansons'],'mensural-notation':['mensural notation'],'chinese-opera':['Chinese opera','xiqu'],'yuefu':['yuefu'],'ci-poetry':['ci'],
 'mannheim-school':['Mannheim School'],'franco-flemish-school':['Franco-Flemish'],'pre-columbian-art':['Pre-Columbian'],
 'photography':['photography'],'six-principles':['Six Principles'],
}
out={}
for eid,ts in C.items():
    out[eid]=[]
    for t in ts:
        try: out[eid]+= q(t)
        except Exception as e: print('ERR',eid,t,e)
        time.sleep(0.3)
    print(eid,[(a,b,n[:120]) for a,b,n in out[eid]])
json.dump(out,open('tmp/aat_c233.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
