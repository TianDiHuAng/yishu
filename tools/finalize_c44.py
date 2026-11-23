# -*- coding: utf-8 -*-
"""Cycle44 收尾：D047 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D047 — Cycle44 按系列批量配对：再得 4 组「同作品·双机构」（161 → 165）
- **方法**：不再逐条猜标题，而是**按系列名**在 V&A 双侧检索（`Fugaku sanjurokkei` / `Meisho Edo hyakkei` / `Tokaido gojusan tsugi` / `Hyakunin isshu` / `Omi hakkei`，共 221 条 V&A 记录池），再与 CMA 候选按**变音折叠后的词集合重合度**比对，人工复核年代后采纳。
- **结果（4 组，均双机构）**：
  1. `hiroshige-ryogoku-fireworks`《两国花火》CMA 1940.986（1858，33.7×22）+ V&A O420241（36.2×24.8，该馆未记年代）；
  2. `hiroshige-karasaki-night-rain`《唐崎夜雨》CMA 1985.312（c.1835，24.4×36.8）+ V&A O423295（22.9×35.6）；
  3. `hokusai-muneyuki-poem`《源宗于朝臣》CMA 1985.327（1835–36）+ V&A O422853（24.92×37.3）；
  4. `hokusai-hitomaro-poem`《柿本人麻吕》CMA 1930.190（25.8×37.8）+ V&A O424258（**35.6×24.1，方向相反**）。
- **同批否决**：9 个自动候选里 5 个被判否——命中 V&A 的"系列名记录"而非具体印本（O422860、O420576），或同名异幅（Kambara 对 Asakusa）。**否决记录详见 reports/pairs_c44.json 与本节**。
- **和歌处理**：CMA 记录附有英译（《唐崎夜雨》署名 Matthi Forrer）。本批条目**只述其意、不整段迻录**，并注明译者与"未核原书"。
- **尺寸反向问题**：V&A 的《柿本人麻吕》著录为高35.6×宽24.1，与 CMA 的25.8×37.8 方向相反——条目**并列两馆记录并列入待核实**，不擅自统一。
- **可逆方式**：删 4 条 overlay 与 catalog 元组、移除 8 条来源，重跑 `build_scope.py`。
- **代价**：V&A 记录普遍**不记年代**，故 4 条的断代实际只有 CMA 一家；这一点已在每条待核实首条写明，未伪装成双源断代。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle44","date":"2026-11-23","status":"completed",
 "gap_methods":["按系列批量配对（CMA↔V&A）"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["hiroshige-ryogoku-fireworks","hiroshige-karasaki-night-rain","hokusai-muneyuki-poem","hokusai-hitomaro-poem"],
 "dual_institution_all":True,"candidates_scanned":9,"rejected":5,
 "reject_reasons":"命中V&A「系列名记录」而非具体印本（O422860/O420576）；同名异幅（Kambara vs Asakusa）",
 "new_sources":8,"sources_total":309,"entries_total":165,"pages":196,
 "caveat":"V&A 记录普遍不记年代，断代仅 CMA 一家（已在各条待核实写明）",
 "check_result":"errors=0","check_links_result":"broken=0(196页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle44","date":"2026-11-23","methods_used":["系列批量配对"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)",
 "verdict":"4 组同作品双机构（165）；5 候选被否并记录原因；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle44"' not in t:
    block=('if cyc=="cycle44":\n'
           '    L.append("- 配对方法升级为**按系列批量比对**：在 V&A 侧以系列名检索（36 Views / 100 Edo / 53 Stations / 100 Poems / 8 Views Omi，'
           '共 221 条记录池），再与 CMA 候选做变音折叠后的词集重合度比对，人工复核年代。'
           '**再得 4 组同作品双机构（161 → 165）**：《两国花火》《唐崎夜雨》《源宗于朝臣》《柿本人麻吕》。'
           '同批 9 个自动候选里**否决 5 个**——命中 V&A 的「系列名记录」而非具体印本（O422860 / O420576），或同名异幅（Kambara 对 Asakusa）。'
           '两处如实记录：V&A 普遍**不记年代**，故断代仍只有 CMA 一家（写明未伪装成双源）；'
           '《柿本人麻吕》两馆尺寸**方向相反**（35.6×24.1 对 25.8×37.8），并列不统一。站点 192 → 196 页，体检 8/8。")\n')
    anchor='if cyc=="cycle43":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 161（L2 155 / L3 6 / L1 0） |","| 条目 | 165（L2 159 / L3 6 / L1 0） |"),
    ("| 来源 | 301（全部 verified；隔离区 5 条不可核验） |","| 来源 | 309（全部 verified；隔离区 5 条不可核验） |"),
    ("| 页面 | 192，站内断链 **0** |","| 页面 | 196，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **161** | L2 155 / L3 6 / **L1 0** |","| 条目总数 | **165** | L2 159 / L3 6 / **L1 0** |"),
    ("| 来源库 | **301** |","| 来源库 | **309** |"),
    ("| 站点页面 | **192** |","| 站点页面 | **196** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-150:])