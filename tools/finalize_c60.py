# -*- coding: utf-8 -*-
"""Cycle60 收尾：D064 + METRICS/SATURATION/REPORT/PROGRESS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D064 — Cycle60 首次全站可用性审计（243 页）：1 处跳级已修，并成为体检第 11 步
- **决定**：新写 `tools/usability_c60.py`，对**全部 243 页**做 8 项结构检查并接入 `audit_all`（第 11 步）。
- **检查项与结果**：
  | 检查 | 结果 |
  |---|---|
  | 每页恰好一个 `<h1>` | 0 问题 |
  | 标题层级不跳级 | **1 问题**：`units.html` 的 h1 直接跳到 h3 → **已修** |
  | `<meta name=viewport>` | 0 问题 |
  | `<html lang=…>` | 0 问题 |
  | 来源表含 `<thead>` | 0 问题 |
  | 页内锚点 `href="#x"` 有对应 id | 0 问题 |
  | **无 `<img>`**（本站政策：只用自绘 SVG） | 0 问题 |
  | 有跳转链接与 `<nav>` | 0 问题 |
  | `style.css` 无 >900px 固定宽度（防横向溢出） | 0 处 |
- **修法**：`units.html` 原本是「h1 + 26 张卡片各用 h3」。改为**先按域分 7 组 h2**（西方艺术史 / 中国艺术 / 其他地区艺术 / 西方音乐史 / 中国音乐 / 作品档案 / 导读比较与术语），卡片仍为 h3。既修好层级，也让 26 个单元**分块可扫**。
- **验证**：修后全站 0 问题；守卫做**注入测试**（删掉一个 h2 → 报 `skip_level` 且 **rc=1**；还原 → rc=0）。顺带再次踩到「管道吞退出码」——`| head` 会让 `$?` 变成 head 的状态，**必须直接运行才看得到真实返回码**。
- **可逆方式**：还原 `build_units_index` 的平铺结构、移除审计第 11 步。
- **代价**：`units.html` 多出 7 个小标题；体检增至 **11 步**（约多 1 秒）。
""")

m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle60","date":"2026-11-23","status":"completed",
 "gap_methods":["全站可用性审计（243页，8项）"],"network":"partial",
 "new_entries":0,"fixes":1,
 "usability":{"pages":243,"issues_found":1,"issue":"units.html h1→h3 跳级","fixed":"加 7 个 h2 分组",
   "clean":["h1 唯一","viewport","lang","thead","锚点","无 img","skip link","nav","无过大固定宽度"]},
 "audit_steps":11,"guard_test":"删除一个 h2 → rc=1；还原 → rc=0（管道会吞退出码，需直跑）",
 "entries_total":208,"sources_total":339,"pages":243,
 "check_result":"errors=0","check_links_result":"broken=0(243页)","audit_all":"11/11 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle60","date":"2026-11-23","methods_used":["可用性审计"],
 "gaps_found":{"heading_skip":1},"network":"partial",
 "verdict":"243 页可用性审计，1 处跳级已修；体检增至 11 步；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)

P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle60"' not in t:
    block=('if cyc=="cycle60":\n'
           '    L.append("- **首次全站可用性审计（243 页）**，8 项结构检查：`h1` 唯一、标题不跳级、viewport、`lang`、'
           '来源表 `<thead>`、页内锚点、**无 `<img>`**（只用自绘 SVG）、跳转链接与 `nav`、以及 `style.css` 无 >900px 固定宽度。'
           '结果只有 **1 处问题**：`units.html` 的 h1 直接跳 h3 → 改为**按域分 7 组 h2**（西方艺术史/中国艺术/其他地区艺术/'
           '西方音乐史/中国音乐/作品档案/导读比较术语），26 个单元顺带分块可扫。修后**全站 0 问题**，'
           '并接入 `audit_all` 成为**第 11 步**（注入测试：删一个 h2 → rc=1，还原 → rc=0）。'
           '另记一条操作教训：**`| head` 会让 `$?` 变成 head 的退出码**，验证返回码必须直跑。站点 243 页，体检 11/11。")\n')
    anchor='if cyc=="cycle59":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])