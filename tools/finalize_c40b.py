# -*- coding: utf-8 -*-
"""Cycle40 收尾补完：REPORT 生成器加 cycle40 段（锚点=cycle38）+ PROGRESS 数字更新。"""
import io,os,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle40"' not in t:
    block=('if cyc=="cycle40":\n'
           '    L.append("- 通道再测绘后的实质扩充：Wikipedia / Wikidata / archive.org 本轮均为 000，'
           '但博物馆开放数据 API 全部可达（Cleveland 开放数据 API、V&A API v2、Met 对象端点、Europeana、SMK）。'
           '据此新增 4 个条目（145 → 149）：德加、罗丹、罗丹《青铜时代》、米友仁《云山图》；'
           '来源类型新增「权威机构藏品记录」，URL 指向实测 200 的 API 端点（机构网页 000 已在 verified_note 注明）。'
           '独立性如实区分：罗丹为 CMA + V&A 双机构；其余 3 条单机构，按 R10 标 needs_verification 并在待核实首条写明。'
           '本次首次取得可引用的机构级正文（策展说明与艺术家传记），评价性判断仍一律留白。'
           '站点 176 → 180 页，八步体检 8/8。")\n')
    anchor='if cyc=="cycle38":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor, block+anchor))
    print("report block added")
PP=os.path.join(ROOT,"PROGRESS.md"); s2=io.open(PP,encoding="utf-8").read()
for a,b in [("| 条目 | 145（L2 139 / L3 6 / L1 0） |","| 条目 | 149（L2 143 / L3 6 / L1 0） |"),
            ("| 来源 | 279（全部 verified；隔离区 5 条不可核验） |","| 来源 | 283（全部 verified；隔离区 5 条不可核验） |"),
            ("| 页面 | 176，站内断链 **0** |","| 页面 | 180，站内断链 **0** |"),
            ("- 当前轮次：**Cycle 39/40 收尾已完成（结构完成 → 维护模式待命）**",
             "- 当前轮次：**Cycle 40 已完成（新增 4 条目：145 → 149）**")]:
    if a in s2: s2=s2.replace(a,b)
io.open(PP,"w",encoding="utf-8").write(s2)
r=subprocess.run([sys.executable,"-X","utf8",os.path.join(ROOT,"tools","build_report_autonomous.py")],
                 cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:60],(r.stderr or "").strip()[-160:])