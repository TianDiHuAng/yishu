# -*- coding: utf-8 -*-
"""Cycle58 收尾：D062 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D062 — Cycle58 泰/越窑口**确认无可用对象**，转而补埃塞俄比亚与阿散蒂（200 → 204）
- **探测结果（换用更具体的检索词后）**：
  - **泰国**（sukhothai / sawankhalok / si satchanalai / thai celadon）：**0 件**符合条件（culture 字段需含 Thai/Sukhothai 等，且说明 >250 字符）；
  - **越南**（vietnamese jar / le dynasty / chu dau / bat trang）：**0 件**；
  - **埃塞俄比亚**（ethiopian cross / manuscript / icon / lakai）：**2 件**历史时期作品可用；
  - 因此泰、越**继续零覆盖**，本轮不再勉强凑数，如实记入未覆盖清单。
- **新增 4 条**：
  1. `ethiopian-gospel-leaf` 福音书页（圣路加，约1440—1480，犊皮纸墨与蛋彩 37×25cm，吉兹文题记）；
  2. `ethiopian-diptych` 十二使徒与圣保罗双联画（约1700，贡德尔推定，蛋彩木胎 39×51cm）；
  3. `asante-goldweight` 阿散蒂鱼形金衡砝码（1800年代，铜合金 2.8×6.6×0.4cm）；
  4. `asante-soul-disc` 阿散蒂灵魂圆盘 akrafokɔnmu（1800年代/1871前，金 7×7.6×1.6cm）。
- **四处值得记录的内容**：
  1. **埃塞俄比亚的"早"**：该馆称基督教**300年代**传入埃塞俄比亚，**远早于北欧**——这为「埃塞俄比亚基督教艺术独立于欧洲中世纪」提供了一条可引用依据；题记为吉兹文（该馆称其为教会语言）。
  2. **双联画的地方化**：使徒穿的竟是**自印度输入的时髦衣料**；面容与发型各自区别，姿态与着装却统一以强调群体身份；该馆并把吉兹文描述为「可追溯至公元前400年代」的语言（**照录并注明是该馆说法**）。
  3. **砝码即谚语**：阿散蒂衡金砝码的具象图像多指涉谚语，「恰当使用谚语」被视为明智者的标志——度量工具同时是修辞装置。
  4. **圆盘与断裂**：akrafokɔnmu 关联 kradware（为国王「清洗灵魂」的官员）；形制**很可能受北非伊斯兰金币**启发；且这类金饰制作**中断直至1924年**，当代官员改佩较大圆盘——「传统」经历过断裂与再造。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构（`needs_verification`）；非洲由 9 条升至 13 条，但**泰/越/东南亚陶瓷仍缺口**。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle58","date":"2026-11-23","status":"completed",
 "gap_methods":["定向检索（泰/越/埃塞）"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["ethiopian-gospel-leaf","ethiopian-diptych","asante-goldweight","asante-soul-disc"],
 "confirmed_unavailable":["泰国素可泰/宋加洛窑","越南李陈窑"],
 "notable":["埃塞俄比亚300年代接受基督教（早于北欧）","双联画中印度输入衣料","砝码即谚语","金饰生产中断至1924年"],
 "new_sources":4,"sources_total":335,"entries_total":204,"pages":239,
 "check_result":"errors=0","check_links_result":"broken=0(239页)","audit_all":"10/10 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle58","date":"2026-11-23","methods_used":["定向检索"],
 "gaps_found":{"entries":4,"confirmed_unavailable":2},"network":"partial (museum APIs)",
 "verdict":"埃塞俄比亚+阿散蒂 4 条（204）；泰/越确认不可得；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle58"' not in t:
    block=('if cyc=="cycle58":\n'
           '    L.append("- 换具体检索词重试**泰/越窑口：确认无可用对象**（泰国 sukhothai/sawankhalok/si satchanalai、'
           '越南 le dynasty/chu dau/bat trang 均 0 件），不再勉强凑数，如实记入未覆盖清单。'
           '转而新增 **4 条（200 → 204）**：埃塞俄比亚福音书页（圣路加，约1440—80，吉兹文题记）与十二使徒双联画（约1700）；'
           '阿散蒂鱼形金衡砝码与灵魂圆盘 akrafokɔnmu。四处内容值得记：①该馆称基督教**300年代**传入埃塞俄比亚「远早于北欧」；'
           '②双联画中使徒穿**自印度输入的时髦衣料**，且吉兹文被该馆描述为「可追溯至公元前400年代」；'
           '③阿散蒂砝码的具象图像多指涉**谚语**，恰当使用谚语被视为明智者——度量工具同时是修辞装置；'
           '④灵魂圆盘形制**很可能受北非伊斯兰金币**启发，且此类金饰制作**中断直至1924年**——「传统」经历过断裂与再造。'
           '站点 235 → 239 页，体检 10/10。")\n')
    anchor='if cyc=="cycle57":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 200（L2 196 / L3 4 / L1 0） |","| 条目 | 204（L2 200 / L3 4 / L1 0） |"),
    ("| 来源 | 331（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 335（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 235，站内断链 **0** |","| 页面 | 239，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **200** | L2 196 / L3 4 / **L1 0** |","| 条目总数 | **204** | L2 200 / L3 4 / **L1 0** |"),
    ("| 来源库 | **331**（另 11 条预备来源未计入） |","| 来源库 | **335**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **235** |","| 站点页面 | **239** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])