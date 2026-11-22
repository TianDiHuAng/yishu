# -*- coding: utf-8 -*-
"""修复 gen_site.py 中 known-gaps 字符串被换行截断的问题。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py")
lines=io.open(P,encoding="utf-8").read().split("\n")
# 找到 _arch 行索引，重写其后 4 行
idx=None
for i,l in enumerate(lines):
    if l.strip().startswith("_arch=sum(1 for e in entries"):
        idx=i; break
assert idx is not None, "_arch line not found"
new_block=[
 '    _arch=sum(1 for e in entries if "建筑" in e["medium"].split(","))',
 '    s.append("<p>已知缺口（诚实披露）：①A 类覆盖缺口 58 项，建筑已开工 %d 条，其余待可核验来源；"%_arch',
 '             +"②B2 类候选缺口 22 项（非西方音乐体裁在站内零覆盖）；③部分条目「待核实」项仍待第二来源；"',
 '             "④Wikipedia / Met / Tate 在当前构建环境不可达，内容类来源无法即时复核。</p>")',
]
# 原块 = idx 开始共 4 行（_arch + 3 行）
lines[idx:idx+4]=new_block
io.open(P,"w",encoding="utf-8").write("\n".join(lines))
print("block rewritten at line",idx+1)
import py_compile
try:
    py_compile.compile(P,doraise=True); print("py_compile OK")
except Exception as e:
    print("py_compile FAIL:",e)