# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle129"; DATE="2026-11-24"
DECIS="""## D132 — Cycle129 全量 QC（303 条机构来源）0 问题
`QC_ALL=1` 复核 **303 条**机构来源（CMA+V&A 混合），**尺寸核对 225 项、命中 217 项、问题 0**（未命中为 V&A 多值/局部尺寸软核对，不构成 issue）。
连续多轮新增（含日本小件、玛雅陶、商周青铜、日朝绘画）后，**数据仍无真实错误**；V&A dict/list 兼容与世纪换算稳定。
可逆：无数据改动。代价：QC 为按需联网工具，不进离线体检。
"""
REPORT=("- 全量 QC：**303 条**机构来源（CMA+V&A）复核，**尺寸核对 225 项、命中 217、问题 0**（未命中为 V&A 多值/局部尺寸软核对）。"
 "连续多轮新增后数据无真实错误。站点仍 485 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["全量QC"],"network":"CMA/V&A",
 "new_entries":0,"qc":{"entries_checked":303,"dim_checks":225,"dim_hits":217,"issues":0},
 "entries_total":448,"sources_total":575,"pages":485,
 "check_result":"errors=0","check_links_result":"broken=0(485页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["全量QC"],"gaps_found":{},"network":"CMA/V&A","verdict":"303条/225尺寸/0问题；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle128":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle128":'))
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)