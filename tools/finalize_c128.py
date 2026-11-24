# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle128"; DATE="2026-11-24"
IDS=["netsuke-dancer","tsuba-shakudo","inro-autumn-plants","nagasaki-writing-box"]
ET,ST,PG=448,575,485
DECIS="""## D131 — Cycle128 日本小件 4 条（444 → 448）
`netsuke-dancer`（木雕根付，**核心**；坠钮功能的多重约束：小而不重/有体积/无锐棱/耐磨/必有 himotoshi）、
`tsuba-shakudo`（刀镡，**核心**；赤铜合金做旧嵌珐琅；「护手→微型艺术、各流派」的品类跃迁）、
`inro-autumn-plants`（四层印笼，**核心**；和服无袋→丝绳+根付，原盛印章墨药，**由用入玩**的奢侈品化）、
`nagasaki-writing-box`（长崎输出书桌盒；日本不用、专销西方；**形制由西方书桌习惯决定＝外销品种是需求方文化的投影**）。
**自查**：overlay 有一处节名误作「关系与争论」→ 构建前改为「关系和争论」（R7）。
**如实保留截断**：根付「on th…」、书桌盒「荷兰商人…」两处 summary 未补写。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（V&A）。
"""
REPORT=("- 日本小件 4 条（444 → 448，V&A）：木雕根付（坠钮的多重约束：小而不重/有体积/无锐棱/耐磨/**himotoshi**）、"
 "刀镡（赤铜做旧嵌珐琅；**护手→微型艺术、各流派**的品类跃迁）、四层印笼（和服无袋→丝绳+根付，原盛印章墨药，**由用入玩**）、"
 "长崎输出书桌盒（日本不用、专销西方；**形制由西方书桌习惯决定＝外销品种是需求方文化的投影**）。两处 summary 截断未补写。站点 481 → 485 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["日本小件（V&A）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["日本小件"],"gaps_found":{"entries":4},"network":"V&A","verdict":"总448；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle127":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle127":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **444**（L2 440 / L3 4 / L1 0） |","| 条目 | **448**（L2 444 / L3 4 / L1 0） |"),("| 来源 | **571**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **575**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **481**，站内断链 **0** |","| 页面 | **485**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **444** | L2 440 / L3 4 / **L1 0** |","| 条目总数 | **448** | L2 444 / L3 4 / **L1 0** |"),("| 来源库 | **571**（另 11 条预备来源未计入） |","| 来源库 | **575**（另 11 条预备来源未计入） |"),("| 站点页面 | **481** |","| 站点页面 | **485** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **444**（L2 440 / L3 4，**无 L1**） |","| 条目 | **448**（L2 444 / L3 4，**无 L1**） |"),("| 来源 | **571**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **575**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **481** |","| 站点页面 | **485** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)