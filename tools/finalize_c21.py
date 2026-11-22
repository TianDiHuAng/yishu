# -*- coding: utf-8 -*-
"""Cycle21 收尾：D024 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEC=os.path.join(ROOT,"DECISIONS.md")
io.open(DEC,"a",encoding="utf-8").write("""
## D024 — Cycle21：作品尺寸/材质/藏品号入档（但**不写入正文**）+ 日本/印度建筑暂不建
- **决定**：
  1. 通过 Wikidata 取得 5 个作品条目的**尺寸（P2048/P2049）、材质（P186）、藏品编号（P217）**，作为【已复核·Wikidata】登记在各自"待核实"节；**不写入正文**。理由：这组数据目前**只有单一结构化来源**（Wikidata），未达 TASK 的双源互证标准，写在正文即等于单源断言。
  2. 已登记日本建筑（Q1422874）、印度建筑（Q61050）两个 Wikidata 实体作为来源，但**本轮不建条目**：现有 `enc-japanese-art` / `enc-indian-art` 页面此刻不可复核是否含建筑章节，若据此写"木构/出檐"或"石窟/窣堵坡"等特征即为无源断言。
- **理由**：TASK 明言"作品年份、尺寸、收藏地必须核对，这类信息最容易写错；查不到的不写"。本轮拿到的是可靠数值，但仍需克制——**能查证 ≠ 可以单源写入**。
- **可逆方式**：从 5 个 `data/l2/*.json` 的待核实中删除对应句子即可；两条建筑来源可留作下轮基础。
- **代价**：站点正文暂不显示尺寸（读者需在待核实节查看），略有不便，但保持了"正文断言必双源"的一致性。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle21","date":"2026-11-22","status":"completed",
 "gap_methods":["作品事实扩核(Wikidata P2048/P2049/P186/P217)","A类建筑实体预登记"],
 "network":"partial: wikidata ok; 内容来源不可达",
 "new_entries":0,"upgrades":0,"reviews":5,"fixes":5,
 "new_sources":2,"sources_total":207,
 "facts_added":{"mona-lisa":"79.4×53.4cm INV779/MR316","starry-night":"73.7×92.1cm 472.1941",
   "birth-of-venus":"172.5×278.5cm 00158551","sistine-ceiling":"4093×1341cm fresco",
   "guernica":"349×776cm DE00050"},
 "note":"尺寸等仅登记于待核实，不写入正文（单一来源，未达双源）",
 "check_result":"errors=0","check_links_result":"broken=0(174页)","audit_all":"6/6 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle21","date":"2026-11-22","methods_used":["作品事实扩核"],
 "gaps_found":{"facts_filled":5},"network":"partial",
 "verdict":"5 作品尺寸/材质/藏品号入档（待核实）；日本/印度建筑实体已登记但不建条；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle21"' not in t:
    block=('if cyc=="cycle21":\n'
           '    L.append("- 本轮特别说明：用 Wikidata 补齐 **5 个作品条目的尺寸/材质/藏品编号**'
           '（蒙娜丽莎 79.4×53.4cm、INV 779/MR 316；星夜 73.7×92.1cm、472.1941；维纳斯的诞生 172.5×278.5cm、00158551；'
           '西斯廷天顶 4093×1341cm；格尔尼卡 349×776cm、DE00050），这正是 TASK 提示"最容易写错"的信息。'
           '但**只登记在待核实节、不写入正文**——该组数据仅有一个结构化来源，未达双源互证标准。'
           '另登记日本建筑(Q1422874)/印度建筑(Q61050)实体，但**本轮不建条目**：现有日/印艺术页此刻无法复核是否含建筑章节，'
           '据此写木构或石窟特征即属无源断言。")\n')
    anchor='if cyc=="cycle20":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 20（体检轮）已完成** → 下轮 **Cycle 21**",
              "- 当前轮次：**Cycle 21 已完成** → 下轮 **Cycle 22**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")