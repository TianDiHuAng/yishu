# -*- coding: utf-8 -*-
"""Cycle78 收尾：D082（115 条机构来源全量复核：0 问题）+ METRICS/REPORT。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D082 — Cycle78 扩量后全量复核：115 条机构来源条目、尺寸 74/74 命中、0 真问题
- **背景**：自 Cycle56 那次复核后，本会话又新增约 115 条（含 100+ 条机构来源条目）。本轮做一次**全量**核对：逐条重抓机构记录，比对正文中的尺寸数字。
- **结果**：**受检 115 条、尺寸核对 74 项、命中 74 项、问题 0**。这一轮**没有抓到任何真实错误**——这与前几轮不同，如实记下。
- **但仍修了校验器两处误判（否则会虚报 4 项与 52 项）**：
  1. **多元尺寸记录**（如 `Overall: 49.5 cm; Bag: 21.5 x 19.6`、`Diameter of mouth: 15.6; Overall: 39.4 x 37.5`）：原实现假定记录的前两个数字就是「宽×高」一对，于是把 `49.5×21.5` 当作待查组合——必然找不到。改为**逐个数字都须在正文出现**。
  2. **英制换算混入**：记录形如 `25.6 x 37.5 cm (10 1/16 x 14 3/4 in.)`，原实现把括号内的英制也算进数字串（`101`、`1415`），于是 52 条被误报。改为**只取括号前的公制部分**。
- **意义**：这是本会话第二次证明「**先修工具再信结论**」的必要性（前两次为 D029 限流、D058 汇总行）。若不修，本轮会得出「半数条目尺寸与记录不符」这一**完全错误**的结论。
- **可逆方式**：无数据改动（纯工具修正）。
- **代价**：无；`qc_sample_c56.py` 仍是**按需联网**工具，不接入离线体检。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle78","date":"2026-11-23","status":"completed",
 "gap_methods":["扩量后机构来源全量复核"],"network":"partial: museum APIs ok",
 "new_entries":0,"fixes":2,
 "qc":{"entries_checked":115,"dim_checks":74,"dim_hits":74,"issues":0},
 "checker_bugs_fixed":["多元尺寸记录假定首两数为宽高对","英制换算混入数字提取"],
 "note":"本轮未发现真实错误（如实记录）",
 "entries_total":260,"sources_total":391,"pages":297,
 "check_result":"errors=0","check_links_result":"broken=0(297页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle78","date":"2026-11-23","methods_used":["全量尺寸复核"],
 "gaps_found":{},"network":"partial (museum APIs)",
 "verdict":"115 条机构来源全量复核：74/74 命中、0 真问题；修校验器 2 处误判；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle78"' not in t:
    block=('if cyc=="cycle78":\n'
           '    L.append("- 扩量后**全量复核**：**115 条机构来源条目**逐条重抓记录比对尺寸，**74 项核对、74 项命中、0 真问题**——'
           '本轮**没有抓到真实错误**（与 Cycle56 抓到 4 处不同，如实记录）。'
           '但仍修了校验器**两处误判**，否则会虚报 4 项与 **52 项**：①**多元尺寸记录**（`Overall: 49.5; Bag: 21.5 x 19.6`）'
           '被假定「首两数字即宽高对」；②**英制换算混入**（`25.6 x 37.5 cm (10 1/16 …)` 里的 `101`/`1415`）。'
           '改为「只取公制、逐个数字须出现」后归零。这是本会话**第二次**证明「先修工具再信结论」的必要性'
           '（前两次：D029 限流、D058 汇总行）。")\n')
    anchor='if cyc=="cycle77":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])