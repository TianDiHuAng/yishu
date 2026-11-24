# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle146"; DATE="2026-11-24"
IDS=["heqat-frog-goddess","caryatid-mirror","decorated-situla","bakenmut-coffin"]
ET,ST,PG=512,638,549
DECIS="""## D149 — Cycle146 埃及雕塑 4 条（508 → 512）
`heqat-frog-goddess`（前王朝蛙像，约前2950，**核心**；动物雕塑之始、石纹随形、**前王朝含义未知**仅后世认同赫奎特）、
`caryatid-mirror`（女像柱镜，第18王朝，**核心**；裸女柄时尚、哈托尔/阿佛洛狄忒、nefrut）、
`decorated-situla`（托勒密西图拉瓶，**核心**；**受供/献供双重角色**、爱犬 Nefer）、
`bakenmut-coffin`（巴肯穆特棺，第21–22王朝，**核心**；法老北葬、西岸无名墓、**棺饰取代墓饰＝移动的墓室**）。
**工程**：write_c146 初稿因转义引号导致 situla 的 W() 未闭合，**构建前发现并修复**（补 `"),`）。
art-ancient 38→42。写前查重通过。
**如实**：多处 desc/summary 截断未补写；「镶嵌」为疑问。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）。
"""
REPORT=("- 埃及雕塑 4 条（508 → 512，CMA）：前王朝**蛙像**（动物雕塑之始、**前王朝含义未知**仅后世认同赫奎特）、女像柱镜（裸女柄时尚、哈托尔、nefrut）、"
 "托勒密**西图拉瓶**（**受供/献供双重角色**、爱犬 Nefer）、**巴肯穆特棺**（法老北葬、西岸无名墓、**棺饰取代墓饰＝移动墓室**）。"
 "构建前修复了 write_c146 一处未闭合的 W()。art-ancient 38→42。站点 545 → 549 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["埃及雕塑（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"fixed":"write_c146 未闭合 W() 构建前修复",
 "new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["埃及雕塑"],"gaps_found":{"entries":4},"network":"CMA","verdict":"art-ancient 38→42（总512）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle145":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle145":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **508**（L2 504 / L3 4 / L1 0） |","| 条目 | **512**（L2 508 / L3 4 / L1 0） |"),("| 来源 | **634**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **638**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **545**，站内断链 **0** |","| 页面 | **549**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **508** | L2 504 / L3 4 / **L1 0** |","| 条目总数 | **512** | L2 508 / L3 4 / **L1 0** |"),("| 来源库 | **634**（另 11 条预备来源未计入） |","| 来源库 | **638**（另 11 条预备来源未计入） |"),("| 站点页面 | **545** |","| 站点页面 | **549** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **508**（L2 504 / L3 4，**无 L1**） |","| 条目 | **512**（L2 508 / L3 4，**无 L1**） |"),("| 来源 | **634**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **638**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **545** |","| 站点页面 | **549** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)