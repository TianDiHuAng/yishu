# -*- coding: utf-8 -*-
"""Cycle63 收尾：D067 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D067 — Cycle63 北美原住民**由零覆盖起步**（208 → 212）
- **背景**：`art-americas` 此前只有中美洲与安第斯（玛雅/阿兹特克/莫切/印加/帕拉卡斯/奇穆/纳斯卡），**北美原住民为零**。本轮定向检索（navajo/hopi/pueblo/tlingit/haida/inuit/plains/mississippian）得到 **26 件**可写件，取 4 件建条。
- **新增 4 条（均 art-americas，region 记「北美洲」）**：
  1. `navajo-hubbell-rug` 纳瓦霍 Hubbell 复兴风格地毯（约1890—1910，羊毛挂毯 194.8×138.4cm）；
  2. `hopi-kachina-painting` 霍皮 Katsina 偶人图（Fred Kabotie/Naqavoy’ma 水彩，约1920s，47.6×31.1cm）；
  3. `navajo-chief-blanket-rug` 纳瓦霍「酋长毯」样式地毯（约1900，178.4×151.1cm）；
  4. `hopi-canteen-katsina` 霍皮带 Katsina 面容水壶（1890，陶器施化妆土 21.5×24.5cm）。
- **四处「纠正性」内容，一律写进正文**：
  1. **「chief’s blanket」是误称** —— **Diné 并无酋长**；
  2. **市场转向有具体创伤史** —— 1860年代 Diné 被囚 **Bosque Redondo**、原住民贸易渠道崩解后，织者从「为本族/交易制衣」转为「为外来收藏市场制毯」；
  3. **「非真 Katsina」** —— 霍皮水壶上的面容是**想象性描绘**，非真实 Katsina；该馆并以**反问**收束：「制作者是否在以这种方式掌握自己的文化，以及文化被外来者消费的过程？」——条目**保留为问句**，不代答；
  4. **Moki 纹来源不明** —— 该馆并列「来自普韦布洛」与「来自1540年入西南的西班牙人」两说，不择一。
- **一处必须说清的体例问题**：`hopi-kachina-painting` 是**水彩画**（描绘 katsina 偶人），不是偶人本身；该馆描画内容时用 **seems to**，条目照录该限定。
- **实现坑**：元组里出现英文撇号（`Naqavoy'ma`、`chief's blanket`）会破坏 Python 字符串，已统一改为正式撇号 `’`，并在插入前用 `ast.parse` 自检。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构（`needs_verification`）；北美仍只覆盖西南部（纳瓦霍/霍皮），因纽特、西北海岸、平原诸族仍为零。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle63","date":"2026-11-23","status":"completed",
 "gap_methods":["北美原住民定向检索"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["navajo-hubbell-rug","hopi-kachina-painting","navajo-chief-blanket-rug","hopi-canteen-katsina"],
 "milestone":"北美原住民由零覆盖起步（4 条）",
 "corrective_content":["chief's blanket 为误称（Diné 无酋长）","Bosque Redondo 囚禁后的市场转向","水壶面容非真 Katsina（馆方反问保留）","Moki 纹来源不明并列两说"],
 "pitfall":"元组中英文撇号破坏字符串，改 ’（插入前 ast.parse 自检）",
 "new_sources":4,"sources_total":343,"entries_total":212,"pages":247,
 "check_result":"errors=0","check_links_result":"broken=0(247页)","audit_all":"11/11 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle63","date":"2026-11-23","methods_used":["北美定向检索"],
 "gaps_found":{"entries":4,"note":"北美此前零覆盖"},"network":"partial (museum APIs)",
 "verdict":"北美 0→4（总 212）；误称与创伤史入正文；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle63"' not in t:
    block=('if cyc=="cycle63":\n'
           '    L.append("- **北美原住民由零覆盖起步**：`art-americas` 此前只有中美洲与安第斯，北美为零；'
           '定向检索得 26 件可写件，取 4 件建条（208 → 212）——纳瓦霍 Hubbell 复兴地毯、霍皮 Katsina 偶人图（Kabotie 水彩）、'
           '纳瓦霍「酋长毯」样式地毯、霍皮带 Katsina 面容水壶。四处**纠正性内容**写进正文：'
           '①「**chief’s blanket 是误称**」，**Diné 并无酋长**；②市场转向有具体创伤史——1860s **Bosque Redondo** 囚禁后'
           '原住民贸易崩解，织者转做外来收藏市场；③水壶面容是**想象性描绘而非真 Katsina**，该馆以**反问**收束'
           '「制作者是否在掌握自己的文化及其被外来消费的过程？」——条目**保留为问句不代答**；④Moki 纹来源不明，普韦布洛与西班牙两说并列。'
           '体例上还澄清：那条是**画偶人的水彩画**，不是偶人本身（馆方原文用 seems to）。站点 243 → 247 页，体检 11/11。")\n')
    anchor='if cyc=="cycle62":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 208（L2 204 / L3 4 / L1 0） |","| 条目 | 212（L2 208 / L3 4 / L1 0） |"),
    ("| 来源 | 339（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 343（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 243，站内断链 **0** |","| 页面 | 247，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **208** | L2 204 / L3 4 / **L1 0** |","| 条目总数 | **212** | L2 208 / L3 4 / **L1 0** |"),
    ("| 来源库 | **339**（另 11 条预备来源未计入） |","| 来源库 | **343**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **243** |","| 站点页面 | **247** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])