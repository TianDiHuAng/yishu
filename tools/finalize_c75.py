# -*- coding: utf-8 -*-
"""Cycle75 收尾：D079 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D079 — Cycle75 中国陶瓷再补 4 条（248 → 252；陶瓷 8 → 12）
- **决定**：新增 `cizhou-toy-figurine`（磁州窑持瓶女俑，1100—1200s，19.7×9.5cm）、`transitional-square-bottle`（过渡期青花方瓶，1628—1722，高31.1cm）、`kangxi-lobed-vase`（康熙青花瓣瓶，20.4×12.2cm，**核心**）、`cizhou-floral-vase`（北宋磁州窑花卉纹瓶，900—1000s，高41.3cm）。
- **四处要点**：
  1. **磁州窑是「釉上彩先声」**：磁州窑**从不供御用**，只做日用器与陶俑（后者**被认为**是玩具）；该馆称其陶工是**中国最早在已烧成高温釉面上施釉上彩的一批人之一**——与景德镇斗彩/粉彩连成一条可追踪的技术线。
  2. **过渡期方瓶＝失去订单后的市场实验**：器形**源自欧洲杜松子酒瓶**，纹样为豹、麒麟、马等异兽；明末清初陶工**失去宫廷赞助**，转而寻找中外的**新客户**。
  3. **康熙青花的「绘画性」与一条跨藏品互证**：该馆指出康熙朝青花绘画性最高、画工可比专业画家；并提示读者看**同馆博纳尔《水果与果盘》（CMA 2020.100）**中的青花——「这样的瓷器出现在法国餐桌上，所受启发的正是此类中国青花」。条目**只照录该关联，不扩大其含义**（该馆只说「此类」，未指同一器形）。
  4. **磁州窑的「白」靠覆盖而非描绘**：化妆土与嵌白经烧成呈**象牙色**，露胎呈**肉桂褐**——装饰依赖**覆盖与暴露的色差**；这与定窑追求薄胎白釉的路径**不同**。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构；陶瓷 12 条覆盖唐至清与四个窑系（景德镇/龙泉/定/钧/磁州），**吉州窑、耀州窑与清后期外销瓷仍缺**。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle75","date":"2026-11-23","status":"completed",
 "gap_methods":["中国陶瓷续深"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["cizhou-toy-figurine","transitional-square-bottle","kangxi-lobed-vase","cizhou-floral-vase"],
 "ceramics_total":12,
 "must_state":["磁州窑为釉上彩先声","过渡期方瓶源自欧洲酒瓶形","康熙青花与博纳尔画中瓷器的跨藏品关联（不扩大）","磁州窑的「白」靠覆盖而非描绘"],
 "new_sources":4,"sources_total":383,"entries_total":252,"pages":289,
 "check_result":"errors=0","check_links_result":"broken=0(289页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle75","date":"2026-11-23","methods_used":["陶瓷续深"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"陶瓷 8→12（总 252）；跨藏品关联如实限定；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle75"' not in t:
    block=('if cyc=="cycle75":\n'
           '    L.append("- 中国陶瓷再补 **4 条（248 → 252，陶瓷 8 → 12）**：磁州窑持瓶女俑、过渡期青花方瓶、康熙青花瓣瓶、'
           '北宋磁州窑花卉纹瓶。四处要点：①磁州窑**从不供御用**，却可能是**中国最早在高温釉面上施釉上彩的一批人之一**'
           '（与斗彩/粉彩连成技术线）；陶俑「被认为」是玩具。②过渡期方瓶**器形源自欧洲杜松子酒瓶**、纹样为豹/麒麟/马，'
           '背景是**失去宫廷订单后寻找新客源**。③康熙青花绘画性最高、画工可比专业画家，并有一条**跨藏品互证**：'
           '该馆提示看同馆**博纳尔《水果与果盘》（2020.100）**中的青花——条目**只照录关联、不扩大含义**（「此类」非同一器形）。'
           '④磁州窑的「白」靠**化妆土覆盖与露胎的色差**（象牙 vs 肉桂褐），与定窑薄胎白釉路径不同。站点 285 → 289 页，体检 12/12。")\n')
    anchor='if cyc=="cycle74":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 248（L2 244 / L3 4 / L1 0） |","| 条目 | 252（L2 248 / L3 4 / L1 0） |"),
    ("| 来源 | 379（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 383（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 285，站内断链 **0** |","| 页面 | 289，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **248** | L2 244 / L3 4 / **L1 0** |","| 条目总数 | **252** | L2 248 / L3 4 / **L1 0** |"),
    ("| 来源库 | **379**（另 11 条预备来源未计入） |","| 来源库 | **383**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **285** |","| 站点页面 | **289** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])