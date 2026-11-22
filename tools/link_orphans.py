# -*- coding: utf-8 -*-
"""孤儿页补链（P1）：只添加【已有条目 related 中明确提到该孤儿】的反向链，
以及基于 L1 seed related 的传递关系（A->B 且 B->orphan 不危险，因为 B 的 related 是编辑基准线里的真实关系）。
具体策略：对每个孤儿 O，找所有条目 E 使 O 在 E 的 related 中（正向，已存在）——若无则为孤儿。
补法：找与 O 同 unit 且 related 中含 O 的"父"条目不存在时，改为在 O 自己的 related 里补同 unit 的核心/重要条目（双向化），
即 O.related 里的每个 id X，确保 X.related 也含 O。这是最保守的" reciprocity 补链"，不虚构新关系。"""
import json,os,glob,sys
from collections import defaultdict
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
byid={e["id"]:e for e in es}
gapfile=sys.argv[1] if len(sys.argv)>1 else "gaps_cycle3.json"
g=json.load(open(os.path.join(ROOT,"reports",gapfile),encoding="utf-8"))
orphans=g["orphan"]
# 现有 related 映射
rel={e["id"]:set(e.get("related",[])) for e in es}
added=[]
for o in orphans:
 if o not in byid: continue
 targets=[t for t in rel[o] if t in byid and o not in rel[t]]
 if not targets: continue
 # 在目标的L2覆盖层里补 o 到 related
 for t in targets:
  p=os.path.join(LD,t+".json")
  if not os.path.exists(p):
   # 从 seed 建一个最小覆盖层
   seed=next(e for e in json.load(open(os.path.join(D,"entries.json"),encoding="utf-8"))["entries"] if e["id"]==t)
   ov={"id":t,"level":"L1","related":list(seed.get("related",[]))+[o]}
  else:
   ov=json.load(open(p,encoding="utf-8"))
   ov["related"]=list(dict.fromkeys(ov.get("related",byid[t].get("related",[]))+[o]))
  json.dump(ov,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
  added.append((t,o))
print("reciprocal links added",len(added))
for a,b in added[:40]: print(" ",a,"->",b)
