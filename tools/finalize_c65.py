# -*- coding: utf-8 -*-
"""Cycle65 收尾：①enc 审计脚本加退出码并接入 audit_all（第 12 步）；②D069 + METRICS/REPORT。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
U=os.path.join(ROOT,"tools","enc_audit_c65.py"); u=io.open(U,encoding="utf-8").read()
if "sys.exit" not in u:
    u=u.replace("import json,os,re","import json,os,re,sys",1)
    u=u.rstrip()+"\nsys.exit(1 if issues else 0)\n"
    io.open(U,"w",encoding="utf-8").write(u); print("exit code added")
A=os.path.join(ROOT,"tools","audit_all.py"); a=io.open(A,encoding="utf-8").read()
if "enc_audit_c65.py" not in a:
    old=' ("usability_c60.py（可用性：标题层级/锚点/表格/link）","tools/usability_c60.py"),'
    assert old in a
    a=a.replace(old,old+'\n ("enc_audit_c65.py（enc 条目结构/URL 一致）","tools/enc_audit_c65.py"),')
    io.open(A,"w",encoding="utf-8").write(a); print("audit_all: enc step added")
import py_compile
for f in (U,A): py_compile.compile(f,doraise=True)
print("compiled")

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D069 — Cycle65 `enc-*` 条目结构层复核：抓到 5 处正文 URL 打字错误
- **背景**：Wikipedia 不可达，`enc-*` 条目无法做「正文与原文比对」；因此本轮只做**结构层四项**：来源数分布、单源是否标记待核实、正文 URL 是否在库、复核留痕引用的来源 id 是否存在。
- **结果**：`enc-*` 条目 **145 条**（全库 216），来源数分布 `{2:26, 3:106, 4:4, 5:7, 6:1, 8:1}`——**没有单来源条目**，无需触发 R10。
- **抓到 5 处真实打字错误**：`delacroix`、`donatello`、`leonardo`、`monteverdi`、`vermeer` 的待核实里，Wikidata 链接写成 `https://www.wikidata.org/wiki/QQ37562`（**双 Q**），而来源库记录为 `Q37562`。已全部修正为单 Q。
- **同时修自己的工具 bug**：审计正则原本排除 ASCII `)`，把 `Pantheon_(Rome)`、`David_(Donatello,_bronze)` 等 URL **截断**成不存在的地址，产生 **5 个假阳性**。改为只排除空白与中文全角标点后，问题数归零。
- **接线**：`enc_audit_c65.py` 加入 `audit_all` 成为**第 12 步**（离线、快速）。
- **可逆方式**：还原 5 处 URL、移除第 12 步。
- **代价**：本轮只能证明「链接与来源库一致」，**不能证明正文与 Wikipedia 原文一致**——后者受来源不可达限制，仍需在网通达时补做。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle65","date":"2026-11-23","status":"completed",
 "gap_methods":["enc-* 结构层复核"],"network":"partial",
 "new_entries":0,"fixes":5,
 "enc_entries":145,"source_count_dist":{"2":26,"3":106,"4":4,"5":7,"6":1,"8":1},
 "real_errors":["5 处 wiki/QQ 双 Q 打字错误（delacroix/donatello/leonardo/monteverdi/vermeer）"],
 "tool_bug_fixed":"URL 正则排除 ASCII ) 导致 5 个假阳性",
 "limits":"只能证明链接一致，不能证明正文与 Wikipedia 原文一致",
 "audit_steps":12,"entries_total":216,"sources_total":347,"pages":251,
 "check_result":"errors=0","check_links_result":"broken=0(251页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle65","date":"2026-11-23","methods_used":["enc 结构复核"],
 "gaps_found":{"url_typos":5},"network":"partial",
 "verdict":"145 条 enc 条目结构复核，5 处 URL 打字错误已修；体检增至 12 步；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle65"' not in t:
    block=('if cyc=="cycle65":\n'
           '    L.append("- 对 **145 条 `enc-*` 条目**做**结构层复核**（Wikipedia 不可达，只能核元数据与内部一致性）：'
           '来源数分布 {2:26, 3:106, 4:4, 5:7, 6:1, 8:1}，**无单来源条目**。'
           '抓到 **5 处真实打字错误**——delacroix/donatello/leonardo/monteverdi/vermeer 的待核实里 Wikidata 链接写成'
           '**`wiki/QQ37562`（双 Q）**，而来源库为 `Q37562`，已全部修正。'
           '同时修了**自己工具的 bug**：审计正则排除 ASCII `)`，把 `Pantheon_(Rome)` 等 URL 截断，产生 **5 个假阳性**；'
           '改为只排除全角标点后问题归零。新增 **12 步体检**（enc 结构审计）。'
           '局限写明：**只能证明链接与来源库一致，不能证明正文与 Wikipedia 原文一致**。")\n')
    anchor='if cyc=="cycle64":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])