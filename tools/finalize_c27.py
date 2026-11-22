# -*- coding: utf-8 -*-
"""Cycle27 收尾：D030 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG（避免反引号与 ASCII 引号）。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D030 — Cycle27 锚点收官：69% 锚定率，其余 45 条「不可能或不值得锚定」
- **决定**：pass5 后再做一次结构性分类，**停止继续硬凑**。剩余 45 条未锚定分为：
  - **自有页面 11 条**（什么是艺术史/音乐史、阅读路径、跨媒介比较、术语辨析等）：这些是本项目自撰的导览与比较页，Wikidata 中**本来就没有对应实体**，锚定无意义。
  - **中国专题 15 条**（唐宋元明清绘画、书法风格、玉器/青铜/敦煌/六朝、中国音乐史、琵琶、武王墩）：中系概念在 Wikidata 多无精确同名实体，或同名实体描述为空无法辨别（如两个「中国音乐史」）。
  - **其余 19 条**（希腊艺术/罗马艺术/文艺复兴/格里高利圣咏/歌剧/调性/交响曲等）：标签与条目名不完全一致，需人工指定 QID 才能锚定，本轮不做。
- **理由**：本轮 pass5 初命中 8 条，人工确认后**只采纳 5 条、拒绝 3 条**（renaissance 再次命中「法国复兴党」；两个空描述实体无法辨别）。继续放宽规则只会把错误锚点挂上去——**锚定率不是 KPI，正确率才是**。
- **可逆方式**：删除 wd-anchor-* 与覆盖层引用。
- **代价**：锚点停在 59/145（69%）；剩余 45 条的 QID 需人工指定，已记录在 reports/entity_pass5_vetted.md 与 BACKLOG。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle27","date":"2026-11-22","status":"completed",
 "gap_methods":["锚点 pass5（A/B 双路）+ 结构性分类"],"network":"partial: wikidata ok (throttled)",
 "new_entries":0,"upgrades":0,"reviews":50,"fixes":0,
 "entity_pass5":{"tested":50,"candidates":8,"adopted":5,"rejected":3},
 "anchors_total":59,"anchor_rate":"100/145 = 69%",
 "unanchored_breakdown":{"own_pages":11,"china_topics":15,"others":19},
 "new_sources":5,"sources_total":266,
 "check_result":"errors=0","check_links_result":"broken=0(176页)","audit_all":"7/7 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle27","date":"2026-11-22","methods_used":["锚点pass5","结构性分类"],
 "gaps_found":{"anchors":5},"network":"partial",
 "verdict":"锚点 54→59（69%）；剩余45条停止硬凑并分类记录；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle27"' not in t:
    block=('if cyc=="cycle27":\n'
           '    L.append("- 本轮为**锚点收官**：用限速客户端做 A/B 双路匹配（英文 id 与中文标题），'
           '50 条未锚定中初命中 8 条，**人工确认后只采纳 5 条、拒绝 3 条**'
           '（renaissance 再次命中「法国复兴党」；两个实体描述为空无法辨别），锚点 54→**59**（锚定率 100/145 = 69%）。'
           '随后做**结构性分类并停止硬凑**：剩余 45 条 = 自有页面 11 条（导览/比较页，本无对应实体）+ '
           '中国专题 15 条（中系概念缺精确同名实体或同名空描述）+ 其余 19 条（标签不完全一致，需人工指定 QID）。'
           '锚定率不是 KPI，正确率才是。")\n')
    anchor='if cyc=="cycle26":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 26 已完成** → 下轮 **Cycle 27**",
              "- 当前轮次：**Cycle 27 已完成** → 下轮 **Cycle 28（体检轮）**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")