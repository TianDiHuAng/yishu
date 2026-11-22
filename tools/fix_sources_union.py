# -*- coding: utf-8 -*-
"""修复：①merge_l2 对 sources 采用并集（seed ∪ overlay），避免覆盖层漏写导致基础来源被丢弃；
②回填 5 个作品档案覆盖层的 sources（seed 两项 + wikidata）。"""
import io,os,json
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data"); LD=os.path.join(D,"l2")

# ① merge_l2 并集
P=os.path.join(ROOT,"tools","merge_l2.py"); s=io.open(P,encoding="utf-8").read()
old='''    merged[eid].update(ov)'''
new='''    base=list(merged[eid].get("sources",[]))
    merged[eid].update(ov)
    # 来源并集：覆盖层只增不删
    merged[eid]["sources"]=list(dict.fromkeys(base+list(ov.get("sources",[]))))'''
assert old in s, "merge anchor missing"
io.open(P,"w",encoding="utf-8").write(s.replace(old,new))
print("merge_l2: sources union applied")

# ② 回填覆盖层 sources
seed={e["id"]:e for e in json.load(open(os.path.join(D,"entries.json"),encoding="utf-8"))["entries"]}
for eid in ["starry-night","birth-of-venus-work","sistine-ceiling-work","guernica-work","rite-of-spring-work"]:
    p=os.path.join(LD,eid+".json"); o=json.load(open(p,encoding="utf-8"))
    base=list(seed[eid]["sources"]); cur=list(o.get("sources",[]))
    o["sources"]=list(dict.fromkeys(base+cur))
    json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
    print(" patched",eid,o["sources"])