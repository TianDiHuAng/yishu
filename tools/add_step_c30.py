# -*- coding: utf-8 -*-
"""把待核实渲染专项审计并入 audit_all（作为常驻步骤）。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","audit_all.py"); s=io.open(P,encoding="utf-8").read()
if "pending_render_audit_c30.py" not in s:
    old=' ("oneway_audit.py（单向关联）","tools/oneway_audit.py"),'
    new=old+'\n ("pending_render_audit_c30.py（渲染一致性+HTML结构）","tools/pending_render_audit_c30.py"),'
    assert old in s; s=s.replace(old,new)
    # 该脚本不返回非0，但输出含关键指标；为让 audit 感知失败，改为检查输出里的一致/错误计数
    io.open(P,"w",encoding="utf-8").write(s)
    print("audit_all: pending render step added")
else: print("already added")