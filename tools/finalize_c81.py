# -*- coding: utf-8 -*-
"""Cycle81 收尾：D085 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D085 — Cycle81 印度绘画再补 4 条（268 → 272；印度绘画 8）
- **决定**：新增 `jagat-singh-portrait`（努尔普尔王肖像，约1619，**核心**）、`murad-bakhsh-jewel`（穆拉德·巴赫什肖像宝石，约1635）、`utka-nayika`（等待的女主人公，帕哈里，约1800）、`maru-ragini`（马鲁·拉吉尼，1650—80）。
- **四处要点**：
  1. **一幅肖像成为政治证据**：贾加特·辛格是**西喜马拉雅山小王国王子**，成长于贾汉吉尔与努尔·贾汉的宫廷；**山国贵族在莫卧儿宫廷任职极罕见**，故此像属**罕见的帝国级绘画**；1624 年他参与**推翻皇帝的叛乱**，**王后为其斡旋**。
  2. **「肖像宝石」与贸易准入缠绕**：穆拉德小像**画面仅 4.3×3.5 厘米**，原本**嵌于宝石座**供家族与支持者佩戴；该风尚起于 **1616 年托马斯·罗爵士**向莫卧儿皇帝呈递**英国肖像细密画与浮雕宝石**之时，**同年他谈成了英国进入印度港口**。
  3. **情绪靠身体语言**：`utka-nayika` 以**紧张手势与不安双足**写焦虑，而非面部表情；并给出**帕哈里时代特征**——淡雅色彩、远景城市、**长腿大眼与圆头比例**。
  4. **Ragamala 的地域标记**：`maru-ragini` 的调式**基于拉贾斯坦民歌**，当地故事主角**以骆驼为坐骑**——骆驼因此不只是坐骑，而是**调式的地域标记**。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构；印度绘画 8 条（拉杰普特/梅瓦尔/帕哈里/莫卧儿），**德干画派与公司画（Company painting）仍缺**。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle81","date":"2026-11-23","status":"completed",
 "gap_methods":["印度绘画续深"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["jagat-singh-portrait","murad-bakhsh-jewel","utka-nayika","maru-ragini"],
 "indian_paintings":8,
 "must_state":["山国贵族在莫卧儿宫廷之罕与1624斡旋","肖像宝石4.3×3.5cm+1616英国赠礼与港口准入","焦虑靠手势与双足","骆驼=调式的地域标记"],
 "new_sources":4,"sources_total":403,"entries_total":272,"pages":309,
 "check_result":"errors=0","check_links_result":"broken=0(309页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle81","date":"2026-11-23","methods_used":["印度绘画续深"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"印度绘画 4→8（总 272）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle81"' not in t:
    block=('if cyc=="cycle81":\n'
           '    L.append("- 印度绘画再补 **4 条（268 → 272，印度绘画 8）**：努尔普尔王肖像（约1619）、穆拉德·巴赫什「肖像宝石」、'
           '帕哈里《乌特卡·纳伊卡》（约1800）、《马鲁·拉吉尼》（1650—80）。四处要点：①**一幅肖像成为政治证据**——'
           '山国贵族在莫卧儿宫廷任职**极罕见**，故属**稀有帝国级绘画**；1624 年该王公参与**推翻皇帝的叛乱**、**王后为其斡旋**；'
           '②**「肖像宝石」与贸易准入缠绕**——小像仅 **4.3×3.5 厘米**、原嵌宝石座佩戴，风尚起于 **1616 年英国使节呈赠细密画与浮雕宝石**，'
           '**同年谈成英人进入印度港口**；③等待的女主人公以**紧张手势与不安双足**写焦虑，并给出**帕哈里长腿大眼圆头**的时代比例；'
           '④《马鲁·拉吉尼》的调式**基于拉贾斯坦民歌**，当地故事主角**骑骆驼**——骆驼成为**调式的地域标记**。站点 305 → 309 页，体检 12/12。")\n')
    anchor='if cyc=="cycle80":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 268（L2 264 / L3 4 / L1 0） |","| 条目 | 272（L2 268 / L3 4 / L1 0） |"),
    ("| 来源 | 399（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 403（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 305，站内断链 **0** |","| 页面 | 309，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **268** | L2 264 / L3 4 / **L1 0** |","| 条目总数 | **272** | L2 268 / L3 4 / **L1 0** |"),
    ("| 来源库 | **399**（另 11 条预备来源未计入） |","| 来源库 | **403**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **305** |","| 站点页面 | **309** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])