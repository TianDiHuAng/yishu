# -*- coding: utf-8 -*-
"""Cycle54 补记：D058（audit_all 汇总行漏算编译失败——第二个"静默失败"）。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D058 — Cycle54 抓到第二个「静默失败」：audit_all 的汇总行漏算工具编译失败
- **发现过程**：本轮我把 `build_report_autonomous.py` 写坏（ASCII 引号，第 5 次同类事故），提交后跑体检，屏幕上 **py_compile 那行明明显示 `FAIL`**，但最后一行仍打印「失败项：0」。我做注入测试（临时塞语法错误）确认：**逐行能报 FAIL、退出码确实为 1，但汇总打印漏算了编译失败**（`print("失败项：%d"%fails)` 未加 `fails_compile`）。
- **危害**：本轮我正是**读了那行「失败项：0」才把坏文件提交上去的**（提交 `f4a2849` 内含语法错误的生成器）。也就是说，**汇总行在骗人**，而人看的是汇总行。
- **决定**：修正汇总为 `失败项：N（其中工具编译失败 M）`，并同步写入 `reports/audit_all.json` 的 `fails` / `fails_compile` 字段。
- **验证**：注入语法错误 → 打印「失败项：1（其中工具编译失败 1）」且 **退出码 1**；还原 → 「失败项：0（其中工具编译失败 0）」且 **退出码 0**。
- **同类归纳**：这与 D029（把 Wikidata 限流当成"无数据"）属同一类错误——**聚合/包装层把失败吞掉**。教训：**凡"汇总型"输出，必须与退出码使用同一份计数**，且要做注入验证。
- **可逆方式**：还原打印语句（不建议）。
- **代价**：无（纯修复）；但提醒后续所有汇总脚本都需同样体检。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle54b","date":"2026-11-23","status":"completed",
 "gap_methods":["守卫自检（注入测试）"],"network":"partial",
 "new_entries":0,"fixes":1,
 "finding":"audit_all 汇总行漏算 fails_compile：逐行显示 FAIL、退出码为 1，但打印「失败项：0」——本轮据此误提交了语法错误的生成器",
 "fix":"打印含编译失败并单列；json 同步 fails/fails_compile",
 "verification":"注入→打印1且rc=1；还原→打印0且rc=0",
 "audit_steps":10,"entries_total":195,"sources_total":326,"pages":230,
 "check_result":"errors=0","check_links_result":"broken=0(230页)","audit_all":"10/10 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle54b","date":"2026-11-23","methods_used":["守卫自检"],
 "gaps_found":{"silent_failure":1},"network":"partial",
 "verdict":"修汇总行静默失败（第二个同类问题，首个为 D029 限流）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle54b"' not in t:
    block=('if cyc=="cycle54b":\n'
           '    L.append("- 抓到**第二个「静默失败」**：我把 REPORT 生成器写坏（ASCII 引号，第 5 次）后跑体检，'
           '屏幕上 py_compile 那行**明明显示 FAIL**，但汇总行仍打印**失败项：0**——逐行能报错、'
           '退出码其实为 1，但**打印漏算了编译失败**（`print` 未加 `fails_compile`）。'
           '危害是实打实的：本轮我正是**读了那行「失败项：0」才把坏文件提交上去**。'
           '已修正为「失败项：N（其中工具编译失败 M）」并同步 JSON；注入测试：破损→打印 1 且 rc=1，还原→打印 0 且 rc=0。'
           '与 D029（把限流当无数据）同类——**聚合层把失败吞掉**；凡汇总型输出必须与退出码共用同一份计数。")\n')
    anchor='if cyc=="cycle54":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-120:])