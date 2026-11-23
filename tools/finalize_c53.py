# -*- coding: utf-8 -*-
"""Cycle53 收尾：D056 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D056 — Cycle53 再补 5 条（190 → 195）：纳斯卡、朝鲜朝两件、占婆两件
- **决定**：继续按薄弱区块推进，新增：
  1. `nazca-trophy-head-bowl` 纳斯卡人首纹碗（约100—650，陶器施化妆土 10.2×10.2cm）；
  2. `joseon-hollyhock-cup` 朝鲜朝蜀葵形杯（15世纪，官窑瓷器，高3.6cm）；
  3. `joseon-hwarot-robe` 朝鲜朝婚礼袍（1800年代末，丝缎地平绣 114.3×174cm）；
  4. `champa-planetary-deity` 占婆行星神坐像（850—875，砂岩 86.5×37.5cm）；
  5. `champa-apsara-bracket` 占婆飞天托架（900年代，砂岩 55.9×53.3cm）。
- **四处「与直觉相反」的内容，均据该馆说明写入正文**：
  1. **婚礼袍不是奢华证明**：大量修补与拼补反映朝鲜朝女性对新儒学**俭约**审美的践行；领与袖的**厚白纸每嫁换新**、袍身沿数十年，说明它是可共享传承的**公共资源**。
  2. **蜀葵杯是政治器物**：蜀葵向阳→**忠君**；据该馆转述的朝鲜王室档案，用于国王赐酒的国宴与接待明使的茶礼；且与晚期「自然质朴」趣味形成**早期精整**的对照。
  3. **行星神与开光挂钩**：其护法身份不止泛泛，而与该寺**开光时行星与星辰正确排列**的具体仪式时点绑定。
  4. **纳斯卡人首母题同时指战争与丰产**：该馆以并列方式给出，条目照录不取舍。
- **两处保留馆方推测语气**：占婆飞天的建筑位置「可能为栏楯端头或天花托架」；莲蕾「可能」。
- **可逆方式**：删 5 条 overlay 与 catalog 元组、移除 5 条来源，重跑 `build_scope.py`。
- **代价**：5 条均单机构（`needs_verification`）；朝鲜朝与占婆各 2 条，纳斯卡 1 条，深度仍浅。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle53","date":"2026-11-23","status":"completed",
 "gap_methods":["薄弱区块推进（纳斯卡/朝鲜朝/占婆）"],"network":"partial: museum APIs ok",
 "new_entries":5,"new_entry_ids":["nazca-trophy-head-bowl","joseon-hollyhock-cup","joseon-hwarot-robe","champa-planetary-deity","champa-apsara-bracket"],
 "gaps_closed":["纳斯卡","朝鲜朝（瓷+服饰）","占婆（雕塑+建筑构件）"],
 "counterintuitive_findings":["婚礼袍以修补体现俭约、为共享资源","蜀葵杯为政治器物且见王室档案","行星神与开寺星象绑定"],
 "new_sources":5,"sources_total":337,"entries_total":195,"pages":230,
 "check_result":"errors=0","check_links_result":"broken=0(230页)","audit_all":"9/9 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle53","date":"2026-11-23","methods_used":["薄弱区块推进"],
 "gaps_found":{"entries":5},"network":"partial (museum APIs)",
 "verdict":"新增 5 条（195）；四处反直觉内容据馆方说明写入；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle53"' not in t:
    block=('if cyc=="cycle53":\n'
           '    L.append("- 再补 **5 条（190 → 195）**：纳斯卡人首纹碗、朝鲜朝蜀葵形杯、朝鲜朝婚礼袍、占婆行星神、占婆飞天托架。'
           '四处**与直觉相反**的内容据馆方说明写入正文：①婚礼袍**不是奢华证明**——大量修补拼补体现新儒学俭约，'
           '领袖厚白纸**每嫁换新**而袍身沿用数十年，是可共享的公共资源；②蜀葵杯向阳→**忠君**，'
           '据王室档案用于国王赐酒的国宴与接待明使的茶礼，并与晚期「自然质朴」形成早期精整的对照；'
           '③行星神的护法身份与该寺**开光时行星排列**的具体仪式时点绑定；④纳斯卡人首母题**同时指战争与丰产**（并列照录）。'
           '占婆飞天的建筑位置与莲蕾均保留馆方推测语气。站点 225 → 230 页，体检 9/9。")\n')
    anchor='if cyc=="cycle52":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 190（L2 184 / L3 6 / L1 0） |","| 条目 | 195（L2 189 / L3 6 / L1 0） |"),
    ("| 来源 | 332（全部 verified；隔离区 5 条不可核验） |","| 来源 | 337（全部 verified；隔离区 5 条不可核验） |"),
    ("| 页面 | 225，站内断链 **0** |","| 页面 | 230，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **190** | L2 184 / L3 6 / **L1 0** |","| 条目总数 | **195** | L2 189 / L3 6 / **L1 0** |"),
    ("| 来源库 | **332** |","| 来源库 | **337** |"),
    ("| 站点页面 | **225** |","| 站点页面 | **230** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])