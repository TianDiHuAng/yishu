# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle145"; DATE="2026-11-24"
IDS=["mughal-alamgir-portrait","mughal-muhammad-ali-beg","pahari-abhisarika-nayika","pahari-balwant-singh"]
ET,ST,PG=508,634,545
DECIS="""## D148 — Cycle145 印度细密画 4 条（504 → 508）
`mughal-alamgir-portrait`（奥朗则布像，1698—99，**核心**；素白无饰＝晚年苦行、帕輿出行、祈祷手势）、
`mughal-muhammad-ali-beg`（伊朗使节像，约1631，**核心**；Hashim 作、波斯铭署名、绿底花虫边饰）、
`pahari-abhisarika-nayika`（帕哈里《阿毗萨里卡·纳伊卡》，约1760，**核心**；八纳伊卡体系、风雨夜＋蛇＋破碎饰物）、
`pahari-balwant-singh`（Nainsukh《巴尔万特·辛格》，约1750，**核心**；赞助人—画师长程关系、水烟观舞、留白背景）。
**校验器立功（R21）**：`when` 写「1698—1699年（1110 AH）」含拉丁字母「AH」被 R21 拦下；把 AH 移出 `when`（正文已述）后通过。
art-asia 南亚细密画扩充。写前查重通过。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（V&A）。
"""
REPORT=("- 印度细密画 4 条（504 → 508，V&A）：奥朗则布像（**素白无饰＝晚年苦行**、帕輿出行、祈祷手势）、伊朗使节像（Hashim 作、波斯铭署名、绿底花虫边饰）、"
 "帕哈里《阿毗萨里卡·纳伊卡》（**八纳伊卡**、风雨夜＋蛇＋破碎饰物）、Nainsukh《巴尔万特·辛格》（**赞助人—画师长程关系**、水烟观舞、留白背景）。"
 "**R21 立功**：`when` 含「AH」被拦，把 AH 移出 when（正文已述）后通过。art-asia 南亚细密画扩充。站点 541 → 545 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["印度细密画（V&A）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"checker_catch":"R21 when 含 AH，已修正",
 "new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["印度细密画"],"gaps_found":{"entries":4},"network":"V&A","verdict":"总508；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle144":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle144":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **504**（L2 500 / L3 4 / L1 0） |","| 条目 | **508**（L2 504 / L3 4 / L1 0） |"),("| 来源 | **630**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **634**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **541**，站内断链 **0** |","| 页面 | **545**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **504** | L2 500 / L3 4 / **L1 0** |","| 条目总数 | **508** | L2 504 / L3 4 / **L1 0** |"),("| 来源库 | **630**（另 11 条预备来源未计入） |","| 来源库 | **634**（另 11 条预备来源未计入） |"),("| 站点页面 | **541** |","| 站点页面 | **545** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **504**（L2 500 / L3 4，**无 L1**） |","| 条目 | **508**（L2 504 / L3 4，**无 L1**） |"),("| 来源 | **630**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **634**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **541** |","| 站点页面 | **545** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)