# -*- coding: utf-8 -*-
"""Cycle62：修 SVG 图示窄屏可读性。
现状：viewBox 760×300，标签 15px；在 320–600px 视口下缩放至 0.37–0.75，标签 5.5–11px，低于可读下限。
修法：窄屏改为**横向滚动 + 最小宽度**（宁滚动不缩到不可读），并把基础字号略增。
"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py"); s=io.open(P,encoding="utf-8").read()
if "@media (max-width:700px)" not in s:
    old=".svg-frame svg{width:100%;height:auto;display:block}"
    assert old in s
    new=(old+"\n"
      "@media (max-width:700px){.svg-frame{overflow-x:auto}.svg-frame svg{width:680px;min-width:680px;height:auto}}")
    s=s.replace(old,new,1)
# 字号略增（提高全宽度下的可读性）
s=s.replace(".svg-label{fill:var(--svg-text);font-family:var(--sans);font-size:15px;font-weight:600}",
            ".svg-label{fill:var(--svg-text);font-family:var(--sans);font-size:16px;font-weight:600}",1)
s=s.replace(".svg-sub{fill:var(--ink-soft);font-family:var(--sans);font-size:12px}",
            ".svg-sub{fill:var(--ink-soft);font-family:var(--sans);font-size:13px}",1)
io.open(P,"w",encoding="utf-8").write(s)
print("CSS patched")
import py_compile; py_compile.compile(P,doraise=True); print("compiled")
print("has media query:", "@media (max-width:700px)" in io.open(P,encoding="utf-8").read())