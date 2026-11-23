# -*- coding: utf-8 -*-
"""Cycle46 收尾：D049 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D049 — Cycle46 补正 scope 遗漏：新增单元「伊斯兰艺术」+ 5 条目（166 → 171，单元 22 → 23）
- **发现**：`scope.md` 的权威大纲并集包含 **AP Art History（O3）**，其地理范围明确含**伊斯兰艺术**；但条目标单里**一条也没有**，覆盖矩阵里也没有对应行——这不是「缺口被判定为不适用」，而是**当初搭建清单时漏掉了**。属**补正**而非扩张。
- **决定**：新增单元 **`art-islamic`（伊斯兰艺术·西亚中亚）**，并建 1 条单元导览 + 4 条器物实例：
  1. `islamic-art` 伊斯兰艺术（导览，4 个来源）；
  2. `wade-cup` 韦德杯（伊朗塞尔柱，1200—1221，黄铜嵌银，人物化铭文 + 黄道十二宫）；
  3. `mihrab-isfahan` 伊斯法罕祈祷龛（陶瓷马赛克，290.7×245.3cm，thuluth 铭文）；
  4. `iznik-dish-artichokes` 伊兹尼克洋蓟纹大盘（约1535—40，fritware 釉下彩）；
  5. `nishapur-figural-bowl` 尼沙布尔人物纹碗（900年代，萨珊金属器母题）。
- **两处「馆方自己不确定」如实处理**：
  - **祈祷龛**：该馆断代写「约1500年代**或**1900年代中期」，本条目**不裁定**，明确说明它更适合当作「萨法维风格的祈祷龛实例」而不是「16世纪标准器」；
  - **韦德杯**：该馆文化栏写「塞尔柱时期（1037—1194）」，断代却为1200—1221，**二者不能同时成立**，条目并列而不调和。
- **导览条目的写法**：不写通史，只把四件藏品当「可核验节点」，所有概括都注明「据该馆说明」；并声明「伊斯兰艺术作为统一范畴本身在学界有争议，未取得两方材料」。
- **可逆方式**：删 5 条 overlay 与 catalog 元组、移除单元与 4 条来源；`build_scope.py` 重跑。
- **代价**：5 条均单机构（`needs_verification`）；新增 1 个单元使单元数由 22 变 23，`units.html`、sitemap 与矩阵随之变化（已重生成并校验）。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle46","date":"2026-11-23","status":"completed",
 "gap_methods":["scope 漏项排查（对照 AP 地理范围）"],"network":"partial: museum APIs ok",
 "new_entries":5,"new_entry_ids":["islamic-art","wade-cup","mihrab-isfahan","iznik-dish-artichokes","nishapur-figural-bowl"],
 "new_unit":"art-islamic","units_total":23,
 "finding":"scope 并集含 AP Art History（含伊斯兰艺术），但清单遗漏该门类——属补正非扩张",
 "date_discrepancies":[{"wade-cup":"文化栏塞尔柱1037–1194 vs 断代1200–1221"},
   {"mihrab-isfahan":"约1500年代或1900年代中期（馆方未裁定）"}],
 "new_sources":4,"sources_total":316,"entries_total":171,"pages":203,
 "check_result":"errors=0","check_links_result":"broken=0(203页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle46","date":"2026-11-23","methods_used":["scope漏项排查"],
 "gaps_found":{"entries":5,"units":1,"note":"伊斯兰艺术整门类此前遗漏"},"network":"partial (museum APIs)",
 "verdict":"新增伊斯兰艺术单元+5条（171/23单元）；两处馆方断代矛盾已如实标注；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle46"' not in t:
    block=('if cyc=="cycle46":\n'
           '    L.append("- **发现 scope 漏项**：并集所引 AP Art History（O3）的地理范围明确含**伊斯兰艺术**，'
           '但条目标单一条也没有、矩阵里也没有对应行——属当初搭建清单时的**遗漏**，本轮作补正（非扩张）：'
           '新增单元 **伊斯兰艺术** 与 5 条（1 条导览 + 4 件器物：韦德杯、伊斯法罕祈祷龛、伊兹尼克洋蓟纹大盘、尼沙布尔人物纹碗），'
           '条目 166 → **171**、单元 22 → **23**。'
           '两处「馆方自己不确定」如实标注：祈祷龛断代写「约1500年代**或**1900年代中期」，条目明确不当作16世纪标准器；'
           '韦德杯文化栏（塞尔柱1037–1194）与断代（1200–1221）**互相矛盾**，并列而不调和。'
           '导览条目不写通史，只把四件藏品当可核验节点。站点 197 → 203 页，体检 8/8。")\n')
    anchor='if cyc=="cycle45":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 166（L2 160 / L3 6 / L1 0） |","| 条目 | 171（L2 165 / L3 6 / L1 0） |"),
    ("| 来源 | 312（全部 verified；隔离区 5 条不可核验） |","| 来源 | 316（全部 verified；隔离区 5 条不可核验） |"),
    ("| 页面 | 197，站内断链 **0** |","| 页面 | 203，站内断链 **0** |"),
    ("| 单元 | 22 |","| 单元 | 23（新增伊斯兰艺术） |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **166** | L2 160 / L3 6 / **L1 0** |","| 条目总数 | **171** | L2 165 / L3 6 / **L1 0** |"),
    ("| 来源库 | **312** |","| 来源库 | **316** |"),
    ("| 站点页面 | **197** |","| 站点页面 | **203** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])