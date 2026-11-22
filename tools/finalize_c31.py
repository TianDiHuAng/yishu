# -*- coding: utf-8 -*-
"""Cycle31 收尾：D034 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D034 — Cycle31 人工指定 QID：锚定率 69% → 79%，并确立「口径一致」否决标准
- **决定**：为 D030 列出的 19 条「其余」未锚定条目**人工指定英文检索词**（如 'Romanesque art'、'Renaissance art'、'tonal system'），逐个检索并核对口径后：**采纳 14 条、拒绝 5 条**。锚定率 100/145 → **114/145 = 79%**。
- **采纳要点**（口径匹配的例子）：
  - `romanesque` → **Q46805『Romanesque art』**（艺术风格，非建筑）——正好补上 Cycle23 拒绝 Q46261『Romanesque architecture』时的缺口。
  - `tonality` → **Q192822『tonal system』**（对应条目的「大小调体系」）。
  - `gregorian-chant` → Q26473；`opera` → Q1344；`20th-century-classical` → Q1338153；`minimalism-music` → Q572901『minimalist music』；`zen-painting` → Q8069073『Zenga』。
- **否决标准（新明确）**：实体与条目**口径必须一致**，宽或窄都拒：
  - `buddhist-art-india` ← Q1001041『Buddhist art』（泛佛教艺术，比"印度佛教艺术"宽）→ 拒
  - `paleolithic-sculpture` ← Q755548『art of the Paleolithic』（比"旧石器雕塑"宽）→ 拒
  - `realism-art`、`symphony` → 检索到的都是论文/专辑，无对应实体 → 拒
  - `khmer-art` → Q109016942 描述为空 → 拒（沿用"空描述不采信"规则）
- **可逆方式**：删除对应 wd-anchor-* 与覆盖层引用。
- **代价**：仍有 31 条未锚定（自有页 11 + 中国专题 15 + 上述 5 条），已记录。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle31","date":"2026-11-22","status":"completed",
 "gap_methods":["人工指定QID（pass6）"],"network":"partial: wikidata ok",
 "new_entries":0,"upgrades":0,"reviews":19,"fixes":0,
 "entity_pass6":{"tested":19,"adopted":14,"rejected":5},
 "anchors_total":73,"anchor_rate":"114/145 = 79%",
 "new_sources":14,"sources_total":280,
 "liveness_sample":"5/5 HTTP 200",
 "check_result":"errors=0","check_links_result":"broken=0(176页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle31","date":"2026-11-22","methods_used":["人工指定QID"],
 "gaps_found":{"anchors":14},"network":"partial",
 "verdict":"锚定 59→73（79%）；确立口径一致否决标准；剩余31条记录在案；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle31"' not in t:
    block=('if cyc=="cycle31":\n'
           '    L.append("- 本轮按 D030 的待办做**人工指定 QID**：为 19 条「其余」未锚定条目手工给出英文检索词，'
           '逐个检索并核对口径，**采纳 14 条、拒绝 5 条**，锚定率 **69% → 79%（114/145）**。'
           '亮点：romanesque 终于锚到 **Q46805『Romanesque art』**（艺术风格，而非 Cycle23 被拒的『建筑』实体）；'
           'tonality → Q192822『tonal system』对应「大小调体系」。'
           '并确立**口径一致**否决标准：宽（Buddhist art 对印度佛教艺术、Paleolithic art 对旧石器雕塑）'
           '或窄（法国巴洛克音乐）、或描述为空，一律拒绝。活性抽样 5/5 HTTP 200。")\n')
    anchor='if cyc=="cycle30":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 30（体检轮）已完成** → 下轮 **Cycle 31**",
              "- 当前轮次：**Cycle 31 已完成** → 下轮 **Cycle 32**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")