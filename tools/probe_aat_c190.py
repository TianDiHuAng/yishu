# -*- coding: utf-8 -*-
"""Cycle190 探测：为百科同源的风格/术语条目查 AAT 候选词条（精确标签匹配），结果存 tmp/aat_c190.json，不写入数据。"""
import json,urllib.request,urllib.parse,sys,time
EP='https://vocab.getty.edu/sparql.json'
def q(t):
    s='''select ?s ?l ?n where {?s a gvp:Concept; skos:inScheme aat: ; gvp:prefLabelGVP/xl:literalForm ?l . filter(lcase(str(?l))="%s") optional {?s skos:scopeNote/rdf:value ?n . filter(lang(?n)="en" || lang(?n)="")}} limit 6'''%t.lower()
    r=urllib.request.urlopen(urllib.request.Request(EP+'?query='+urllib.parse.quote(s),headers={'Accept':'application/sparql-results+json'}),timeout=30)
    return [(b['s']['value'].rsplit('/',1)[-1],b['l']['value'],b.get('n',{}).get('value','')) for b in json.load(r)['results']['bindings']]
C={
 'gothic':['Gothic','Gothic (Medieval)'],'mannerism':['Mannerist','Mannerism'],'neoclassicism':['Neoclassical','Neo-Classical'],
 'fauvism':['Fauve','Fauvist'],'minimalism':['Minimalist','Minimal art'],'conceptual-art':['Conceptual art','Conceptual'],
 'abstract-expressionism':['Abstract Expressionist'],'realism-art':['Realist','Realism (style)'],'romanesque':['Romanesque'],
 'byzantine-art':['Byzantine'],'early-christian-art':['Early Christian'],'art-deco':['Art Deco'],'ukiyo-e':['ukiyo-e'],
 'venetian-school':['Venetian'],'northern-renaissance':['Northern Renaissance'],'high-renaissance':['High Renaissance'],
 'early-renaissance':['Early Renaissance'],'beaux-arts-architecture':['Beaux-Arts'],'gothic-revival-architecture':['Gothic Revival'],
 'modern-architecture':['Modernist','International Style'],'mughal-architecture':['Mughal'],'khmer-art':['Khmer'],
 'xieyi':['xieyi'],'gongbi':['gongbi'],'fugue':['fugues'],'sonata':['sonatas'],'symphony':['symphonies'],'concerto':['concertos'],
 'motet':['motets'],'mass-music':['masses (musical works)'],'madrigal':['madrigals'],'opera':['operas'],'lied':['lieder'],
 'counterpoint':['counterpoint'],'polyphony':['polyphony'],'organum':['organum'],'serialism':['serialism'],
 'gregorian-chant':['Gregorian chant'],'violin':['violins'],'piano':['pianos'],'pipa':['pipas'],'guzheng':['zhengs','guzhengs'],
 'seal-script':['seal script'],'clerical-script':['clerical script'],'regular-script':['regular script'],
 'running-script':['running script'],'cursive-script':['cursive script'],'music-notation':['musical notation'],
}
def main():
    out={}
    for eid,ts in C.items():
        out[eid]=[]
        for t in ts:
            try: r=q(t)
            except Exception as e: r=[('ERR',str(e)[:60],'')]
            out[eid]+=r
            time.sleep(0.4)
        print(eid,'->',[(a,b,c[:50]) for a,b,c in out[eid]][:3]); sys.stdout.flush()
    json.dump(out,open('tmp/aat_c190.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
if __name__=="__main__": main()
