# -*- coding: utf-8 -*-
"""Cycle32 收尾：D035 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D035 — Cycle32 中国专题别名锚定：锚定率 79% → 81%，否决 11 条并逐条记明口径
- **决定**：为 15 条中国专题条目试中文**同义别名**检索（宋代绘画→宋朝绘画、琵琶→乐器、敦煌→莫高窟等），**采纳 4 条、拒绝 11 条**。
- **采纳（口径精确匹配）**：
  - `ming-painting` → **Q6864640『Ming dynasty painting』**（"overview of Ming dynasty painting"）—— 与条目口径完全一致
  - `xieyi` → **Q10894988『xieyi painting』**（"style of painting"）
  - `china-music-history` → **Q277393『music of China』**
  - `pipa` → **Q6685124『pipa』（"Chinese plucked lute"）** —— 终于拿到中国琵琶乐器，而非此前命中的日本 biwa/古诗/馆藏器物
- **否决（逐条记明，避免"看似相近"）**：唐代绘画→『Tang dynasty art』偏宽；扬州/宋/元/清绘画与绘画史仅有论文或单件藏品；仰韶彩陶→『Yangshao culture』偏宽；玉器/青铜器仅有材质门类或铭文；敦煌艺术→『Mogao Caves』是遗址；魏晋南北朝→是历史时期；武王墩→是墓葬遗址。
- **可逆方式**：删除对应 wd-anchor-* 与覆盖层引用。
- **代价**：仍余 27 条未锚定（自有页 11 + 中国专题 11 + 早前被拒 5），已记录。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle32","date":"2026-11-22","status":"completed",
 "gap_methods":["中国专题别名锚定(pass7)"],"network":"partial: wikidata ok",
 "new_entries":0,"upgrades":0,"reviews":15,"fixes":0,
 "entity_pass7":{"tested":15,"adopted":4,"rejected":11},
 "anchors_total":77,"anchor_rate":"118/145 = 81%",
 "new_sources":4,"sources_total":284,
 "liveness_sample":"4/4 HTTP 200",
 "check_result":"errors=0","check_links_result":"broken=0(176页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle32","date":"2026-11-22","methods_used":["中国别名锚定"],
 "gaps_found":{"anchors":4},"network":"partial",
 "verdict":"锚定 73→77（81%）；11 条逐条记明否决理由；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle32"' not in t:
    block=('if cyc=="cycle32":\n'
           '    L.append("- 本轮针对 15 条中国专题条目试**中文同义别名**检索，**采纳 4 条、拒绝 11 条**，'
           '锚定率 79%→**81%（118/145）**。采纳的都是口径严丝合缝者：'
           'ming-painting→Q6864640『Ming dynasty painting』、xieyi→Q10894988『xieyi painting』、'
           'china-music-history→Q277393『music of China』、pipa→Q6685124『pipa』（Chinese plucked lute，'
           '终于不是日本 biwa/古诗/馆藏器物）。'
           '11 条否决理由逐条写进 reports/entity_pass7_vetted.md：唐代绘画→Tang dynasty art 偏宽、'
           '敦煌艺术→Mogao Caves 是遗址、魏晋南北朝→是历史时期、玉器/青铜器→仅材质门类等。'
           '活性抽样 4/4 HTTP 200。")\n')
    anchor='if cyc=="cycle31":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 31 已完成** → 下轮 **Cycle 32**",
              "- 当前轮次：**Cycle 32 已完成** → 下轮 **Cycle 33（体检轮）**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")