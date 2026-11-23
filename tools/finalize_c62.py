# -*- coding: utf-8 -*-
"""Cycle62 收尾：D066 + METRICS/SATURATION/REPORT。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D066 — Cycle62 SVG 图示窄屏不可读：改为「宁滚动不缩小」，并加守卫
- **量化问题**：全部图示 `viewBox="0 0 760 300"`、标签字号 15px、`.svg-frame svg{width:100%}`。于是在 **320px 视口**下缩放约 **0.37**，标签只剩 **≈5.5px**（副标签 12px→4.4px）；600px 视口也只有 ≈11px。**结论：窄屏上图注不可读**，而图示是本站唯一的视觉表达手段（不含图片）。
- **修法（两条）**：
  1. **窄屏改为横向滚动 + 最小宽度**：`@media (max-width:700px){.svg-frame{overflow-x:auto}.svg-frame svg{width:680px;min-width:680px}}`——在窄屏上**宁可让图示框内横向滚动，也不把它缩到读不清**（与 D065 表格的处理同构）。320px 视口下缩放 0.89，标签约 **14.3px**。
  2. **字号整体略增**：标签 15→**16px**、副标签 12→**13px**（对宽屏同样有益）。
- **验证**：`assets/style.css` 已含该媒体查询与 min-width；可用性审计**新增第 10 项**（缺少该规则即报）。
- **代价**：窄屏下图示需在框内横向滑动才能看完；这是刻意的取舍——**可读优先于「一屏装下」**。宽屏不受影响。
- **可逆方式**：删媒体查询那一条 CSS 与字号调整。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle62","date":"2026-11-23","status":"completed",
 "gap_methods":["SVG 窄屏可读性审计"],"network":"partial",
 "new_entries":0,"fixes":2,
 "problem":{"viewBox":"760x300","label_px":15,"scale_at_320px":0.37,"rendered_label_px":5.5},
 "fix":{"media_query":"max-width:700px → svg min-width 680px + frame overflow-x:auto","font_bump":"label 15→16px, sub 12→13px"},
 "after":{"scale_at_320px":0.89,"rendered_label_px":14.3},
 "new_check":"usability 第 10 项（须含窄屏 SVG 规则）","audit_steps":11,
 "entries_total":208,"sources_total":339,"pages":243,
 "check_result":"errors=0","check_links_result":"broken=0(243页)","audit_all":"11/11 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle62","date":"2026-11-23","methods_used":["SVG 可读性"],
 "gaps_found":{"narrow_svg_illegible":1},"network":"partial",
 "verdict":"SVG 窄屏改为滚动+最小宽度，标签 5.5px→14.3px；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle62"' not in t:
    block=('if cyc=="cycle62":\n'
           '    L.append("- 查**SVG 图示窄屏可读性**，先做量化：图示 `viewBox=760×300`、标签 15px、`width:100%`，'
           '于是 **320px 视口下缩放仅 0.37，标签≈5.5px**（副标签 4.4px）——**窄屏上图注不可读**，而图示是本站唯一的视觉手段。'
           '修法：**宁滚动不缩小**——`@media(max-width:700px)` 令 `.svg-frame` 横向滚动、svg 固定 680px，'
           '320px 下标签回到 **≈14.3px**；并把基础字号标签 15→16、副标签 12→13（对宽屏亦有裨益）。'
           '可用性审计**新增第 10 项**（缺该规则即报）。代价写明：窄屏需在框内横滑，**可读优先于一屏装下**。站点 243 页，体检 11/11。")\n')
    anchor='if cyc=="cycle61":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50])