# -*- coding: utf-8 -*-
"""Cycle67 收尾：D071（饱和评估 + 北美再补 4 条）+ METRICS/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D071 — Cycle67 饱和评估（未饱和）+ 北美再补 4 条（216 → 220）
- **饱和评估（§5）结论：`saturated=false`**，证据见 `reports/saturation_c67.json`：
  - **条件②成立**：核心 55 条、重要 149 条**全部 ≥L2**；层级 L2 216 / L3 4 / L1 0；
  - **条件①不成立**：最近 6 轮（cycle61–66）仍有**新条目产出**（cycle63 +4、cycle64 +4），且缺口清单里有**明确可补项**（北美平原/东南、非洲余量、东南亚泰越窑虽确认不可得但其他区域仍有候选）。
- **决定**：判定**未饱和**，继续推进；不写 ALL_DONE。
- **同日内容推进（北美 8 → 12 条）**：新增
  1. `maria-martinez-olla` 玛丽亚·马丁内斯黑陶水罐（1920前，28.5×34cm，**核心**）；
  2. `ma-pe-wi-three-antelope`《三只羚羊》（Ma Pe Wi，1920s，水粉 50.8×38.1cm）；
  3. `tlingit-mask` 特林吉特面具（身份**已佚**，桤木彩绘 21.4×17.2×8.9cm）；
  4. `haida-raven-rattle` 海达渡鸦响器（31.8×9.3×11.2cm）。
- **三处表述的克制**：
  1. **面具身份已失传**：该馆明言 identity is lost，条目**不作形制推断**；同时引 1998 年酋长 Robert Joseph 的佩戴自述（只摘大意、署名、注明是该馆转述的节译），把「所指断裂」与「身体经验未断」并列。
  2. **Martinez 的「最早之一」**：该馆的判断，条目注明未给序列依据；**黑亮色出自烧成技法**（非颜料）单独点出。
  3. **响器的功能转移**：可能始于萨满，后为世俗酋长用于冬季仪式因而成为**权力象征**——同一器物、职能转换，形态不必改变。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：北美 12 条仍只覆盖西南与西北岸；平原、东南、北极其余地区为零。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle67","date":"2026-11-23","status":"completed",
 "gap_methods":["§5 饱和评估","北美候选筛选"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["maria-martinez-olla","ma-pe-wi-three-antelope","tlingit-mask","haida-raven-rattle"],
 "saturation":{"saturated":False,"cond2":True,"cond1":False,"recent6_new":8},
 "north_america_total":12,
 "new_sources":4,"sources_total":351,"entries_total":220,"pages":255,
 "check_result":"errors=0","check_links_result":"broken=0(255页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle67b","date":"2026-11-23","methods_used":["北美候选筛选"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"北美 8→12（总 220）；仍未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle67"' not in t:
    block=('if cyc=="cycle67":\n'
           '    L.append("- **首次认真的饱和评估（§5）**：`saturated=false`。**条件②成立**（核心 55 / 重要 149 全部 ≥L2，L1=0），'
           '**条件①不成立**——最近 6 轮仍在产出新条目（cycle63 +4、cycle64 +4），且缺口清单有明确可补项。'
           '同日推进内容：北美 **8 → 12 条**，新增 Maria Martinez 黑陶水罐（核心）、Ma Pe Wi《三只羚羊》、Tlingit 面具、Haida 渡鸦响器。'
           '三处表述克制：①面具**身份已失传**，条目不作形制推断，同时引 1998 年酋长 Robert Joseph 的佩戴自述（节译＋署名）'
           '把「所指断裂」与「身体经验未断」并列；②Martinez 的「最早之一」标注为该馆判断，并点出**黑亮色出自烧成而非颜料**；'
           '③响器可能始于萨满、后为世俗酋长于冬季仪式所用而成为**权力象征**——同一器物、职能转换、形态不变。'
           '站点 251 → 255 页，体检 12/12。")\n')
    anchor='if cyc=="cycle66":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 216（L2 212 / L3 4 / L1 0） |","| 条目 | 220（L2 216 / L3 4 / L1 0） |"),
    ("| 来源 | 347（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 351（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 251，站内断链 **0** |","| 页面 | 255，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **216** | L2 212 / L3 4 / **L1 0** |","| 条目总数 | **220** | L2 216 / L3 4 / **L1 0** |"),
    ("| 来源库 | **347**（另 11 条预备来源未计入） |","| 来源库 | **351**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **251** |","| 站点页面 | **255** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])