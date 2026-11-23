# -*- coding: utf-8 -*-
"""Cycle92 收尾：D095 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D095 — Cycle92 两河/波斯早期 4 条（308 → 312）
新增 `sumer-bull-polemount`（苏美尔牛犊杆头饰，约前2700，**核心**）、`xerxes-guard-relief`（波斯波利斯卫兵浮雕，前486—465，**核心**）、
`luristan-master-cheekpiece`（卢里斯坦动物主人马颊饰，约前700）、`sasanian-hunting-dish`（萨珊狩猎银盘，400—600）。
四处要点：①苏美尔小牛原为神庙崇拜像，眼与额饰曾嵌异色石/骨，今已失，属极少数幸存原作；
②薛西斯宫卫兵浮雕或出自波斯波利斯西阶梯，该馆引希罗多德以「民主对君主制」概括希波战争；
③卢里斯坦马颊饰把「动物主人」母题装在控制坐骑的器具上，人—翼兽—兔构成支配链；
④萨珊银盘以王冠认作霍尔米兹德二世，但装备风格提示或为后世纪念作，条目保留两说。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；两河/波斯早期仍以点状分布为主，未成体系。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle92","date":"2026-11-23","status":"completed",
 "gap_methods":["两河/波斯早期"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["sumer-bull-polemount","xerxes-guard-relief","luristan-master-cheekpiece","sasanian-hunting-dish"],
 "mesopotamian_persian":4,"new_sources":4,"sources_total":443,"entries_total":312,"pages":349,
 "check_result":"errors=0","check_links_result":"broken=0(349页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle92","date":"2026-11-23","methods_used":["两河/波斯早期"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"两河/波斯早期 0→4（总 312）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle92"' not in t:
    block=('if cyc=="cycle92":\n'
           '    L.append("- 两河/波斯早期补 4 条（308 → 312）：苏美尔牛犊杆头饰、波斯波利斯卫兵浮雕、卢里斯坦动物主人马颊饰、萨珊狩猎银盘。'
           '①小牛原为神庙崇拜像，镶嵌已失，属极少数幸存原作；②卫兵浮雕或出自宫殿西阶梯，该馆引希罗多德以**民主对君主制**概括希波战争；'
           '③「动物主人」母题被装在**控制坐骑的器具**上，人—翼兽—兔构成支配链；④萨珊银盘**王冠**认作二世、**装备风格**指向后世纪念作，条目保留两说。'
           '站点 345 → 349 页，体检 12/12。")\n')
    anchor='if cyc=="cycle91":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **308**（L2 304 / L3 4 / L1 0） |","| 条目 | **312**（L2 308 / L3 4 / L1 0） |"),
    ("| 来源 | **439**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **443**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **345**，站内断链 **0** |","| 页面 | **349**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **308** | L2 304 / L3 4 / **L1 0** |","| 条目总数 | **312** | L2 308 / L3 4 / **L1 0** |"),
    ("| 来源库 | **439**（另 11 条预备来源未计入） |","| 来源库 | **443**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **345** |","| 站点页面 | **349** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **308**（L2 304 / L3 4，**无 L1**） |","| 条目 | **312**（L2 308 / L3 4，**无 L1**） |"),
    ("| 来源 | **439**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **443**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **345** |","| 站点页面 | **349** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])