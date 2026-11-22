# -*- coding: utf-8 -*-
"""Cycle16 收尾：状态与 REPORT。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle16","date":"2026-11-22","status":"completed",
 "gap_methods":["B5人物/作品事实核验(Wikidata)"],"network":"partial: wikidata ok (curl)",
 "new_entries":0,"upgrades":0,"reviews":6,"fixes":5,
 "person_verification":{"total":32,"with_wd_source":32,"mismatch":0},
 "work_verification":{"monet":"1840-1926","mona-lisa":"1503 创作 / 卢浮宫 / 达·芬奇"},
 "new_sources":28,"sources_total":202,"sources_verified":197,
 "fix_detail":"6条未匹配人物全部补齐(英文别名/类型词)；32人物均挂 Wikidata 来源；monet/mona-lisa 事实核验；修正5处QQ重复QID",
 "check_result":"errors=0","check_links_result":"broken=0(171页)","audit_all":"6/6 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle16","date":"2026-11-22","methods_used":["Wikidata人物/作品核验"],
 "gaps_found":{"date_conflicts":0},"network":"partial","verdict":"32/32人物生卒核验一致且已挂Wikidata来源；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle16"' not in t:
    block=('if cyc=="cycle16":\n'
           '    L.append("- 本轮特别说明：把 Cycle15 遗留的 6 条未匹配人物全部补齐（补英文别名检索与个别人物类型词，如 polymath），'
           '并为 **全部 32 个人物条目** 挂上 Wikidata 来源与【已复核·Wikidata】生卒留痕 → 人物 Wikidata 覆盖率 6→**32/32**，'
           '生卒年核验 **mismatch 0**；另核验 monet（1840—1926）与 mona-lisa（1503 创作、卢浮宫、达·芬奇）与条目一致；'
           '修正 5 处「QQ」重复 QID 的标题与 URL。来源 174→**202（verified 197）**，全库平均 2.46 来源/条。")\n')
    anchor='if cyc=="cycle15":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
else: print("exists")