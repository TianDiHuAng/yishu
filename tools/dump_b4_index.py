# -*- coding: utf-8 -*-
"""把站点的标题、概述、七节内容摘要dump给B4代理做读者问题覆盖分析。"""
import json, os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
es=json.load(open(os.path.join(ROOT,"data","site_entries.json"),encoding="utf-8"))["entries"]
# 紧凑索引：id/title/overview + 每节首60字
idx=[]
for e in es:
    sec=e.get("sections",{})
    sig=" | ".join("%s:%s"%(k,sec[k][:55]) for k in ["时代背景","风格特征","技法或形式分析"] if sec.get(k))
    idx.append({"id":e["id"],"title":e["title"],"tier":e["tier"],"overview":e["overview"][:110],"sig":sig[:220]})
for i in range(4):
    json.dump(idx,open(os.path.join(ROOT,"b4_site_index_%d.json"%i),"w",encoding="utf-8"),ensure_ascii=False,indent=0)
print("site index dumped, entries",len(idx))
