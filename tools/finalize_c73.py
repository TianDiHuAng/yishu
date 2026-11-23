# -*- coding: utf-8 -*-
"""Cycle73 收尾：D077（新增陶瓷单元 + 4 条）+ METRICS/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D077 — Cycle73 中国陶瓷长期缺位：新增单元「陶瓷工艺」+ 4 条（240 → 244，单元 27 → 28）
- **背景**：中国绘画与书法都有专单元，但**中国陶瓷此前几乎空白**（仅有高丽/朝鲜/伊斯兰陶瓷与仰韶彩陶）。检索得 45 件可写件，本轮取 4 件覆盖四个窑系。
- **决定**：新增单元 **`art-ceramics`（陶瓷工艺）**，并建：
  1. `yuan-blue-white-jar` 元青花狮耳罐（景德镇，1300s，39.4×37.5cm，**核心**）；
  2. `longquan-export-bowl` 龙泉窑模印大碗（1300—1400s，15.1×42cm）；
  3. `ding-tea-bowl` 定窑「邢式」白瓷碗（907—960，4.7×18.5cm）；
  4. `jun-numbered-bulb-bowl` 钧窑数字款钵（1400s 初，23.5×8cm）。
- **四处「技术与制度」内容**：
  1. **元青花的钴料来自伊朗**（很可能卡尚）；**云肩凤凰**母题在**伊儿汗伊朗装饰艺术**中同样存在——器物是跨蒙古帝国**双向交流**的证物，不是单向传入。
  2. **龙泉大碗的尺寸即市场**：窑工掌握**巨形器**烧造，主运**中东**，用于**食物置于围坐者中央**的宴会形制。
  3. **茶色决定釉色**：唐人饮**红茶**、以为**淡青或白釉**最显茶色；宋代**末茶**流行后**转为深釉茶碗**；同类碗另**远销萨马拉（伊拉克）**。
  4. **钧窑数字款是尺寸序列**（「一」最大、「十」最小，本件为「二」）；内壁**蚯蚓走泥纹**为烧成开裂所致，外壁**紫调来自铜呈色**。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除单元与 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构；陶瓷单元 4 条，尚未纳入朝鲜/日本陶瓷（现有条目在 art-asia 内），**单元边界需在后续统一**。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle73","date":"2026-11-23","status":"completed",
 "gap_methods":["中国陶瓷缺位填补"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["yuan-blue-white-jar","longquan-export-bowl","ding-tea-bowl","jun-numbered-bulb-bowl"],
 "new_unit":"art-ceramics","units_total":28,"candidates":45,
 "must_state":["元青花钴料自伊朗（很可能卡尚）","龙泉尺寸即中东宴会市场","茶色决定釉色（唐→宋转向）","钧窑数字款＝尺寸序列；蚯蚓走泥纹与铜呈紫"],
 "new_sources":4,"sources_total":375,"entries_total":244,"pages":281,
 "note":"陶瓷单元与 art-asia 内的朝鲜/日本陶瓷边界待统一",
 "check_result":"errors=0","check_links_result":"broken=0(281页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle73","date":"2026-11-23","methods_used":["中国陶瓷填补"],
 "gaps_found":{"entries":4,"units":1},"network":"partial (museum APIs)",
 "verdict":"新增陶瓷单元+4条（244/28单元）；技术与制度关系入正文；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle73"' not in t:
    block=('if cyc=="cycle73":\n'
           '    L.append("- **中国陶瓷长期缺位**（仅仰韶彩陶与高丽/朝鲜/伊斯兰陶瓷），检索得 45 件可写件，本轮新增单元 **陶瓷工艺** 与 4 条'
           '（240 → 244，单元 27 → 28）：元青花狮耳罐、龙泉模印大碗、定窑白瓷碗、钧窑数字款钵。四处「技术与制度」：'
           '①**元青花的钴料来自伊朗**（很可能卡尚），**云肩凤凰**在伊儿汗装饰艺术中同样存在——器物是**双向交流**的证物；'
           '②**龙泉的尺寸即市场**：掌握巨形器烧造，主运**中东**，服务「食物置于围坐者中央」的**宴会形制**；'
           '③**茶色决定釉色**——唐人红茶宜**淡青/白釉**，宋代**末茶**流行后转**深釉**；同类碗另远销**萨马拉（伊拉克）**；'
           '④**钧窑数字款是尺寸序列**（本件「二」），内壁**蚯蚓走泥纹**为烧成开裂、外壁**紫调来自铜呈色**。'
           '并记录一处待统一：陶瓷单元与 art-asia 内的朝鲜/日本陶瓷边界。站点 276 → 281 页，体检 12/12。")\n')
    anchor='if cyc=="cycle72":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 240（L2 236 / L3 4 / L1 0） |","| 条目 | 244（L2 240 / L3 4 / L1 0） |"),
    ("| 来源 | 371（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 375（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 276，站内断链 **0** |","| 页面 | 281，站内断链 **0** |"),
    ("| 单元 | **27**（新增乐器·跨文化） |","| 单元 | **28**（新增陶瓷工艺） |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **240** | L2 236 / L3 4 / **L1 0** |","| 条目总数 | **244** | L2 240 / L3 4 / **L1 0** |"),
    ("| 来源库 | **371**（另 11 条预备来源未计入） |","| 来源库 | **375**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **276** |","| 站点页面 | **281** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])