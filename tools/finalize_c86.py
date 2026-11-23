# -*- coding: utf-8 -*-
"""Cycle86 收尾：D090 + METRICS/REPORT/PROGRESS/PROJECT_STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D090 — Cycle86 古埃及/近东 4 条（288 → 292）；R2 抓到一处「公元前」写法缺陷
新增 `gudea-statue`（古迪亚像，约前2144—2124，**核心**）、`minnefer-statue`（明内弗行进像，约前2377—2311，**核心**）、
`amenhotep-tomb-relief`（阿蒙霍特普医生墓浮雕，约前1279—1257）、`nefertiti-talatat`（纳芙蒂蒂 talatat，约前1353—1347，**核心**）。
四处要点：①古迪亚双手交握姿势见于30余尊像，2400余铭文记其统治与营建，雕像作为神庙中的统治者替身；
②明内弗像出土于 serdab 密室，仪式后成为亡者替身、以供品维系 ka；
③医师墓浮雕1913—14年发掘后分藏四城，右半在苏黎世；
④阿肯那顿改革中王后纳芙蒂蒂出现频率远高于国王，原因该馆明言未知；阿顿神庙后来被拆作阿蒙神庙填料。
**工程记录**：初稿 when 写作「约前2144—2124年」，R2 把后面的 2124 当作公元后年份而报错；改为「约公元前2144—公元前2124年」后通过。这是「校验器抓到表述歧义」的一个实例。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；古埃及与近东各只 2 条，仍属起步。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle86","date":"2026-11-23","status":"completed",
 "gap_methods":["古埃及/近东实物"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["gudea-statue","minnefer-statue","amenhotep-tomb-relief","nefertiti-talatat"],
 "ancient_objects":4,"new_sources":4,"sources_total":423,"entries_total":292,"pages":329,
 "checker_catch":"R2 公元前区间写法歧义（已改为双写公元前）",
 "check_result":"errors=0","check_links_result":"broken=0(329页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle86","date":"2026-11-23","methods_used":["古埃及/近东"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"古埃及/近东 0→4（总 292）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle86"' not in t:
    block=('if cyc=="cycle86":\n'
           '    L.append("- 古埃及与近东实物此前几乎为零，本轮补 4 条（288 → 292）：古迪亚像、明内弗行进像、'
           '阿蒙霍特普医生墓浮雕、纳芙蒂蒂 talatat。①古迪亚双手交握姿势见于**30余尊像**，**2400余铭文**记其统治，'
           '雕像作为**神庙替身**；②明内弗像出自 **serdab 密室**，仪式后成为亡者替身、以供品维系 **ka**；'
           '③医师墓浮雕1913—14年发掘后**分藏四城**（右半在苏黎世）；④阿肯那顿改革中王后出现频率远高于国王，'
           '原因馆方**明言未知**，阿顿神庙后被拆作阿蒙神庙填料。另记工程实例：初稿写「约前2144—2124年」被 R2 判为越界，'
           '改为「约公元前2144—公元前2124年」后通过——**校验器抓到表述歧义**。站点 325 → 329 页，体检 12/12。")\n')
    anchor='if cyc=="cycle85":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | 288（L2 284 / L3 4 / L1 0） |","| 条目 | 292（L2 288 / L3 4 / L1 0） |"),
    ("| 来源 | 419（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | 423（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | 325，站内断链 **0** |","| 页面 | 329，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **288** | L2 284 / L3 4 / **L1 0** |","| 条目总数 | **292** | L2 288 / L3 4 / **L1 0** |"),
    ("| 来源库 | **419**（另 11 条预备来源未计入） |","| 来源库 | **423**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **325** |","| 站点页面 | **329** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])