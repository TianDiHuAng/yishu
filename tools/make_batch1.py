# -*- coding: utf-8 -*-
"""生成 Phase4 第一批（40条核心条目）的工作输入：仅携带 catalog 已核验事实 + 来源标题，供写作代理 grounding。"""
import json, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
S={s["id"]:s for s in json.load(open(os.path.join(D,"sources.json"),encoding="utf-8"))["sources"]}
done={"impressionism","baroque-music"}
core=[e for e in es if e["tier"]=="核心" and e["id"] not in done][:40]
out=[]
for e in core:
    out.append({
      "id":e["id"],"title":e["title"],"kind":e["kind"],"era":e["era"],
      "region":e["region"],"medium":e["medium"],
      "def":e["def"],"when":e["when"],"overview":e["overview"],
      "related":[{"id":r,"title":next((x["title"] for x in es if x["id"]==r),r)} for r in e["related"]],
      "sources":[{"id":s,"title":S[s]["title"],"author":S[s]["author"],"type":S[s]["type"]}
                 for s in e["sources"] if s in S and S[s]["verified"]]
    })
json.dump(out,open(os.path.join(ROOT,"batch1_input.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("batch size",len(out))
print("ids",",".join(e["id"] for e in out))
