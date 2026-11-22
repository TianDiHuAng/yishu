# -*- coding: utf-8 -*-
"""在 audit_all 里加"全部工具可编译"检查：对 tools/*.py 执行 py_compile，
任何语法错误立即暴露（防再次提交损坏的生成器）。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","audit_all.py"); s=io.open(P,encoding="utf-8").read()
old='STEPS=[\n ("check.py（R1-R17 硬规则）","tools/check.py"),'
new=('import glob,py_compile\n'
     '_bad=[]\n'
     'for _p in sorted(glob.glob(os.path.join(ROOT,"tools","*.py"))):\n'
     '    try: py_compile.compile(_p,doraise=True)\n'
     '    except Exception as _e: _bad.append((os.path.basename(_p),str(_e)[:80]))\n'
     'STEPS=[\n ("py_compile（全部工具可编译）", "__COMPILE__"),\n ("check.py（R1-R17 硬规则）","tools/check.py"),')
assert old in s; s=s.replace(old,new)
# 在循环里处理 __COMPILE__
old2='for name,script in STEPS:\n    p=os.path.join(ROOT,script)'
new2=('for name,script in STEPS:\n'
      '    if script=="__COMPILE__":\n'
      '        summary.append({"step":name,"status":"ok" if not _bad else "FAIL",\n'
      '                        "tail":"%d 个 .py 全部通过"%len(glob.glob(os.path.join(ROOT,"tools","*.py"))) if not _bad else str(_bad[:3])})\n'
      '        if _bad: fails_compile=1\n'
      '        continue\n'
      '    p=os.path.join(ROOT,script)')
assert old2 in s; s=s.replace(old2,new2)
s=s.replace("summary=[]\nfails=0","summary=[]\nfails=0\nfails_compile=0")
s=s.replace('print("失败项：%d"%fails)','print("失败项：%d"%fails)')  # 保持
s=s.replace('json.dump({"steps":summary,"fails":fails}','json.dump({"steps":summary,"fails":fails+ (1 if fails_compile else 0)}')
s=s.replace('sys.exit(1 if fails else 0)','sys.exit(1 if (fails or fails_compile) else 0)')
io.open(P,"w",encoding="utf-8").write(s)
print("audit_all: compile check added")