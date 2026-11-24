# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle121"; DATE="2026-11-24"
IDS=["qianlong-jade-mountain","kangxi-jade-dragon-cup","kangxi-jade-buffalo","qing-jade-horse"]
ET,ST,PG=420,548,457
DECIS="""## D124 — Cycle121 清代玉器 4 条（416 → 420）
`qianlong-jade-mountain`（乾隆玉山，**核心**；大料山形表寻仙，玉屑晨露为长生药之文献）、
`kangxi-jade-dragon-cup`（康熙玉龙耳杯，**核心**；三龙抓沿+寿字，苏州工，款识「乐观归属陆子刚」＝借名市场策略）、
`kangxi-jade-buffalo`（玉卧牛；受众扩至女性/商人/在野文人，竞争市场觅客；**年代字段记1642—1722与通行纪年不符，照录存疑**）、
`qing-jade-horse`（玉马 3.4cm；科举文人案头清玩，明清成收藏品）。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（CMA）；清代玉器由 0 增至 4，汉代玉器仍缺。
"""
REPORT=("- 清代玉器 4 条（416 → 420，CMA）：乾隆玉山（寻仙主题+玉屑晨露长生文献）、康熙玉龙耳杯（三龙抓沿+寿字、苏州工、"
 "「乐观归属陆子刚」＝借名市场策略）、玉卧牛（受众扩大+竞争觅客；**年代字段1642—1722与通行不符，照录存疑**）、玉马（3.4cm 文人案头清玩）。"
 "清代玉器 0 → 4。站点 453 → 457 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["清代玉器（CMA）"],"network":"CMA ok",
 "new_entries":4,"new_entry_ids":IDS,"date_suspect":"玉卧牛年代字段1642—1722照录存疑",
 "new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["清代玉器"],"gaps_found":{"entries":4},"network":"CMA","verdict":"清代玉器 0→4（总420）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle120":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle120":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **416**（L2 412 / L3 4 / L1 0） |","| 条目 | **420**（L2 416 / L3 4 / L1 0） |"),("| 来源 | **544**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **548**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **453**，站内断链 **0** |","| 页面 | **457**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **416** | L2 412 / L3 4 / **L1 0** |","| 条目总数 | **420** | L2 416 / L3 4 / **L1 0** |"),("| 来源库 | **544**（另 11 条预备来源未计入） |","| 来源库 | **548**（另 11 条预备来源未计入） |"),("| 站点页面 | **453** |","| 站点页面 | **457** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **416**（L2 412 / L3 4，**无 L1**） |","| 条目 | **420**（L2 416 / L3 4，**无 L1**） |"),("| 来源 | **544**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **548**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **453** |","| 站点页面 | **457** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)