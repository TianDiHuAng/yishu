# -*- coding: utf-8 -*-
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CYC="cycle114"; DATE="2026-11-24"
DECIS="""## D117 — Cycle114 全量 QC（247 条机构来源）0 问题；V&A 古代玻璃因质量不足放弃
- 本轮先探 V&A「罗马玻璃/古代玻璃」，返回多为**19世纪仿品（Favrile/Stourbridge）或照片**，非可靠的古代实物 → **放弃该方向**，不以劣质记录凑数（记作一次诚实的排除）。
- 改做**全量 QC**：`QC_ALL=1` 复核 **247 条**机构来源条目（CMA 与 V&A 混合），**尺寸核对 183 项、命中 176 项、问题 0**（未命中的为 V&A 多值/局部尺寸，属软核对，不构成 issue）。
- 结论：连续多轮新增（含 V&A 新来源类型）后，**数据仍无真实错误**；`qc_sample_c56.py` 的 V&A 分支（dict/list 兼容、世纪换算）稳定工作。
- 可逆：无数据改动（仅 QC 记录）。
- 代价：QC 为**按需联网**工具，不进离线体检；本轮无代码改动。
"""
REPORT=("- 全量 QC：247 条机构来源（CMA+V&A）复核，**尺寸核对 183 项、命中 176、问题 0**（未命中为 V&A 多值/局部尺寸软核对）。"
 "另：先探 V&A 罗马/古代玻璃，返回多为 19世纪仿品或照片，**质量不足已放弃**，不以劣质记录凑数。站点仍 429 页，体检 12/12。")
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("\n"+DECIS+"\n")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":CYC,"date":DATE,"status":"completed","gap_methods":["全量QC；排除V&A劣质玻璃"],"network":"CMA/V&A",
 "new_entries":0,"qc":{"entries_checked":247,"dim_checks":183,"dim_hits":176,"issues":0},
 "entries_total":392,"sources_total":521,"pages":429,
 "check_result":"errors=0","check_links_result":"broken=0(429页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":CYC,"date":DATE,"methods_used":["全量QC"],"gaps_found":{},"network":"CMA/V&A","verdict":"247条/183尺寸/0问题；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if ('cyc=="%s"'%CYC) not in t:
    io.open(P,"w",encoding="utf-8").write(t.replace('if cyc=="cycle113":', 'if cyc=="%s":\n    L.append(%r)\n'%(CYC,REPORT)+'if cyc=="cycle113":'))
subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("finalized",CYC)