# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle113"; DATE="2026-11-24"
IDS=["baffo-harpsichord","maler-lute","northumberland-bagpipe","stradivari-violin"]
ET,ST,PG=392,521,429
DECIS="""## D116 — Cycle113 乐器 4 条（388 → 392；music-instruments 13→17）
以 V&A 实物扩充 `music-instruments`（绕开音乐文本 BLOCKER 的合规路径）：`baffo-harpsichord`（Baffo 羽管键琴，1574，**核心**）、`maler-lute`（Maler 鲁特琴，约1540，**核心**）、`northumberland-bagpipe`（诺森伯兰风笛，约1830，**核心**）、`stradivari-violin`（斯特拉迪瓦里小提琴，1699，**核心**）。
要点：①Baffo 琴 50 键 GG/BB–c3、两列同音弦、柏木音板哥特圆饰，兼饰**伊斯兰纹样**与古典母题；②Maler 鲁特琴**仅肋为原件**、颈与头约1967补配；③诺森伯兰风笛以**风箱**鼓气（非口吹）、音色柔和、多室内；④斯氏小提琴明言**漆非原漆、颈后配、琴头取自另一琴**，条目据此拆分「可核结构」与「不可复现的漆」。
**如实保留截断**：Maler 籍贯（「德国或…」）、Baffo 截断原因、诺森伯兰入藏细节均**未补写**。
可逆：删 4 条 overlay 与 catalog 元组、移除 4 条来源。代价：均单机构（V&A）；乐器 13→17 条。
"""
REPORT=("- 乐器实物 4 条（388 → 392，V&A）：Baffo 羽管键琴（1574）、Maler 鲁特琴（约1540）、诺森伯兰风笛（约1830）、斯特拉迪瓦里小提琴（1699）。"
 "①Baffo 琴 50 键、柏木音板哥特圆饰、兼饰**伊斯兰纹样**；②Maler 鲁特**仅肋为原件**、颈/头约1967补配；③诺森伯兰风笛**风箱驱动、非口吹**、音色柔和室内；"
 "④斯氏小提琴**漆非原漆、颈后配、琴头取自另一琴**，条目拆「可核结构」与「失传之漆」。此为绕开音乐文本 BLOCKER 的合规路径（器物可核）。站点 425 → 429 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["乐器实物（V&A）"],"network":"V&A 200",
 "new_entries":4,"new_entry_ids":IDS,"new_sources":4,"sources_total":ST,"entries_total":ET,"pages":PG,
 "check_result":"errors=0","check_links_result":"broken=0(%d页)"%PG,"audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["乐器实物"],"gaps_found":{"entries":4},"network":"V&A","verdict":"乐器 13→17（总392）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle112":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle112":'))
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),[("| 条目 | **388**（L2 384 / L3 4 / L1 0） |","| 条目 | **392**（L2 388 / L3 4 / L1 0） |"),("| 来源 | **517**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **521**（全部被引用且 verified；隔离区 5 + 预备 11） |"),("| 页面 | **425**，站内断链 **0** |","| 页面 | **429**，站内断链 **0** |")]),
 (os.path.join(ROOT,"PROJECT_STATUS.md"),[("| 条目总数 | **388** | L2 384 / L3 4 / **L1 0** |","| 条目总数 | **392** | L2 388 / L3 4 / **L1 0** |"),("| 来源库 | **517**（另 11 条预备来源未计入） |","| 来源库 | **521**（另 11 条预备来源未计入） |"),("| 站点页面 | **425** |","| 站点页面 | **429** |")]),
 (os.path.join(ROOT,"README.md"),[("| 条目 | **388**（L2 384 / L3 4，**无 L1**） |","| 条目 | **392**（L2 388 / L3 4，**无 L1**） |"),("| 来源 | **517**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **521**（全部 verified；另有 11 预备 / 5 隔离） |"),("| 站点页面 | **425** |","| 站点页面 | **429** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)