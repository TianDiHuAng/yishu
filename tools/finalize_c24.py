# -*- coding: utf-8 -*-
"""Cycle24（体检轮）收尾：METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle24","date":"2026-11-22","status":"completed",
 "gap_methods":["F体检(七项)","来源活性全量核验"],"network":"partial: wikidata ok",
 "new_entries":0,"upgrades":0,"reviews":145,"fixes":0,
 "healthcheck":{"audit_steps":"7/7","dead_links":0,"duplicates":0,"contradictions":0,"orphans":0,
   "bad_anchors":0,"sitemap":"一致","contrast":"AA","oneway":0,"cross_domain":2},
 "liveness":{"wd_sources":76,"http_200":76,"failed":0},
 "check_result":"errors=0","check_links_result":"broken=0(175页)","audit_all":"7/7 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle24","date":"2026-11-22","methods_used":["F体检","来源活性"],
 "gaps_found":{"structural":0},"network":"partial",
 "verdict":"体检七项全通过；76 条 Wikidata 来源全量 200；未饱和（内容缺口仍待来源）"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle24"' not in t:
    block=('if cyc=="cycle24":\n'
           '    L.append("- 本轮为**体检轮 F**（第四次）：`audit_all` **7/7 全通过**'
           '（含 py_compile 守卫：112 个工具文件无语法错误）、死链0、重复0、数据矛盾0、孤儿0、'
           '页内锚点0错、sitemap 与实体页一致、对比度全部≥AA、单向关联0、跨域2（合法）。'
           '另做**来源活性全量核验**：全部 **76 条 Wikidata 来源**逐个 curl，**76/76 返回 HTTP 200**、0 失败——'
           '这是比“记录里写着 verified”更硬的证据。内容来源（Wikipedia/Met/Tate）仍不可达，'
           '故 A 类建筑剩余、B2 音乐地区空白、B5 剩 5 项继续挂起。")\n')
    anchor='if cyc=="cycle23":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 23 已完成** → 下轮 **Cycle 24（体检轮）**",
              "- 当前轮次：**Cycle 24（体检轮）已完成** → 下轮 **Cycle 25**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")