# -*- coding: utf-8 -*-
"""Cycle74 收尾：D078 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D078 — Cycle74 中国陶瓷再补 4 条（244 → 248）；并把单元改名为「中国陶瓷工艺」以解决边界含混
- **先解决上轮遗留的边界问题**：上一轮新增的单元原称「陶瓷工艺」，但库内朝鲜/日本陶瓷仍在 `art-asia`、伊斯兰陶瓷在 `art-islamic`——名称暗示跨文化，实际只收中国。**改名为「中国陶瓷工艺」**（一处字符串），比强行搬动 5 个已有条目的 `unit` 字段更安全（避免再次做"文本手术"）。
- **决定**：新增 4 条中国陶瓷：
  1. `tang-tomb-guardian` 唐三彩镇墓兽（700年代初，92.3×43.8×41.9cm，**核心**）；
  2. `qingbai-silver-bowl` 青白瓷银扣碗（1100—1200s，8.2×14.5cm）；
  3. `ding-duck-bowl` 定窑鸭纹碗（1100s，20.3×5.4cm）；
  4. `chenghua-doucai-cup` 成化斗彩儿童纹杯（1465—87，高4.8cm，**核心**）。
- **四处「工艺决定形态」的证据**：
  1. **唐三彩镇墓兽的双重身份**：守墓辟邪并**防亡魂游荡**；但入墓前**曾由人抬着在街市游行**；随葬品同时是**孝道表达**与**财富权势展示**。
  2. **釉色在模仿别的材料**：深釉仿**黑漆**、青瓷比**绿玉**、青白瓷仿**银**；碗沿**宽银带**强化「贵重」；莲纹既指**佛教语境**也可能只是**宴会盛食**——两说并列。
  3. **定窑的因果链**：**倒置烧成 → 口沿无釉 → 便于金属包边**；釉流至足形成「**泪痕**」；上品曾被**北宋宫廷**选用。
  4. **斗彩＝两次烧成的分工**：先**钴蓝勾线**并烧成青花，**出窑后**在釉上填彩，**再烧一次**；线属第一道工序、色属第二道，故轮廓清晰。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源；单元名可改回。
- **代价**：4 条均单机构；中国陶瓷 8 条（唐、五代、宋、元、明），**清瓷与地方窑（磁州、吉州）仍缺**。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle74","date":"2026-11-23","status":"completed",
 "gap_methods":["中国陶瓷续深 + 单元边界整备"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["tang-tomb-guardian","qingbai-silver-bowl","ding-duck-bowl","chenghua-doucai-cup"],
 "unit_rename":"art-ceramics 标签: 陶瓷工艺 → 中国陶瓷工艺（解决与 art-asia/art-islamic 的边界含混）",
 "must_state":["唐三彩：守墓+出丧游行+孝道","釉色模仿材质（黑漆/绿玉/银）","定窑倒烧→无釉口沿→金属包边","斗彩=两次烧成的线/色分工"],
 "new_sources":4,"sources_total":379,"entries_total":248,"pages":285,
 "check_result":"errors=0","check_links_result":"broken=0(285页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle74","date":"2026-11-23","methods_used":["陶瓷续深","单元改名"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"中国陶瓷 4→8（总 248）；单元改名消边界含混；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle74"' not in t:
    block=('if cyc=="cycle74":\n'
           '    L.append("- 中国陶瓷再补 **4 条（244 → 248，陶瓷 4 → 8）**：唐三彩镇墓兽、青白瓷银扣碗、定窑鸭纹碗、成化斗彩杯。'
           '并先解决上轮遗留的**单元边界含混**：原称「陶瓷工艺」实际只收中国，而朝鲜/日本陶瓷在 `art-asia`、伊斯兰陶瓷在 `art-islamic`——'
           '**改名为「中国陶瓷工艺」**（改一处字符串，比搬动 5 个条目的 unit 字段安全）。'
           '四处「工艺决定形态」：①唐三彩镇墓兽既守墓辟邪、**入墓前曾由人抬着游街**，随葬品同时是**孝道与权势展示**；'
           '②**釉色在模仿别的材料**（深釉仿黑漆、青瓷比绿玉、青白瓷仿银），碗沿银带强化贵重，莲纹**佛教/宴饮两说并列**；'
           '③定窑**倒置烧成→口沿无釉→金属包边**，釉流成「泪痕」，上品曾为北宋宫廷所用；'
           '④**斗彩＝两次烧成的分工**：钴蓝勾线先烧，出窑后釉上填彩再烧，故线色分属两道工序。站点 281 → 285 页，体检 12/12。")\n')
    anchor='if cyc=="cycle73":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 244（L2 240 / L3 4 / L1 0） |","| 条目 | 248（L2 244 / L3 4 / L1 0） |"),
    ("| 来源 | 375（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 379（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 281，站内断链 **0** |","| 页面 | 285，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **244** | L2 240 / L3 4 / **L1 0** |","| 条目总数 | **248** | L2 244 / L3 4 / **L1 0** |"),
    ("| 来源库 | **375**（另 11 条预备来源未计入） |","| 来源库 | **379**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **281** |","| 站点页面 | **285** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])