# -*- coding: utf-8 -*-
"""Cycle93 收尾：D096 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D096 — Cycle93 文艺复兴 4 条（312 → 316）
新增 `lippi-holy-family-tondo`（利皮圆形画，约1488—93，**核心**）、`lotto-portrait-man`（洛托男子肖像，1533—34，**核心**）、
`buglioni-glazed-terracotta`（布利奥尼釉陶祭坛，约1510—20）、`verrocchio-christ-bust`（韦罗基奥基督胸像，约1470—1500，**核心**）。
四处要点：①利皮圆形画的草图中**古维纳斯像被改写成圣玛格丽特**——古代形式在基督教图像中的再利用；
②洛托肖像以「被打断的瞬间」区别于程式化肖像，三叶草/茉莉/玫瑰构成婚姻与爱的象征网络，身份与手势均属考订；
③布利奥尼釉陶因**耐久、洁白、在幽暗教堂中醒目**而流行，由 della Robbia 推广以替代昂贵大理石；
④韦罗基奥工坊以陶复制名作供**中产市场**，**躯干由助手、面容与头发由本人**完成，故躯干比例失调是分工痕迹。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；文艺复兴单元得以用实物支撑，但仍以意大利为主，北方文艺复兴实物偏少。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle93","date":"2026-11-23","status":"completed",
 "gap_methods":["文艺复兴实物填补"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["lippi-holy-family-tondo","lotto-portrait-man","buglioni-glazed-terracotta","verrocchio-christ-bust"],
 "renaissance_objects":4,"new_sources":4,"sources_total":447,"entries_total":316,"pages":353,
 "check_result":"errors=0","check_links_result":"broken=0(353页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle93","date":"2026-11-23","methods_used":["文艺复兴实物"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"文艺复兴实物 0→4（总 316）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle93"' not in t:
    block=('if cyc=="cycle93":\n'
           '    L.append("- 文艺复兴单元此前少实物，本轮补 4 条（312 → 316）：利皮圆形画、洛托男子肖像、布利奥尼釉陶祭坛、韦罗基奥基督胸像。'
           '①利皮草图把**古维纳斯改写为圣玛格丽特**，是古代形式的再利用；②洛托以**被打断的瞬间**区别于程式化肖像，'
           '三叶草/茉莉/玫瑰织成婚姻与爱的象征网络；③釉陶因**耐久洁白、在幽暗教堂中醒目**而流行，della Robbia 推广以**替代大理石**；'
           '④韦罗基奥工坊以陶复制名作供**中产市场**，**躯干由助手、面容与头发由本人**完成——躯干比例失调即分工痕迹。'
           '站点 349 → 353 页，体检 12/12。")\n')
    anchor='if cyc=="cycle92":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **312**（L2 308 / L3 4 / L1 0） |","| 条目 | **316**（L2 312 / L3 4 / L1 0） |"),
    ("| 来源 | **443**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **447**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **349**，站内断链 **0** |","| 页面 | **353**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **312** | L2 308 / L3 4 / **L1 0** |","| 条目总数 | **316** | L2 312 / L3 4 / **L1 0** |"),
    ("| 来源库 | **443**（另 11 条预备来源未计入） |","| 来源库 | **447**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **349** |","| 站点页面 | **353** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **312**（L2 308 / L3 4，**无 L1**） |","| 条目 | **316**（L2 312 / L3 4，**无 L1**） |"),
    ("| 来源 | **443**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **447**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **349** |","| 站点页面 | **353** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])