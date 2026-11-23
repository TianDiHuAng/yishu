# -*- coding: utf-8 -*-
"""Cycle79 收尾：D083 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D083 — Cycle79 中国绘画作品补 4 条（260 → 264）
- **背景**：`art-china-painting` 单元是通史性条目的家，但**具体画作**此前只有 3 件（米友仁、赵孟頫、陈洪绶）。检索得 45 件可写件，取 4 件。
- **决定**：新增
  1. `juran-buddhist-retreat` 巨然《溪山兰若》（960—85，绢本水墨184.5×56.1cm，**核心**）；
  2. `muqi-dragon` 牧溪《龙》（约1250—79，绢本水墨125.2×57.2cm，与《虎》成对，**核心**）；
  3. `du-jin-lin-bu` 杜堇《林逋行吟图》（1400s 末，纸本设色156.4×72.4cm，**核心**）；
  4. `ten-stages-bodhisattvas`《菩萨十地》立轴（**1454**，绢本设色140.8×79.3cm，**核心**）。
- **四处内容要点**：
  1. **风格混合＝身份变迁的形式后果**：巨然与董源共开**江南画派**（湿墨平远）；而本画的**巍峨主峰**属**北宋院体**样式。该馆把这一混合归因于**南唐降宋、巨然北迁开封**，并推测本画**作于976年后**——条目照录并标注推测。
  2. **对屏是「三件一组」的两翼**：牧溪龙虎应**阴阳**；在**禅寺语境**中「很可能夹护一幅中央图像（如观音）」；另记两处**时间痕迹**——**绢色变暗**、**虎舌鼻淡红已褪**。
  3. **签款本身就是价值**：杜堇画北宋隐士**林逋**（967—1028，梅妻鹤子）月下看梅；该馆点明「**杜堇署款真迹存世稀少，此画即为其中之一**」。
  4. **仪式性绘画＋宫廷指令**：十地轴与同馆另轴同属**水陆法会**组画；**右上钤御玺并有金字题记**「大明景泰五年八月初三日施」，**左下墨书记「奉旨所制」**，很可能**施送北京大隆福寺**。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 4 条来源，重跑 `build_scope.py`。
- **代价**：4 条均单机构；中国绘画作品 7 件（宋元明清各代均有），**壁画与卷轴长卷仍缺**。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle79","date":"2026-11-23","status":"completed",
 "gap_methods":["中国绘画作品填补"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["juran-buddhist-retreat","muqi-dragon","du-jin-lin-bu","ten-stages-bodhisattvas"],
 "chinese_painting_works":7,
 "must_state":["巨然：南唐降宋北迁与院体主峰混合","牧溪龙虎=阴阳+三件一组（中央观音为推断）","杜堇签款真迹稀少","十地轴=水陆法会+景泰五年金字题记+奉旨"],
 "new_sources":4,"sources_total":395,"entries_total":264,"pages":301,
 "check_result":"errors=0","check_links_result":"broken=0(301页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle79","date":"2026-11-23","methods_used":["中国绘画作品"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"中国绘画作品 3→7（总 264）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle79"' not in t:
    block=('if cyc=="cycle79":\n'
           '    L.append("- 中国绘画**具体画作**此前仅 3 件，本轮补 4 条（260 → 264）：巨然《溪山兰若》、牧溪《龙》、'
           '杜堇《林逋行吟图》、《菩萨十地》轴（1454）。四处要点：①**风格混合＝身份变迁**——巨然与董源共开'
           '**江南画派**（湿墨平远），而本画**巍峨主峰**属**北宋院体**样式，该馆归因于**南唐降宋、巨然北迁**并推测作于 976 年后；'
           '②牧溪龙虎应**阴阳**，在禅寺语境「很可能**夹护观音**」而为**三件一组**的两翼；另记**绢色变暗**、**虎舌淡红褪去**；'
           '③杜堇画**林逋**（梅妻鹤子）月下看梅，该馆点明「**杜堇署款真迹存世稀少，此画即为其中之一**」；'
           '④十地轴与同馆另轴同属**水陆法会**组画，**右上御玺＋金字题记**「景泰五年八月初三日施」、**左下墨书「奉旨所制」**，'
           '很可能施送**大隆福寺**。站点 297 → 301 页，体检 12/12。")\n')
    anchor='if cyc=="cycle78":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 260（L2 256 / L3 4 / L1 0） |","| 条目 | 264（L2 260 / L3 4 / L1 0） |"),
    ("| 来源 | 391（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 395（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 297，站内断链 **0** |","| 页面 | 301，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **260** | L2 256 / L3 4 / **L1 0** |","| 条目总数 | **264** | L2 260 / L3 4 / **L1 0** |"),
    ("| 来源库 | **391**（另 11 条预备来源未计入） |","| 来源库 | **395**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **297** |","| 站点页面 | **301** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])