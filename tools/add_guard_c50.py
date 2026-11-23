# -*- coding: utf-8 -*-
"""Cycle50 收尾：①清掉最后一个 overview 载者；②新增 overlay_guard（覆盖层不得携带基础字段）；
③把 guard 接入 audit_all。"""
import io,json,os,glob
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
D=os.path.join(ROOT,"data")
BASE=["title","kind","unit","era","region","medium","tier","def","when","overview"]
# ① 清理
for p in glob.glob(os.path.join(D,"l2","*.json")):
    o=json.load(open(p,encoding="utf-8"))
    hit=[k for k in BASE if k in o]
    if hit:
        for k in hit: del o[k]
        json.dump(o,open(p,"w",encoding="utf-8"),ensure_ascii=False,indent=1)
        print("cleaned",o.get("id"),hit)

# ② guard
G=os.path.join(ROOT,"tools","overlay_guard.py")
io.open(G,"w",encoding="utf-8").write('''# -*- coding: utf-8 -*-
"""R20 守卫：覆盖层（data/l2/*.json）**不得**携带基础字段——基础字段的唯一真值是 tools/catalog.py。
若出现，说明有人又在覆盖层里改基础信息，会导致 catalog 与全站不一致（历史上的 when/overview 漂移即由此而来）。
返回码 1 表示违规。"""
import json,os,glob,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
BASE=["title","kind","unit","era","region","medium","tier","def","when","overview"]
bad=[]
for p in sorted(glob.glob(os.path.join(ROOT,"data","l2","*.json"))):
    o=json.load(open(p,encoding="utf-8"))
    hit=[k for k in BASE if k in o]
    if hit: bad.append((os.path.basename(p),hit))
print("overlay_guard: 违规 %d 个文件%s"%(len(bad),(" → %s"%bad[:5]) if bad else ""))
sys.exit(1 if bad else 0)
''')
print("guard written")

# ③ 接入 audit_all
A=os.path.join(ROOT,"tools","audit_all.py"); a=io.open(A,encoding="utf-8").read()
if "overlay_guard.py" not in a:
    old=' ("pending_render_audit_c30.py（渲染一致性+HTML结构）","tools/pending_render_audit_c30.py"),'
    assert old in a
    a=a.replace(old,old+'\n ("overlay_guard.py（覆盖层不得改基础字段）","tools/overlay_guard.py"),')
    io.open(A,"w",encoding="utf-8").write(a); print("audit_all: guard added")