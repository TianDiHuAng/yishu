# -*- coding: utf-8 -*-
"""放宽人物消歧：中文检索的前3名中，若 description 含人物类型词 且 生年与条目 when 相差≤2，
即接受（生年+类型双闸已足够区分同名实体）；否则仍拒绝。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","person_dates_c15.py")
s=io.open(P,encoding="utf-8").read()
old='''    cands=search(e["title"],"zh",6) or search(e["title"],"en",6)'''
new='''    cands=search(e["title"],"zh",6)
    used_lang="zh"
    if not cands:
        cands=search(e["title"],"en",6); used_lang="en"'''
assert old in s; s=s.replace(old,new)
old2='''        if tmatch and kmatch and near:'''
new2='''        rank=cands.index((qid,lbl,desc))
        strict_ok = tmatch and kmatch and near
        loose_ok = (used_lang=="zh") and rank<3 and kmatch and (by is not None and wy and abs(by-wy[0])<=2)
        if strict_ok or loose_ok:'''
assert old2 in s; s=s.replace(old2,new2)
io.open(P,"w",encoding="utf-8").write(s)
print("relaxed rule applied")