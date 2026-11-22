# -*- coding: utf-8 -*-
"""Cycle1 批次输入：全部剩余L1条目（27旧+5新=32），分8块。"""
import json, os, glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
S={s["id"]:s for s in json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))["sources"]}
done={os.path.basename(p)[:-5] for p in glob.glob(os.path.join(D,"l2","*.json"))}
order={"核心":0,"重要":1,"补充":2}
cands=[e for e in es if e.get("level","L1")=="L1" and e["id"] not in done]
cands.sort(key=lambda e:(order[e["tier"]],e["unit"],e["id"]))
out=[]
for e in cands:
    out.append({
      "id":e["id"],"title":e["title"],"kind":e["kind"],"era":e["era"],
      "region":e["region"],"medium":e["medium"],
      "def":e["def"],"when":e["when"],"overview":e["overview"],
      "related":[{"id":r,"title":next((x["title"] for x in es if x["id"]==r),r)} for r in e["related"]],
      "sources":[{"id":s,"title":S[s]["title"],"author":S[s]["author"],"type":S[s]["type"]}
                 for s in e["sources"] if s in S and S[s]["verified"]]
    })
gen=os.path.join(ROOT,"data","l2_generated")
for p in glob.glob(os.path.join(gen,"_input_*.json"))+glob.glob(os.path.join(gen,"out_*.json")):
    os.remove(p)
json.dump(out,open(os.path.join(ROOT,"batch3_input.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
ids=[e["id"] for e in out]
for i in range(0,len(ids),4):
    grp=ids[i:i+4]
    json.dump([e for e in out if e["id"] in grp],
              open(os.path.join(gen,"_input_%02d.json"%(i//4+1)),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("batch3 size",len(out),"chunks",(len(ids)+3)//4)
print("ids",",".join(ids))
