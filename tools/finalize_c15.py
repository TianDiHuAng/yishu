# -*- coding: utf-8 -*-
"""Cycle15 收尾：更新 METRICS/SATURATION，并补 REPORT 说明（脚本方式，避免反引号问题）。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle15","date":"2026-11-22","status":"completed",
 "gap_methods":["B5/Wikidata人物核验"],"network":"partial: wikidata ok via curl; urllib DNS unstable",
 "new_entries":0,"upgrades":0,"reviews":32,"fixes":0,
 "person_verification":{"confirmed":26,"mismatch":0,"no_match":6},
 "new_sources":0,
 "check_result":"errors=0","check_links_result":"broken=0(171页)","audit_all":"6/6 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle15","date":"2026-11-22","methods_used":["Wikidata人物核验"],
 "gaps_found":{"dataconflicts":0},"network":"partial",
 "verdict":"32人物核验：26一致/0矛盾/6消歧未过；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle15"' not in t:
    block=('if cyc=="cycle15":\n'
           '    L.append("- 本轮特别说明：用 Wikidata 对全部 32 个人物条目做生卒年交叉核验'
           '（要求描述含人物类型词且生年与条目 when 相差≤2 才接受，同名实体一律拒绝）：'
           '**confirmed 26 / mismatch 0 / no_match 6**。即凡能与权威结构化数据对齐者生卒年全部一致，未发现年份错误；'
           '6 条为消歧未过（实体缺中文标签或抓取抖动），已拒绝强行匹配，明细见 reports/person_dates_c15.md。'
           '本轮未据此改动任何条目（无差异可改）。")\n')
    anchor='if cyc=="cycle14":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
else:
    print("report block exists")