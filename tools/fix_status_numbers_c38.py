# -*- coding: utf-8 -*-
"""Cycle38 修正：status.html 两处硬编码改动态/更新。
①「建筑已开工 N 条」→ 从数据统计 medium 含"建筑"的条目数；
② 硬规则范围 R1–R17 → R1–R18。
"""
import io,os
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","gen_site.py"); s=io.open(P,encoding="utf-8").read()
old='''    s.append("<p>已知缺口（诚实披露）：①A 类覆盖缺口 58 项，建筑已开工 3 条，其余待可核验来源；"'''
new='''    _arch=sum(1 for e in entries if "建筑" in e["medium"].split(","))
    s.append("<p>已知缺口（诚实披露）：①A 类覆盖缺口 58 项，建筑已开工 %d 条，其余待可核验来源；"%_arch+"'''
assert old in s, "gap line anchor missing"
s=s.replace(old,new)
s=s.replace("<p>每次构建前运行 <code>tools/audit_all.py</code>：硬规则（R1–R17）",
            "<p>每次构建前运行 <code>tools/audit_all.py</code>：硬规则（R1–R18）")
io.open(P,"w",encoding="utf-8").write(s)
print("status numbers dynamic")
chk=io.open(P,encoding="utf-8").read()
print("R1–R18:", "R1–R18" in chk, "| dynamic arch:", "_arch=sum" in chk)