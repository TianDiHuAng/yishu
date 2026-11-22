# -*- coding: utf-8 -*-
"""Cycle28（体检轮）收尾：D031 + METRICS/SATURATION/REPORT/PROGRESS/BACKLOG。"""
import json,os,io
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D031 — Cycle28 体检发现并修复：sitemap 硬编码导致新页漏收
- **事实**：体检九维中「sitemap 与实体页一致」一项报 **2 页未收录**（entities.html、status.html）。原因是 `build_sitemap()` 里写死了 7 个根页面，Cycle22/25 新增的页面没进去。
- **决定**：改为**自动收录**站点根目录下全部 `.html`（`glob`），配合已有的 units/entries 子目录枚举；sitemap 由 174 → **176** 条，unlisted=0、missing=0。
- **理由**：这类"新增页面忘记登记"的缺陷靠人工很难持续盯住，交给生成器自动发现才可靠。此前几轮体检都报"一致"，是因为当时确实没有新增根页面——**体检的价值恰恰在于新内容引入后能立刻抓到回归**。
- **附带修复**：作品尺寸说明里的「该组数据**目前**只有一个来源」触发"过期数据"规则误报，改为中性表述；stale 由 6 回到 3（3 处为已知成语/断代误报）。
- **可逆方式**：改回硬编码列表（不建议）。
- **代价**：sitemap 会收录任何根目录 html（若将来放临时页需注意排除）。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle28","date":"2026-11-22","status":"completed",
 "gap_methods":["F体检(第五次)"],"network":"partial: wikidata ok",
 "new_entries":0,"upgrades":0,"reviews":145,"fixes":2,
 "healthcheck":{"audit":"7/7","dead":0,"duplicates":0,"contradictions":0,"orphans":0,
   "bad_anchors":0,"sitemap_unlisted":"2 → 0（已修）","stale":"6 → 3（余为已知误报）",
   "contrast":"AA","oneway":0,"cross_domain":2,"total_links":430},
 "liveness":{"wd_sources":102,"http_200":102,"failed":0},
 "fix_detail":"sitemap 改为自动收录根目录 html（+2页）；尺寸说明去掉「目前」消除误报",
 "check_result":"errors=0","check_links_result":"broken=0(176页)","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle28","date":"2026-11-22","methods_used":["F体检","来源活性"],
 "gaps_found":{"sitemap_missing":2},"network":"partial",
 "verdict":"体检抓到 sitemap 漏收 2 页并修复；102/102 来源活性 200；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle28"' not in t:
    block=('if cyc=="cycle28":\n'
           '    L.append("- 本轮为**体检轮 F**（第五次），七项检查通过，但抓到**一个真实回归**：'
           '「sitemap 与实体页一致」报 **2 页未收录**（entities.html、status.html）——'
           '根因是 build_sitemap 里写死了根页面列表，Cycle22/25 新增的页面没进去。'
           '已改为**自动收录根目录全部 html**，sitemap 174→176 条、unlisted=0、missing=0。'
           '另修一处自造噪音：尺寸说明中的「目前」触发过期数据规则，stale 6→3（余 3 为已知误报）。'
           '来源活性：**102 条 Wikidata 来源 102/102 返回 HTTP 200**。")\n')
    anchor='if cyc=="cycle27":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

PROG=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PROG,encoding="utf-8").read()
s2=s2.replace("- 当前轮次：**Cycle 27 已完成** → 下轮 **Cycle 28（体检轮）**",
              "- 当前轮次：**Cycle 28（体检轮）已完成** → 下轮 **Cycle 29**")
io.open(PROG,"w",encoding="utf-8").write(s2)
print("done")