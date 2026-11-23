# -*- coding: utf-8 -*-
"""Cycle69 收尾：D073（新增单元 + 4 乐器）+ METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D073 — Cycle69 直攻 B2 缺口：新增单元「乐器（跨文化）」+ 4 条（224 → 228，单元 26 → 27）
- **背景**：B2 类缺口最集中的一项是「**非西方音乐**」——此前音乐条目几乎全是西方体裁（中世纪至20世纪）加中国音乐史，**没有一件非西方乐器**。本轮改用「器物」路径：博物馆藏有可核验的乐器实物与其说明。
- **决定**：新增单元 **`music-instruments`（乐器·跨文化）**，并建 4 条：
  1. `kora-instrument` 科拉琴（西非，21弦葫芦竖琴—琉特，111.8cm）；
  2. `sitar-instrument` 西塔琴（东印度／孟加拉，约1850，95.2×15.3cm）；
  3. `guqin-instrument` 古琴（苏州张瑞修制，**1584**，123.5×18.1×4.5cm，**核心**）；
  4. `drum-ngoma` 恩戈马鼓（东非，40cm／径31.2cm）。
- **四处内容要点（全部据馆方说明）**：
  1. **西塔 vs 维纳的形制区分**：西塔有**可移动的金属品**，移位即变音高；本件小西塔的葫芦尺寸仿**鸵鸟蛋**（19世纪新奇做法），**主供陈列**、偶由女性或儿童演奏；孟加拉是装饰性乐器制作中心。
  2. **古琴是可核查的历史节点**：内款记为**严澂（1547—1625，虞山派创立者）**所作、**张瑞修**制；张氏名下仅十件、**本件纪年最早**。
  3. **科拉琴的「非原初状态」**：21弦已大量缺失；背面**针脚**显示葫芦多处裂缝曾被修补——它是**被长期使用并维修过的乐器**。
  4. **恩戈马鼓的双层蒙皮与「心」**：仅击第一层皮才共鸣；乌干达鼓内含**仅制作者知的仪式之「心」**；相对王室鼓 mpango，本件**不被视为神圣**——但本件是否含「心」**未记录**，条目不臆断。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除单元与 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构（`needs_verification`）；**乐器单元不等于音乐史补齐**——非西方音乐的**体裁与理论**（甘美兰的调律、印度拉格的程式）仍缺来源，只能靠器物侧证。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle69","date":"2026-11-23","status":"completed",
 "gap_methods":["以乐器实物攻 B2 非西方音乐缺口"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["kora-instrument","sitar-instrument","guqin-instrument","drum-ngoma"],
 "new_unit":"music-instruments","units_total":27,
 "b2_addressed":True,
 "must_state":["西塔可移动品+鸵鸟蛋新奇形制","古琴内款严澂与张瑞修（十件中最早）","科拉琴缺弦与修补痕（非原初状态）","恩戈马鼓双层蒙皮与「心」（本件是否含心未记录）"],
 "new_sources":4,"sources_total":359,"entries_total":228,"pages":264,
 "check_result":"errors=0","check_links_result":"broken=0(264页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle69","date":"2026-11-23","methods_used":["乐器实物路径"],
 "gaps_found":{"entries":4,"units":1},"network":"partial (museum APIs)",
 "verdict":"新增乐器单元+4条（228/27单元），B2 非西方音乐首次有实物覆盖；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle69"' not in t:
    block=('if cyc=="cycle69":\n'
           '    L.append("- **直攻 B2 缺口**：非西方音乐此前**零实物**，本轮改用「器物」路径，新增单元 **乐器（跨文化）** 与 4 条'
           '（224 → 228，单元 26 → 27）：西非**科拉琴**、东印度**西塔琴**、苏州**张瑞修制古琴（1584）**、东非**恩戈马鼓**。'
           '四处要点：①**西塔与维纳的区分**在**可移动金属品**，本件小西塔葫芦仿**鸵鸟蛋**、主供陈列（孟加拉为装饰乐器中心）；'
           '②**古琴是可核查的历史节点**——内款记为**严澂（虞山派创立者）**所作、张瑞修制，张氏名下仅十件而**本件纪年最早**；'
           '③**科拉琴已非原初状态**：21弦大量缺失、背面针脚显示葫芦裂缝曾被修补；'
           '④**恩戈马鼓**双层蒙皮仅击第一层即共鸣，乌干达鼓含**仅制作者知的仪式「心」**，而本件是否含「心」**未记录、不臆断**。'
           '站点 259 → 264 页，体检 12/12。")\n')
    anchor='if cyc=="cycle68":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 224（L2 220 / L3 4 / L1 0） |","| 条目 | 228（L2 224 / L3 4 / L1 0） |"),
    ("| 来源 | 355（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 359（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 259，站内断链 **0** |","| 页面 | 264，站内断链 **0** |"),
    ("| 单元 | 26（新增伊斯兰/非洲/美洲/太平洋） |","| 单元 | **27**（新增乐器·跨文化） |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **224** | L2 220 / L3 4 / **L1 0** |","| 条目总数 | **228** | L2 224 / L3 4 / **L1 0** |"),
    ("| 来源库 | **355**（另 11 条预备来源未计入） |","| 来源库 | **359**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **259** |","| 站点页面 | **264** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])