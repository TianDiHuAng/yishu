# -*- coding: utf-8 -*-
import json,urllib.request,urllib.parse,sys
TERMS=['watercolor','pastel (crayon)','installation art','still lifes','pointillism','plein air','vanitas','triptychs','altarpieces','gouache','mosaic','mezzotint','aquatint','drypoint','pentimento','scumbling','tenebrism','anamorphosis','sinopia','miniature (painting)']
EP='https://vocab.getty.edu/sparql.json'
def q(t):
    s='''select ?s ?l ?n where {?s a gvp:Concept; skos:inScheme aat: ; gvp:prefLabelGVP/xl:literalForm ?l . filter(lcase(str(?l))="%s") optional {?s skos:scopeNote/rdf:value ?n . filter(lang(?n)="en" || lang(?n)="")}} limit 6'''%t.lower()
    u=EP+'?query='+urllib.parse.quote(s)
    r=urllib.request.urlopen(urllib.request.Request(u,headers={'Accept':'application/sparql-results+json'}),timeout=25)
    return [(b['s']['value'].rsplit('/',1)[-1],b['l']['value'],b.get('n',{}).get('value','')) for b in json.load(r)['results']['bindings']]
if __name__!="__main__": raise SystemExit
out={}
for t in TERMS:
    try: out[t]=q(t)
    except Exception as e: out[t]=[('ERR',str(e)[:80],'')]
    print(t,'->',[(a,b,c[:70]) for a,b,c in out[t]][:3]); sys.stdout.flush()
json.dump(out,open('tmp/aat_batch3.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
