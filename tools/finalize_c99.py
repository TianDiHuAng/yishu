# -*- coding: utf-8 -*-
"""Cycle99 收尾：D102 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D102 — Cycle99 东南亚艺术 4 条（336 → 340）
新增 `khmer-naga-buddha`（吴哥那伽座佛，12世纪，**核心**）、`dvaravati-buddha-bust`（堕罗钵底佛首，约700，**核心**）、
`burmese-seated-buddha`（蒲甘坐佛，12世纪，**核心**）、`champa-planetary-deity-dongduong`（占婆九曜神，850—75，**核心**）。
四处要点：①阇耶跋摩七世自比「那伽座佛」＝慈悲与智慧所生之觉悟者，那伽**指高棉人民**；
②堕罗钵底佛首图像元素源自印度，而**孟族的面部处理**（锐眼/厚唇）造就「穿透性宁静」；
③蒲甘坐佛**整木黑漆鎏金**，右手**触地印**请地为证；因**漆易损**故此类大件极罕；④占婆九曜神以**短匕首/须/蹙眉**示猛护，王者坐姿与宝冠示天界之王，座上 **kirtimukha** 示创造能量。
**纪律**：写前查重发现 `champa-planetary-deity` 已存在，改用 **`champa-planetary-deity-dongduong`**（同阳寺本件），避免重名。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源。
代价：4 条均单机构；东南亚由极少增至 4 条以上，但印尼（爪哇/婆罗浮屠）与海岛东南亚仍缺。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle99","date":"2026-11-24","status":"completed",
 "gap_methods":["东南亚艺术"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["khmer-naga-buddha","dvaravati-buddha-bust","burmese-seated-buddha","champa-planetary-deity-dongduong"],
 "sea_objects":4,"discipline":"写前查重 id（champa-planetary-deity→-dongduong）",
 "new_sources":4,"sources_total":469,"entries_total":340,"pages":377,
 "check_result":"errors=0","check_links_result":"broken=0(377页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle99","date":"2026-11-24","methods_used":["东南亚艺术"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"东南亚 4 条新增（总340）；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle99"' not in t:
    block=('if cyc=="cycle99":\n'
           '    L.append("- 东南亚（此前极薄）补 4 条（336 → 340）：吴哥那伽座佛、堕罗钵底佛首、蒲甘坐佛、占婆九曜神。'
           '①阇耶跋摩七世自比「那伽座佛」＝慈悲与智慧所生之觉悟者，**那伽指高棉人民**；②堕罗钵底佛首图像源自印度，'
           '而**孟族面容**（锐眼/厚唇）造就「穿透性宁静」；③蒲甘坐佛**整木黑漆鎏金**、右手**触地印**，因**漆易损**故大件极罕；'
           '④占婆九曜神以匕首/须/蹙眉示猛护、王者坐姿示天界之王，座上 **kirtimukha** 示创造能量。'
           '**纪律**：写前查重，避开既有 `champa-planetary-deity`，改用 `-dongduong`。站点 373 → 377 页，体检 12/12。")\n')
    anchor='if cyc=="cycle98":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **336**（L2 332 / L3 4 / L1 0） |","| 条目 | **340**（L2 336 / L3 4 / L1 0） |"),
    ("| 来源 | **466**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **469**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **373**，站内断链 **0** |","| 页面 | **377**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **336** | L2 332 / L3 4 / **L1 0** |","| 条目总数 | **340** | L2 336 / L3 4 / **L1 0** |"),
    ("| 来源库 | **466**（另 11 条预备来源未计入） |","| 来源库 | **469**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **373** |","| 站点页面 | **377** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **336**（L2 332 / L3 4，**无 L1**） |","| 条目 | **340**（L2 336 / L3 4，**无 L1**） |"),
    ("| 来源 | **466**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **469**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **373** |","| 站点页面 | **377** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])