# -*- coding: utf-8 -*-
"""修正 entity_map：候选判定改为读实体自身的 zh/en 标签（而非搜索结果里的单语 label），
命中任一语言标签与标题规范化相等 + 描述含类型词 才算匹配。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","entity_map_c22.py"); s=io.open(P,encoding="utf-8").read()
old='''    cands=search(e["title"],"zh",6) or search(e["title"],"en",6)
    pick=None; alts=[]
    for qid,lbl,desc in cands:
        if norm(lbl)!=title_n: 
            alts.append((qid,lbl,desc)); continue
        d=(desc or "").lower()
        if any(w in d for w in words): pick={"qid":qid,"label":lbl,"desc":desc}; break
        alts.append((qid,lbl,desc))'''
new='''    cands=search(e["title"],"zh",6) or search(e["title"],"en",6)
    pick=None; alts=[]
    for qid,lbl,desc in cands:
        payload=(ent(qid) or {})
        qt=(payload.get("entities") or {}).get(qid) or {}
        labels={k:v["value"] for k,v in qt.get("labels",{}).items() if k in ("zh","en")}
        desc2=((qt.get("descriptions",{}).get("en") or {}).get("value") or desc or "")
        same=any(norm(v)==title_n for v in labels.values()) or norm(lbl)==title_n
        d=desc2.lower()
        if same and any(w in d for w in words):
            pick={"qid":qid,"label":(labels.get("zh") or labels.get("en") or lbl),"desc":desc2[:60]}; break
        alts.append((qid,lbl,desc2))'''
assert old in s; s=s.replace(old,new)
io.open(P,"w",encoding="utf-8").write(s)
print("patched: entity-level label check")