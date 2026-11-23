# -*- coding: utf-8 -*-
"""Cycle95 收尾：D098 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D098 — Cycle95 非洲面具/雕像 4 条（320 → 324）；R22 再次拦截点号 id
新增 `luba-bowl-figure`（卢巴持碗女像，19—20世纪，**核心**）、`dogon-female-figure`（多贡举臂女像，约1940，**核心**）、
`dogon-satimbe-mask`（多贡 satimbe 面具，20世纪）、`kuba-bwoom-mask`（库巴 bwoom 面具，1800s，**核心**）。
四处要点：①卢巴美学「**器物的美影响其效力**」；像身残留 mpemba 白垩、菱形瘢纹、白/蓝珠或象征月亮与 Mbidi Kiluwe；且「多数此类作品由男性创作并拥有」；
②多贡女像的举臂有**三说**（Amma 所造第一个存在／求雨时的黑化像／播种仪式），并列不裁定；
③satimbe 面具用于 **dama 终丧**，顶部 Yasigine 关乎**每60年一次的 sigi**；
④bwoom 与一女一男面具组成**三件一组**，是「库巴王国建立」重演的主角；**都城之外**则见于男子入会会社。
**工程记录**：元组里再次误写 `cma-1935.304`（点号），**R22 立刻报「来源 id 含非法字符」**并阻断构建；改为连字符后通过。R22 自 Cycle80 建立以来已第 2 次拦住此类错误。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；非洲 15 → 19 条（含本批），但区域仍集中西非/中非/东非。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle95","date":"2026-11-23","status":"completed",
 "gap_methods":["非洲面具/雕像"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["luba-bowl-figure","dogon-female-figure","dogon-satimbe-mask","kuba-bwoom-mask"],
 "africa_objects":4,"new_sources":4,"sources_total":455,"entries_total":324,"pages":361,
 "checker_catch":"R22 拦住 cma-1935.304 点号 id（第2次）",
 "check_result":"errors=0","check_links_result":"broken=0(361页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle95","date":"2026-11-23","methods_used":["非洲面具/雕像"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"非洲 320→324（总324）；R22 再拦截；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle95"' not in t:
    block=('if cyc=="cycle95":\n'
           '    L.append("- 非洲面具/雕像补 4 条（320 → 324）：卢巴持碗女像、多贡举臂女像、多贡 satimbe 面具、库巴 bwoom 面具。'
           '①卢巴「**器物的美影响其效力**」，像身残留 mpemba 白垩，且「多数此类作品由男性创作并拥有」；'
           '②多贡女像举臂有**三说**（创世／求雨／播种）并列不裁定；③satimbe 用于 **dama 终丧**，Yasigine 关乎**六十年 sigi**；'
           '④bwoom 与另两面具成**三件一组**演述建国，京外则见于男子入会。'
           '**工程**：元组又误写 `cma-1935.304` 点号 id，**R22 立刻拦截**（自建规以来第 2 次），改连字符后通过。'
           '站点 357 → 361 页，体检 12/12。")\n')
    anchor='if cyc=="cycle94":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **320**（L2 316 / L3 4 / L1 0） |","| 条目 | **324**（L2 320 / L3 4 / L1 0） |"),
    ("| 来源 | **451**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **455**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **357**，站内断链 **0** |","| 页面 | **361**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **320** | L2 316 / L3 4 / **L1 0** |","| 条目总数 | **324** | L2 320 / L3 4 / **L1 0** |"),
    ("| 来源库 | **451**（另 11 条预备来源未计入） |","| 来源库 | **455**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **357** |","| 站点页面 | **361** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **320**（L2 316 / L3 4，**无 L1**） |","| 条目 | **324**（L2 320 / L3 4，**无 L1**） |"),
    ("| 来源 | **451**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **455**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **357** |","| 站点页面 | **361** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])