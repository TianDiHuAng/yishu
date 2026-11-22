# -*- coding: utf-8 -*-
"""Cycle26 收尾：D029 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D029 — 重大发现：Wikidata API 一直处于「静默限流」状态；新建限速+缓存客户端
- **事实**：本轮直接 curl 批量接口得到纯文本响应「You are making too many requests to the API...」。
  而此前所有 `curl_json` 只接受以 `{` 开头的响应，遇到这段文本就返回 None —— **于是限流被当成「无数据」**。
  这解释了 Cycle22 的「desc cached 0」、pass2 的批量失效，以及若干「no_match」究竟是真空还是限流。
- **决定**：
  1. 新建 `tools/wd_api.py`：正确 User-Agent（含用途与联系）、**串行限速 1 秒**、429 指数退避（5/15/45/90 秒）、
     磁盘缓存（`data/_cache/wd/`）、返回 `(data, err)` 元组，**绝不把限流当作空结果**。
  2. 后续所有 Wikidata 访问一律走该客户端，禁止再写裸 curl + 宽松判定。
- **效果**：用新客户端重跑中文标签锚定，187 个实体信息 **187/187 成功、0 错误**（此前为 0/90）；
  精确命中 2 条 + 近似 29 条，经人工确认采纳 20 条、拒绝 5 组。
- **拒绝记录（人工确认为误配）**：minimalism→『计算哲学』/论文；polyphony→学术论文；symphony→Sarah Brightman 专辑；
  pipa→日本琵琶/馆藏器物/古诗；china-music-history→两个同名空描述实体无法区分。
- **可逆方式**：删除 wd-anchor-* 与覆盖层引用；客户端可保留（无害且加速）。
- **代价**：限速后全量核验变慢（约 1 请求/秒）；已用缓存缓解。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle26","date":"2026-11-22","status":"completed",
 "gap_methods":["中文标签锚定 pass4","Wikidata 客户端重构"],"network":"partial: wikidata ok (rate-limited, now throttled+cached)",
 "new_entries":0,"upgrades":0,"reviews":70,"fixes":1,
 "finding":"Wikidata API 长期静默限流：纯文本 429 响应被旧 curl_json 当作空数据",
 "entity_pass4":{"tested":70,"precise":2,"near":29,"adopted":20,"rejected_groups":5},
 "new_sources":20,"sources_total":261,"anchors_total":54,
 "check_result":"errors=0","check_links_result":"broken=0(176页)","audit_all":"7/7 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle26","date":"2026-11-22","methods_used":["中文标签锚定","客户端重构"],
 "gaps_found":{"anchors":20},"network":"partial (throttled)",
 "verdict":"发现并修复静默限流；锚点 34→54；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle26"' not in t:
    block=('if cyc=="cycle26":\n'
           '    L.append("- 本轮**发现一个一直存在的静默故障**：直接 curl Wikidata 批量接口返回纯文本'
           '「You are making too many requests」，而旧代码只接受以 { 开头的响应 → **限流被当成「无数据」**，'
           '解释了此前多轮「批量缓存为 0」与部分 no_match。已新建 tools/wd_api.py（正确 UA、串行限速 1 秒、'
           '指数退避、磁盘缓存、返回 (data, err)），重跑中文标签锚定：187 个实体 **187/187 成功、0 错误**。'
           '结果：精确命中 2 条、近似 29 条，**人工确认采纳 20 条**（锚点 34→**54**），并拒绝 5 组误配'
           '（minimalism→计算哲学、polyphony→论文、symphony→Brightman 专辑、pipa→日本琵琶、'
           'china-music-history→两个空描述同名实体）。来源 241→261，站点 176 页。")\n')
    anchor='if cyc=="cycle25":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 25 已完成** → 下轮 **Cycle 26**",
              "- 当前轮次：**Cycle 26 已完成** → 下轮 **Cycle 27**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")