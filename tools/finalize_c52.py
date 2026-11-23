# -*- coding: utf-8 -*-
"""Cycle52 收尾：D055 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D055 — Cycle52 补上上轮未竟的约鲁巴，并加深安第斯与朝鲜（185 → 190）
- **决定**：上轮我要补约鲁巴却得到 Nok，本轮**定向**检索（`yoruba`/`ife`/`gelede`）并确认为真约鲁巴对象后才建条：
  1. `yoruba-gelede-masks` 约鲁巴 Gelede 成对面具（约1945—50，木与颜料，77.7 / 86 cm）；
  2. `asante-memorial-head` 阿坎/阿散蒂赤陶纪念头像（约17世纪末—18世纪初，19.1×13.6×15.5 cm）；
  3. `paracas-mantle` 帕拉卡斯披巾（约前300—200年，154.9×292.1 cm，双头鸟纹）；
  4. `chimu-litter-backrest` 奇穆抬舆靠背（放射性碳 1185—1275，60.4×95 cm）；
  5. `goryeo-celadon-cup` 高丽青瓷莲瓣盏（12世纪）。
- **三处值得记录的写法**：
  1. **约鲁巴 Gelede**：游行由**男性表演**、内容却是敬奉「大母」Ìyá Nlá——该馆把这层张力（敬奉女性力量却处在男性主导社会）明确写出，条目照录不裁定；鳄鱼"与女巫和雷神相关"标注为该馆解释。
  2. **帕拉卡斯披巾**：该馆直言双头鸟纹「**很可能有象征意义，但具体含义仍未知**」——条目把「未知」保留为内容，不填补。
  3. **奇穆抬舆**：该馆以「无畜力与车轮的社会里，肩抬专属受尊者」解释器物功能——把装饰性与社会等级挂钩；人物身份该馆用 perhaps，条目保留推测语气。
- **第二例「女性制作者」**：阿坎纪念头像同样被记为 `unknown female ceramicist`，理由与 Nok 头像不同——此处是「在世时委托女性艺人、依记忆无草图塑像」。两条并置，可以看出「女性作者」在非洲陶塑研究中的位置。
- **可逆方式**：删 5 条 overlay 与 catalog 元组、移除 5 条来源，重跑 `build_scope.py`。
- **代价**：5 条均单机构（`needs_verification`）；阿散蒂与奇穆各仅 1 条，约鲁巴仅 1 条，深度仍浅。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle52","date":"2026-11-23","status":"completed",
 "gap_methods":["定向检索补缺（约鲁巴）","区块加深（安第斯/朝鲜）"],"network":"partial: museum APIs ok",
 "new_entries":5,"new_entry_ids":["yoruba-gelede-masks","asante-memorial-head","paracas-mantle","chimu-litter-backrest","goryeo-celadon-cup"],
 "gaps_closed":["约鲁巴（上轮未竟）","阿散蒂/阿坎","帕拉卡斯","奇穆","高丽日用青瓷"],
 "explicit_unknowns":["帕拉卡斯双头鸟纹含义（馆方明言未知）"],
 "new_sources":5,"sources_total":332,"entries_total":190,"pages":225,
 "check_result":"errors=0","check_links_result":"broken=0(225页)","audit_all":"9/9 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle52","date":"2026-11-23","methods_used":["定向检索","区块加深"],
 "gaps_found":{"entries":5},"network":"partial (museum APIs)",
 "verdict":"补约鲁巴/阿散蒂/帕拉卡斯/奇穆/高丽（190）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle52"' not in t:
    block=('if cyc=="cycle52":\n'
           '    L.append("- **补上上轮未竟的约鲁巴**（定向检索确认对象文化后才建条），并加深安第斯与朝鲜：'
           '约鲁巴 Gelede 成对面具、阿散蒂赤陶纪念头像、帕拉卡斯披巾、奇穆抬舆靠背、高丽青瓷莲瓣盏（185 → **190**）。'
           '三处写法值得记录：Gelede 由**男性表演**却敬奉「大母」，该馆把这层张力写出，条目照录不裁定；'
           '帕拉卡斯披巾的双头鸟纹该馆直言「**具体含义仍未知**」，条目把未知保留为内容；'
           '奇穆抬舆以「无畜力无车轮社会里肩抬专属受尊者」解释功能，人物身份保留 perhaps 语气。'
           '另出现第二例「女性制作者」（阿坎头像：凭记忆、无草图），与 Nok 头像并置可见非洲陶塑研究的作者问题。'
           '站点 220 → 225 页，体检 9/9。")\n')
    anchor='if cyc=="cycle51":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 185（L2 179 / L3 6 / L1 0） |","| 条目 | 190（L2 184 / L3 6 / L1 0） |"),
    ("| 来源 | 327（全部 verified；隔离区 5 条不可核验） |","| 来源 | 332（全部 verified；隔离区 5 条不可核验） |"),
    ("| 页面 | 220，站内断链 **0** |","| 页面 | 225，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **185** | L2 179 / L3 6 / **L1 0** |","| 条目总数 | **190** | L2 184 / L3 6 / **L1 0** |"),
    ("| 来源库 | **327** |","| 来源库 | **332** |"),
    ("| 站点页面 | **220** |","| 站点页面 | **225** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])