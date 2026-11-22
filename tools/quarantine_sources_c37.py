# -*- coding: utf-8 -*-
"""Cycle37：来源库隔离（新增 R18 不变式）
把 sources.json 中未核验的 5 条移入 data/sources_quarantine.json（保留历史与原因），
使"来源库内全部 verified=true"成为可机器校验的不变式。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
sp=os.path.join(D,"sources.json"); sd=json.load(open(sp,encoding="utf-8"))
es=json.load(open(os.path.join(D,"site_entries.json"),encoding="utf-8"))["entries"]
used={s for e in es for s in e["sources"]}
bad=[s for s in sd["sources"] if not s["verified"]]
assert all(s["id"] not in used for s in bad), "存在被引用的未核验来源，不能隔离"
qp=os.path.join(D,"sources_quarantine.json")
q=json.load(open(qp,encoding="utf-8")) if os.path.exists(qp) else {"sources":[], "note":""}
q["note"]=("隔离区：记录「尝试过但当前不可核验」的来源，保留以备来源通道恢复后重新核验。"
           "这些来源**不得**被任何条目引用（check.py R18 强制）。")
have={s["id"] for s in q["sources"]}
for s in bad:
    if s["id"] not in have:
        rec=dict(s); rec["quarantine_reason"]=s.get("verified_note","未核验")
        q["sources"].append(rec)
sd["sources"]=[s for s in sd["sources"] if s["verified"]]
json.dump(sd,open(sp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
json.dump(q,open(qp,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
print("隔离 %d 条；来源库现有 %d 条（全部 verified）"%(len(bad),len(sd["sources"])))

# R18：来源库全部 verified + 引用必须存在于来源库
P=os.path.join(ROOT,"tools","check.py"); s=io.open(P,encoding="utf-8").read()
if "R18" not in s:
    anchor='    # R11 coverage一致'
    code='''    # R18 来源库不变式：库内全部 verified；被引用者必须在库内
    for x in S:
        if not x.get("verified"): err("R18",x.get("id","?"),"来源库含未核验来源（应移入 quarantine）")
    for e in ENTRIES:
        for sid in e.get("sources",[]):
            if sid not in sm and not any(q.get("id")==sid for q in []):
                err("R18",e["id"],"引用不在来源库:%s"%sid)
'''
    assert anchor in s
    s=s.replace(anchor, code+anchor, 1)
    io.open(P,"w",encoding="utf-8").write(s)
    print("R18 added to check.py")
else: print("R18 exists")