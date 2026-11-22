# -*- coding: utf-8 -*-
"""修正 DECISIONS.md 中 D014/D015 的顺序（按轮次）。"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"DECISIONS.md"); s=io.open(P,encoding="utf-8").read()
i15=s.index("## D015 —"); i14=s.index("## D014 —")
# i15 < i14 currently; swap blocks
b15=s[i15:i14]; b14=s[i14:]
# b14 runs to EOF (D014 is last) — verify
assert "D015" not in b14 and "D014" in b14
s=s[:i15]+b14.rstrip()+"\n\n"+b15.rstrip()+"\n"
io.open(P,"w",encoding="utf-8").write(s)
print("DECISIONS order fixed")
