# -*- coding: utf-8 -*-
"""Cycle100 收尾：D103 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D103 — Cycle100 中世纪艺术 4 条（340 → 344）
依据「按单元计数」找出最薄的视觉艺术单元 `art-medieval`（原 6 条），定向补 4 件异媒介实物：
`auvergne-virgin-majesty`（奥弗涅「智慧宝座」圣母，约1150—1200，**核心**）、`paris-mirror-chess`（巴黎象牙镜背，1325—50，**核心**）、
`gothic-casket-panels`（哥特象牙匣板，约1330—50，**核心**）、`stained-glass-donors-pair`（彩窗供养人一对，约1480）。
四处要点：①Sedes Sapientiae 中**圣母即圣子的宝座**，道成肉身使其成为**神人中介**，12世纪后圣母图像激增；
②巴黎象牙镜背**棋兼喻爱与战**，情侣身份（特里斯坦/兰斯洛特）**该馆明言无定论**；
③象牙匣板取自**《玫瑰传奇》与克雷蒂安·德·特鲁瓦**的宫廷传奇，或为**男女赠礼**；
④彩窗供养人**中央画面已失**，今仅存两翼，或为**家族礼拜堂**。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；中世纪由 6 → 10 条，补入象牙/彩窗/木雕，但**写本彩饰（illuminated manuscript）**仍缺。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle100","date":"2026-11-24","status":"completed",
 "gap_methods":["按单元计数定向补最薄 art-medieval"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["auvergne-virgin-majesty","paris-mirror-chess","gothic-casket-panels","stained-glass-donors-pair"],
 "medieval_objects":4,"new_sources":4,"sources_total":473,"entries_total":344,"pages":381,
 "check_result":"errors=0","check_links_result":"broken=0(381页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle100","date":"2026-11-24","methods_used":["中世纪艺术（定向最薄单元）"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"中世纪 6→10（总344）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle100"' not in t:
    block=('if cyc=="cycle100":\n'
           '    L.append("- 按单元计数找出最薄视觉单元 `art-medieval`（原6条），定向补 4 件（340 → 344）：奥弗涅「智慧宝座」圣母、'
           '巴黎象牙镜背、哥特象牙匣板、彩窗供养人。①Sedes Sapientiae 中**圣母即圣子的宝座**，道成肉身使她为**神人中介**，12世纪后圣母图像激增；'
           '②巴黎象牙镜背**棋兼喻爱与战**，情侣身份**明言无定论**；③象牙匣板取自**《玫瑰传奇》等宫廷传奇**，或为**男女赠礼**；'
           '④彩窗供养人**中央画面已失**，今仅存两翼。站点 377 → 381 页，体检 12/12。")\n')
    anchor='if cyc=="cycle99":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **340**（L2 336 / L3 4 / L1 0） |","| 条目 | **344**（L2 340 / L3 4 / L1 0） |"),
    ("| 来源 | **469**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **473**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **377**，站内断链 **0** |","| 页面 | **381**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **340** | L2 336 / L3 4 / **L1 0** |","| 条目总数 | **344** | L2 340 / L3 4 / **L1 0** |"),
    ("| 来源库 | **469**（另 11 条预备来源未计入） |","| 来源库 | **473**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **377** |","| 站点页面 | **381** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **340**（L2 336 / L3 4，**无 L1**） |","| 条目 | **344**（L2 340 / L3 4，**无 L1**） |"),
    ("| 来源 | **469**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **473**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **377** |","| 站点页面 | **381** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])