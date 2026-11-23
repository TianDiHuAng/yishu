# -*- coding: utf-8 -*-
"""Cycle56 收尾：D060 + METRICS/SATURATION/REPORT/PROGRESS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D060 — Cycle56 抽查复核：抓到 4 条条目的**事实性错误**（"CMA 未给尺寸"是错的）
- **方法**：先做 10% 抽样（20 条），再把范围扩到**全部引用机构记录的 55 条**，逐条**重新抓取机构记录**并核对正文中的**尺寸与年代**是否与记录一致。
- **抓到的真问题（4 条）**：`hokusai-red-fuji`、`hiroshige-shono`、`hiroshige-ohashi-atake`、`hokusai-nakahara-sagami` 此前在待核实里写「**克利夫兰记录未给尺寸，故尺寸仅据 V&A 一家**」——经复核，**该馆记录确有 measurements 字段**（分别为 25.6×37.5、38×25.4、35.3×23.2、25.1×37.8 厘米）。这句话是**事实性错误**，已按实测值更正，并在各条待核实末尾留下「【已复核·Cycle56】此前误称…已按实测值更正」。
- **顺带的诚实收获**：更正后两馆尺寸差异变得可见且**必须写出**——《庄野 白雨》CMA 38×25.4 对 V&A 22.9×34.9、《大桥》35.3×23.2 对 14.13×9.04（差数倍），成因（版次/裁切/著录方向）**未判定**，条目照实并列。
- **校验器本身也有三个 bug（已修）**：①用 `cd[:4]` 切年代，得到「c. 1」这类垃圾 → 改为提取四位年份；②`norm()` 把「 x 」的空格删了，导致尺寸检查恒为 0 项 → 改用原始串判断；③世纪型年代（"c. 1500s or mid-1900s"、"late 1600s"）与中文「16世纪」不匹配 → 这类跳过。**不修这些，"发现问题 21 项"里 17 项都是误报**。
- **最终结论**：55 条机构来源条目，**尺寸核对 36 项 / 命中 36 项**，问题 0。工具：`tools/qc_sample_c56.py`（`QC_ALL=1` 为全量模式，需联网，未接入离线体检）。
- **可逆方式**：删除 4 条的更正段落、还原误称（不建议）。
- **代价**：4 条待核实变长；`hokusai-red-fuji` 等三条的「单一机构尺寸」论点不再成立（现已双馆并列）。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle56","date":"2026-11-23","status":"completed",
 "gap_methods":["抽样复核（10%）+ 机构来源全量复核"],"network":"partial: museum APIs ok",
 "new_entries":0,"fixes":4,
 "sample":20,"full_check_entries":55,
 "real_errors":["hokusai-red-fuji/hiroshige-shono/hiroshige-ohashi-atake/hokusai-nakahara-sagami 误称「CMA 未给尺寸」"],
 "checker_bugs_fixed":["cd[:4] 切年代","norm 删空格致尺寸检查恒 0","世纪型年代不匹配"],
 "dim_checks":36,"dim_hits":36,"issues":0,
 "entries_total":200,"sources_total":331,"pages":235,
 "check_result":"errors=0","check_links_result":"broken=0(235页)","audit_all":"10/10 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle56","date":"2026-11-23","methods_used":["抽样+全量复核"],
 "gaps_found":{"factual_errors":4},"network":"partial (museum APIs)",
 "verdict":"抽查抓到 4 条事实性错误并更正；55 条机构来源尺寸 36/36 命中；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle56"' not in t:
    block=('if cyc=="cycle56":\n'
           '    L.append("- **抽查复核抓到真错误**：先 10% 抽样（20 条），再扩到**全部 55 条机构来源条目**，'
           '逐条重抓机构记录核对尺寸与年代。结果 4 条浮世绘/北斋条目此前写「**克利夫兰记录未给尺寸**」——'
           '**该馆记录确有 measurements**（25.6×37.5、38×25.4、35.3×23.2、25.1×37.8 厘米），这句话是事实性错误，已更正并留下复核痕。'
           '更正后两馆尺寸差异必须写出：《庄野》38×25.4 对 22.9×34.9、《大桥》35.3×23.2 对 14.13×9.04，成因未判定。'
           '另修**校验器自身三个 bug**（年代切片、norm 删空格致尺寸恒 0、世纪型年代不匹配）——'
           '不修的话「发现问题 21 项」里 17 项都是误报。最终：尺寸核对 **36/36 命中、问题 0**。")\n')
    anchor='if cyc=="cycle55":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])