# -*- coding: utf-8 -*-
"""修复 DECISIONS.md 中 D025 被 bash 反引号吞掉的「决定」行。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"DECISIONS.md")
lines=io.open(P,encoding="utf-8").read().split("\n")
for i,ln in enumerate(lines):
    if ln.startswith("- **决定**： 新增第一步"):
        lines[i]=("- **决定**：在 audit_all.py 的 STEPS 最前面加入一个特殊项，"
                  "对 tools 目录下全部 Python 文件执行 py_compile 编译检查；"
                  "任一文件语法错误即整轮体检失败（返回码 1），结果写入 reports/audit_all.json。")
        print("fixed line",i+1)
io.open(P,"w",encoding="utf-8").write("\n".join(lines))
print("done")