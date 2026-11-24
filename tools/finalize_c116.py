# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle116"; DATE="2026-11-24"
IDS=["urbino-cittern","tielke-guitar","baroque-oboe-holland","bowie-koto-heroes"]
ET,ST,PG=400,529,437
DECIS="""## D119 — Cycle116 乐器再补 4 条（396 → 400；达到 400 条目里程碑）
以 V&A 补 `music-instruments`：`urbino-cittern`（乌尔比诺 Citrin，1582，**核心**）、`tielke-guitar`（Tielke 细木吉他，1693，**核心**）、`baroque-oboe-holland`（荷兰巴洛克双簧管，约1700）、`bowie-koto-heroes`（鲍伊《Heroes》「Moss Garden」所用玩具古筝，约1977，**核心**）。
要点：①Citrin 以**金属弦/品、拨片扫奏**为特征，1574 年 Vitale 出版物驱动其在意/中欧流行；②Tielke 吉他以**玳瑁/象牙/锡细木镶嵌**（花卉/丘比特/带铭古典场景）著称，今存十五把；③巴洛克双簧管**由肖姆管（hautbois）演变**，喇叭口雕**奏乐场景**（乐器自画像）；④鲍伊筝为**模塑塑料 13 弦玩具**，证明东方乐器借用电可经**大众消费制品**。
**写前查重**已执行（grep 4 个 id 均无冲突）。summary 截断处（Tielke「floral m…」）未补写。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（V&A）；乐器 17→21 条。
"""
REPORT=("- 乐器再补 4 条（396 → 400，V&A）：乌尔比诺 Citrin（1582）、Tielke 细木吉他（1693）、荷兰巴洛克双簧管（约1700）、鲍伊《Heroes》玩具古筝（约1977）。"
 "①Citrin 以**金属弦/品、拨片扫奏**，1574 年出版物驱动流行；②Tielke 吉他以**玳瑁/象牙/锡镶嵌**（花卉/丘比特/古典场景）著称；"
 "③巴洛克双簧管**由肖姆管演变**、喇叭口**雕奏乐场景**（乐器自画像）；④鲍伊筝为**塑料 13 弦玩具**——东方乐器借用可经**大众消费制品**。"
 "**写前查重**通过。站点 433 → 437 页，体检 12/12。**达到 400 条目**；数量里程碑不等于覆盖均衡。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["乐器实物（V&A）续"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"milestone":"400 entries","new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["乐器实物续"],"gaps_found":{"entries":4},"network":"V&A","verdict":"达到400条目；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle115":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle115":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **396**（L2 392 / L3 4 / L1 0） |","| 条目 | **400**（L2 396 / L3 4 / L1 0） |"),("| 来源 | **525**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **529**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **433**，站内断链 **0** |","| 页面 | **437**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **396** | L2 392 / L3 4 / **L1 0** |","| 条目总数 | **400** | L2 396 / L3 4 / **L1 0** |"),("| 来源库 | **525**（另 11 条预备来源未计入） |","| 来源库 | **529**（另 11 条预备来源未计入） |"),("| 站点页面 | **433** |","| 站点页面 | **437** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **396**（L2 392 / L3 4，**无 L1**） |","| 条目 | **400**（L2 396 / L3 4，**无 L1**） |"),("| 来源 | **525**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **529**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **433** |","| 站点页面 | **437** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)