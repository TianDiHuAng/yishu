# -*- coding: utf-8 -*-
"""Cycle20（体检轮）收尾：METRICS/SATURATION/REPORT/PROGRESS。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle20","date":"2026-11-22","status":"completed",
 "gap_methods":["F体检(九维,第三次)"],"network":"partial: wikidata ok; 内容来源不可达",
 "new_entries":0,"upgrades":0,"reviews":145,"fixes":2,
 "healthcheck":{"dead_links":0,"stale_data":"3处为已知误报","duplicates":0,"contradictions":0,
   "orphans":0,"overlap":"不可执行(内容来源不可达)","bad_anchors":0,"sitemap":"一致",
   "contrast":"全部≥AA","oneway_links":0,"cross_domain":2,"total_links":430},
 "wd_source_check":"抽样5条 URL 全部 HTTP 200；41 条 wd-* 全部 verified",
 "new_sources":0,"sources_total":205,"sources_verified":200,
 "tool_improvement":"healthcheck 精确化 overlap 原因 + 并入 link_audit 摘要",
 "check_result":"errors=0","check_links_result":"broken=0(174页)","audit_all":"6/6 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle20","date":"2026-11-22","methods_used":["F体检九维"],
 "gaps_found":{"structural":0},"network":"partial",
 "verdict":"体检全通过；修复2条新单向关联；未饱和（B2/A类缺口仍需来源）"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle20"' not in t:
    block=('if cyc=="cycle20":\n'
           '    L.append("- 本轮为**体检轮 F**（第三次）：九维全部通过——死链0 / 重复0 / 数据矛盾0 / 孤儿0 / 页内锚点0错 / sitemap 与实体页一致 / 对比度全部≥AA / 单向关联0 / 跨域仅2（浪漫主义跨媒介合法对）；'
           '过期数据规则命中3处经人工确认均为误报（存成语与断代用语）。'
           '**新增一项来源活性抽查**：41 条 Wikidata 来源全部 verified，抽样 5 条 URL 均返回 HTTP 200。'
           '**发现并修复 2 条新单向关联**（gothic-architecture→gothic、romanesque-architecture→romanesque），修复后单向归零、关联总数 430。'
           '另改进体检工具：把「来源重合度不可执行」的原因写精确（内容来源不可达、Wikidata 无正文），并把关联图摘要并入输出。")\n')
    anchor='if cyc=="cycle19":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 19 已完成** → 下轮 **Cycle 20（体检轮）**",
              "- 当前轮次：**Cycle 20（体检轮）已完成** → 下轮 **Cycle 21**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")