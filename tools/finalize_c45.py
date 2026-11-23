# -*- coding: utf-8 -*-
"""Cycle45 收尾：D048 + METRICS/SATURATION/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D048 — Cycle45 配对扫描收尾：再得 1 组、补 1 条第三来源、否决 1 组
- **扩大检索面**（V&A 侧 13 个系列/地名查询，CMA 侧 108 条），重合阈值降到 0.25 并排除「仅由系列词构成」的 V&A 记录，得到 70 个候选。
- **采纳 1 组**：`hokusai-nakahara-sagami`《相模中原》CMA 1940.997（约1835，25.1×37.8）+ V&A O422861（38.5×25.5）。条目 165 → **166**。
- **补强 1 条**：为 **《唐崎夜雨》** 增加 V&A 第二份印本 `vam-o407359` 作第三来源，并在待核实写明"三份印本的先后与印次差异未判定"。
- **否决 1 组（写明原因）**：`1924.964`《武藏千住堰》与 V&A O422881 标题、尺寸（37.8×25.4 对 37.2×25.9）、年代均吻合，但 **CMA 该件没有策展说明**，可写的只剩标题/系列/尺寸——**内容不足以支撑一条 L2 条目**，故不建，避免制造"空壳条目"。此判断与"宁可少写不可注水"一致。
- **其余候选（约 68 个）**：命中 V&A 的系列名记录、或同名异幅（Susaka 对 Shinagawa、Kambara 对 Asakusa、Fuji 1700s 对 1904），均否。
- **可逆方式**：删 1 条 overlay 与 catalog 元组、移除 3 条来源；`build_scope.py` 重跑。
- **代价**：配对空间接近用尽——同一系列的主要印本已被前两批覆盖，进一步扩充需换系列（如《名所江户百景》剩余幅、北斋《诸国名桥奇览》）或换机构（SMK/Europeana 藏品）。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle45","date":"2026-11-23","status":"completed",
 "gap_methods":["配对扫描扩大面（阈值0.25+排除系列记录）"],"network":"partial: museum APIs ok",
 "new_entries":1,"new_entry_ids":["hokusai-nakahara-sagami"],
 "source_upgrades":["hiroshige-karasaki-night-rain +vam-o407359（第三来源）"],
 "rejected":{"1924.964":"与 V&A O422881 完全吻合但 CMA 无策展说明，内容不足以成条"},
 "candidates":70,"new_sources":3,"sources_total":312,"entries_total":166,"pages":197,
 "check_result":"errors=0","check_links_result":"broken=0(197页)","audit_all":"8/8 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle45","date":"2026-11-23","methods_used":["配对扫描"],
 "gaps_found":{"entries":1,"source_upgrade":1},"network":"partial (museum APIs)",
 "verdict":"再得 1 组双机构（166）+1 条第三来源；1 组因无策展说明不建；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle45"' not in t:
    block=('if cyc=="cycle45":\n'
           '    L.append("- 配对扫描扩大面（V&A 侧 13 个系列/地名、CMA 侧 108 条，阈值降到 0.25 并排除「仅系列词」记录），70 个候选里：'
           '**采纳 1 组**《相模中原》（CMA 1940.997 + V&A O422861，双机构）→ 条目 **166**；'
           '**补强 1 条**：为《唐崎夜雨》加上 V&A 第二份印本 O407359 作第三来源；'
           '**否决 1 组并写明理由**：《武藏千住堰》与 V&A O422881 标题/尺寸/年代全吻合，但 **CMA 该件无策展说明**，'
           '可写的只剩标题与尺寸，内容不足以成条——不建空壳。'
           '其余候选多为系列名记录或同名异幅（Susaka 对 Shinagawa、Kambara 对 Asakusa）。站点 196 → 197 页，体检 8/8。")\n')
    anchor='if cyc=="cycle44":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")

for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 165（L2 159 / L3 6 / L1 0） |","| 条目 | 166（L2 160 / L3 6 / L1 0） |"),
    ("| 来源 | 309（全部 verified；隔离区 5 条不可核验） |","| 来源 | 312（全部 verified；隔离区 5 条不可核验） |"),
    ("| 页面 | 196，站内断链 **0** |","| 页面 | 197，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **165** | L2 159 / L3 6 / **L1 0** |","| 条目总数 | **166** | L2 160 / L3 6 / **L1 0** |"),
    ("| 来源库 | **309** |","| 来源库 | **312** |"),
    ("| 站点页面 | **196** |","| 站点页面 | **197** |")])]:
    s2=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in s2: s2=s2.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])