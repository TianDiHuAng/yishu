# -*- coding: utf-8 -*-
"""生成 L3 写作输入：4个核心条目的现有七节+来源，供代理写争议/数据块。"""
import json,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
ids=["greek-art","gothic","impressionism","baroque-music"]
out=[]
for e in es:
 if e["id"] not in ids: continue
 out.append({"id":e["id"],"title":e["title"],"when":e["when"],"overview":e["overview"],
   "sections":e["sections"],"sources":e["sources"],
   "related":e["related"]})
json.dump(out,open(os.path.join(ROOT,"l3_input.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
json.dump(out[:2],open(os.path.join(ROOT,"l3_input_1.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
json.dump(out[2:],open(os.path.join(ROOT,"l3_input_2.json"),"w",encoding="utf-8"),ensure_ascii=False,indent=1)
print("L3 input",len(out))
