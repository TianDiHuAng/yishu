# -*- coding: utf-8 -*-
"""Cycle60 收尾：usable 审计接入 audit_all（第 11 步）+ 让脚本在有问题时返回 1。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# 1) 脚本补退出码
U=os.path.join(ROOT,"tools","usability_c60.py"); u=io.open(U,encoding="utf-8").read()
if "sys.exit" not in u:
    u=u.replace("import json,os,glob,re","import json,os,glob,re,sys",1)
    u=u.rstrip()+"\nsys.exit(1 if tot else 0)\n"
    io.open(U,"w",encoding="utf-8").write(u); print("exit code added")
# 2) 接入 audit_all
A=os.path.join(ROOT,"tools","audit_all.py"); a=io.open(A,encoding="utf-8").read()
if "usability_c60.py" not in a:
    old=' ("invariants_c54.py（不变式盘点：死重/孤儿/L3/单元页）","tools/invariants_c54.py"),'
    assert old in a
    a=a.replace(old,old+'\n ("usability_c60.py（可用性：标题层级/锚点/表格/link）","tools/usability_c60.py"),')
    io.open(A,"w",encoding="utf-8").write(a); print("audit_all: usability step added")
import py_compile
for f in (U,A): py_compile.compile(f,doraise=True)
print("compiled")