# -*- coding: utf-8 -*-
"""Cycle54 补修：audit_all 的汇总行漏算 fails_compile（退出码正确、打印错误）。
修法：汇总打印包含编译失败，并单列；同时写入 json 的 fails 字段保持一致。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","audit_all.py"); s=io.open(P,encoding="utf-8").read()
old='''print("失败项：%d"%fails)'''
new='''_total=fails+fails_compile
print("失败项：%d（其中工具编译失败 %d）"%(_total,fails_compile))'''
assert old in s
s=s.replace(old,new)
s=s.replace('json.dump({"steps":summary,"fails":fails+ (1 if fails_compile else 0)}','json.dump({"steps":summary,"fails":_total,"fails_compile":fails_compile}')
io.open(P,"w",encoding="utf-8").write(s)
print("summary line fixed")
import py_compile; py_compile.compile(P,doraise=True); print("compiled")