# -*- coding: utf-8 -*-
"""Cycle64 收尾：D068 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D068 — Cycle64 北美再补 4 条（212 → 216）：覆盖 Tlingit / Navajo / Ancestral Pueblo / Inuit
- **决定**：重扫北美候选（35 件，含定居点、西北海岸、因纽特），新增 4 条：
  1. `tlingit-totem-pole` 特林吉特图腾柱（模型，约1880，彩绘木雕 189.2×8.8cm）；
  2. `navajo-biilee-dress` 纳瓦霍两片式女装 biil’éé（约1880—85，羊毛挂毯 145×99cm）；
  3. `sikyatki-jar` 西基亚茨基风格罐（祖先普韦布洛，1400—1600，21.2×38.8cm）；
  4. `inuit-devil-fish` 因纽特石版画《魔鬼鱼》（Peter Aliknak Banksland，1972，50.8×76.2cm）。
- **四处必须原样保留的内容**：
  1. **图腾柱是模型，且说明被截断**：本件是**小型模型柱**（室内存放故原色无损），曾属**银鲑氏族·渡鸦部落的说故事者**；柱上自下而上是陆獭 Kushda-Kaw → 其妻 → 化猫头鹰守望 → 陆獭埋伏惊扰路人 → 长须鲸载友出海。**馆方说明在柱顶处被截断**，本条目不补写柱顶形象。
  2. **女装不是「不变的传统」**：据当代织者 **D. Y. Begay** 转述，biil’éé 承载灵力、护佑、审美叙事与社会位置；同时该馆指出它**今天仍随时尚变化**、用于特殊场合。
  3. **陶器的「声」与「灵」**：Sikyatki 罐薄壁石磨故叩之成声；霍皮视**斑驳橙色**为「带生命与灵出窑」之征；该馆判断这类观念「**很可能**源自古远」——照录并标注为推断。
  4. **版画运动与强制定居同期**：因纽特石版画描绘传统的**同一时期**，「部落成员正被**加拿大政府强制迁入定居点**」。条目照录时间关系，**不就因果下判断**。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构（`needs_verification`）；北美累计 **8 条**（纳瓦霍 3、霍皮 2、特林吉特 1、祖先普韦布洛 1、因纽特 1），仍远不足以代表北美原住民的多样性（平原、东南、北极其余地区为零）。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle64","date":"2026-11-23","status":"completed",
 "gap_methods":["北美剩余候选筛选"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["tlingit-totem-pole","navajo-biilee-dress","sikyatki-jar","inuit-devil-fish"],
 "north_america_total":8,
 "must_state":["图腾柱为模型且说明截断（不补写柱顶）","biil'éé 仍在变化","陶器之声与带灵出窑（推断）","因纽特版画与强制定居同期（不判因果）"],
 "new_sources":4,"sources_total":347,"entries_total":216,"pages":251,
 "check_result":"errors=0","check_links_result":"broken=0(251页)","audit_all":"11/11 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle64","date":"2026-11-23","methods_used":["北美候选筛选"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"北美累计 8 条（总 216）；截断与同期背景如实处理；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle64"' not in t:
    block=('if cyc=="cycle64":\n'
           '    L.append("- 北美再补 **4 条（212 → 216）**，覆盖 **Tlingit / Navajo / 祖先普韦布洛 / Inuit**：图腾柱（模型）、'
           '纳瓦霍两片式女装 biil’éé、西基亚茨基风格罐、因纽特石版画《魔鬼鱼》。四处口径：'
           '①图腾柱是**小型模型**（室内存放故原色无损）且**馆方说明在柱顶被截断**，本条**不补写柱顶形象**；'
           '②biil’éé 并非「不变的传统」——据当代织者 Begay 转述它承载灵力与身份，同时**今天仍随时尚变化**；'
           '③Sikyatki 罐「叩之成声」，霍皮视斑驳橙为「带灵出窑」，该馆称观念「**很可能**源自古远」——照录为推断；'
           '④因纽特石版画描绘传统的**同一时期**「部落成员正被加拿大政府强制迁入定居点」，条目照录时间关系、'
           '**不就因果下判断**。北美累计 8 条，站点 247 → 251 页，体检 11/11。")\n')
    anchor='if cyc=="cycle63":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 212（L2 208 / L3 4 / L1 0） |","| 条目 | 216（L2 212 / L3 4 / L1 0） |"),
    ("| 来源 | 343（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 347（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 247，站内断链 **0** |","| 页面 | 251，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **212** | L2 208 / L3 4 / **L1 0** |","| 条目总数 | **216** | L2 212 / L3 4 / **L1 0** |"),
    ("| 来源库 | **343**（另 11 条预备来源未计入） |","| 来源库 | **347**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **247** |","| 站点页面 | **251** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])