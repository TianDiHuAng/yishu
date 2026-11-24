# -*- coding: utf-8 -*-
"""Cycle103 收尾：D106 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D106 — Cycle103 新古典/浪漫 4 条（348 → 352）
按单元计数（`art-neo-romantic` 8 条）定向补 4 件：
`turner-burning-parliament`（透纳《议会焚毁》，1835，**核心**）、`david-cupid-psyche`（大卫《丘比特与普绪克》，1817，**核心**）、
`hackert-pozzuoli`（哈克特《波佐利湾》，1803）、`paelinck-self-portrait`（帕林克《自画像》，约1812）。
四处要点：①透纳以**1834 议会大火**为题材，**夸大火势**表达人对自然破坏力的无力，色光**近乎抽象**；
②大卫把丘比特画成**笨拙少年**而非理想少年，取材 **Moschus 的冷僻希腊诗**——文本考据改写图像惯例；
③哈克特的**清晰造型**被归为**德国浪漫**特征，景观又叠**保罗登陆地**的历史层；
④帕林克**在大卫门下**学习、后赴罗马，自画像的 **dandy 衣饰与仿古桌椅**把「新古典」延伸为**生活方式**。大卫—帕林克构成**师承链**。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；新古典/浪漫由 8 → 12 条，但**西班牙（戈雅）与北欧**仍缺。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle103","date":"2026-11-24","status":"completed",
 "gap_methods":["新古典/浪漫（定向最薄单元）"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["turner-burning-parliament","david-cupid-psyche","hackert-pozzuoli","paelinck-self-portrait"],
 "neo_romantic_objects":4,"new_sources":4,"sources_total":481,"entries_total":352,"pages":389,
 "check_result":"errors=0","check_links_result":"broken=0(389页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle103","date":"2026-11-24","methods_used":["新古典/浪漫"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"新古典/浪漫 8→12（总352）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle103"' not in t:
    block=('if cyc=="cycle103":\n'
           '    L.append("- 新古典/浪漫（`art-neo-romantic` 8条）补 4 件（348 → 352）：透纳《议会焚毁》、大卫《丘比特与普绪克》、'
           '哈克特《波佐利湾》、帕林克《自画像》。①透纳以**1834议会大火**为题、**夸大火势**表达人面对自然破坏力的无力，色光**近乎抽象**；'
           '②大卫把丘比特画成**笨拙少年**（反程式），取材 **Moschus 冷僻希腊诗**——文本考据改写图像；③哈克特**清晰造型**归为**德国浪漫**、'
           '景观叠**保罗登陆地**历史层；④帕林克**在大卫门下**、后赴罗马，**dandy 衣饰与仿古桌椅**把新古典延伸为生活方式（大卫—帕林克师承链）。'
           '站点 385 → 389 页，体检 12/12。")\n')
    anchor='if cyc=="cycle102":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **348**（L2 344 / L3 4 / L1 0） |","| 条目 | **352**（L2 348 / L3 4 / L1 0） |"),
    ("| 来源 | **477**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **481**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **385**，站内断链 **0** |","| 页面 | **389**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **348** | L2 344 / L3 4 / **L1 0** |","| 条目总数 | **352** | L2 348 / L3 4 / **L1 0** |"),
    ("| 来源库 | **477**（另 11 条预备来源未计入） |","| 来源库 | **481**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **385** |","| 站点页面 | **389** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **348**（L2 344 / L3 4，**无 L1**） |","| 条目 | **352**（L2 348 / L3 4，**无 L1**） |"),
    ("| 来源 | **477**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **481**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **385** |","| 站点页面 | **389** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])