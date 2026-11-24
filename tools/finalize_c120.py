# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle120"; DATE="2026-11-24"
IDS=["vandiem-lacquer-box","canton-umbrella-mender","kutahya-tile-panel","harp-lute-guitar-va"]
ET,ST,PG=416,544,453
DECIS="""## D123 — Cycle120 V&A 4 条（412 → 416）
`vandiem-lacquer-box`（范迪门外销漆盒，1636—39，**核心**；京都定做→出岛→荷兰外销；盒盖内铭 Maria van Diemen，与 Beckford「Buys 盒」双证据定年）、
`canton-umbrella-mender`（广州外销画《修伞匠》，约1790；百业组画 100 幅之一，为欧人求知欲而作）、
`kutahya-tile-panel`（屈塔希亚 80 砖板，约1660，**核心**；龛瓶对称满铺，承伊兹尼克 1550s 开创的釉下彩墙砖板模式）、
`harp-lute-guitar-va`（哈普鲁特吉他，约1810；三器混成、鲁特式轴箱＋低音空弦、玫瑰「亲王羽毛」或指夏洛特公主）。
**如实保留截断**：范迪门盒 summary 末句「w…」截断未补写；公主关联标 may。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（V&A）。
"""
REPORT=("- V&A 4 条（412 → 416）：范迪门外销漆盒（1636—39，京都定做→出岛→荷兰；盒盖内铭 van Diemen 之妻，与 Beckford「Buys 盒」**双证据定年**）、"
 "广州外销画《修伞匠》（约1790，**百业组画 100 幅**之一）、屈塔希亚 80 砖板（约1660，龛瓶对称满铺，承伊兹尼克 1550s 模式）、"
 "哈普鲁特吉他（约1810，**三器混成**、鲁特式轴箱＋低音空弦、「亲王羽毛」玫瑰或指夏洛特公主）。"
 "范迪门 summary 末句截断未补写。站点 449 → 453 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["V&A 日本漆器/广州外销画/屈塔希亚砖/混成乐器"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["V&A 漆器/外销画/砖板/乐器"],"gaps_found":{"entries":4},"network":"V&A","verdict":"总416；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle119":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle119":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **412**（L2 408 / L3 4 / L1 0） |","| 条目 | **416**（L2 412 / L3 4 / L1 0） |"),("| 来源 | **540**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **544**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **449**，站内断链 **0** |","| 页面 | **453**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **412** | L2 408 / L3 4 / **L1 0** |","| 条目总数 | **416** | L2 412 / L3 4 / **L1 0** |"),("| 来源库 | **540**（另 11 条预备来源未计入） |","| 来源库 | **544**（另 11 条预备来源未计入） |"),("| 站点页面 | **449** |","| 站点页面 | **453** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **412**（L2 408 / L3 4，**无 L1**） |","| 条目 | **416**（L2 412 / L3 4，**无 L1**） |"),("| 来源 | **540**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **544**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **449** |","| 站点页面 | **453** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)