# -*- coding: utf-8 -*-
"""Cycle96 收尾：D099 + METRICS/SATURATION/REPORT/PROGRESS/STATUS。"""
import json,os,io,subprocess,sys
ROOT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
io.open(os.path.join(ROOT,"DECISIONS.md"),"a",encoding="utf-8").write("""
## D099 — Cycle96 大洋洲 4 条（324 → 328）＋ 一次重名重复事故的修复
新增 `maori-hei-tiki-1969`（毛利绿玉颈坠，1800s，**核心**）、`maori-wakahuia`（毛利宝盒，1800s，**核心**）、
`maori-wahaika-club`（毛利短棍，mid-1800s）、`tami-bowl`（塔米群岛木碗，1800s）。
四处要点：①hei-tiki 承载世袭 **mana**，连接前欧祖先，或表现生育守护者 Hine-te-Iwaiwa；
②Wakahuia 因首领头颈 **tapu** 而悬于屋椽，库克1769—70 已见此类；
③Wahaika 侧附小人像或表武器 mana、柄端人面表攻击性；④塔米木碗以**骨牙竹**为工具，**花纹为家族所有、不得借用**。
**【事故与修复】** 本轮初次写入时，`maori-hei-tiki` 与 `asmat-war-shield` 两 id **与既有条目重名**（既有 hei-tiki 用 1954.147；既有阿斯马特战盾与本轮同一件 1963.554），
且 `write_*.py` **覆盖了这两个既有 overlay**，导致 build_scope=328 而合并后仅 326、并触发 `R11 coverage 与条目数不符`。
**处置**：`git checkout HEAD -- data/l2/maori-hei-tiki.json data/l2/asmat-war-shield.json` 恢复原覆盖层；把本轮 hei-tiki 改用 **`maori-hei-tiki-1969`**（唯一 id）；
**删除**与既有重复的 asmat 元组，改用第 4 件 **Wahaika 短棍（1964.455）**补齐。修复后 328 条目、check errors=0、audit 12/12。
**教训**：每轮新增前必须**先查 catalog 是否已有同名 id**；`check.py` 的 R5/R11 是最后防线，但不能替代写前的 id 查重。
可逆方式：删 4 条 overlay 与 catalog 元组、移除 4 条来源、还原两处 git 恢复。
代价：4 条均单机构；大洋洲由 4 → 8 条，仍以波利尼西亚/美拉尼西亚为主，密克罗尼西亚与澳洲原住民缺失。
""")
m=os.path.join(ROOT,"METRICS.json"); d=json.load(open(m,encoding="utf-8"))
d["rounds"].append({"cycle":"cycle96","date":"2026-11-23","status":"completed",
 "gap_methods":["大洋洲艺术"],"network":"partial: museum APIs ok",
 "new_entries":4,"new_entry_ids":["maori-hei-tiki-1969","maori-wakahuia","maori-wahaika-club","tami-bowl"],
 "oceania_objects":4,"incident":"hei-tiki/asmat id 与既有重名并覆盖 overlay；已 git 恢复改用唯一 id",
 "new_sources":5,"sources_total":459,"entries_total":328,"pages":365,
 "check_result":"errors=0","check_links_result":"broken=0(365页)","audit_all":"12/12 ok","commits":1})
json.dump(d,open(m,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
s=os.path.join(ROOT,"SATURATION.json"); sd=json.load(open(s,encoding="utf-8"))
sd["cycles"].append({"cycle":"cycle96","date":"2026-11-23","methods_used":["大洋洲艺术"],
 "gaps_found":{"entries":4},"network":"partial (museum APIs)","verdict":"大洋洲 4→8（总328）；发生重名事故已修复；未饱和"})
json.dump(sd,open(s,"w",encoding="utf-8"),ensure_ascii=False,indent=2)
P=os.path.join(ROOT,"tools","build_report_autonomous.py"); t=io.open(P,encoding="utf-8").read()
if 'cyc=="cycle96"' not in t:
    block=('if cyc=="cycle96":\n'
           '    L.append("- 大洋洲补 4 条（324 → 328）：毛利 hei-tiki 颈坠、毛利 Wakahuia 宝盒、毛利 Wahaika 短棍、塔米群岛木碗。'
           '①hei-tiki 承载世袭 **mana**、连接前欧祖先；②Wakahuia 因首领头颈 **tapu** 悬于屋椽（库克1769—70 已见）；'
           '③Wahaika 侧附小人像表武器 mana、柄端人面表攻击性；④塔米木碗以**骨牙竹**为工具、**花纹为家族所有**。'
           '**事故**：初写时 `maori-hei-tiki`/`asmat-war-shield` 两 id 与既有条目重名且覆盖了原 overlay，导致合并 326≠328 并触发 R11；'
           '已 `git checkout` 恢复原覆盖层、hei-tiki 改用 `maori-hei-tiki-1969`、删重复 asmat、补 Wahaika 为第4件，修复后 328 条/errors=0。'
           '**教训：新增前先查 catalog 同名 id**。站点 361 → 365 页，体检 12/12。")\n')
    anchor='if cyc=="cycle95":'
    assert anchor in t
    io.open(P,"w",encoding="utf-8").write(t.replace(anchor,block+anchor)); print("report block added")
for path,pairs in [(os.path.join(ROOT,"PROGRESS.md"),
   [("| 条目 | **324**（L2 320 / L3 4 / L1 0） |","| 条目 | **328**（L2 324 / L3 4 / L1 0） |"),
    ("| 来源 | **455**（全部被引用且 verified；隔离区 5 + 预备 11） |","| 来源 | **459**（全部被引用且 verified；隔离区 5 + 预备 11） |"),
    ("| 页面 | **361**，站内断链 **0** |","| 页面 | **365**，站内断链 **0** |")]),
   (os.path.join(ROOT,"PROJECT_STATUS.md"),
   [("| 条目总数 | **324** | L2 320 / L3 4 / **L1 0** |","| 条目总数 | **328** | L2 324 / L3 4 / **L1 0** |"),
    ("| 来源库 | **455**（另 11 条预备来源未计入） |","| 来源库 | **459**（另 11 条预备来源未计入） |"),
    ("| 站点页面 | **361** |","| 站点页面 | **365** |")]),
   (os.path.join(ROOT,"README.md"),
   [("| 条目 | **324**（L2 320 / L3 4，**无 L1**） |","| 条目 | **328**（L2 324 / L3 4，**无 L1**） |"),
    ("| 来源 | **455**（全部 verified；另有 11 预备 / 5 隔离） |","| 来源 | **459**（全部 verified；另有 11 预备 / 5 隔离） |"),
    ("| 站点页面 | **361** |","| 站点页面 | **365** |")])]:
    x=io.open(path,encoding="utf-8").read()
    for a,b in pairs:
        if a in x: x=x.replace(a,b)
    io.open(path,"w",encoding="utf-8").write(x)
r=subprocess.run([sys.executable,"-X","utf8",P],cwd=ROOT,capture_output=True,text=True,encoding="utf-8",errors="replace")
print("report rc=",r.returncode,(r.stdout or "").strip()[:50],(r.stderr or "").strip()[-100:])