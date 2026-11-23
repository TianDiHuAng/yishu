# -*- coding: utf-8 -*-
"""Cycle68 收尾：D072 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D072 — Cycle68 非洲再补 4 条（220 → 224）：殖民期"纪念品"与权力器物
- **决定**：新增 `vili-ivory-tusk`（维利象牙雕，约1900，17.8cm）、`asante-knife-sheath`（金鞘尖，1800s，8.7cm）、`yoruba-veranda-post`（埃基蒂推定，106.6cm）、`yoruba-ifa-necklace`（Ifá 占卜者项链，1900s，49.5cm）。
- **四处必须写进正文的内容**：
  1. **维利象牙雕的「为谁而作／表现了谁」分离**：委托方是**欧洲客户**（象牙为到访中非海岸的欧洲人所追捧的纪念品），但画面里是**刚果人自己**，衣着从**本地腰布**到**欧洲呢帽**并列。该馆明言这些虽是委托之作，也反映**艺术家选择要表现什么**——条目并列两侧，既不称其「纯正传统」，也不简单斥为「迎合市场」。
  2. **阿散蒂金鞘的制作垄断**：金体现 **kra（生命之力）**、是太阳在世间的对应物；**只有金匠行会成员**可为王室制作金饰。材料的珍贵与制作的垄断**共同**构成王权象征。
  3. **门廊柱＝社会秩序的可视化**：宫殿院落环以雕柱；骑马武士与跪姿女性为埃基蒂常见配对，"权力分配"因此被做成**可观看的结构**；该馆把武士拆为军事技能／智识／体能三层。**跪姿女性的含义该馆未展开，本条目不补写。**
  4. **Ifá 项链：装饰与法力不分离**：彩玻璃珠为仪式增辉、标示高地位；占卜者「像国王一样」权威源自 **òrún**；游走型占卜者随身携带带双袋的项链，**袋内缝入护身之物以确保法力**。**袋内成分属不宜公开的知识，本条目不追问。**
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构（`needs_verification`）；非洲 15 → **19 条**（贝宁2/Nok1/约鲁巴3/阿散蒂4/刚果5/埃塞4…），仍无撒哈拉以南其他大区（卢巴、方、祖鲁等检索无结果）。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle68","date":"2026-11-23","status":"completed",
 "gap_methods":["非洲余量推进"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["vili-ivory-tusk","asante-knife-sheath","yoruba-veranda-post","yoruba-ifa-necklace"],
 "africa_total":19,
 "must_state":["维利象牙雕：为欧洲客户而作却含自我再现","金鞘：kra + 行会垄断","门廊柱：权力分配的可视化（女性形象含义未展开）","Ifá 项链：袋内成分属不宜公开知识，不追问"],
 "new_sources":4,"sources_total":355,"entries_total":224,"pages":259,
 "check_result":"errors=0","check_links_result":"broken=0(259页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle68","date":"2026-11-23","methods_used":["非洲余量"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"非洲 15→19（总 224）；殖民期再现与不宜公开知识如实处理；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle68"' not in t:
    block=('if cyc=="cycle68":\n'
           '    L.append("- 非洲再补 **4 条（220 → 224，非洲 15 → 19）**：维利象牙雕、阿散蒂金鞘尖、约鲁巴门廊柱、Ifá 占卜者项链。'
           '四处内容照实处理：①**维利象牙雕**把「为谁而作／表现了谁」分开——委托方是**欧洲客户**，画面却是**刚果人自己**'
           '（衣着从本地腰布到欧洲呢帽并列），该馆称其虽为委托之作也反映艺术家**选择要表现什么**；'
           '②**金鞘**：金体现 **kra**、**只有行会**可为王室制金饰，材料珍贵与制作垄断**共同**构成王权象征；'
           '③**门廊柱**把「权力分配」做成可观看结构（武士拆为军事／智识／体能三层），**跪姿女性的含义该馆未展开，条目不补写**；'
           '④**Ifá 项链**装饰与法力不分离（珠光增辉＋袋内护身物），**袋内成分属不宜公开知识，条目不追问**。'
           '站点 255 → 259 页，体检 12/12。")\n')
    anchor='if cyc=="cycle67":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 220（L2 216 / L3 4 / L1 0） |","| 条目 | 224（L2 220 / L3 4 / L1 0） |"),
    ("| 来源 | 351（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 355（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 255，站内断链 **0** |","| 页面 | 259，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **220** | L2 216 / L3 4 / **L1 0** |","| 条目总数 | **224** | L2 220 / L3 4 / **L1 0** |"),
    ("| 来源库 | **351**（另 11 条预备来源未计入） |","| 来源库 | **355**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **255** |","| 站点页面 | **259** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])