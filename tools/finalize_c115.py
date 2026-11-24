# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle115"; DATE="2026-11-24"
IDS=["damascus-lidded-bowl","khurasan-ewer-va","qaitbay-basin","zayn-al-din-bucket"]
ET,ST,PG=396,525,433
DECIS="""## D118 — Cycle115 伊斯兰金属器 4 条（392 → 396）；再遇重名并修复
新增 `damascus-lidded-bowl`（大马士革嵌银盖钵，1500—50）、`khurasan-ewer-va`（呼罗珊嵌金银执壶，约1200—50，**核心**）、`qaitbay-basin`（Qa'itbay 盆，1468—96，**核心**）、`zayn-al-din-bucket`（Zayn al-Din 署名铜桶，约1475—1500）。
要点：①盖钵**平贴合盖或为香料量器**，器上带**未识意大利家族纹章**（跨地中海贸易物证）；②呼罗珊执壶**九宽九窄棱＋结绳纹＋为匿名主人祈福铭＋蹲狮**，体现「贱材经工艺而贵重」；③Qa'itbay 治下**宫廷赞助**致品质高涨；④Zayn al-Din 桶以**贴银增威望**、提手凸缘内侧署名，其署名见于数件同类器（工匠声望证据）。
**【事故与修复】** 本轮 `khurasan-ewer` **与既有条目（cma-1945-27「呼罗珊多棱执壶」）重名**，且 `write_c115.py` **覆盖了原 overlay**；build_scope=396 而 merge=395，触发 R11。处置：`git checkout` 恢复原 overlay；把本轮新件改 id 为 **`khurasan-ewer-va`**、标题加「（V&A）」；原 overlay 与页面复原。修复后 396 条 / errors=0。
**教训重申**：即便已建立"写前查重"，本轮因批量拉取未先 grep catalog 而漏检；后续每批必先 `grep "'id'"`。
**如实保留截断**：盖钵 summary「foug…」、执壶「sophisti…」、Qa'itbay「some objects…」、桶「产地/用途」均**未补写**。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条 V&A 来源。代价：均单机构（V&A）；伊斯兰金属器由数件增至 8 件级。
"""
REPORT=("- 伊斯兰金属器 4 条（392 → 396，V&A）：大马士革嵌银盖钵、呼罗珊嵌金银执壶、Qa'itbay 盆、Zayn al-Din 桶。"
 "①盖钵平贴合盖或为**香料量器**、带**未识意大利纹章**（跨地中海贸易物证）；②呼罗珊执壶**九宽九窄棱＋结绳纹＋匿名主人祈福铭＋蹲狮**；"
 "③Qa'itbay **宫廷赞助**致品质高涨；④Zayn al-Din 桶**贴银增威望**、凸缘内侧署名（工匠声望）。"
 "**事故**：`khurasan-ewer` 与既有 cma-1945-27 重名且覆盖原 overlay（R11 拦下）→ `git checkout` 恢复、新件改 `khurasan-ewer-va`，修复后 396 条/errors=0。站点 429 → 433 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["伊斯兰金属器（V&A）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"incident":"khurasan-ewer 重名并覆盖原 overlay；已 git 恢复并改名 -va",
 "new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["伊斯兰金属器"],"gaps_found":{"entries":4},"network":"V&A","verdict":"总396；重名事故已修复；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle114":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle114":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **392**（L2 388 / L3 4 / L1 0） |","| 条目 | **396**（L2 392 / L3 4 / L1 0） |"),("| 来源 | **521**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **525**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **429**，站内断链 **0** |","| 页面 | **433**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **392** | L2 388 / L3 4 / **L1 0** |","| 条目总数 | **396** | L2 392 / L3 4 / **L1 0** |"),("| 来源库 | **521**（另 11 条预备来源未计入） |","| 来源库 | **525**（另 11 条预备来源未计入） |"),("| 站点页面 | **429** |","| 站点页面 | **433** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **392**（L2 388 / L3 4，**无 L1**） |","| 条目 | **396**（L2 392 / L3 4，**无 L1**） |"),("| 来源 | **521**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **525**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **429** |","| 站点页面 | **433** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)